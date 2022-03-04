from cgitb import text
from tokenize import String
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load


app = Flask(__name__,template_folder='templates')

@app.route("/", methods=["GET", "POST"])
def hello_world():
     request_type_str = request.method
     if request_type_str == "GET":
        return render_template("index.html", output = "Enter the values and hit Submit to view results")
     else: 
        # text = request.form["text"]

        text = ""

        age = request.form["age"]
        text = text + ","

        anaemia = request.form["anaemia"]
        text = text + anaemia
        text = text + ","

        creatinine_phosphokinase = request.form["creatinine_phosphokinase"]
        text = text + creatinine_phosphokinase
        text = text + ","
        
        diabetes = (request.form["diabetes"])
        text = text + diabetes
        text = text + ","
        
        ejection_fraction = (request.form["ejection_fraction"])
        text = text + ejection_fraction
        text = text + ","
         
        high_blood_pressure = (request.form["high_blood_pressure"])
        text = text + high_blood_pressure
        text = text + ","
         
        platelets = (request.form["platelets"])
        text = text + platelets
        text = text + ","
         
        serum_creatinine = (request.form["serum_creatinine"])
        text = text + serum_creatinine
        text = text + ","
         
        serum_sodium = (request.form["serum_sodium"])
        text = text + serum_sodium
        text = text + ","
         
        sex = (request.form["sex"])
        text = text + sex
        text = text + ","
         
        smoking = (request.form["smoking"])
        text = text + smoking
        text = text + ","
         
        time = (request.form["time"])
        text = text + time

        model = load("app/model.joblib")
        np_arr = floats_string_to_np_arr(text)

        pred = model.predict(np_arr)
        if pred[0] == 0: 
            return render_template("index.html", output = "Thank God! The Person is Out Of Danger!")
        else: 
            return render_template("index.html", output = "Sorry, The Person will not be alive too long!")
     
def floats_string_to_np_arr(floats_str):
    def is_float(s):
        try:
            float(s)
            return True
        except:
            return False
    floats = np.array([float(x) for x in floats_str.split(",") if is_float(x)])
    return floats.reshape(len(floats), 1)
