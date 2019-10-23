from app import db

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<volunteer %r>' % self.name


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timing = db.Column(db.Integer(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<schedule %r>' % self.name


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<schedule %r>' % self.name


class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timing = db.Column(db.Integer(80), unique=True, nullable=False)
    sname = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<schedule %r>' % self.sname


class Donation(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<schedule %r>' % self.name

