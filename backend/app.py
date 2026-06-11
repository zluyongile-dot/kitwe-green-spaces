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

def run_db_migrations():
    """Runs schema migrations automatically on startup."""
    print("⏳ Running database schema migrations...")
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # 1. Add city column to green_spaces
        cur.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name='green_spaces' AND column_name='city'
        """)
        if cur.fetchone() is None:
            print("   + Adding column 'city' to 'green_spaces'")
            cur.execute("ALTER TABLE green_spaces ADD COLUMN city VARCHAR(100) DEFAULT 'Kitwe'")
            conn.commit()
            
        # 2. Add ndvi_value column to green_spaces
        cur.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name='green_spaces' AND column_name='ndvi_value'
        """)
        if cur.fetchone() is None:
            print("   + Adding column 'ndvi_value' to 'green_spaces'")
            cur.execute("ALTER TABLE green_spaces ADD COLUMN ndvi_value FLOAT DEFAULT 0.45")
            conn.commit()

        # 3. Add city column to environmental_data
        cur.execute("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name='environmental_data' AND column_name='city'
        """)
        if cur.fetchone() is None:
            print("   + Adding column 'city' to 'environmental_data'")
            cur.execute("ALTER TABLE environmental_data ADD COLUMN city VARCHAR(100) DEFAULT 'Kitwe'")
            conn.commit()

        cur.close()
        conn.close()
        print("✅ Database schema migrations complete!")
    except Exception as e:
        print(f"⚠️ Migration warning/error (running rollback): {e}")
        if conn:
            conn.rollback()
            conn.close()

# Auto-execute migrations on import / startup
try:
    run_db_migrations()
except Exception as e:
    print(f"Startup migration warning: {e}")

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
            image_url TEXT,
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
                                'ward', ward,
                                'image_url', image_url,
                                'city', COALESCE(city, 'Kitwe'),
                                'ndvi_value', COALESCE(ndvi_value, 0.45)
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
        city = data.get('city', 'Kitwe')
        ndvi_value = data.get('ndvi_value', 0.45)
        
        # Validate required fields
        if not all([name, lon, lat]):
            return jsonify({"status": "error", "message": "Name and coordinates are required"}), 400
        
        # Connect to database and insert
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("""
            INSERT INTO green_spaces (name, type, area_sq_m, ward, city, ndvi_value, geom)
            VALUES (%s, %s, %s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
            RETURNING id
        """, (name, gtype, area, ward, city, ndvi_value, lon, lat))
        
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
# Note: create-feedback-table route is defined later in the file
# Removed duplicate to avoid conflicts

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
        
        # Return just the array for easier frontend consumption
        return jsonify(feedback)
        
    except Exception as e:
        # Return empty array if table doesn't exist yet
        # Return empty array if table doesn't exist yet
        return jsonify([])

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

@app.route('/create-environmental-table')
def create_environmental_table():
    """Creates the 'environmental_data' table."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS environmental_data (
            id SERIAL PRIMARY KEY,
            location VARCHAR(255) NOT NULL,
            air_quality VARCHAR(50),
            temperature FLOAT,
            humidity FLOAT,
            noise_level FLOAT,
            green_space_id INTEGER REFERENCES green_spaces(id),
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            notes TEXT
        );
        """
        cur.execute(create_table_sql)
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "success", "message": "Table 'environmental_data' created."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Note: submit-feedback route is defined earlier in the file
# Removed duplicate to avoid conflicts

@app.route('/add-created-at-column')
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
    """Returns simple statistics for the dashboard, optionally filtered by city."""
    try:
        from flask import request
        city = request.args.get('city', 'Kitwe')
        
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Build filter condition
        if city.lower() == 'all':
            filter_sql = ""
            params = []
        else:
            filter_sql = "WHERE city = %s"
            params = [city]
            
        # Get total green spaces
        cur.execute(f"SELECT COUNT(*) as total FROM green_spaces {filter_sql}", params)
        total = cur.fetchone()['total']
        
        # Get total area
        cur.execute(f"SELECT COALESCE(SUM(area_sq_m), 0) as area FROM green_spaces {filter_sql}", params)
        area = cur.fetchone()['area']
        
        # Get breakdown by type
        cur.execute(f"""
            SELECT type, COUNT(*) as count, COALESCE(SUM(area_sq_m), 0) as total_area
            FROM green_spaces 
            {filter_sql}
            GROUP BY type
        """, params)
        types_data = cur.fetchall()
        
        # Get feedback count
        try:
            if city.lower() == 'all':
                cur.execute("SELECT COUNT(*) as total FROM public_feedback")
            else:
                cur.execute("""
                    SELECT COUNT(f.*) as total 
                    FROM public_feedback f
                    JOIN green_spaces gs ON f.green_space_id = gs.id
                    WHERE gs.city = %s
                """, params)
            feedback_count = cur.fetchone()['total']
        except:
            feedback_count = 0
        
        # Get environmental data count
        try:
            if city.lower() == 'all':
                cur.execute("SELECT COUNT(*) as total FROM environmental_data")
            else:
                cur.execute("SELECT COUNT(*) as total FROM environmental_data WHERE city = %s", params)
            environmental_count = cur.fetchone()['total']
        except:
            environmental_count = 0
        
        cur.close()
        conn.close()
        
        return jsonify({
            "city": city,
            "total_spaces": total,
            "total_green_spaces": total,
            "total_area_m2": area,
            "total_area_hectares": round(area / 10000, 2) if area else 0,
            "types_breakdown": types_data,
            "total_feedback": feedback_count,
            "total_environmental": environmental_count,
            "total_visitors": 0  # Placeholder for future visitor tracking
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500 

@app.route('/api/dashboard/recent-activity')
def get_recent_activity():
    """Returns recent activity across the system."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        activities = []
        
        # Get recent green spaces added
        try:
            cur.execute("""
                SELECT 
                    'green_space' as type,
                    name as description,
                    created_at as timestamp,
                    'added' as status
                FROM green_spaces
                WHERE created_at IS NOT NULL
                ORDER BY created_at DESC
                LIMIT 5
            """)
            activities.extend(cur.fetchall())
        except:
            pass  # Table might not have created_at column yet
        
        # Get recent feedback
        try:
            cur.execute("""
                SELECT 
                    'feedback' as type,
                    CONCAT(user_name, ' submitted feedback') as description,
                    created_at as timestamp,
                    status
                FROM public_feedback
                ORDER BY created_at DESC
                LIMIT 5
            """)
            activities.extend(cur.fetchall())
        except:
            pass  # Table might not exist yet
        
        # Get recent environmental data
        try:
            cur.execute("""
                SELECT 
                    'environmental' as type,
                    CONCAT('Environmental data recorded at ', location) as description,
                    recorded_at as timestamp,
                    'recorded' as status
                FROM environmental_data
                ORDER BY recorded_at DESC
                LIMIT 5
            """)
            activities.extend(cur.fetchall())
        except:
            pass  # Table might not exist yet
        
        # Sort all activities by timestamp
        activities.sort(key=lambda x: x['timestamp'] if x['timestamp'] else '', reverse=True)
        
        cur.close()
        conn.close()
        
        return jsonify(activities[:20])  # Return top 20 most recent
        
    except Exception as e:
        # Return empty array if there's an error
        return jsonify([])

@app.route('/api/register', methods=['POST'])
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
    """One-click route to add sample green spaces for Kitwe and Ndola."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Clear existing data for a fresh comparative start
        cur.execute("TRUNCATE TABLE green_spaces RESTART IDENTITY CASCADE;")
        
        # Insert all sample green spaces (26 Kitwe + 12 Ndola)
        insert_sql = """
        INSERT INTO green_spaces (name, type, area_sq_m, ward, city, ndvi_value, geom) VALUES
        -- Kitwe Study Area (26 spaces)
        ('Freedom Park', 'municipal_park', 45000, 'City Centre', 'Kitwe', 0.62, ST_SetSRID(ST_MakePoint(28.21551, -12.80693), 4326)),
        ('Kitwe Playing Fields', 'sports_recreation', 65000, 'City Centre', 'Kitwe', 0.35, ST_SetSRID(ST_MakePoint(28.21822, -12.79229), 4326)),
        ('Zambezi Way Park', 'neighborhood_park', 28000, 'Riverside', 'Kitwe', 0.55, ST_SetSRID(ST_MakePoint(28.23229, -12.79260), 4326)),
        ('Fyapakale Park', 'neighborhood_park', 32000, 'Riverside', 'Kitwe', 0.58, ST_SetSRID(ST_MakePoint(28.23458, -12.79800), 4326)),
        ('Burrum Park', 'neighborhood_park', 22000, 'Parklands', 'Kitwe', 0.51, ST_SetSRID(ST_MakePoint(28.243056, -12.802083), 4326)),
        ('Kew Gardens Park', 'neighborhood_park', 19000, 'Parklands', 'Kitwe', 0.56, ST_SetSRID(ST_MakePoint(28.232778, -12.803889), 4326)),
        ('Garden Park Stadium', 'sports_recreation', 28000, 'City Centre', 'Kitwe', 0.32, ST_SetSRID(ST_MakePoint(28.219722, -12.791389), 4326)),
        ('Cheswa Park', 'neighborhood_park', 15000, 'Parklands', 'Kitwe', 0.53, ST_SetSRID(ST_MakePoint(28.2250, -12.8080), 4326)),
        ('Kitwe Stream', 'tributary_stream', 15000, 'Riverside', 'Kitwe', 0.22, ST_SetSRID(ST_MakePoint(28.25811, -12.80936), 4326)),
        ('Kafue River', 'major_river', 185000, 'Riverside', 'Kitwe', 0.10, ST_SetSRID(ST_MakePoint(28.250756572152678, -12.825001678275749), 4326)),
        ('Mindolo Dam', 'dam_lake', 425000, 'Mindolo', 'Kitwe', 0.08, ST_SetSRID(ST_MakePoint(28.14111998142754, -12.790960190352685), 4326)),
        ('Mwekwera Falls', 'waterfall_lake', 95000, 'Mwekwera', 'Kitwe', 0.18, ST_SetSRID(ST_MakePoint(28.358938982476428, -12.828180654957118), 4326)),
        ('Chembe Bird Sanctuary Lake', 'lake_wetland', 285000, 'Chembe', 'Kitwe', 0.25, ST_SetSRID(ST_MakePoint(27.993929731853243, -12.832010423511084), 4326)),
        ('Kumasamba Lodge Water', 'lake_fishing', 125000, 'Kumasamba', 'Kitwe', 0.15, ST_SetSRID(ST_MakePoint(28.23994476728268, -12.905264693431171), 4326)),
        ('Ngoma Lake', 'lake', 165000, 'Ngoma', 'Kitwe', 0.05, ST_SetSRID(ST_MakePoint(28.24254722, -12.79860833), 4326)),
        ('Country Side Dam', 'dam_lake', 95000, 'Mindolo', 'Kitwe', 0.09, ST_SetSRID(ST_MakePoint(28.1600, -12.7950), 4326)),
        ('Chandamali Lake', 'lake', 110000, 'Garneton', 'Kitwe', 0.07, ST_SetSRID(ST_MakePoint(28.2550, -12.7850), 4326)),
        ('Serene Gardens', 'commercial_garden', 12000, 'City Centre', 'Kitwe', 0.60, ST_SetSRID(ST_MakePoint(28.223056, -12.810278), 4326)),
        ('Mist Gardens', 'commercial_garden', 15000, 'Riverside', 'Kitwe', 0.64, ST_SetSRID(ST_MakePoint(28.236111, -12.813889), 4326)),
        ('Sunset Gardens Kitwe', 'commercial_event_garden', 18500, 'City Centre', 'Kitwe', 0.61, ST_SetSRID(ST_MakePoint(28.217778, -12.813056), 4326)),
        ('Casablanca Gardens', 'commercial_garden', 14000, 'Nkana', 'Kitwe', 0.59, ST_SetSRID(ST_MakePoint(28.205556, -12.831944), 4326)),
        ('Nkana Golf Club', 'golf_course_18hole', 485000, 'Nkana West', 'Kitwe', 0.42, ST_SetSRID(ST_MakePoint(28.17966, -12.82881), 4326)),
        ('Nkana Cricket Club', 'cricket_ground', 35000, 'Nkana', 'Kitwe', 0.38, ST_SetSRID(ST_MakePoint(28.20839907714752, -12.830287133445191), 4326)),
        ('Savanna Woodlands', 'miombo_woodland', 1250000, 'Surrounding Area', 'Kitwe', 0.82, ST_SetSRID(ST_MakePoint(28.25, -12.85), 4326)),
        ('Dambos Seasonal Wetlands', 'grassland_wetland', 385000, 'Surrounding Area', 'Kitwe', 0.48, ST_SetSRID(ST_MakePoint(28.28, -12.82), 4326)),
        ('CBU Nature Park', 'university_nature_park', 125000, 'Riverside', 'Kitwe', 0.74, ST_SetSRID(ST_MakePoint(28.239010623101414, -12.80234209672651), 4326)),
        
        -- Ndola Reference Area (12 spaces)
        ('Ndola Golf Club', 'golf_course_18hole', 350000, 'Ndola Central', 'Ndola', 0.38, ST_SetSRID(ST_MakePoint(28.6400, -12.9750), 4326)),
        ('Kanini Community Park', 'neighborhood_park', 22000, 'Kanini', 'Ndola', 0.52, ST_SetSRID(ST_MakePoint(28.6480, -12.9800), 4326)),
        ('Itawa Springs Reserve', 'forest', 120000, 'Itawa', 'Ndola', 0.75, ST_SetSRID(ST_MakePoint(28.6650, -13.0100), 4326)),
        ('Hillcrest Public Gardens', 'commercial_garden', 14000, 'Hillcrest', 'Ndola', 0.58, ST_SetSRID(ST_MakePoint(28.6380, -12.9650), 4326)),
        ('Kavu Forest Reserve', 'forest', 450000, 'Kavu', 'Ndola', 0.81, ST_SetSRID(ST_MakePoint(28.6900, -12.9500), 4326)),
        ('Dag Hammarskjöld Memorial Site', 'municipal_park', 90000, 'Hammarskjöld', 'Ndola', 0.72, ST_SetSRID(ST_MakePoint(28.5200, -12.9780), 4326)),
        ('Ndola Boating Club Lake', 'dam_lake', 150000, 'Itawa', 'Ndola', 0.12, ST_SetSRID(ST_MakePoint(28.6550, -13.0200), 4326)),
        ('Chifubu Sports Ground', 'sports_recreation', 45000, 'Chifubu', 'Ndola', 0.32, ST_SetSRID(ST_MakePoint(28.6600, -12.9450), 4326)),
        ('Kansenji Linear Park', 'neighborhood_park', 18000, 'Kansenji', 'Ndola', 0.55, ST_SetSRID(ST_MakePoint(28.6250, -12.9700), 4326)),
        ('Jubilee Park Ndola', 'municipal_park', 25000, 'City Centre', 'Ndola', 0.61, ST_SetSRID(ST_MakePoint(28.6420, -12.9820), 4326)),
        ('Masala Community Garden', 'commercial_garden', 8500, 'Masala', 'Ndola', 0.48, ST_SetSRID(ST_MakePoint(28.6300, -13.0150), 4326)),
        ('Mapepe Woodland', 'forest', 280000, 'Kavu', 'Ndola', 0.78, ST_SetSRID(ST_MakePoint(28.6950, -12.9900), 4326));
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
            "message": f"Successfully seeded 38 green spaces (26 Kitwe + 12 Ndola)!",
            "total_green_spaces": total,
            "next_steps": [
                "Visit /api/green-spaces to see all green spaces",
                "Visit /api/dashboard/simple-stats?city=all for statistics",
                "Add more via /api/add-green-space endpoint"
            ]
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
@app.route('/api/environmental-data')
def get_environmental_data():
    """Returns simulated environmental monitoring data or database records list."""
    try:
        from flask import request
        import random
        from datetime import datetime, timedelta
        
        # Check if format=list is requested for database environmental records
        format_param = request.args.get('format')
        if format_param == 'list':
            conn = get_db_connection()
            cur = conn.cursor(cursor_factory=RealDictCursor)
            
            # Check if table has records, if not, auto-seed with beautiful realistic telemetry
            try:
                cur.execute("SELECT COUNT(*) as total FROM environmental_data")
                count = cur.fetchone()['total']
            except Exception:
                # Must roll back aborted transaction before running CREATE TABLE in PostgreSQL
                conn.rollback()
                
                # Table might not exist, create it on-the-fly
                create_table_sql = """
                CREATE TABLE IF NOT EXISTS environmental_data (
                    id SERIAL PRIMARY KEY,
                    location VARCHAR(255) NOT NULL,
                    air_quality VARCHAR(50),
                    temperature FLOAT,
                    humidity FLOAT,
                    noise_level FLOAT,
                    green_space_id INTEGER,
                    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    notes TEXT
                );
                """
                cur.execute(create_table_sql)
                conn.commit()
                count = 0
            
            if count == 0:
                now = datetime.now()
                samples = [
                    # Kitwe (6)
                    ("Kitwe City Centre", "Moderate", 28.5, 55.0, now - timedelta(hours=1), "City centre active monitoring", "Kitwe"),
                    ("Mindolo Sanctuary", "Good", 23.4, 68.0, now - timedelta(hours=4), "Protected woodland reserve", "Kitwe"),
                    ("Nkana Industrial Area", "Unhealthy", 32.1, 40.0, now - timedelta(hours=12), "Industrial zone near smelting plant", "Kitwe"),
                    ("Riverside Parklands", "Good", 25.6, 60.0, now - timedelta(days=1), "Residential riverside green belt", "Kitwe"),
                    ("Wusakile Mine Zone", "Poor", 29.8, 46.0, now - timedelta(days=1, hours=6), "Mine tailings monitoring station", "Kitwe"),
                    ("Mwekera Forest Reserve", "Good", 21.8, 75.0, now - timedelta(days=2, hours=12), "Dense Miombo woodland canopy", "Kitwe"),
                    # Ndola (5)
                    ("Ndola Central District", "Moderate", 27.2, 58.0, now - timedelta(hours=2), "City centre active monitor", "Ndola"),
                    ("Kanini Woodlands", "Good", 24.8, 62.0, now - timedelta(hours=5), "Active suburban parklands", "Ndola"),
                    ("Chifubu High-Traffic", "Moderate", 29.5, 52.0, now - timedelta(hours=8), "Transit corridor baseline station", "Ndola"),
                    ("Itawa Springs Watershed", "Good", 22.1, 72.0, now - timedelta(days=1), "Protected hydrological recharge area", "Ndola"),
                    ("Kansenji Residential", "Good", 25.0, 60.0, now - timedelta(days=1, hours=4), "Suburban green space belt", "Ndola")
                ]
                for loc, aq, temp, hum, dt, notes, city_name in samples:
                    cur.execute("""
                        INSERT INTO environmental_data (location, air_quality, temperature, humidity, recorded_at, notes, city)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (loc, aq, temp, hum, dt, notes, city_name))
                conn.commit()
            
            # Fetch filtered or all records
            city_param = request.args.get('city')
            if city_param and city_param.lower() != 'all':
                cur.execute("""
                    SELECT id, location, air_quality, temperature, humidity, noise_level, recorded_at, notes, city
                    FROM environmental_data
                    WHERE city = %s
                    ORDER BY recorded_at DESC
                """, (city_param,))
            else:
                cur.execute("""
                    SELECT id, location, air_quality, temperature, humidity, noise_level, recorded_at, notes, city
                    FROM environmental_data
                    ORDER BY recorded_at DESC
                """)
            records = cur.fetchall()
            cur.close()
            conn.close()
            return jsonify(records)
        
        # Otherwise, proceed with default summary telemetry mock
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


# ========================================
# PHASE 2: EVENTS SYSTEM
# ========================================

@app.route('/create-events-tables')
def create_events_tables():
    """Creates events and RSVPs tables."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Events table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                description TEXT,
                event_type VARCHAR(50),
                location_id INTEGER REFERENCES green_spaces(id),
                event_date DATE NOT NULL,
                start_time TIME,
                end_time TIME,
                max_participants INTEGER DEFAULT 50,
                current_participants INTEGER DEFAULT 0,
                status VARCHAR(20) DEFAULT 'open',
                created_by INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # RSVPs table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS rsvps (
                id SERIAL PRIMARY KEY,
                event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
                user_name VARCHAR(100) NOT NULL,
                user_email VARCHAR(100),
                user_phone VARCHAR(20),
                status VARCHAR(20) DEFAULT 'confirmed',
                rsvp_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(event_id, user_email)
            );
        """)
        
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({"status": "success", "message": "Events tables created"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/events', methods=['GET'])
def get_events():
    """Get all events with RSVP counts."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute("""
            SELECT 
                e.*,
                gs.name as location_name,
                gs.ward,
                COUNT(r.id) as rsvp_count
            FROM events e
            LEFT JOIN green_spaces gs ON e.location_id = gs.id
            LEFT JOIN rsvps r ON e.id = r.event_id AND r.status = 'confirmed'
            GROUP BY e.id, gs.name, gs.ward
            ORDER BY e.event_date ASC
        """)
        
        events = cur.fetchall()
        cur.close()
        conn.close()
        
        return jsonify({"status": "success", "events": events})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/events', methods=['POST'])
def create_event():
    """Create a new event."""
    try:
        data = request.json
        
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute("""
            INSERT INTO events (title, description, event_type, location_id, 
                              event_date, start_time, end_time, max_participants)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (
            data['title'],
            data.get('description'),
            data.get('event_type'),
            data.get('location_id'),
            data['event_date'],
            data.get('start_time'),
            data.get('end_time'),
            data.get('max_participants', 50)
        ))
        
        event_id = cur.fetchone()['id']
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({"status": "success", "event_id": event_id})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/events/<int:event_id>/rsvp', methods=['POST'])
def rsvp_event(event_id):
    """RSVP to an event."""
    try:
        data = request.json
        
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Check if event is full
        cur.execute("""
            SELECT max_participants, 
                   (SELECT COUNT(*) FROM rsvps WHERE event_id = %s AND status = 'confirmed') as current
            FROM events WHERE id = %s
        """, (event_id, event_id))
        
        event = cur.fetchone()
        if event['current'] >= event['max_participants']:
            cur.close()
            conn.close()
            return jsonify({"status": "error", "message": "Event is full"}), 400
        
        # Create RSVP
        cur.execute("""
            INSERT INTO rsvps (event_id, user_name, user_email, user_phone)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (event_id, user_email) DO NOTHING
            RETURNING id
        """, (event_id, data['name'], data['email'], data.get('phone')))
        
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        
        if result:
            return jsonify({"status": "success", "message": "RSVP confirmed!"})
        else:
            return jsonify({"status": "error", "message": "Already registered"}), 400
            
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/add-sample-events')
def add_sample_events():
    """Add sample events for testing."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Clear existing events
        cur.execute("DELETE FROM events")
        
        # Add sample events
        cur.execute("""
            INSERT INTO events (title, description, event_type, location_id, event_date, start_time, end_time, max_participants, current_participants, status)
            VALUES
            ('Tree Planting at Parklands', 'Join us for a community tree planting event. We will plant 100 indigenous trees.', 'planting', 5, '2024-12-15', '09:00', '12:00', 50, 45, 'open'),
            ('Central Park Cleanup', 'Help us keep our parks clean! Bring gloves and bags.', 'cleanup', 2, '2024-12-20', '08:00', '11:00', 30, 12, 'open'),
            ('Urban Gardening Workshop', 'Learn sustainable gardening techniques for urban spaces.', 'workshop', 6, '2024-12-22', '14:00', '16:00', 25, 24, 'open'),
            ('Mindolo Dam Nature Walk', 'Guided nature walk around Mindolo Dam. Family friendly!', 'education', 14, '2025-01-05', '07:00', '09:00', 40, 8, 'open'),
            ('Community Garden Launch', 'Grand opening of the new Chimwemwe community garden.', 'event', 13, '2025-01-10', '10:00', '13:00', 100, 35, 'open'),
            ('Nkana Sports Complex Greening', 'Plant grass and shrubs around the sports complex.', 'planting', 8, '2025-01-15', '09:00', '12:00', 60, 58, 'open')
        """)
        
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({"status": "success", "message": "Sample events added"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ========================================
# PHASE 3: ANALYTICS
# ========================================

@app.route('/api/analytics/summary')
def analytics_summary():
    """Get overall analytics summary."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Total green spaces and area
        cur.execute("""
            SELECT 
                COUNT(*) as total_spaces,
                COALESCE(SUM(area_sq_m), 0) as total_area_m2,
                COUNT(DISTINCT ward) as total_wards
            FROM green_spaces
        """)
        stats = cur.fetchone()
        
        # Events stats
        cur.execute("""
            SELECT 
                COUNT(*) as total_events,
                COALESCE(SUM(max_participants), 0) as total_capacity
            FROM events
            WHERE event_date >= CURRENT_DATE
        """)
        events_stats = cur.fetchone()
        
        # Mock data for trees planted and volunteers
        trees_planted = 1320
        volunteers = 450
        
        cur.close()
        conn.close()
        
        return jsonify({
            "status": "success",
            "summary": {
                "total_green_spaces": stats['total_spaces'],
                "total_area_hectares": round(stats['total_area_m2'] / 10000, 2),
                "total_wards": stats['total_wards'],
                "trees_planted_ytd": trees_planted,
                "volunteers_engaged": volunteers,
                "upcoming_events": events_stats['total_events']
            }
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/analytics/coverage')
def analytics_coverage():
    """Get ward coverage data."""
    try:
        # Mock coverage data (in production, calculate from actual ward boundaries)
        coverage_data = [
            {"ward": "City Centre", "coverage": 75, "area_m2": 180000, "spaces": 5},
            {"ward": "Parklands", "coverage": 62, "area_m2": 65000, "spaces": 3},
            {"ward": "Nkana", "coverage": 58, "area_m2": 150000, "spaces": 2},
            {"ward": "Chimwemwe", "coverage": 45, "area_m2": 58500, "spaces": 3},
            {"ward": "Mindolo", "coverage": 68, "area_m2": 187000, "spaces": 3},
            {"ward": "Buchi", "coverage": 38, "area_m2": 145000, "spaces": 3},
            {"ward": "Garneton", "coverage": 52, "area_m2": 29000, "spaces": 1},
            {"ward": "Riverside", "coverage": 71, "area_m2": 130000, "spaces": 2},
            {"ward": "Wusakile", "coverage": 42, "area_m2": 12000, "spaces": 1}
        ]
        
        return jsonify({"status": "success", "coverage": coverage_data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/analytics/trends')
def analytics_trends():
    """Get time-series data for charts."""
    try:
        # Mock monthly data
        trends = {
            "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            "trees_planted": [120, 150, 180, 200, 220, 250, 180, 160, 190, 210, 230, 250],
            "events_held": [3, 4, 5, 6, 5, 7, 4, 5, 6, 7, 6, 8],
            "volunteers": [45, 52, 68, 75, 82, 95, 70, 65, 78, 88, 92, 105]
        }
        
        return jsonify({"status": "success", "trends": trends})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ========================================
# PHASE 4: PLANNER TOOLS
# ========================================

@app.route('/api/export/geojson')
def export_geojson():
    """Export green spaces as GeoJSON."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
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
                                'ward', ward,
                                'city', city,
                                'ndvi_value', ndvi_value
                            )
                        )
                    )
                ) AS geojson
            FROM green_spaces
        """)
        
        result = cur.fetchone()
        cur.close()
        conn.close()
        
        return jsonify(result['geojson'])
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/reports/gap-analysis')
def generate_gap_report():
    """Generate gap analysis report data."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Get all green spaces grouped by ward
        cur.execute("""
            SELECT 
                ward,
                COUNT(*) as space_count,
                SUM(area_sq_m) as total_area,
                AVG(area_sq_m) as avg_area
            FROM green_spaces
            GROUP BY ward
            ORDER BY ward
        """)
        
        ward_data = cur.fetchall()
        
        # Mock coverage percentages
        coverage_map = {
            "City Centre": 75, "Parklands": 62, "Nkana": 58,
            "Chimwemwe": 45, "Mindolo": 68, "Buchi": 38,
            "Garneton": 52, "Riverside": 71, "Wusakile": 42,
            "Itimpi": 35, "Kamitondo": 28, "Miseshi": 48, "Ndeke": 55
        }
        
        report_data = []
        for ward in ward_data:
            coverage = coverage_map.get(ward['ward'], 50)
            status = "critical" if coverage < 30 else ("low" if coverage < 60 else "healthy")
            
            report_data.append({
                "ward": ward['ward'],
                "spaces": ward['space_count'],
                "total_area_m2": float(ward['total_area']),
                "coverage_percent": coverage,
                "status": status,
                "recommendation": get_recommendation(coverage)
            })
        
        cur.close()
        conn.close()
        
        return jsonify({
            "status": "success",
            "report": {
                "generated_at": datetime.datetime.now().isoformat(),
                "wards": report_data,
                "summary": {
                    "critical_wards": len([w for w in report_data if w['status'] == 'critical']),
                    "low_wards": len([w for w in report_data if w['status'] == 'low']),
                    "healthy_wards": len([w for w in report_data if w['status'] == 'healthy'])
                }
            }
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def get_recommendation(coverage):
    """Get recommendation based on coverage."""
    if coverage < 30:
        return "URGENT: Immediate intervention required. Develop new green spaces."
    elif coverage < 60:
        return "MODERATE: Expand existing spaces and create new pocket parks."
    else:
        return "GOOD: Maintain current spaces and focus on quality improvements."

@app.route('/api/heat-island/zones')
def get_heat_zones():
    """Get heat island risk zones (mock data)."""
    try:
        # Mock heat island data
        heat_zones = [
            {"zone": "Industrial Area", "risk": "high", "avg_temp": 34.5, "ward": "City Centre"},
            {"zone": "Commercial District", "risk": "high", "avg_temp": 33.8, "ward": "City Centre"},
            {"zone": "Buchi Residential", "risk": "medium", "avg_temp": 31.2, "ward": "Buchi"},
            {"zone": "Chimwemwe", "risk": "medium", "avg_temp": 30.8, "ward": "Chimwemwe"},
            {"zone": "Parklands", "risk": "low", "avg_temp": 28.5, "ward": "Parklands"},
            {"zone": "Mindolo Dam Area", "risk": "low", "avg_temp": 27.2, "ward": "Mindolo"}
        ]
        
        return jsonify({"status": "success", "zones": heat_zones})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/timeline')
def get_timeline():
    """Get development timeline data."""
    try:
        # Mock timeline data
        timeline = [
            {
                "date": "2024-01-15",
                "title": "Parklands Park Renovation",
                "type": "improvement",
                "status": "completed",
                "description": "Upgraded playground equipment and added benches"
            },
            {
                "date": "2024-03-20",
                "title": "Chimwemwe Community Garden",
                "type": "new",
                "status": "completed",
                "description": "New 8,500 m² community garden established"
            },
            {
                "date": "2024-06-10",
                "title": "Mindolo Dam Cleanup",
                "type": "maintenance",
                "status": "completed",
                "description": "Major cleanup and trail maintenance"
            },
            {
                "date": "2024-09-05",
                "title": "Buchi Forest Expansion",
                "type": "expansion",
                "status": "in_progress",
                "description": "Adding 15,000 m² to existing forest area"
            },
            {
                "date": "2025-01-15",
                "title": "City Centre Green Corridor",
                "type": "new",
                "status": "planned",
                "description": "New linear park connecting major spaces"
            },
            {
                "date": "2025-03-01",
                "title": "Nkana Sports Complex Greening",
                "type": "improvement",
                "status": "planned",
                "description": "Add trees and landscaping around complex"
            }
        ]
        
        return jsonify({"status": "success", "timeline": timeline})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500



# ========================================
# ADMIN DASHBOARD ENDPOINTS
# ========================================

# Note: /api/feedback is already defined earlier in the file (line 409)
# Removed duplicate route definition to fix 500 Internal Server Error

@app.route('/api/feedback/<int:feedback_id>/status', methods=['PUT'])
def update_feedback_status(feedback_id):
    """Update feedback status."""
    try:
        data = request.json
        new_status = data.get('status')
        
        if new_status not in ['pending', 'reviewed', 'resolved']:
            return jsonify({"status": "error", "message": "Invalid status"}), 400
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("""
            UPDATE public_feedback 
            SET status = %s 
            WHERE id = %s
        """, (new_status, feedback_id))
        
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({"status": "success", "message": f"Feedback updated to {new_status}"})
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/feedback/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    """Delete feedback."""
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("DELETE FROM public_feedback WHERE id = %s", (feedback_id,))
        
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({"status": "success", "message": "Feedback deleted"})
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ========================================
# COUNCIL PAGE ENDPOINTS
# ========================================

@app.route('/api/council/stats')
def council_stats():
    """Get stats for council dashboard."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        # Total green spaces
        cur.execute("SELECT COUNT(*) as total_spaces FROM green_spaces")
        total_spaces = cur.fetchone()['total_spaces']
        
        # Total area
        cur.execute("SELECT COALESCE(SUM(area_sq_m), 0) as total_area FROM green_spaces")
        total_area = cur.fetchone()['total_area']
        
        # Feedback stats
        cur.execute("""
            SELECT 
                COUNT(*) as total_feedback,
                COUNT(CASE WHEN status = 'pending' THEN 1 END) as pending,
                COUNT(CASE WHEN status = 'reviewed' THEN 1 END) as reviewed,
                COUNT(CASE WHEN status = 'resolved' THEN 1 END) as resolved
            FROM public_feedback
        """)
        feedback_stats = cur.fetchone()
        
        # Ward coverage
        cur.execute("""
            SELECT ward, COUNT(*) as spaces, SUM(area_sq_m) as area
            FROM green_spaces
            WHERE ward IS NOT NULL
            GROUP BY ward
            ORDER BY spaces DESC
        """)
        ward_stats = cur.fetchall()
        
        cur.close()
        conn.close()
        
        return jsonify({
            "status": "success",
            "stats": {
                "total_spaces": total_spaces,
                "total_area_hectares": round(total_area / 10000, 2),
                "feedback": feedback_stats,
                "ward_distribution": ward_stats
            }
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ========================================
# ENVIRONMENTAL MONITORING ENDPOINTS
# ========================================

@app.route('/api/environmental/metrics')
def environmental_metrics():
    """Get environmental monitoring metrics."""
    try:
        # Mock environmental data
        metrics = {
            "air_quality": {
                "pm25": 12.5,
                "pm10": 25.3,
                "aqi": 45,
                "status": "Good",
                "last_updated": datetime.datetime.now().isoformat()
            },
            "temperature": {
                "current": 28.5,
                "min": 22.3,
                "max": 32.1,
                "avg": 26.8,
                "trend": "stable"
            },
            "biodiversity": {
                "tree_species": 42,
                "bird_species": 28,
                "butterfly_species": 15,
                "status": "Moderate"
            },
            "water_quality": {
                "ph": 7.2,
                "turbidity": 5.8,
                "dissolved_oxygen": 8.4,
                "status": "Good"
            }
        }
        
        return jsonify({"status": "success", "metrics": metrics})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ========================================
# REPORT GENERATOR ENDPOINTS
# ========================================

@app.route('/api/reports/generate', methods=['POST'])
def generate_report():
    """Generate a custom report."""
    try:
        data = request.json
        report_type = data.get('type', 'summary')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        if report_type == 'summary':
            # Summary report
            cur.execute("""
                SELECT 
                    COUNT(*) as total_spaces,
                    COALESCE(SUM(area_sq_m), 0) as total_area,
                    COUNT(DISTINCT ward) as total_wards
                FROM green_spaces
            """)
            summary = cur.fetchone()
            
            cur.execute("""
                SELECT 
                    type,
                    COUNT(*) as count,
                    SUM(area_sq_m) as area
                FROM green_spaces
                GROUP BY type
                ORDER BY count DESC
            """)
            types = cur.fetchall()
            
            report_data = {
                "type": "summary",
                "generated_at": datetime.datetime.now().isoformat(),
                "summary": summary,
                "type_distribution": types
            }
            
        elif report_type == 'feedback':
            # Feedback report
            query = """
                SELECT 
                    f.*,
                    gs.name as green_space_name,
                    TO_CHAR(f.created_at, 'DD Mon YYYY') as date
                FROM public_feedback f
                LEFT JOIN green_spaces gs ON f.green_space_id = gs.id
            """
            
            if start_date and end_date:
                query += f" WHERE f.created_at BETWEEN '{start_date}' AND '{end_date}'"
            
            query += " ORDER BY f.created_at DESC"
            
            cur.execute(query)
            feedback = cur.fetchall()
            
            # Count by status
            cur.execute("""
                SELECT 
                    status,
                    COUNT(*) as count
                FROM public_feedback
                GROUP BY status
            """)
            status_counts = cur.fetchall()
            
            report_data = {
                "type": "feedback",
                "generated_at": datetime.datetime.now().isoformat(),
                "period": {"start": start_date, "end": end_date},
                "total_feedback": len(feedback),
                "status_distribution": status_counts,
                "feedback": feedback
            }
            
        else:
            return jsonify({"status": "error", "message": "Invalid report type"}), 400
        
        cur.close()
        conn.close()
        
        return jsonify({"status": "success", "report": report_data})
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


