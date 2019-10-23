from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from requests import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3:////homeschools.db'
db = SQLAlchemy(app)
ns_conf = api.namespace('homeschools', description='homeschool functions')

if __name__ == "__main__":
    app.run()



