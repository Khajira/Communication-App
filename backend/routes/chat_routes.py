from flask import Blueprint, request, jsonify
from backend.models.message import Message
from backend.app import db

chat_bp = Blueprint("chat", __name__)

@chat_bp.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.all()
    return jsonify([message.to_dict() for message in messages])

@chat_bp.route('/messages', methods=['POST'])
def post_message():
    data = request.json
    new_message = Message(username=data["username"], content=data["content"])
    db.session.add(new_message)
    db.session.commit()
    return jsonify(new_message.to_dict()), 201
