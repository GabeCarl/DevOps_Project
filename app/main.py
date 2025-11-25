from flask import Flask, request, jsonify
import os

orders = [
    {'id': 1, 'item': 'Test', 'quantity': 3} # Orders list
]

app = Flask(__name__)

@app.route('/', methods=['GET']) # Root endpoint
def root():
    return  'Route Endpoints: \n' \
            'http://127.0.0.1:5000/health - health check \n' \
            'http://127.0.0.1:5000/orders - view orders  \n' \
            , 200

@app.route('/health', methods=['GET']) # Health endpoint
def health_check():
    return 'Server health', 200

@app.route('/orders', methods=['GET', 'POST'])
def orders_requests():
    if request.method == 'POST': # Case POST add new order
        new_order = request.get_json()

        if new_order is None: # Validation
            return 'Invalid order', 400
        
        if 'item' not in new_order or 'quantity' not in new_order: # Field Validation
            return 'Missing order fields (item: string, quantity: number)', 400
        
        if not isinstance(new_order['item'], str) or not isinstance(new_order['quantity'], int): # Type Validation
            return 'Invalid field types (item: string, quantity: number)', 400
        
        new_order['id'] = len(orders) + 1 # Auto increment ID
        
        orders.append(new_order)
        return jsonify(new_order=new_order), 201
    else:
        return {'orders': orders}, 200 # Case GET return all orders
    
"""
For POST test with curl:      #ID Auto Incremented

curl -X POST -H "Content-Type: application/json" -d '{"item": "Item", "quantity": "(Number Quantity)"}' http://127.0.0.1:5000/orders

"""
    
    

