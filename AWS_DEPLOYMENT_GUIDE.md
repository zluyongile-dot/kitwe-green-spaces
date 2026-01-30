# 🚀 AWS Deployment Guide - Kitwe Green Spaces Backend

## 📋 **AWS Free Tier Overview**
- **EC2**: 750 hours/month of t2.micro instances (enough for 24/7)
- **RDS**: 750 hours/month of db.t2.micro + 20GB storage
- **S3**: 5GB storage + 20,000 GET requests
- **Valid for 12 months** from signup

---

## 🎯 **Recommended AWS Architecture**

### **Option 1: EC2 + RDS (Recommended)**
- **EC2 t2.micro**: Host Flask application
- **RDS PostgreSQL**: Database with PostGIS
- **Route 53**: Custom domain (optional)
- **Total Cost**: FREE for 12 months

### **Option 2: Elastic Beanstalk (Easier)**
- **Elastic Beanstalk**: Managed Flask deployment
- **RDS PostgreSQL**: Integrated database
- **Total Cost**: FREE for 12 months

---

## 🚀 **Method 1: EC2 + RDS (Full Control)**

### **Step 1: Create RDS PostgreSQL Database**

1. **Go to RDS Console**: https://console.aws.amazon.com/rds/
2. **Create Database**:
   - Engine: **PostgreSQL**
   - Version: **13.x or 14.x**
   - Template: **Free tier**
   - Instance: **db.t2.micro**
   - Storage: **20 GB** (free tier limit)
   - Database name: `kitwe_green_spaces`
   - Username: `postgres`
   - Password: `[your-secure-password]`
   - **Public access**: Yes (for now)
   - **Security group**: Create new (allow PostgreSQL port 5432)

3. **Enable PostGIS Extension**:
   ```sql
   -- Connect to your database and run:
   CREATE EXTENSION postgis;
   ```

### **Step 2: Create EC2 Instance**

1. **Go to EC2 Console**: https://console.aws.amazon.com/ec2/
2. **Launch Instance**:
   - AMI: **Ubuntu Server 22.04 LTS**
   - Instance type: **t2.micro** (free tier)
   - Key pair: Create new or use existing
   - Security group: Allow HTTP (80), HTTPS (443), SSH (22)
   - Storage: **8 GB** (free tier)

3. **Connect to Instance**:
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-public-ip
   ```

### **Step 3: Setup EC2 Instance**

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3 python3-pip python3-venv nginx git postgresql-client -y

# Clone your repository
git clone https://github.com/zluyongile-dot/kitwe-green-spaces.git
cd kitwe-green-spaces

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Install additional production dependencies
pip install gunicorn psycopg2-binary

# Create environment file
nano .env
```

### **Step 4: Configure Environment Variables**

Create `.env` file:
```bash
DATABASE_URL=postgresql://postgres:your-password@your-rds-endpoint:5432/kitwe_green_spaces
FLASK_ENV=production
SECRET_KEY=your-super-secret-key-here
```

### **Step 5: Setup Database**

```bash
# Test database connection
python3 -c "
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
print('Database connection successful!')
conn.close()
"

# Run your database setup script
python3 backend/insert_sample_data.py
```

### **Step 6: Configure Gunicorn**

Create `gunicorn.conf.py`:
```python
bind = "127.0.0.1:5000"
workers = 2
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 100
preload_app = True
```

### **Step 7: Create Systemd Service**

```bash
sudo nano /etc/systemd/system/kitwe-backend.service
```

Add:
```ini
[Unit]
Description=Kitwe Green Spaces Backend
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/kitwe-green-spaces
Environment=PATH=/home/ubuntu/kitwe-green-spaces/venv/bin
EnvironmentFile=/home/ubuntu/kitwe-green-spaces/.env
ExecStart=/home/ubuntu/kitwe-green-spaces/venv/bin/gunicorn --config gunicorn.conf.py backend.app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable kitwe-backend
sudo systemctl start kitwe-backend
sudo systemctl status kitwe-backend
```

### **Step 8: Configure Nginx**

```bash
sudo nano /etc/nginx/sites-available/kitwe-backend
```

Add:
```nginx
server {
    listen 80;
    server_name your-domain.com;  # Replace with your domain or EC2 public IP

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/kitwe-backend /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

---

## 🎈 **Method 2: Elastic Beanstalk (Easier)**

### **Step 1: Prepare Application**

Create `application.py` in root:
```python
from backend.app import app

if __name__ == "__main__":
    app.run()
```

Create `.ebextensions/01_packages.config`:
```yaml
packages:
  yum:
    postgresql-devel: []
    gcc: []
```

### **Step 2: Deploy with EB CLI**

```bash
# Install EB CLI
pip install awsebcli

# Initialize Elastic Beanstalk
eb init -p python-3.9 kitwe-green-spaces

# Create environment
eb create kitwe-production

# Deploy
eb deploy
```

### **Step 3: Add RDS Database**

```bash
# Add RDS to your EB environment
eb console
# Go to Configuration > Database
# Engine: PostgreSQL
# Instance class: db.t2.micro
# Storage: 20 GB
```

---

## 🔧 **Update Frontend Configuration**

Once your AWS backend is running, update your frontend:

```bash
# Get your AWS backend URL (EC2 public IP or EB URL)
# Example: http://ec2-xx-xx-xx-xx.compute-1.amazonaws.com
# Or: http://kitwe-production.us-east-1.elasticbeanstalk.com

# Update the config
python update_backend_url.py https://your-aws-backend-url.com
```

---

## 💰 **Cost Monitoring**

### **Free Tier Limits:**
- **EC2**: 750 hours t2.micro (1 instance 24/7)
- **RDS**: 750 hours db.t2.micro + 20GB storage
- **Data Transfer**: 15GB out per month
- **Elastic Load Balancer**: NOT free (avoid for now)

### **Stay Within Free Tier:**
- Use only **t2.micro** instances
- Keep RDS storage under **20GB**
- Monitor usage in **AWS Billing Dashboard**

---

## 🔒 **Security Best Practices**

### **Database Security:**
```bash
# Restrict RDS access to EC2 only
# Security Group: Allow 5432 only from EC2 security group
```

### **EC2 Security:**
```bash
# Update regularly
sudo apt update && sudo apt upgrade -y

# Configure firewall
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable
```

---

## 🚀 **Quick Start Commands**

```bash
# 1. Create RDS PostgreSQL database (Free Tier)
# 2. Launch EC2 t2.micro Ubuntu instance
# 3. SSH into EC2:
ssh -i your-key.pem ubuntu@your-ec2-ip

# 4. Run setup:
git clone https://github.com/zluyongile-dot/kitwe-green-spaces.git
cd kitwe-green-spaces
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt gunicorn psycopg2-binary

# 5. Configure environment and start service
# 6. Update frontend with your AWS URL
```

---

## 🆘 **Troubleshooting**

### **Common Issues:**
1. **Database connection fails**: Check security groups and RDS public access
2. **502 Bad Gateway**: Check if gunicorn service is running
3. **CORS errors**: Ensure Flask-CORS is configured properly

### **Useful Commands:**
```bash
# Check service status
sudo systemctl status kitwe-backend

# View logs
sudo journalctl -u kitwe-backend -f

# Test database connection
python3 -c "import psycopg2; conn = psycopg2.connect('your-db-url'); print('OK')"
```

---

## 🎯 **Expected Result**

After deployment, you'll have:
- ✅ **Live backend API** at your AWS URL
- ✅ **PostgreSQL database** with your 51 green spaces
- ✅ **Professional hosting** on AWS infrastructure
- ✅ **Free for 12 months** under AWS Free Tier
- ✅ **Scalable architecture** ready for production

Your GitHub Pages frontend will connect to the AWS backend for real-time data! 🚀