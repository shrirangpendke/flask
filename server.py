from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])

def root():
    return "Welcome to first version of flask application: v1"

app.run(host="0.0.0.0", port=4000, debug=True)
