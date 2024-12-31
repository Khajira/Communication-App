import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Message
from routes import chat_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

app.register_blueprint(chat_bp, url_prefix="/api")

@socketio.on('send_message')
def handle_message(data):
    print(f"Message received: {data}")
    socketio.emit('receive_message', data)  # Broadcast to all clients

if __name__ == '__main__':
    db.create_all()  # Initialize the database

    socketio.run(app, debug=True)