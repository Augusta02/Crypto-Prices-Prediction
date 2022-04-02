from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Day_of_Prediction
        date_prediction = request.form["Date"]
        Prediction_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Prediction_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        Prediction_year = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").year)
        # print("Prediction Date : ",Prediction_day, Predciton_month, Prediction_year)



