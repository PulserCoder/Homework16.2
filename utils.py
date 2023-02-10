import json
from models import *


def add_users_to_database():
    """ Return users from json file by model Users"""
    ll = []
    with open('users.json', 'r') as file:
        file = json.load(file)
        for user in file:
            ll.append(Users(id=user['id'], first_name=user['first_name'], last_name=user['last_name'], age=user['age'],
                            email=user['email'], role=user['role'], phone=user['phone']))
    return ll


def add_order_to_database():
    """ Return users from json file by model Order"""
    ll = []
    with open('order.json', 'r') as file:
        file = json.load(file)
        for order in file:
            ll.append(Orders(id=order['id'], name=order['name'], description=order['description'],
                             start_date=order['start_date'], end_date=order['end_date'], address=order['address'],
                             price=order['price'], customer_id=order['customer_id'], executor_id=order['executor_id']))
    return ll


def add_offer_to_database():
    """ Return users from json file by model Offer"""
    ll = []
    with open('offers.json', 'r') as file:
        file = json.load(file)
        for offer in file:
            ll.append(Offers(id=offer['id'], order_id=offer['order_id'], executor_id=offer['executor_id']))
    return ll


def create_tables():
    """Loading all of tables"""
    db.create_all()
    db.session.add_all(add_users_to_database())
    db.session.add_all(add_order_to_database())
    db.session.add_all(add_offer_to_database())
    db.session.commit()
