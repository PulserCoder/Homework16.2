from flask import Blueprint, jsonify, request
from models import *

orders_bl = Blueprint('orders_bl', __name__)


@orders_bl.route('/orders')
def get_orders():
    """Return json all orders from table orders"""
    ll = []
    for order in Orders.query.all():
        ll.append({'id': order.id, 'name': order.name, 'description': order.description,
                   'start_date': order.start_date, 'end_date': order.end_date, 'address': order.address,
                   'price': order.price, 'customer_id': order.customer_id, 'executor_id': order.executor_id})
    return jsonify(ll)


@orders_bl.route('/orders/<int:x>')
def get_one_order(x):
    """Return json with one user"""
    order = Orders.query.get(x)
    return jsonify({'id': order.id, 'name': order.name, 'description': order.description,
                    'start_date': order.start_date, 'end_date': order.end_date, 'address': order.address,
                    'price': order.price, 'customer_id': order.customer_id, 'executor_id': order.executor_id})


@orders_bl.route('/orders', methods=['POST'])
def add_ord():
    """Add order to table"""
    order = request.get_json(silent=True)
    order = Orders(id=order['id'], name=order['name'], description=order['description'],
                   start_date=order['start_date'], end_date=order['end_date'], address=order['address'],
                   price=order['price'], customer_id=order['executor_id'], executor_id=order['executor_id'])
    db.session.add(order)
    db.session.commit()
    return 'Done'


@orders_bl.route('/orders/<int:x>', methods=['PUT'])
def change_margins_ord(x):
    """change order"""
    data = request.json
    order = Orders.query.get(x)
    order.name = data['name']
    order.description = data['description']
    order.start_date = data['start_date']
    order.end_date = data['end_date']
    order.address = data['address']
    order.price = data['price']
    order.customer_id = data['executor_id']
    order.executor_id = data['executor_id']
    db.session.add(order)
    db.session.commit()
    return 'Done'


@orders_bl.route('/orders/<int:pk>', methods=['DELETE'])
def delete_ord(pk):
    """delete order"""
    Orders.query.filter(Orders.id == pk).delete()
    db.session.commit()
    return 'Done'
