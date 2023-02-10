from flask import Blueprint, jsonify, request

from models import *

users_bl = Blueprint('users_bl', __name__)


@users_bl.route('/users')
def get_users():
    """Return json all users from table users"""
    ll = []
    for user in Users.query.all():
        ll.append({
            'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'age': user.age,
            'email': user.email, 'role': user.role, 'phone': user.phone
        })
    return jsonify(ll)


@users_bl.route('/users/<int:x>')
def get_one_user(x):
    """get user from table"""
    user = Users.query.get(x)
    return jsonify({
        'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'age': user.age,
        'email': user.email, 'role': user.role, 'phone': user.phone
    })


@users_bl.route('/users', methods=['POST'])
def add_user():
    """add user from table"""
    data = request.get_json(silent=True)
    user = Users(id=data['id'], first_name=data['first_name'], last_name=data['last_name'], age=data['age'],
                 email=data['email'], role=data['role'], phone=data['phone'])
    db.session.add(user)
    db.session.commit()
    return 'Done'


@users_bl.route('/users/<int:x>', methods=['PUT'])
def change_margins(x):
    """update user from table"""
    data = request.json
    user = Users.query.get(x)
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.age = data['age']
    user.email = data['email']
    user.role = data['role']
    user.phone = data['phone']
    db.session.add(user)
    db.session.commit()
    return 'Done'


@users_bl.route('/users/<int:pk>', methods=['DELETE'])
def delete_user(pk):
    """delete user from table"""
    Users.query.filter(Users.id == pk).delete()
    db.session.commit()
    return 'Done'
