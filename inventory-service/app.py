from flask import Flask, jsonify

app = Flask(__name__)

inventory = {
    "laptop": 20,
    "mobile": 15,
    "tablet": 10
}

@app.route("/inventory/<item>")
def get_stock(item):

    return jsonify({
        "product": item,
        "stock": inventory.get(item,0)
    })

app.run(host="0.0.0.0", port=5001)