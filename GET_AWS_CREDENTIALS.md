# 🔑 How to Get Your AWS Credentials

## Step 1: Go to AWS Console
1. Open your browser and go to: https://aws.amazon.com/console/
2. Sign in with your AWS account

## Step 2: Navigate to IAM
1. In the AWS Console, search for "IAM" in the search bar
2. Click on "IAM" (Identity and Access Management)

## Step 3: Create Access Keys
1. In the left sidebar, click on "Users"
2. Click on your username (the user you created)
3. Click on the "Security credentials" tab
4. Scroll down to "Access keys" section
5. Click "Create access key"
6. Select "Command Line Interface (CLI)"
7. Check the confirmation box and click "Next"
8. Add a description (optional): "Kitwe Green Spaces Deployment"
9. Click "Create access key"

## Step 4: Copy Your Credentials
You'll see:
- **Access Key ID**: Something like `AKIAIOSFODNN7EXAMPLE`
- **Secret Access Key**: Something like `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

**IMPORTANT**: Copy both values immediately! The secret key won't be shown again.

## Step 5: Configure AWS CLI
Run this command and enter your real credentials:
```bash
aws configure
```

Enter:
- **AWS Access Key ID**: Your actual access key from step 4
- **AWS Secret Access Key**: Your actual secret key from step 4  
- **Default region name**: `us-east-1` (recommended for free tier)
- **Default output format**: `json`

## Step 6: Test Configuration
```bash
aws sts get-caller-identity
```

This should return your AWS account information if configured correctly.

---

## ⚠️ Security Notes
- Never share your AWS credentials
- Don't commit them to GitHub
- Keep them secure and private
- You can always create new ones if needed