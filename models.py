from loader import db
from sqlalchemy.orm import relationship



class Users(db.Model):
    """Model of database 'Users' """
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    age = db.Column(db.Integer())
    email = db.Column(db.String())
    role = db.Column(db.String())
    phone = db.Column(db.String())



class Orders(db.Model):
    """Model of database 'Orders' """
    __tablename__ = 'orders'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    start_date = db.Column(db.String())
    end_date = db.Column(db.String())
    address = db.Column(db.String())
    price = db.Column(db.Integer())
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    customer = relationship('Users', foreign_keys=[customer_id])
    executors = relationship('Users', foreign_keys=[executor_id])


class Offers(db.Model):
    """Model of database 'Offers' """
    __tablename__ = 'offers'
    id = db.Column(db.Integer(), primary_key=True)
    order_id = db.Column(db.Integer(), db.ForeignKey('orders.id'))
    executor_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    orders = relationship('Orders')
    users = relationship('Users')
