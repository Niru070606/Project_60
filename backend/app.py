from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config
from database import db

from routes.chat import chat_bp
from routes.personality import personality_bp
from routes.memory import memory_bp
from routes.analytics import analytics_bp
from models.conversation import Conversation
from models.chat_session import ChatSession
from models.message import Message
from models.memory import Memory
from models.relationship import Relationship
from models.entity import Entity
from models.memory_entity import MemoryEntity

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

# CORS
CORS(
    app,
    resources={
        r"/*": {
            "origins": "http://localhost:5173"
        }
    }
)

# Route
app.register_blueprint(chat_bp)
app.register_blueprint(personality_bp)
app.register_blueprint(memory_bp)
app.register_blueprint(analytics_bp)

@app.route("/")
def home():
    return jsonify({"reply": "Hi Niru"})

if __name__ == "__main__":
    app.run(debug=True)