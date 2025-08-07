# Digital Dear Diary

A modern, AI-powered digital journaling application built with Python Flask, featuring voice-to-text transcription, emotion detection, and beautiful themes.

## 🌟 Features

- **Voice-to-Text Transcription**: Dictate your thoughts using your browser's microphone
- **Emotion Detection**: AI-powered sentiment analysis to understand your mood
- **Beautiful Themes**: Light and dark theme options
- **User Authentication**: Secure login and registration system
- **Entry Management**: Create, view, and delete journal entries
- **Export Functionality**: Download your entries as JSON
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Modern UI**: Clean, elegant interface with Bootstrap 5

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd Digital_Dear_Diary
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   - Go to: `http://localhost:5000`
   - Register a new account or login

## 📁 Project Structure

```
Digital_Dear_Diary/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template with common elements
│   ├── index.html        # Landing page
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   └── dashboard.html    # Main dashboard
└── diary.db             # SQLite database (created automatically)
```

## 🎯 Key Features Explained

### Voice-to-Text Transcription
- Uses the Web Speech API for real-time voice recognition
- Click the microphone button to start recording
- Automatically transcribes your speech to text
- Works in modern browsers (Chrome, Edge, Safari)

### Emotion Detection
- Powered by TextBlob for sentiment analysis
- Automatically detects emotions: Happy, Positive, Neutral, Negative, Sad
- Color-coded emotion badges for easy identification
- Helps you track your mood patterns over time

### Theme Switching
- Toggle between light and dark themes
- Persistent theme selection
- Modern gradient backgrounds
- Smooth transitions

### User Authentication
- Secure password hashing with Werkzeug
- Session-based authentication
- User-specific entries and data
- Protected routes and functionality

## 🛠️ Technical Details

### Backend
- **Framework**: Flask 2.3.3
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Emotion Analysis**: TextBlob
- **Password Security**: Werkzeug

### Frontend
- **CSS Framework**: Bootstrap 5.1.3
- **Icons**: Font Awesome 6.0.0
- **JavaScript**: Vanilla JS with Web Speech API
- **Responsive Design**: Mobile-first approach

### Database Schema
```sql
-- Users table
CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(120) NOT NULL
);

-- Entries table
CREATE TABLE entry (
    id INTEGER PRIMARY KEY,
    content TEXT NOT NULL,
    emotion VARCHAR(50) NOT NULL,
    theme VARCHAR(50) DEFAULT 'light',
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER FOREIGN KEY REFERENCES user(id)
);
```

## 🎨 Customization

### Adding New Themes
1. Add theme options in `templates/dashboard.html`
2. Define CSS classes in `templates/base.html`
3. Update the theme switching JavaScript

### Modifying Emotion Detection
1. Edit the `detect_emotion()` function in `app.py`
2. Adjust sentiment thresholds
3. Add new emotion categories

### Styling Changes
1. Modify CSS in `templates/base.html`
2. Update Bootstrap classes in templates
3. Customize color variables in `:root`

## 🔧 Troubleshooting

### Common Issues

1. **Speech Recognition Not Working**
   - Ensure you're using a modern browser (Chrome, Edge, Safari)
   - Check microphone permissions
   - Use HTTPS in production

2. **Database Errors**
   - Delete `diary.db` and restart the application
   - Check file permissions in the project directory

3. **Installation Issues**
   - Update pip: `pip install --upgrade pip`
   - Use virtual environment: `python -m venv venv`
   - Activate virtual environment before installing

### Browser Compatibility
- ✅ Chrome 66+
- ✅ Edge 79+
- ✅ Safari 14.1+
- ✅ Firefox (limited speech recognition support)

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment
1. Set `FLASK_ENV=production`
2. Use a production WSGI server (Gunicorn, uWSGI)
3. Configure a reverse proxy (Nginx, Apache)
4. Set up SSL certificates for HTTPS

### Environment Variables
```bash
export FLASK_ENV=production
export SECRET_KEY=your-secret-key-here
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the documentation

## 🎉 Acknowledgments

- Flask community for the excellent framework
- Bootstrap team for the responsive CSS framework
- TextBlob developers for the sentiment analysis library
- Web Speech API for voice recognition capabilities

---

**Happy Journaling! 📖✨** 