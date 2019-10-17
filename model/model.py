from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/tanuj/Documents/myrepo/python_exercises/homeschool/model/homeschool.db'


db = SQLAlchemy(app)
print("tanu")

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Schedule(db.Model):
    id = db.Column(db.Integer(80), primary_key=True)
    timings = db.Column(db.Integer(80), unique=True, nullable=False)

    def __repr__(self):
        return '<schedule %r>' % self.schedule


class Students(db.Model):
    id = db.Column(db.Integer(80), primary_key=True)
    studentname = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer(120), unique=True, nullable=False)
    address=db.column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<students %r>' % self.studentname


class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subjectname = db.Column(db.String(80), unique=True, nullable=False)
    timing = db.Column(db.Integer(120), unique=True, nullable=False)

    def __repr__(self):
        return '<program %r>' % self.program


class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donatorname = db.Column(db.String(80), unique=True, nullable=False)
    amount = db.Column(db.Integer(120), unique=True, nullable=False)

    def __repr__(self):
        return '<donation %r>' % self.donation
