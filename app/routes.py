from os import name
from urllib import request
from xml.sax.handler import all_features
from app import app
from flask import render_template
from flask import Flask, render_template,request,flash,redirect


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/pagina")
def pagina2 ():
    return render_template("pagina.html")

def pagina ():
    altura = request.form['altura']
    peso = request.form['peso']
    print(altura)
    print(peso)
    return render_template("pagina.html")