import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.schema import Column

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#######################################
class Puppy(db.Model):
    id = Column(db.Integer,primary_key=True)
    name = Column(db.Text)
    age = Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old"
    

