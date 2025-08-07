Write-Host "========================================" -ForegroundColor Green
Write-Host "    Digital Dear Diary - Setup Script" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

Write-Host "Step 1: Installing Python dependencies..." -ForegroundColor Yellow
pip install Flask==2.3.3 Flask-SQLAlchemy==3.0.5 Flask-Login==0.6.3 Werkzeug==2.3.7 TextBlob==0.17.1 python-dotenv==1.0.0

Write-Host ""
Write-Host "Step 2: Starting the application..." -ForegroundColor Yellow
Write-Host ""
Write-Host "The application will be available at: http://localhost:5000" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the application" -ForegroundColor Yellow
Write-Host ""

python app.py 