# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:27:16 2019

@author: Katharina
"""
from flask import Flask, render_template, request
from program.weatherAPI_functions import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

#Asks for user input 
@app.route("/generate")
def generate():
    return render_template("generate.html")


#confirmation function then calls the confirmation html 
@app.route("/confirmation", methods=['POST'])
def confirmation():
    formdata = request.form
    form_postcode = formdata['postcode']
#    result = 'If postcode is okay, this will show.'
    results = finding_city(form_postcode)
    return render_template("confirmation.html", **locals())



if __name__ == "__main__":
    app.run(debug = True)

