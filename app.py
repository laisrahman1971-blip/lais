from flask import Flask, jsonify
import requests

app = Flask(__name__)

FIREBASE_URL = "https://smart-ammeter-default-rtdb.firebaseio.com/meter.json"

@app.route("/data")
def get_data():
    try:
        response = requests.get(FIREBASE_URL)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
