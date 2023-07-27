
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])

def root():
    return "welcome to my flask application"

app.run("0.0.0.0", port=4000, debug=True)
