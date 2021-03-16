from flask import Flask
from config import Config


app = Flask(__name__)
# command line for generate the secret key
# print(secrets.token_hex(16))
app.config['SECRET_KEY'] = "82d3b3e552cec2660f402542ddebc41f"


app.config.from_object(Config)


# At the bottom because of circular imports...
# This app is the package app
from app import routes
