from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Allow all origins (good for frontend communication)

quotes = [
    {
        "quote": "Stay hungry, stay foolish.",
        "author": "Steve Jobs"
    },
    {
        "quote": "The best way to predict the future is to invent it.",
        "author": "Alan Kay"
    },
    {
        "quote": "Life is what happens when you're busy making other plans.",
        "author": "John Lennon"
    },
    {
        "quote": "In the middle of every difficulty lies opportunity.",
        "author": "Albert Einstein"
    }
]

@app.route("/quote")
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
