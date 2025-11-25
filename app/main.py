from flask import Flask, request, jsonify
import os

orders = [
    {'id': 0, 'item': 'Test', 'quantity': 3} # Orders list
]

app = Flask(__name__)

@app.route('/health', methods=['GET']) # Health endpoint
def health_check():
    return 'Server health', 200

@app.route('/orders', methods=['GET', 'POST'])
def orders_requests():
    if request.method == 'POST': # Case POST add new order
        new_order = request.get_json() 
        if new_order is None: # Validation
            return 'Invalid order', 400
        orders.append(new_order)
        return jsonify(new_order=new_order), 201
    else:
        return {'orders': orders}, 200 # Case GET return all orders
    

