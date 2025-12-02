# Deployment Guide

## Deploy on Render (Free)

1. **Sign up** at [render.com](https://render.com/)

2. **Create a New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `https://github.com/bishalthakur0/Railway-Management-System`
   - Click "Connect"

3. **Configure the Web Service**:
   - **Name**: `railway-management-system` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn lorax.wsgi:application`
   - **Instance Type**: `Free`

4. **Click "Create Web Service"**

5. **Wait for deployment** (takes 2-5 minutes)

6. **Access your app** at the provided Render URL (e.g., `https://railway-management-system.onrender.com`)

## Important Notes

⚠️ **Database Persistence**: Render's free tier uses ephemeral storage. Your SQLite database will reset when the service restarts (after 15 minutes of inactivity). For persistent data, consider upgrading to a paid plan or using PostgreSQL.

## Login Credentials

- **Username**: `thabishal0`
- **Password**: `1234567890`

## Alternative: PythonAnywhere (Recommended for SQLite)

For persistent SQLite database, use PythonAnywhere:

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com/)
2. Open a Bash console
3. Clone repo: `git clone https://github.com/bishalthakur0/Railway-Management-System.git`
4. Create virtualenv: `mkvirtualenv --python=/usr/bin/python3.10 railway`
5. Install deps: `pip install -r requirements.txt`
6. Go to Web tab → Add new web app → Manual configuration
7. Set source code path and virtualenv path
8. Edit WSGI file to point to your project
9. Reload the web app
