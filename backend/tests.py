from flask import Flask
from werkzeug.security import generate_password_hash
import psycopg2
from flask_cors import CORS
import secrets
import datetime

print("✅ All imports successful!")
print(f"Werkzeug hash test: {generate_password_hash('test')[:30]}...")