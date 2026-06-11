#!/usr/bin/env python3
"""
Test script to verify all backend API endpoints are working.
Run this after starting the Flask server.
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_endpoint(endpoint, method="GET", data=None):
    """Test a single endpoint."""
    url = f"{BASE_URL}{endpoint}"
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        else:
            return False, f"Unsupported method: {method}"
        
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, f"Status {response.status_code}: {response.text}"
            
    except requests.exceptions.ConnectionError:
        return False, "Connection failed - is the server running?"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    print("=" * 60)
    print("Testing Kitwe Green Spaces Backend API Endpoints")
    print("=" * 60)
    
    # Test basic endpoints
    endpoints = [
        ("/", "GET", None, "Home page"),
        ("/test-db", "GET", None, "Database connection test"),
        ("/api/green-spaces", "GET", None, "Get all green spaces"),
        ("/api/dashboard/simple-stats", "GET", None, "Dashboard statistics"),
        ("/api/analytics/summary", "GET", None, "Analytics summary"),
        ("/api/analytics/coverage", "GET", None, "Ward coverage data"),
        ("/api/analytics/trends", "GET", None, "Trends data"),
        ("/api/environmental-data", "GET", None, "Environmental monitoring data"),
        ("/api/feedback", "GET", None, "Get all feedback"),
    ]
    
    all_passed = True
    for endpoint, method, data, description in endpoints:
        print(f"\nTesting: {description}")
        print(f"Endpoint: {endpoint}")
        
        success, result = test_endpoint(endpoint, method, data)
        
        if success:
            print(f"✅ SUCCESS")
            if isinstance(result, dict) and "status" in result:
                print(f"   Status: {result.get('status', 'N/A')}")
            if endpoint == "/api/green-spaces" and isinstance(result, dict):
                features = result.get("features", [])
                print(f"   Green spaces found: {len(features)}")
        else:
            print(f"❌ FAILED: {result}")
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ All endpoints tested successfully!")
        print("\nNext steps:")
        print("1. Add sample data: Visit /add-sample-green-spaces")
        print("2. Create tables: Visit /create-green-spaces-table")
        print("3. Create feedback table: Visit /create-feedback-table")
        print("4. Create users table: Visit /create-users-table")
    else:
        print("⚠️ Some endpoints failed. Check the Flask server logs.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()