from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load


app = Flask(__name__,template_folder='templates')

@app.route("/", methods=["GET", "POST"])
def hello_world():
     request_type_str = request.method
     if request_type_str == "GET":
        return render_template("index.html", output = "Predict the Output by inputting the values and Enter Submit")
     else: 
        text = request.form["text"]
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
