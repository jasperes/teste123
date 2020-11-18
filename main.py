#!/usr/bin/python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

@app.route("/<name>", methods = ["GET"])
def get_user(name):
    result = db.session.execute("SELECT * FROM SECRETWEAPON WHERE NAME = '" + name + "';")
    return result

if __name__ == "__main__":
    app.run()
