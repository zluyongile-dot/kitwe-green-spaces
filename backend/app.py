from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import datetime
from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor
from flask_cors import CORS  # Important for frontend-backend communication

app = Flask(__name__)
CORS(app)  # This allows your frontend to talk to the backend

# Database connection parameters - UPDATE THE PASSWORD!
DB_CONFIG = {
    "dbname": "kitwe_green_spaces",
    "user": "postgres",
    "password": "hapiness",  # 🔴 CHANGE THIS TO YOUR ACTUAL PASSWORD!
    "host": "localhost",
    "port": "5432"
}

def get_db_connection():
    """Creates and returns a connection to the PostgreSQL database."""
    conn = psycopg2.connect(**DB_CONFIG)
    return conn
# Session management (simple in-memory for demo)
sessions = {}

def create_session(user_id, username, user_type):
    """Create a new session for logged-in user."""
    session_token = secrets.token_hex(32)
    sessions[session_token] = {
        'user_id': user_id,
        'username': username,
        'user_type': user_type,
        'created_at': datetime.datetime.now(),
        'last_activity': datetime.datetime.now()
    }
    return session_token

def validate_session(session_token):
    """Check if session is valid."""
    if session_token in sessions:
        # Update last activity
        sessions[session_token]['last_activity'] = datetime.datetime.now()
        return sessions[session_token]
    return None

def hash_password(password):
    """Hash a password for storing."""
    return generate_password_hash(password)

def verify_password(stored_hash, provided_password):
    """Verify a stored password against one provided by user."""
    return check_password_hash(stored_hash, provided_password)
@app.route('/test-passwords')
def test_passwords():
    """Test if password hashing is working."""
    from werkzeug.security import generate_password_hash, check_password_hash
    
    test_passwords = {
        'admin123': generate_password_hash('admin123'),
        'council123': generate_password_hash('council123'),
        'citizen123': generate_password_hash('citizen123')
    }
    
    results = {}
    for password, hashed in test_passwords.items():
        results[password] = {
            'hash': hashed[:50] + '...',
            'verify': check_password_hash(hashed, password)
        }
    
    return jsonify({
        "password_test": results,
        "note": "All should show 'verify': true"
    }) 
# In your app.py, add this route to CLEAR and RESET users
@app.route('/reset-users')
def reset_users():
    """Completely reset users table."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Drop and recreate table
        cur.execute("DROP TABLE IF EXISTS users;")
        cur.execute("""
            CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                user_type VARCHAR(20) DEFAULT 'citizen',
                full_name VARCHAR(100),
                ward VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({
            "status": "success",
            "message": "Users table completely reset. Now run /create-users-table"
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
@app.route('/create-users-table')
def create_users_table():
    """Creates the users table with WORKING test accounts."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # First create the table
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            user_type VARCHAR(20) DEFAULT 'citizen',
            full_name VARCHAR(100),
            ward VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP
        );
        """
        cur.execute(create_table_sql)
        
        # Delete existing test users if they exist
        cur.execute("DELETE FROM users WHERE username IN ('admin', 'council', 'citizen');")
        
        # Create PROPERLY HASHED passwords
        # These are pre-hashed versions of 'admin123', 'council123', 'citizen123'
        from werkzeug.security import generate_password_hash
        
        # Generate fresh hashes
        admin_hash = generate_password_hash('admin123')
        council_hash = generate_password_hash('council123')
        citizen_hash = generate_password_hash('citizen123')
        
        # Insert test users with correct hashes
        insert_users_sql = """
        INSERT INTO users (username, email, password_hash, user_type, full_name, ward) VALUES
        (%s, %s, %s, %s, %s, %s);
        """
        
        # Admin user
        cur.execute(insert_users_sql, (
            'admin',
            'admin@kitwe.gov.zm',
            admin_hash,
            'admin',
            'System Administrator',
            'City Centre'
        ))
        
        # City Council user
        cur.execute(insert_users_sql, (
            'council',
            'council@kitwe.gov.zm',
            council_hash,
            'city_council',
            'City Council Officer',
            'City Centre'
        ))
        
        # Citizen user
        cur.execute(insert_users_sql, (
            'citizen',
            'citizen@kitwe.com',
            citizen_hash,
            'citizen',
            'Test Citizen',
            'Parklands'
        ))
        
        conn.commit()
        
        # Verify the users were created
        cur.execute("SELECT username, user_type FROM users ORDER BY username")
        users = cur.fetchall()
        
        cur.close()
        conn.close()
        
        return jsonify({
            "status": "success", 
            "message": "Users table created with 3 test accounts",
            "accounts_created": len(users),
            "users": [
                {"username": "admin", "password": "admin123", "type": "admin"},
                {"username": "council", "password": "council123", "type": "city_council"},
                {"username": "citizen", "password": "citizen123", "type": "citizen"}
            ]
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
@app.route('/')
def home():
    return "Green Space Mapping API is running!"

@app.route('/test-db')
def test_db():
    """Test endpoint to verify database connection."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"status": "success", "postgres_version": db_version})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/create-green-spaces-table')
def create_table():
    """Creates the 'green_spaces' table with a geometry column."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # SQL to create a spatial table
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS green_spaces (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            type VARCHAR(100),  -- e.g., 'park', 'garden', 'forest'
            area_sq_m FLOAT,
            ward VARCHAR(100),
            geom GEOMETRY(Point, 4326)  -- Spatial column for coordinates
        );
        """
        cur.execute(create_table_sql)
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "success", "message": "Table 'green_spaces' created or already exists."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/green-spaces')
def get_green_spaces():
    """Returns all green spaces as GeoJSON."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Query to get green spaces as GeoJSON
        cur.execute("""
            SELECT 
                jsonb_build_object(
                    'type', 'FeatureCollection',
                    'features', jsonb_agg(
                        jsonb_build_object(
                            'type', 'Feature',
                            'geometry', ST_AsGeoJSON(geom)::jsonb,
                            'properties', jsonb_build_object(
                                'id', id,
                                'name', name,
                                'type', type,
                                'area_sq_m', area_sq_m,
                                'ward', ward
                            )
                        )
                    )
                ) AS geojson
            FROM green_spaces;
        """)
        
        result = cur.fetchone()
        cur.close()
        conn.close()
        
        if result and result['geojson']:
            return jsonify(result['geojson'])
        else:
            return jsonify({"type": "FeatureCollection", "features": []})
            
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/add-green-space', methods=['POST'])
def add_green_space():
    """Adds a new green space to the database."""
    try:
        # Get data from the POST request
        data = request.json
        name = data.get('name')
        gtype = data.get('type')
        area = data.get('area_sq_m')
        ward = data.get('ward')
        lon = data.get('longitude')
        lat = data.get('latitude')
        
        # Validate required fields
        if not all([name, lon, lat]):
            return jsonify({"status": "error", "message": "Name and coordinates are required"}), 400
        
        # Connect to database and insert
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("""
            INSERT INTO green_spaces (name, type, area_sq_m, ward, geom)
            VALUES (%s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
            RETURNING id
        """, (name, gtype, area, ward, lon, lat))
        
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({
            "status": "success", 
            "message": "Green space added successfully",
            "id": new_id
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
@app.route('/create-feedback-table')
def create_feedback_table():
    """Creates the 'public_feedback' table."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS public_feedback (
            id SERIAL PRIMARY KEY,
            green_space_id INTEGER REFERENCES green_spaces(id),
            user_name VARCHAR(100),
            user_email VARCHAR(100),
            issue_type VARCHAR(50) NOT NULL,  -- e.g., 'damage', 'maintenance', 'suggestion'
            description TEXT NOT NULL,
            status VARCHAR(20) DEFAULT 'pending',  -- 'pending', 'reviewed', 'resolved'
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            location GEOMETRY(Point, 4326)  -- Optional: if reporting without selecting a green space
        );
        """
        cur.execute(create_table_sql)
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "success", "message": "Table 'public_feedback' created."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
@app.route('/api/submit-feedback', methods=['POST'])
def submit_feedback():
    """Accepts public feedback about green spaces."""
    try:
        data = request.json
        
        # Extract data
        green_space_id = data.get('green_space_id')
        user_name = data.get('user_name', 'Anonymous')
        user_email = data.get('user_email')
        issue_type = data.get('issue_type')
        description = data.get('description')
        lon = data.get('longitude')
        lat = data.get('latitude')
        
        # Validate
        if not description:
            return jsonify({"status": "error", "message": "Description is required"}), 400
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Insert feedback
        if lon and lat:
            # With location
            cur.execute("""
                INSERT INTO public_feedback 
                (green_space_id, user_name, user_email, issue_type, description, location)
                VALUES (%s, %s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
                RETURNING id
            """, (green_space_id, user_name, user_email, issue_type, description, lon, lat))
        else:
            # Without location
            cur.execute("""
                INSERT INTO public_feedback 
                (green_space_id, user_name, user_email, issue_type, description)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
            """, (green_space_id, user_name, user_email, issue_type, description))
        
        feedback_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({
            "status": "success", 
            "message": "Thank you for your feedback!",
            "feedback_id": feedback_id
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
@app.route('/api/feedback')
def get_feedback():
    """Returns all feedback (for admin viewing)."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute("""
            SELECT 
                f.*,
                gs.name as green_space_name,
                TO_CHAR(f.created_at, 'DD Mon YYYY HH:MI') as formatted_date
            FROM public_feedback f
            LEFT JOIN green_spaces gs ON f.green_space_id = gs.id
            ORDER BY f.created_at DESC
        """)
        
        feedback = cur.fetchall()
        cur.close()
        conn.close()
        
        return jsonify({"status": "success", "feedback": feedback})
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500@app.route('/create-feedback-table')
def create_feedback_table():
    """Creates the 'public_feedback' table."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS public_feedback (
            id SERIAL PRIMARY KEY,
            green_space_id INTEGER REFERENCES green_spaces(id),
            user_name VARCHAR(100),
            user_email VARCHAR(100),
            issue_type VARCHAR(50) NOT NULL,  -- e.g., 'damage', 'maintenance', 'suggestion'
            description TEXT NOT NULL,
            status VARCHAR(20) DEFAULT 'pending',  -- 'pending', 'reviewed', 'resolved'
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            location GEOMETRY(Point, 4326)  -- Optional: if reporting without selecting a green space
        );
        """
        cur.execute(create_table_sql)
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "success", "message": "Table 'public_feedback' created."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500@app.route('/api/submit-feedback', methods=['POST'])
def submit_feedback():
    """Accepts public feedback about green spaces."""
    try:
        data = request.json
        
        # Extract data
        green_space_id = data.get('green_space_id')
        user_name = data.get('user_name', 'Anonymous')
        user_email = data.get('user_email')
        issue_type = data.get('issue_type')
        description = data.get('description')
        lon = data.get('longitude')
        lat = data.get('latitude')
        
        # Validate
        if not description:
            return jsonify({"status": "error", "message": "Description is required"}), 400
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Insert feedback
        if lon and lat:
            # With location
            cur.execute("""
                INSERT INTO public_feedback 
                (green_space_id, user_name, user_email, issue_type, description, location)
                VALUES (%s, %s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
                RETURNING id
            """, (green_space_id, user_name, user_email, issue_type, description, lon, lat))
        else:
            # Without location
            cur.execute("""
                INSERT INTO public_feedback 
                (green_space_id, user_name, user_email, issue_type, description)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
            """, (green_space_id, user_name, user_email, issue_type, description))
        
        feedback_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({
            "status": "success", 
            "message": "Thank you for your feedback!",
            "feedback_id": feedback_id
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500@app.route('/add-created-at-column')
def add_created_at_column():
    """Adds created_at timestamp column to green_spaces table."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Check if column exists
        cur.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name='green_spaces' AND column_name='created_at'
        """)
        
        if cur.fetchone() is None:
            # Add the column with default timestamp
            cur.execute("ALTER TABLE green_spaces ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({"status": "success", "message": "created_at column added successfully"})
        else:
            cur.close()
            conn.close()
            return jsonify({"status": "success", "message": "created_at column already exists"})
            
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
@app.route('/api/dashboard/simple-stats')
def simple_dashboard_stats():
    """Returns simple statistics for the dashboard."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Get total green spaces
        cur.execute("SELECT COUNT(*) as total FROM green_spaces")
        total = cur.fetchone()['total']
        
        # Get total area
        cur.execute("SELECT COALESCE(SUM(area_sq_m), 0) as area FROM green_spaces")
        area = cur.fetchone()['area']
        
        # Get breakdown by type  ← NEW CODE
        cur.execute("""
            SELECT type, COUNT(*) as count 
            FROM green_spaces 
            GROUP BY type
        """)
        types_data = cur.fetchall()
        
        cur.close()
        conn.close()
        
        return jsonify({
            "total_green_spaces": total,
            "total_area_m2": area,
            "total_area_hectares": round(area / 10000, 2) if area else 0,
            "types_breakdown": types_data  # ← NEW CODE
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500 @app.route('/api/register', methods=['POST'])
def register():
    """Register a new user."""
    try:
        data = request.json
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()
        full_name = data.get('full_name', '').strip()
        ward = data.get('ward', '').strip()
        
        # Validation
        if not all([username, email, password]):
            return jsonify({"status": "error", "message": "Username, email, and password are required"}), 400
        
        if len(password) < 6:
            return jsonify({"status": "error", "message": "Password must be at least 6 characters"}), 400
        
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Check if user exists
        cur.execute("SELECT id FROM users WHERE username = %s OR email = %s", (username, email))
        existing = cur.fetchone()
        
        if existing:
            cur.close()
            conn.close()
            return jsonify({"status": "error", "message": "Username or email already exists"}), 400
        
        # Create new user
        password_hash = hash_password(password)
        cur.execute("""
            INSERT INTO users (username, email, password_hash, full_name, ward, user_type)
            VALUES (%s, %s, %s, %s, %s, 'citizen')
            RETURNING id, username, user_type
        """, (username, email, password_hash, full_name, ward))
        
        new_user = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({
            "status": "success",
            "message": "Account created successfully!",
            "user": new_user
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    """SIMPLE login that definitely works."""
    try:
        data = request.json
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        
        if not username or not password:
            return jsonify({"status": "error", "message": "Username and password required"}), 400
        
        # SIMPLE TEST ACCOUNTS (no database needed for testing)
        test_accounts = {
            'admin': {'password': 'admin123', 'type': 'admin', 'name': 'System Admin'},
            'council': {'password': 'council123', 'type': 'city_council', 'name': 'Council Officer'},
            'citizen': {'password': 'citizen123', 'type': 'citizen', 'name': 'Test Citizen'}
        }
        
        # Check against test accounts first
        if username in test_accounts:
            if password == test_accounts[username]['password']:
                # Create simple session token
                import secrets
                session_token = secrets.token_hex(16)
                
                return jsonify({
                    "status": "success",
                    "message": f"Welcome {test_accounts[username]['name']}!",
                    "session_token": session_token,
                    "user": {
                        "username": username,
                        "user_type": test_accounts[username]['type'],
                        "full_name": test_accounts[username]['name']
                    }
                })
            else:
                return jsonify({"status": "error", "message": "Invalid password"}), 401
        
        # If not in test accounts, try database
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute("""
            SELECT id, username, password_hash, user_type, full_name 
            FROM users 
            WHERE username = %s OR email = %s
        """, (username, username))
        
        user = cur.fetchone()
        cur.close()
        conn.close()
        
        if user and verify_password(user['password_hash'], password):
            session_token = create_session(user['id'], user['username'], user['user_type'])
            
            return jsonify({
                "status": "success",
                "message": "Login successful!",
                "session_token": session_token,
                "user": {
                    "id": user['id'],
                    "username": user['username'],
                    "user_type": user['user_type'],
                    "full_name": user['full_name']
                }
            })
        
        return jsonify({"status": "error", "message": "Invalid username or password"}), 401
        
    except Exception as e:
        return jsonify({
            "status": "error", 
            "message": "Login error",
            "debug": str(e)
        }), 500
@app.route('/api/logout', methods=['POST'])
def logout():
    """Log out user by removing session."""
    try:
        data = request.json
        session_token = data.get('session_token', '')
        
        if session_token in sessions:
            del sessions[session_token]
        
        return jsonify({"status": "success", "message": "Logged out successfully"})
        
    except:
        return jsonify({"status": "success", "message": "Session cleared"})

@app.route('/api/check-session', methods=['POST'])
def check_session():
    """Check if session is still valid."""
    try:
        data = request.json
        session_token = data.get('session_token', '')
        
        session_data = validate_session(session_token)
        
        if session_data:
            return jsonify({
                "status": "success",
                "valid": True,
                "user": {
                    "username": session_data['username'],
                    "user_type": session_data['user_type']
                }
            })
        else:
            return jsonify({"status": "success", "valid": False})
            
    except:
        return jsonify({"status": "success", "valid": False})
@app.route('/add-sample-green-spaces')
def add_sample_green_spaces():
    """One-click route to add sample green spaces."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # First, clear existing data if you want fresh start
        # cur.execute("DELETE FROM green_spaces;")
        
        # Insert all sample green spaces
        insert_sql = """
        INSERT INTO green_spaces (name, type, area_sq_m, ward, geom) VALUES
        ('Kitwe City Square', 'public_square', 18000, 'City Centre', ST_SetSRID(ST_MakePoint(28.213611, -12.817778), 4326)),
        ('Central Park Kitwe', 'park', 35000, 'City Centre', ST_SetSRID(ST_MakePoint(28.210000, -12.815000), 4326)),
        ('Copperbelt University Arboretum', 'forest', 42000, 'Riverside', ST_SetSRID(ST_MakePoint(28.226389, -12.825556), 4326)),
        ('Kitwe Golf Club', 'golf_course', 380000, 'Ndeke', ST_SetSRID(ST_MakePoint(28.240000, -12.800000), 4326)),
        ('Parklands Community Park', 'park', 22000, 'Parklands', ST_SetSRID(ST_MakePoint(28.208333, -12.827778), 4326)),
        ('Riverside Gardens', 'garden', 15000, 'Parklands', ST_SetSRID(ST_MakePoint(28.206667, -12.831111), 4326)),
        ('Mukuba Park', 'park', 28000, 'Parklands', ST_SetSRID(ST_MakePoint(28.204444, -12.829167), 4326)),
        ('Nkana Sports Complex', 'sports_field', 55000, 'Nkana', ST_SetSRID(ST_MakePoint(28.218056, -12.810833), 4326)),
        ('Nkana Dam Recreation Area', 'park', 95000, 'Nkana', ST_SetSRID(ST_MakePoint(28.221111, -12.808333), 4326)),
        ('Wusakile Community Garden', 'garden', 12000, 'Wusakile', ST_SetSRID(ST_MakePoint(28.231944, -12.805000), 4326)),
        ('Chimwemwe Children''s Park', 'park', 18000, 'Chimwemwe', ST_SetSRID(ST_MakePoint(28.195833, -12.834722), 4326)),
        ('Chimwemwe Football Ground', 'sports_field', 32000, 'Chimwemwe', ST_SetSRID(ST_MakePoint(28.198056, -12.836111), 4326)),
        ('Chimwemwe Market Garden', 'garden', 8500, 'Chimwemwe', ST_SetSRID(ST_MakePoint(28.200000, -12.838889), 4326)),
        ('Mindolo Dam Park', 'park', 120000, 'Mindolo', ST_SetSRID(ST_MakePoint(28.234722, -12.832778), 4326)),
        ('Mindolo Ecumenical Centre Gardens', 'garden', 25000, 'Mindolo', ST_SetSRID(ST_MakePoint(28.232500, -12.830556), 4326)),
        ('Mindolo Lake View Park', 'park', 42000, 'Mindolo', ST_SetSRID(ST_MakePoint(28.236111, -12.828333), 4326)),
        ('Buchi Park', 'park', 32000, 'Buchi', ST_SetSRID(ST_MakePoint(28.186111, -12.850000), 4326)),
        ('Buchi Football Stadium', 'sports_field', 48000, 'Buchi', ST_SetSRID(ST_MakePoint(28.188889, -12.847222), 4326)),
        ('Buchi Community Forest', 'forest', 65000, 'Buchi', ST_SetSRID(ST_MakePoint(28.183333, -12.845833), 4326)),
        ('Garneton Public Park', 'park', 29000, 'Garneton', ST_SetSRID(ST_MakePoint(28.255556, -12.783333), 4326)),
        ('Itimpi Nature Reserve', 'forest', 180000, 'Itimpi', ST_SetSRID(ST_MakePoint(28.266667, -12.775000), 4326)),
        ('Kamitondo Community Garden', 'garden', 11000, 'Kamitondo', ST_SetSRID(ST_MakePoint(28.277778, -12.766667), 4326)),
        ('Miseshi Public Square', 'public_square', 14000, 'Miseshi', ST_SetSRID(ST_MakePoint(28.244444, -12.791667), 4326)),
        ('Riverside Nature Trail', 'forest', 88000, 'Riverside', ST_SetSRID(ST_MakePoint(28.229167, -12.822222), 4326)),
        ('Kitwe Tennis Club Gardens', 'garden', 9500, 'City Centre', ST_SetSRID(ST_MakePoint(28.215000, -12.818889), 4326)),
        ('Copperbelt Museum Gardens', 'garden', 12500, 'City Centre', ST_SetSRID(ST_MakePoint(28.212222, -12.816667), 4326)),
        ('Kitwe Central Hospital Gardens', 'garden', 21000, 'City Centre', ST_SetSRID(ST_MakePoint(28.209167, -12.813889), 4326)),
        ('Ndeke Village Green', 'park', 16500, 'Ndeke', ST_SetSRID(ST_MakePoint(28.237500, -12.803333), 4326)),
        ('Kwacha Roundabout Garden', 'garden', 5500, 'Kwacha', ST_SetSRID(ST_MakePoint(28.205556, -12.823333), 4326)),
        ('Mufuchani Stream Park', 'park', 31000, 'Chamboli', ST_SetSRID(ST_MakePoint(28.191667, -12.841667), 4326)),
        ('Chisokone Market Green Space', 'public_square', 13500, 'City Centre', ST_SetSRID(ST_MakePoint(28.211389, -12.819444), 4326));
        """
        
        cur.execute(insert_sql)
        
        # Count total
        cur.execute("SELECT COUNT(*) FROM green_spaces")
        total = cur.fetchone()[0]
        
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({
            "status": "success",
            "message": f"Added 31 sample green spaces to Kitwe!",
            "total_green_spaces": total,
            "next_steps": [
                "Visit /api/green-spaces to see all green spaces",
                "Visit /api/dashboard/simple-stats for statistics",
                "Add more via /api/add-green-space endpoint"
            ]
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
@app.route('/api/environmental-data')
def get_environmental_data():
    """Returns simulated environmental monitoring data."""
    try:
        import random
        from datetime import datetime, timedelta
        
        # Simulate environmental data based on green space coverage
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Get total green space area for calculations
        cur.execute("SELECT COALESCE(SUM(area_sq_m), 0) as total_area FROM green_spaces")
        total_area = cur.fetchone()['total_area']
        
        # Calculate environmental metrics based on green space coverage
        base_aqi = 50 - (total_area / 10000000) * 10  # Better air quality with more green space
        base_temp = 28 + random.uniform(-2, 3)  # Base temperature with variation
        humidity = 60 + random.uniform(-10, 15)
        
        # Green space impact calculations
        co2_absorbed = round(total_area * 0.0002)  # kg/year
        rainwater_capacity = round(total_area * 0.001)  # liters
        cooling_effect = round(total_area * 0.00001, 1)  # temperature reduction
        
        # Generate 7 days of historical data
        historical_data = []
        for i in range(7):
            date = datetime.now() - timedelta(days=6-i)
            historical_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'aqi': max(20, base_aqi + random.uniform(-5, 5)),
                'temperature': base_temp + random.uniform(-3, 3),
                'humidity': max(40, min(80, humidity + random.uniform(-5, 5)))
            })
        
        # Air quality breakdown
        air_quality_breakdown = {
            'pm25': max(10, base_aqi * 0.4 + random.uniform(-3, 3)),
            'pm10': max(20, base_aqi * 0.7 + random.uniform(-5, 5)),
            'no2': max(15, base_aqi * 0.9 + random.uniform(-8, 8)),
            'so2': max(5, base_aqi * 0.3 + random.uniform(-2, 2)),
            'co': max(3, base_aqi * 0.2 + random.uniform(-1, 1)),
            'o3': max(30, base_aqi * 1.1 + random.uniform(-10, 10))
        }
        
        # Temperature by area type
        temperature_by_area = {
            'industrial': base_temp + 3.2,
            'city_center': base_temp + 1.8,
            'residential': base_temp + 0.5,
            'green_spaces': base_temp - 2.1,
            'parks': base_temp - 2.8
        }
        
        environmental_data = {
            'current_readings': {
                'aqi': round(base_aqi),
                'temperature': round(base_temp, 1),
                'humidity': round(humidity),
                'green_impact': round((314 / 5000) * 100, 1)  # Percentage impact
            },
            'green_space_impact': {
                'co2_absorbed': co2_absorbed,
                'rainwater_capacity': rainwater_capacity,
                'cooling_effect': cooling_effect,
                'biodiversity_index': 85
            },
            'historical_data': historical_data,
            'air_quality_breakdown': air_quality_breakdown,
            'temperature_by_area': temperature_by_area,
            'alerts': [
                {
                    'type': 'info',
                    'title': 'Air Quality Improving',
                    'message': f'Green spaces contributing to {round((314/5000)*100)}% improvement in city center'
                },
                {
                    'type': 'warning',
                    'title': 'Heat Island Effect',
                    'message': 'Industrial areas 3°C warmer than green spaces'
                },
                {
                    'type': 'success',
                    'title': 'CO₂ Reduction',
                    'message': f'{co2_absorbed}kg CO₂ absorbed this month by green spaces'
                }
            ],
            'recommendations': {
                'immediate': [
                    'Plant 200 additional trees in industrial areas to improve air quality',
                    'Create green corridors to enhance cooling effects',
                    'Install air quality sensors near major green spaces',
                    'Implement rainwater harvesting in parks'
                ],
                'long_term': [
                    'Achieve 15% reduction in urban heat island effect',
                    'Increase CO₂ absorption by 25% through new green spaces',
                    'Establish continuous environmental monitoring network',
                    'Integrate with regional climate monitoring systems'
                ]
            },
            'last_updated': datetime.now().isoformat()
        }
        
        cur.close()
        conn.close()
        
        return jsonify(environmental_data)
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)