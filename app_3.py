import streamlit as st
import numpy as np
import pandas as pd

from sklearn.svm import SVR
from sklearn.metrics import r2_score
from datetime import date
import pickle





loaded_model = pickle.load(open('Cardano_Price_prediction.pkl', 'rb'))

st.set_page_config(page_title="Cardano Price Prediction App", layout='wide')

Today = date.today().strftime('%Y-%m-%d')

def model(df):
    X = ['Price(in dollars)']
    y = [str(future_days) + '_Day_Price_Forecast']

        
    return df




import streamlit.components.v1 as components

html_temp = """
<div style = "background.color:teal; padding:10px">
<h2 style = "color:white; text_align:center;"> ML test </h2>
<p style = "color:white; text_align:center;"> </p>
</div>
"""

st.markdown(html_temp, unsafe_allow_html = True)


#st.cache()
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """




date = st.number_input(date.today().strftime('%Y-%m-%d'))
Amount('USD') = st.number_input("Price (in dollars)")


if st.button("Predict"):
    X= {'Price(in dollars)'}
    res = model(df)
    result = loaded_model.predict(res)
    st.markdown(result)