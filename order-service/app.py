from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route("/orders", methods=["POST"])
def create_order():

    data = request.json

    orders.append(data)

    return jsonify({
        "message": "Order Created",
        "order": data
    })

@app.route("/orders")
def get_orders():
    return jsonify(orders)

app.run(host="0.0.0.0", port=5000)