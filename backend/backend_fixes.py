# Backend Fixes - Add these routes to your app.py
# Copy and paste these into backend/app.py

# ========================================
# ENVIRONMENTAL DATA ENDPOINTS
# ========================================

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

@app.route('/api/environmental-data')
def get_environmental_data():
    """Returns all environmental monitoring data."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute("""
            SELECT 
                e.*,
                gs.name as green_space_name,
                TO_CHAR(e.recorded_at, 'DD Mon YYYY HH24:MI') as formatted_date
            FROM environmental_data e
            LEFT JOIN green_spaces gs ON e.green_space_id = gs.id
            ORDER BY e.recorded_at DESC
            LIMIT 100
        """)
        
        data = cur.fetchall()
        cur.close()
        conn.close()
        
        return jsonify(data)
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/submit-environmental-data', methods=['POST'])
def submit_environmental_data():
    """Submit new environmental monitoring data."""
    try:
        data = request.json
        
        location = data.get('location')
        air_quality = data.get('air_quality')
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        noise_level = data.get('noise_level')
        green_space_id = data.get('green_space_id')
        notes = data.get('notes')
        
        if not location:
            return jsonify({"status": "error", "message": "Location is required"}), 400
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("""
            INSERT INTO environmental_data 
            (location, air_quality, temperature, humidity, noise_level, green_space_id, notes)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (location, air_quality, temperature, humidity, noise_level, green_space_id, notes))
        
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({
            "status": "success",
            "message": "Environmental data recorded successfully",
            "id": new_id
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ========================================
# DASHBOARD ENDPOINTS
# ========================================

@app.route('/api/dashboard/recent-activity')
def get_recent_activity():
    """Returns recent activity across the system."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        activities = []
        
        # Get recent green spaces added
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
        
        # Get recent feedback
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
        
        # Get recent environmental data
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
        
        # Sort all activities by timestamp
        activities.sort(key=lambda x: x['timestamp'] if x['timestamp'] else '', reverse=True)
        
        cur.close()
        conn.close()
        
        return jsonify(activities[:20])  # Return top 20 most recent
        
    except Exception as e:
        # Return empty array if tables don't exist yet
        return jsonify([])

@app.route('/api/dashboard/stats')
def get_dashboard_stats():
    """Returns comprehensive dashboard statistics."""
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        stats = {}
        
        # Green spaces stats
        cur.execute("SELECT COUNT(*) as total FROM green_spaces")
        stats['total_spaces'] = cur.fetchone()['total']
        
        cur.execute("SELECT COALESCE(SUM(area_sq_m), 0) as total FROM green_spaces")
        stats['total_area'] = cur.fetchone()['total']
        
        # Feedback stats
        try:
            cur.execute("SELECT COUNT(*) as total FROM public_feedback")
            stats['total_feedback'] = cur.fetchone()['total']
            
            cur.execute("SELECT COUNT(*) as total FROM public_feedback WHERE status = 'pending'")
            stats['pending_feedback'] = cur.fetchone()['total']
        except:
            stats['total_feedback'] = 0
            stats['pending_feedback'] = 0
        
        # Environmental data stats
        try:
            cur.execute("SELECT COUNT(*) as total FROM environmental_data")
            stats['total_environmental'] = cur.fetchone()['total']
        except:
            stats['total_environmental'] = 0
        
        # Visitors (placeholder - you can implement actual tracking)
        stats['total_visitors'] = 0
        
        cur.close()
        conn.close()
        
        return jsonify(stats)
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ========================================
# FIXED FEEDBACK ENDPOINT (Remove duplicate)
# ========================================

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
                TO_CHAR(f.created_at, 'DD Mon YYYY HH24:MI') as formatted_date
            FROM public_feedback f
            LEFT JOIN green_spaces gs ON f.green_space_id = gs.id
            ORDER BY f.created_at DESC
        """)
        
        feedback = cur.fetchall()
        cur.close()
        conn.close()
        
        return jsonify(feedback)
        
    except Exception as e:
        # Return empty array if table doesn't exist
        return jsonify([])
