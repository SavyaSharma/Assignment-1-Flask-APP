from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Test.db'

db=SQLAlchemy(app)

class ToDo(db.Model):
    __tablename__='to_do'
    id = db.Column('id',db.Integer,primary_key=True)
    name=db.Column('name',db.String(250),nullable=False)
    last_name=db.Column('last_name',db.String(250),nullable=False)
    Dob=db.Column('Dob',db.String(10),nullable=False)
    Amount_Due=db.Column('Amount_Due',db.Integer,nullable=False)

    def __init__(self, id, name, last_name, Dob, Amount_Due):
        self.id= id
        self.name=name 
        self.last_name=last_name
        self.Dob=Dob 
        self.Amount_Due=Amount_Due
      