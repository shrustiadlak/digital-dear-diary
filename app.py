from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from textblob import TextBlob
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    entries = db.relationship('Entry', backref='author', lazy=True)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    emotion = db.Column(db.String(50), nullable=False)
    theme = db.Column(db.String(50), default='light')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def detect_emotion(text):
    """Detect emotion using TextBlob sentiment analysis"""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.3:
        return 'Happy'
    elif polarity > 0:
        return 'Positive'
    elif polarity < -0.3:
        return 'Sad'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email, 
                   password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    entries = Entry.query.filter_by(user_id=current_user.id).order_by(Entry.date_created.desc()).all()
    return render_template('dashboard.html', entries=entries)

@app.route('/save-entry', methods=['POST'])
@login_required
def save_entry():
    data = request.get_json()
    content = data.get('content', '').strip()
    theme = data.get('theme', 'light')
    
    if not content:
        return jsonify({'success': False, 'message': 'Entry cannot be empty'})
    
    emotion = detect_emotion(content)
    
    entry = Entry(content=content, emotion=emotion, theme=theme, user_id=current_user.id)
    db.session.add(entry)
    db.session.commit()
    
    return jsonify({
        'success': True, 
        'message': 'Entry saved successfully!',
        'entry': {
            'id': entry.id,
            'content': entry.content,
            'emotion': entry.emotion,
            'theme': entry.theme,
            'date': entry.date_created.strftime('%Y-%m-%d %H:%M')
        }
    })

@app.route('/get-entries')
@login_required
def get_entries():
    entries = Entry.query.filter_by(user_id=current_user.id).order_by(Entry.date_created.desc()).all()
    entries_data = []
    for entry in entries:
        entries_data.append({
            'id': entry.id,
            'content': entry.content,
            'emotion': entry.emotion,
            'theme': entry.theme,
            'date': entry.date_created.strftime('%Y-%m-%d %H:%M')
        })
    return jsonify(entries_data)

@app.route('/delete-entry/<int:entry_id>', methods=['DELETE'])
@login_required
def delete_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    if entry.user_id == current_user.id:
        db.session.delete(entry)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Entry deleted successfully'})
    return jsonify({'success': False, 'message': 'Unauthorized'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 