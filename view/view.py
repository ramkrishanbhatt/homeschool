from app import app, db
from flask import request, render_template, redirect

class Donation(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Name: {}>".format(self.Name)

@app.route('/', methods=["GET", "POST"])
def home():
    Donation = None
    if request.form:
        try:
            donation = Donation(name=request.form.get("name"))
            db.session.add(donation)
            db.session.commit()
        except Exception as e:
            print("Failed to add donator")
            print(e)
    donation = Donation.query.all()
    return render_template("home.html", donation=donation)

@app.route("/update", methods=["POST"])
def update():
    try:
        newname = request.form.get("previousname")
        name = request.form.get("newname")
        donation = Donation.query.filter_by(name=newname).first()
        donation.name = newname
        db.session.commit()
    except Exception as e:
        print("Couldn't update donator name")
        print(e)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("name")
    donation = Donation.query.filter_by(name=name).first()
    db.session.delete(donation)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
