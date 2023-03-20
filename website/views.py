from flask import Flask, render_template, request, Blueprint
from .models import Besked
from . import db
import random
import json

beskedindeks=0

views = Blueprint("views",__name__)

@views.route("/")
def forside():
    return render_template("forside.html")


@views.route("/beskeder", methods=["GET" , "POST"])
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




