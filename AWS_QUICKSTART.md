# ⚡ AWS Quick Start - 15 Minutes to Live Backend

## 🎯 **What You'll Get**
- ✅ **Live Flask backend** on AWS (FREE for 12 months)
- ✅ **PostgreSQL database** with your 51 green spaces
- ✅ **Professional URL** for your API
- ✅ **Real-time data** for your GitHub Pages frontend

---

## 🚀 **Super Quick Deployment (5 Commands)**

### **Prerequisites:**
- AWS account (free tier)
- Python installed
- Your project files

### **Step 1: Install AWS Tools**
```bash
pip install awscli awsebcli
```

### **Step 2: Configure AWS**
```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key  
# Region: us-east-1
# Output format: json
```

### **Step 3: Setup Environment**
```bash
python aws_setup.py
# Copy .env.template to .env and configure
```

### **Step 4: Deploy to AWS**
```bash
python deploy_aws.py
```

### **Step 5: Update Frontend**
```bash
# Use the URL provided by the deployment script
python update_backend_url.py https://your-eb-url.elasticbeanstalk.com
git add . && git commit -m "Connected to AWS backend" && git push
```

**🎉 Done! Your website now has a live backend!**

---

## 📋 **Detailed Steps**

### **1. Get AWS Credentials**
1. Go to **AWS Console** → **IAM** → **Users** → **Your User**
2. **Security credentials** tab
3. **Create access key** → **Command Line Interface (CLI)**
4. **Download** or copy the keys

### **2. Configure Environment**
Create `.env` file:
```bash
DATABASE_URL=postgresql://postgres:yourpassword@your-rds.amazonaws.com:5432/kitwe_green_spaces
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here
```

### **3. Deploy Commands**
```bash
# Initialize (first time only)
eb init -p python-3.9 kitwe-green-spaces

# Create environment with database
eb create kitwe-production --database.engine postgres

# Deploy your code
eb deploy

# Get your URL
eb status
```

---

## 💰 **AWS Free Tier Limits**

### **What's FREE for 12 months:**
- **EC2**: 750 hours/month (24/7 for 1 instance)
- **RDS**: 750 hours/month + 20GB storage
- **Elastic Beanstalk**: FREE (just pay for underlying resources)
- **Data Transfer**: 15GB/month outbound

### **Estimated Monthly Cost:**
- **Months 1-12**: $0.00 (Free Tier)
- **After 12 months**: ~$15-25/month

---

## 🔧 **Troubleshooting**

### **Common Issues:**

**1. "AWS credentials not configured"**
```bash
aws configure
# Enter your access keys
```

**2. "Database connection failed"**
```bash
# Check your .env file DATABASE_URL
# Ensure RDS security group allows connections
```

**3. "EB CLI not found"**
```bash
pip install awsebcli
```

**4. "Deployment failed"**
```bash
eb logs
# Check the logs for specific errors
```

### **Useful Commands:**
```bash
# Check deployment status
eb status

# View application logs
eb logs

# Open AWS console for your app
eb console

# Redeploy after changes
eb deploy
 
# Terminate environment (to save costs)
eb terminate kitwe-production
```

---

## 🎯 **Expected Results**

### **After Deployment:**
1. **Backend URL**: `https://kitwe-production.us-east-1.elasticbeanstalk.com`
2. **API Endpoints**:
   - `GET /api/green-spaces` - All green spaces
   - `GET /test-db` - Database health check
   - `GET /api/environmental-data` - Environmental monitoring

3. **Database**: PostgreSQL with PostGIS extension and your 51 green spaces

### **Frontend Integration:**
Your GitHub Pages site will automatically connect to the AWS backend for real-time data!

---

## 🔄 **Switching from Static to Live Backend**

Once deployed, your frontend will automatically detect it's on GitHub Pages and use the AWS backend URL. No manual switching needed!

---

## 📊 **Monitoring Your Deployment**

### **AWS Console Locations:**
- **Elastic Beanstalk**: Monitor app health and logs
- **RDS**: Database performance and connections  
- **CloudWatch**: Detailed metrics and alerts
- **Billing**: Track your free tier usage

### **Health Checks:**
- Visit: `https://your-url.elasticbeanstalk.com/test-db`
- Should return: `{"status": "Database connection successful"}`

---

## 🆘 **Need Help?**

### **If deployment fails:**
1. Check `eb logs` for error details
2. Verify your `.env` file configuration
3. Ensure AWS credentials are correct
4. Check AWS service limits

### **If database connection fails:**
1. Verify DATABASE_URL in `.env`
2. Check RDS security group settings
3. Ensure PostGIS extension is installed

---

## 🎉 **Success Checklist**

- [ ] AWS account created and verified
- [ ] AWS CLI configured with credentials
- [ ] EB CLI installed
- [ ] Environment variables configured in `.env`
- [ ] Application deployed successfully
- [ ] Database connection working
- [ ] Frontend updated with backend URL
- [ ] All API endpoints responding

**🚀 Your Kitwe Green Spaces project is now live on AWS!**