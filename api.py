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

    result = database.get(number, {"error": "not found"})
    return jsonify(result)

app.run(host="0.0.0.0", port=10000)
