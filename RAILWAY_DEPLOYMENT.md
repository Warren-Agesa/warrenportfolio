# Deployment Guide - Railway Hosting

This guide will help you deploy your Warren Karanja portfolio to Railway.

## Prerequisites
- GitHub account
- Railway account (https://railway.app)
- Git installed on your computer

## Step 1: Prepare Your Project

✅ **Already Done:**
- ✅ Created `requirements.txt` - All Python dependencies
- ✅ Created `Procfile` - Instructions for Railway
- ✅ Created `runtime.txt` - Python version specification
- ✅ Created `.gitignore` - Files to exclude from Git
- ✅ Updated `settings.py` - Production-ready configuration

## Step 2: Initialize Git and Push to GitHub

```powershell
# Navigate to your project directory
cd c:\Users\LENOVO\warrenportfolio

# Initialize git
git init

# Add all files
git add .

# Commit your changes
git commit -m "Initial commit - Portfolio ready for deployment"

# Add GitHub remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Set Up Railway Project

1. Go to https://railway.app and sign in
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Authorize Railway to access your GitHub
5. Select your portfolio repository
6. Railway will auto-detect it's a Django project

## Step 4: Configure Environment Variables on Railway

In your Railway project dashboard, add these environment variables:

### Required Variables:

```
SECRET_KEY=your_random_secret_key_here
DEBUG=False
ALLOWED_HOSTS=your-railway-domain.up.railway.app
```

To generate a good SECRET_KEY, run:
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Database Variables (Railway will add automatically):
- `DATABASE_URL` - Auto-generated when you add PostgreSQL plugin

### Email Variables (Optional but recommended):

```
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=your_email@gmail.com
```

**Note:** For Gmail, use an App Password, not your regular password:
1. Go to https://myaccount.google.com/apppasswords
2. Select Mail and Windows Computer
3. Google will generate a 16-character password
4. Use that password for EMAIL_HOST_PASSWORD

## Step 5: Add PostgreSQL Database

1. In Railway Dashboard, click "Add Service"
2. Select "PostgreSQL"
3. Railway will automatically link the `DATABASE_URL`

## Step 6: Deploy

1. Push changes to GitHub:
```powershell
git add .
git commit -m "Update for Railway deployment"
git push
```

2. Railway auto-deploys on push
3. Wait for the build to complete (usually 2-3 minutes)
4. Check "Deployments" tab for status

## Step 7: Run Migrations

After the first deployment:
1. Click "View Logs" to see deployment status
2. Migrations run automatically via the `release` command in Procfile
3. Check logs for any errors

## Step 8: Test Your Site

1. Go to the Railway project dashboard
2. Click your web service
3. Look for "Public URL" or "Open URL"
4. Visit your site!

## Common Issues & Solutions

### Issue: Static Files Not Loading
✅ Already fixed with WhiteNoise in settings.py

### Issue: Database Connection Error
- Verify DATABASE_URL is set in Railway
- Check PostgreSQL service is running
- Run migrations: Check deployment logs

### Issue: 500 Error
- Check deployment logs in Railway dashboard
- Verify all environment variables are set
- Ensure DEBUG=False in production

### Issue: Images Not Uploading
- Railway uses ephemeral storage (files deleted on redeploy)
- Solution: Set up cloud storage (AWS S3, Cloudinary, etc.)
- For now, images must be uploaded and persisted

## Updating Your Site After Deployment

1. Make changes locally
2. Run migrations if needed:
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Test locally:
   ```powershell
   python manage.py runserver
   ```
4. Push to GitHub:
   ```powershell
   git add .
   git commit -m "Your message"
   git push
   ```
5. Railway auto-deploys!

## Domain Setup (Optional)

If you have a custom domain:
1. In Railway, go to Settings → Domains
2. Add your domain
3. Update DNS records with Railway's provided values

## Support

- Railway Docs: https://docs.railway.app
- Django Deployment: https://docs.djangoproject.com/en/5.1/howto/deployment/
- Email Help: https://support.google.com/accounts/answer/185833

---

**You're all set!** Your portfolio is ready to deploy to Railway. 🚀
