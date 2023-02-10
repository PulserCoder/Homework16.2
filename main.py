from loader import app
from app.users_bl import users_bl
from app.orders_bl import orders_bl
from app.offer_bl import offers_bl



if __name__ == '__main__':
    app.register_blueprint(users_bl)
    app.register_blueprint(orders_bl)
    app.register_blueprint(offers_bl)
    app.run()