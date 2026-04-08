#!/usr/bin/env python3
"""
PythonAnywhere deployment setup script
Run this after uploading your code to PythonAnywhere
"""

import os
import sys

def setup_pythonanywhere():
    print("🐍 PythonAnywhere Setup Guide")
    print("=" * 50)
    
    print("\n1. Upload your code:")
    print("   - Use the Files tab to upload your project")
    print("   - Or clone from GitHub in a Bash console:")
    print("   git clone https://github.com/zluyongile-dot/kitwe-green-spaces.git")
    
    print("\n2. Install dependencies:")
    print("   pip3.10 install --user -r requirements.txt")
    
    print("\n3. Set up database:")
    print("   - Go to Databases tab")
    print("   - Create a PostgreSQL database")
    print("   - Note the connection details")
    
    print("\n4. Configure web app:")
    print("   - Go to Web tab")
    print("   - Create new web app (Flask)")
    print("   - Set source code: /home/yourusername/kitwe-green-spaces")
    print("   - Set working directory: /home/yourusername/kitwe-green-spaces")
    print("   - WSGI file: /home/yourusername/mysite/flask_app.py")
    
    print("\n5. Update WSGI file:")
    wsgi_content = '''
import sys
import os

# Add your project directory to Python path
project_home = '/home/yourusername/kitwe-green-spaces'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variables
os.environ['DATABASE_URL'] = 'postgresql://username:password@host:port/database'

# Import your Flask app
from backend.app import app as application

if __name__ == "__main__":
    application.run()
'''
    print(f"   Content: {wsgi_content}")
    
    print("\n6. Your app will be available at:")
    print("   https://yourusername.pythonanywhere.com")

if __name__ == "__main__":
    setup_pythonanywhere()