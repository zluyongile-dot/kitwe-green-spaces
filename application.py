#!/usr/bin/env python3
"""
AWS Elastic Beanstalk entry point for Kitwe Green Spaces Backend
This file is required for EB deployment
"""

from backend.app import app

# EB looks for an 'application' callable by default
application = app

if __name__ == "__main__":
    # For local testing
    app.run(debug=False, host='0.0.0.0', port=5000)