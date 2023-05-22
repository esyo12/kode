from flask import Flask, render_template, request, Blueprint
from .models import Besked
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os
import random
import json
print("after import")

beskedindeks=0
app = Flask(__name__)
views = Blueprint("views",__name__)


DB_NAME = "database.db"

print("environment", os.environ)

app.config['SECRET_KEY'] = 'hej'
if 'POSTGRES_URL' not in os.environ:
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["POSTGRES_URL"]
db = SQLAlchemy(app)
#db.init_app(app)
from .app import views
app.register_blueprint(views, url_prefix='/')
from . import models
with app.app_context():
    db.create_all()
print("after config")

@app.route("/")
def forside():
    return render_template("forside.html", env=os.environ)


@app.route("/beskeder", methods=["GET" , "POST"])
def beskeder():
    reneBeskeder = hentBeskeder()
    
    print(reneBeskeder)
    if request.method == "GET":
        return render_template("beskeder.html", reneBeskeder=reneBeskeder)
    if request.method == "POST":
        besked = request.form.get("besked")
        print("besked: " + str(besked))
        global beskedindeks
        ny_besked = Besked(id=beskedindeks, besked=str(besked))
        beskedindeks += 1
        db.session.add(ny_besked)
        db.session.commit()
        reneBeskeder = hentBeskeder()
        return render_template("beskeder.html", reneBeskeder=reneBeskeder)
        
def  hentBeskeder():
    beskeder = Besked.query.all()
    print(beskeder)
    reneBeskeder = []
    for besked in beskeder:
        reneBeskeder.append(besked.besked)
        
    
    reneBeskeder.reverse()
    return reneBeskeder



print("after routes")
