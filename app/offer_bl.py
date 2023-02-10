from flask import Blueprint, jsonify, request
from models import *

offers_bl = Blueprint('offers_bl', __name__)


@offers_bl.route('/offers')
def get_offers():
    """Return json all offers from table offers"""
    ll = []
    for offer in Offers.query.all():
        ll.append({
            'id': offer.id, 'order_id': offer.order_id, 'executor_id': offer.executor_id
        })
    return jsonify(ll)


@offers_bl.route('/offers/<int:x>')
def get_one_offer(x):
    """Return one json wth data about one offer"""
    offer = Offers.query.get(x)
    return jsonify({
            'id': offer.id, 'order_id': offer.order_id, 'executor_id': offer.executor_id
        })

@offers_bl.route('/offers', methods=['POST'])
def add_offer():
    """Add offer to database"""
    data = request.get_json(silent=True)
    offer = Offers(id=data['id'], order_id=data['order_id'], executor_id=data['executor_id'])
    db.session.add(offer)
    db.session.commit()
    return 'Done'


@offers_bl.route('/offers/<int:x>', methods=['PUT'])
def change_margins_offer(x):
    """Update one offer to database"""
    data = request.json
    offer = Offers.query.get(x)
    offer.order_id = data['order_id']
    offer.executor_id = data['executor_id']
    db.session.add(offer)
    db.session.commit()
    return 'Done'


@offers_bl.route('/offers/<int:pk>', methods=['DELETE'])
def delete_offer(pk):
    """Delete offer from database"""
    Offers.query.filter(Offers.id == pk).delete()
    db.session.commit()
    return 'Done'