from flask import Flask
import sqlite3
app = Flask(__name__)
# api = Api(app=app)
ns_conf = api.namespace('homeschools', description='homeschool functions')


class TextField():
    pass


@ns_app.route("/")
class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms and services)',
    [validators.Required()])

@ns_app.route("/")
class StudentRegistrationForm(Form):
    studentname = TextField('Studentname',[validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    password = passwordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='passwords must match')
    ])
    confirm = passwordField('Repeat Password')
    accept_tos = BooleanField('I accept the terms and services)',
    [validators.Required()])

@ns_app.route("/")
class Donation(Resource):
    def get(self):
        db=sqlite3.connect('homeschools.db')
        sql="SELECT * from student;"
        cur=db.cursor()
        cur.execute(sql)
    while True:
        record=cur.fetchone()
    if record==None:
        pass
    print (record)
    db.close()

    def update(self):
        db = sqlite3.connect('homeschools.db')
        qry = "update donation set age=? where name=?;"
        try:
            cur = db.cursor()
            cur.execute(qry, (5, 'Deepthi'))
            db.commit()
            print("record updated successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()

    def delete(self):
        db = sqlite3.connect('homeschools.db')
        qry = "DELETE from student where name=?;"
        try:
            cur = db.cursor()
            cur.execute(qry, ('Bill',))
            db.commit()
            print("record deleted successfully")
        except:
            print("error in operation")
            db.rollback()
            db.close()

    def post(self):
        db = sqlite3.connect('homeschools.db')
        qry = "insert into student (name, age, amount) values(?,?,?);"
        try:
            cur = db.cursor()
            cur.execute(qry, ('Vijaya', 6, 75))
            db.commit()
            print ("one record added successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()

@ns_app.route("/")
class Classes(Resource):
    def get(self):
        db=sqlite3.connect('homeschools.db')
        sql="SELECT * from student;"
        cur=db.cursor()
        cur.execute(sql)
    while True:
        record=cur.fetchall()
    if record==None:
        pass
    print (record)
    db.close()

    def update(self):
        db = sqlite3.connect('homeschools.db')
        qry = "update classes set subject=? where teacher=?;"
        try:
            cur = db.cursor()
            cur.execute(qry, ('maths', 'Deva'))
            db.commit()
            print("record updated successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()

    def delete(self):
        db = sqlite3.connect('homeschools.db')
        qry = "DELETE from classes where name=?;"
        try:
            cur = db.cursor()
            cur.execute(qry, ('maths',))
            db.commit()
            print("record deleted successfully")
        except:
            print("error in operation")
            db.rollback()
            db.close()

    def post(self):
        db = sqlite3.connect('homeschools.db')
        qry = "insert into classes (name, age, subject) values(?,?,?);"
        try:
            cur = db.cursor()
            cur.execute(qry, ('Vijay', 6, 'english'))
            db.commit()
            print ("one record added successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()


