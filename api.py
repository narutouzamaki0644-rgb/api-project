from flask import Flask, jsonify, request

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
