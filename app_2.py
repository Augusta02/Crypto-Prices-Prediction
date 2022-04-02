import streamlit as st
import numpy as np
import pandas as pd
!pip install sklearn
from sklearn.svm import SVR
from sklearn.metrics import r2_score
from datetime import date
import pickle





loaded_model = pickle.load(open('Cardano_Price_prediction.pkl', 'rb'))

st.set_page_config(page_title="Cardano Price Prediction App", layout='wide')

Today = date.today().strftime('%Y-%m-%d')

def model(df):
    X = X[:df.shape[0] - future_days]
    y = y[:-future_days]

        
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




country = st.text_input("country")
ed = st.text_input("education")
yoe = st.number_input("YOE")

if st.button("Predict"):
    X= {'Country': country, 'EdLevel': ed, 'YearsCodePro': int(yoe)}
    res = model_encoder(X)
    result = loaded_model.predict(res)
    st.markdown(result)