from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['SECRET_KEY'] = 'qrjIbgNNRr04lGUdYGoN3485zbff83749#fk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["MONGO_URI"] = "mongodb+srv://Max:WWe914o8vM@cluster0.6qnlv.mongodb.net/<dbname>?retryWrites=true&w=majority"
mongo = PyMongo(app)

from app import routes