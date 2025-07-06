from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # <-- Allow all origins

quotes = [
    "Stay hungry, stay foolish.",
    "The best way to predict the future is to invent it.",
    "Life is what happens when you're busy making other plans.",
    "In the middle of every difficulty lies opportunity."
]

@app.route("/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
