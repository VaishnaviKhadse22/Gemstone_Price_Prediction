import streamlit as st
import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from xgboost import XGBRegressor

with open("model.pkl","rb") as f:
    mod = joblib.load(f)


carat = st.number_input("Enter Carat",min_value=0.200000,max_value=4.50)
cut = st.selectbox("Enter Cut",['Fair','Good', 'Very Good', 'Premium',  'Ideal'])
color = st.selectbox("Enter color",['D','E', 'F', 'G',  'H', 'I','J'])
clarity = st.selectbox("Enter clarity",['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
x = st.number_input("Enter X")
y = st.number_input("Enter Y")
z = st.number_input("Enter Z")

cla_dic={'I1': 1,
 'SI2': 2,
 'SI1': 3,
 'VS2': 4,
 'VS1': 5,
 'VVS2': 6,
 'VVS1': 7,
 'IF': 8}

cut_dic = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}

col_dic = {'D': 1, 'E': 2, 'F': 3, 'G': 4, 'H': 5, 'I': 6, 'J': 7}

if st.button("Calculate your Gem Price"):
    st.header(mod.predict([[carat,cut_dic[cut],col_dic[color],cla_dic[clarity],x,y,z]]))

