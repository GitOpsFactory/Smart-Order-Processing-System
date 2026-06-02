from flask import Flask
import requests

app = Flask(__name__)

@app.route("/health")
def health():
    return "Gateway Running"

@app.route("/stock/<product>")
def stock(product):

    r = requests.get(
        f"http://inventory-service:5001/inventory/{product}"
    )

    return r.json()

app.run(host="0.0.0.0", port=8080)