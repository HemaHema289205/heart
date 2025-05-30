import streamlit as st
import joblib

m=joblib.load('hdp.joblib')

st.title('heart diseases App')
age=st.number_input('enter your age')
cigsPerDay=st.number_input('enter your cigsperday')
totChol	=st.number_input('enter your totalchol')
sysBP=st.number_input('enter your sysBP')
diaBP=st.number_input('enter your diaBP')
BMI=st.number_input('enter your BMI')
heartRate=st.number_input('enter your heartRate')
glucose=st.number_input('enter your glucose')
if st.button('predict'):
    prediction =m.predict([[age,cigsPerDay,totChol,sysBP,diaBP,BMI,heartRate,glucose]])
    if prediction == 0:
        st.write('after 10 years you have no any heart diseases')
    else:
        st.write('after 10 years you may have any heart diseases')
    
