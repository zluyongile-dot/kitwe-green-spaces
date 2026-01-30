#!/usr/bin/env python3
"""
AWS Deployment Script for Kitwe Green Spaces
Automates the deployment process to AWS Elastic Beanstalk
"""

import os
import sys
import subprocess
import json

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return None

def check_prerequisites():
    """Check if all prerequisites are met"""
    print("🔍 Checking prerequisites...")
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("❌ .env file not found. Please create it from .env.template")
        return False
    
    # Check AWS CLI
    if not run_command('aws --version', 'AWS CLI check'):
        return False
    
    # Check EB CLI
    if not run_command('eb --version', 'EB CLI check'):
        return False
    
    # Check if AWS credentials are configured
    if not run_command('aws sts get-caller-identity', 'AWS credentials check'):
        print("❌ AWS credentials not configured. Run: aws configure")
        return False
    
    print("✅ All prerequisites met")
    return True

def deploy_to_aws():
    """Deploy application to AWS"""
    print("🚀 Starting AWS deployment...")
    
    if not check_prerequisites():
        return False
    
    # Initialize EB if not already done
    if not os.path.exists('.elasticbeanstalk'):
        print("🔧 Initializing Elastic Beanstalk...")
        if not run_command('eb init -p python-3.9 kitwe-green-spaces --region us-east-1', 'EB initialization'):
            return False
    
    # Check if environment exists
    result = run_command('eb list', 'Checking EB environments')
    if result and 'kitwe-production' not in result:
        print("🏗️ Creating production environment...")
        if not run_command('eb create kitwe-production --database.engine postgres --database.username postgres', 'Environment creation'):
            return False
    
    # Deploy application
    print("📦 Deploying application...")
    if not run_command('eb deploy', 'Application deployment'):
        return False
    
    # Get application URL
    result = run_command('eb status', 'Getting application status')
    if result:
        print("🎉 Deployment successful!")
        print("📋 Application Status:")
        print(result)
        
        # Extract URL from status
        for line in result.split('\n'):
            if 'CNAME:' in line:
                url = line.split('CNAME:')[1].strip()
                print(f"🌐 Your backend URL: https://{url}")
                print(f"🔧 Update frontend config: python update_backend_url.py https://{url}")
                break
    
    return True

def main():
    """Main deployment function"""
    print("🌳 Kitwe Green Spaces - AWS Deployment")
    print("=" * 40)
    
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("Usage: python deploy_aws.py")
        print("\nThis script will:")
        print("1. Check prerequisites (AWS CLI, EB CLI, credentials)")
        print("2. Initialize Elastic Beanstalk if needed")
        print("3. Create production environment with PostgreSQL")
        print("4. Deploy your Flask application")
        print("5. Provide the backend URL for frontend configuration")
        return
    
    try:
        if deploy_to_aws():
            print("\n🎉 Deployment completed successfully!")
            print("📚 Next steps:")
            print("1. Update your frontend config with the provided URL")
            print("2. Test your API endpoints")
            print("3. Monitor your application in AWS Console")
        else:
            print("\n❌ Deployment failed. Check the errors above.")
            
    except KeyboardInterrupt:
        print("\n⏹️ Deployment cancelled by user")
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")

if __name__ == "__main__":
    main()