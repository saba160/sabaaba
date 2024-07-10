from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "JxP/HL!=wwyTT]4k]gM2$X80dJryA#"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///CoffeShop.db"

db = SQLAlchemy(app)

login_manager = LoginManager(app)