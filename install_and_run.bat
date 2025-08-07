@echo off
echo ========================================
echo    Digital Dear Diary - Setup Script
echo ========================================
echo.

echo Step 1: Installing Python dependencies...
pip install Flask==2.3.3 Flask-SQLAlchemy==3.0.5 Flask-Login==0.6.3 Werkzeug==2.3.7 TextBlob==0.17.1 python-dotenv==1.0.0

echo.
echo Step 2: Starting the application...
echo.
echo The application will be available at: http://localhost:5000
echo Press Ctrl+C to stop the application
echo.

python app.py

pause 