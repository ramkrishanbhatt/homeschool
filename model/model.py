from flask import Flask, request, jsonify,wtf
from flask_restplus import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, flash, request, url_for, redirect, session
from passlib.hash import sha256_crypt
from postgresdb import escape_string as thwart
import gc

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:password@localhost:5432/NGO'
db = SQLAlchemy(app)
api = Api(app=app)
ns_conf = api.namespace('NGO', description='NGO operations')



class User(db.Model):
    __tablename__ = 'volunteer'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    schedule = db.Column(db.Integer(120), unique=True, nullable=False)
    donation = db.Column(db.Integer, unique=True, nullable=False)
    classes = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, name=None, schedule=None, donation=None, classes=None):
        self.name = name
        self.schedule = schedule
        self.donation = donation
        self.classes = classes

    def todict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

db.create_all()
db.session.commit()

class User(db.Model):
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    timings = db.Column(db.Integer(120), unique=True, nullable=False)

    def __init__(self,   timings=None):
        self.timings = timings

    def todict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

db.create_all()
db.session.commit()


class User(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, unique=True, nullable=False)
    area = db.Column(db.String(120), unique=True, nullable=False

    def __init__(self, name=None, age=None, area=None):
        self.name = name
        self.age = age
        self.area = area

    def todict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

db.create_all()
db.session.commit()



class User(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    timings = db.Column(db.Integer(120), unique=True, nullable=False)
    subject = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, timings=None, subject=None):
        self.timings = timings
        self.subject = subject

    def todict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

db.create_all()
db.session.commit()


class User(db.Model):
    __tablename__ = 'donation'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    amount = db.Column(db.Integer(120), unique=True, nullable=False)

    def __init__(self, name=None, amount=None, area=None):
        self.name = name
        self.amount = amount

    def todict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


db.create_all()
db.session.commit()



@app.route('/register/', methods=["GET", "POST"])
def register_page():
    try:
        form = Registrationform(request.form)

        if request.method == "POST" and form.validate():
                username = form.username.data
                adress = form.adress.data
                password = sha256_crypt.encrypt((str(form.password.data)))
                c, conn = connection()
                x = c.execute("SELECT * FROM users WHERE username = (%s)",
                              (thwart(username)))

                if int(x) > 0:
                    flash("That username is already taken, please choose another")
                    return render_template('register.html', form=form)

                else:
                    c.execute("INSERT INTO users (username, password, address, tracking) VALUES (%s, %s, %s, %s)",
                              (thwart(username), thwart(password), thwart(address),
                               thwart("/introduction-to-NGO/")))

                    conn.commit()
                    flash("Thanks for registering!")
                    c.close()
                    conn.close()
                    gc.collect()

                    session['logged_in'] = True
                    session['username'] = username

                    return redirect(url_for('dashboard'))

                return render_template("register.html", form=form)

    except Exception as e:
    return (str(e))


@ns_conf.route("")
class Donation(Resource):
    def post(self):
        try:
            data = request.json
        except:
            return {
                "status": False,
                "msg": "error in request json"
            }
        try:
            user = User(name=data["name"], amount=data["amount"])
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return jsonify({
                "status": False,
                "msg": str(e)
            })
        return {
            "msg": "successful",
            "status": True
        }

@ns_conf.route("/<int:id>")
class Donation(Resource):
    def get(self, id):
        try:
            user = User.query.filter_by(id=id).first().todict()
        except:
            return "id not found"
        return user

    def put(self, id):
        try:
            data = request.json
            user = User.query.filter_by(id=id).first()
            user.name = data['name']
            user.amount = data['amount']
            db.session.commit()
        except Exception as e:
            return jsonify({
                "status": False,
                "msg": str(e)
            })
        return {
            "msg": "updated",
            "status": True
        }

    def delete(self, id):
        try:
            user = User.query.filter_by(id=id).first()
            db.session.delete(user)
            db.session.commit()
            return "successfully deleted"
        except:
               return "id not found"


@ns_conf.route("")
class Classes(Resource):
    def post(self):
        try:
            data = request.json
        except:
            return {
                "status": False,
                "msg": "error in request json"
            }
        try:
            user = User(timings=data["timings"], subject=data["subject"])
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return jsonify({
                "status": False,
                "msg": str(e)
            })
        return {
            "msg": "successful",
            "status": True
        }

@ns_conf.route("/<int:id>")
class Classes(Resource):
    def get(self, id):
        try:
            user = User.query.filter_by(id=id).first().todict()
        except:
            return "id not found"
        return user

    def put(self, id):
        try:
            data = request.json
            user = User.query.filter_by(id=id).first()
            user.timings = data['timings']
            user.subject= data['subject']
            db.session.commit()
        except Exception as e:
            return jsonify({
                "status": False,
                "msg": str(e)
            })
        return {
            "msg": "updated",
            "status": True
        }

    def delete(self, id):
        try:
            user = User.query.filter_by(id=id).first()
            db.session.delete(user)
            db.session.commit()
            return "successfully deleted"
        except:
               return "id not found"


if __name__ == '__main__ ':
    app.run()