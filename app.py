import flask
from flask import request, jsonify
from flask_cors import CORS

from analyzer import analyzeText

app = flask.Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Hello, world!"


@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "Missing text parameter"})
    text = data["text"]
    classification = analyzeText(text)
    return jsonify({"text": text, "classification": classification})


if __name__ == "__main__":
    app.run(port=5000)
