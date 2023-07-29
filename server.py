from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return "welcome to ITIL exam"

@app.route("/me", methods=["GET"])
def root1():
    return "name: shrirang Pendke, prn: 230344233033, mobile no: 9096701292"

@app.route("/modules", methods=["GET"])
def root2():
    return "modules: Networking, Security Concepts, COSA, Complience & Audit, NDC & PKI, Cyber Forensics"



app.run(host="0.0.0.0", port=4000, debug=True)
