from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate


from database import db

from routes.chat import chat_bp
from routes.personality import personality_bp
from routes.memory import memory_bp
from models.conversation import Conversation
from models.chat_session import ChatSession
from models.message import Message
from models.memory import Memory

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:@localhost/project60"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

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

@app.route("/")
def home():
    return jsonify({"reply": "Hi Niru"})

if __name__ == "__main__":
    app.run(debug=True)