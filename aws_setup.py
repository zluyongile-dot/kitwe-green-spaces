#!/usr/bin/env python3
"""
AWS Setup Helper Script for Kitwe Green Spaces
Run this script to help configure your AWS deployment
"""

import os
import sys
import subprocess

def check_aws_cli():
    """Check if AWS CLI is installed"""
    try:
        result = subprocess.run(['aws', '--version'], capture_output=True, text=True)
        print(f"✅ AWS CLI found: {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print("❌ AWS CLI not found. Please install it:")
        print("   Windows: https://aws.amazon.com/cli/")
        print("   Or run: pip install awscli")
        return False

def check_eb_cli():
    """Check if EB CLI is installed"""
    try:
        result = subprocess.run(['eb', '--version'], capture_output=True, text=True)
        print(f"✅ EB CLI found: {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print("❌ EB CLI not found. Installing...")
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'awsebcli'], check=True)
            print("✅ EB CLI installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install EB CLI. Please install manually:")
            print("   pip install awsebcli")
            return False

def create_env_template():
    """Create environment template file"""
    env_content = """# AWS Environment Variables for Kitwe Green Spaces
# Copy this to .env and fill in your actual values

# Database Configuration
DATABASE_URL=postgresql://username:password@your-rds-endpoint:5432/kitwe_green_spaces

# Flask Configuration
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-change-this-in-production

# AWS Configuration (optional)
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key

# CORS Configuration
CORS_ORIGINS=https://zluyongile-dot.github.io,https://your-custom-domain.com
"""
    
    with open('.env.template', 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env.template - copy to .env and configure your values")

def setup_aws_deployment():
    """Main setup function"""
    print("🚀 AWS Deployment Setup for Kitwe Green Spaces")
    print("=" * 50)
    
    # Check prerequisites
    aws_ok = check_aws_cli()
    eb_ok = check_eb_cli()
    
    if not aws_ok:
        print("\n❌ Please install AWS CLI first, then run this script again")
        return False
    
    if not eb_ok:
        print("\n❌ EB CLI installation failed. Please install manually")
        return False
    
    # Create environment template
    create_env_template()
    
    print("\n🎯 Next Steps:")
    print("1. Configure AWS credentials: aws configure")
    print("2. Copy .env.template to .env and fill in your values")
    print("3. Create RDS PostgreSQL database in AWS Console")
    print("4. Run: eb init -p python-3.9 kitwe-green-spaces")
    print("5. Run: eb create kitwe-production")
    print("6. Run: eb deploy")
    
    print("\n📚 Full guide: AWS_DEPLOYMENT_GUIDE.md")
    
    return True

if __name__ == "__main__":
    setup_aws_deployment()