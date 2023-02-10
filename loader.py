from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# loader application and database
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
db = SQLAlchemy(app)

