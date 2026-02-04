from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "API running"

@app.route("/lookup")
def lookup():
    number = request.args.get("number")

    database = {
        "9876543210": {"name": "Rahul", "city": "Delhi"},
        "9123456789": {"name": "Amit", "city": "Mumbai"}
    }

    if not number:
        return jsonify({"error": "number required"})

    result = database.get(number, {"error": "not found"})
    return jsonify(result)


# Render fallback (local testing only)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
