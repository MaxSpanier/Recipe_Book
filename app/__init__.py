from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['SECRET_KEY'] = 'qrjIbgNNRr04lGUdYGoN3485zbff83749#fk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["MONGO_URI"] = 'mongodb+srv://Max:ustWiafVzMeNM2F2@flaskbook.vpq7p.mongodb.net/recipesDB?retryWrites=true&w=majority'
mongo = PyMongo(app)
db = mongo.db

# mongodb+srv://Max:ustWiafVzMeNM2F2@flaskbook.vpq7p.mongodb.net/recipesDB?retryWrites=true&w=majority

from app import routes