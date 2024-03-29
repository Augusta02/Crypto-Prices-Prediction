import streamlit as st
import numpy as np
import pandas as pd

from sklearn.svm import SVR
from sklearn.metrics import r2_score
from datetime import date
import pickle





loaded_model = pickle.load(open('Cardano_Price_prediction.pkl', 'rb'))

st.header('Cardano Price Prediction')

Today = date.today().strftime('%Y-%m-%d')

# def model(df):
#     X = df['Price(in dollars)']
#     y = df[str(future_days) + '_Day_Price_Forecast']

        
#     return df

# def model(X):
#     # df['Date'] = date.today().strftime('%Y-%m-%d')
#     df['Price (in dollars)'] = np.array(df[['Price(in dollars)']])

    # return df


def model2(X):
    return np.array(X).reshape(-1,1)
    


import streamlit.components.v1 as components

html_temp = """
<div style = "background.color:purple; padding:10px">

<p style = "color:white; text_align:center;"> </p>
</div>
"""

st.markdown(html_temp, unsafe_allow_html = True)


#st.cache()
hide_streamlit_style = """
            <style>
           
            footer {visibility: hidden;}
            </style>
            """




Today = st.write(date.today().strftime('%Y-%m-%d'))
Amount = st.number_input("Price (in dollars)")


if st.button("Predict"):
    X= Amount
    res = model2(X)
    result = loaded_model.predict(res)
    st.markdown(result)