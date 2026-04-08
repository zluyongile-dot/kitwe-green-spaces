#!/usr/bin/env python3
"""
Simple AWS Configuration Helper
"""
import os
import subprocess

def configure_aws():
    print("🔧 AWS Configuration Helper")
    print("=" * 30)
    
  what  print("\n📋 You need to get your AWS credentials from:")
    print("1. Go to AWS Console → IAM → Users → Your User")
    print("2. Security credentials tab → Create access key")
    print("3. Select 'Command Line Interface (CLI)'")
    print("4. Copy both Access Key ID and Secret Access Key")
    
    print("\n⚠️  Important: Use your REAL AWS credentials, not placeholder values!")
    
    access_key = input("\n🔑 Enter your AWS Access Key ID: ").strip()
    secret_key = input("🔐 Enter your AWS Secret Access Key: ").strip()
    
    if not access_key or not secret_key:
        print("❌ Both credentials are required!")
        return False
    
    if access_key == "085233" or secret_key == "085233":
        print("❌ Please use your real AWS credentials, not placeholder values!")
        return False
    
    # Configure AWS CLI
    try:
        subprocess.run(['aws', 'configure', 'set', 'aws_access_key_id', access_key], check=True)
        subprocess.run(['aws', 'configure', 'set', 'aws_secret_access_key', secret_key], check=True)
        subprocess.run(['aws', 'configure', 'set', 'region', 'us-east-1'], check=True)
        subprocess.run(['aws', 'configure', 'set', 'output', 'json'], check=True)
        
        print("✅ AWS CLI configured successfully!")
        
        # Test the configuration
        print("\n🧪 Testing AWS connection...")
        result = subprocess.run(['aws', 'sts', 'get-caller-identity'], 
                              capture_output=True, text=True, check=True)
        
        print("✅ AWS connection successful!")
        print("📋 Your AWS Account Info:")
        print(result.stdout)
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ AWS configuration failed: {e}")
        if "SignatureDoesNotMatch" in str(e):
            print("💡 This usually means the credentials are incorrect.")
            print("   Please double-check your Access Key ID and Secret Access Key.")
        return False

if __name__ == "__main__":
    configure_aws()