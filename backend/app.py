from flask import Flask, jsonify
from flask_cors import CORS

from routes.chat import chat_bp

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": "http://localhost:5173"
    }
})

app.register_blueprint(chat_bp)

@app.route("/")
def home():
    return jsonify({'reply':'Hi Niru'})

if __name__ == "__main__":
    app.run(debug=True)