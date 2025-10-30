from flask import Flask, jsonify
import random
app = Flask(__name__)

@app.route("/api/data")
def get_data():
    num = random.randint(10,510)
    return jsonify({"num":num})

if __name__ == "__main__":
    app.run()
