import pickle
import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(layout="wide")

# ##############################################################################################################################

@st.cache_data
def diabetes():
    diabetes1 = pd.read_csv('data/diabetes.csv', low_memory=False)
    return diabetes1
def heart():
    heart1 = pd.read_csv('data/heart.csv', low_memory=False)
    return heart1

def parkinsons():
    parkinsons1 = pd.read_csv('data/parkinsons.csv', low_memory=False)
    return parkinsons1

# ##############################################################################################################################

# loading the saved models

diabetes_model = pickle.load(open('model/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('model/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('model/parkinsons_model.sav', 'rb'))

# ##############################################################################################################################
# sidebar for navigation
# Custom CSS to increase the size of radio button options

with st.sidebar:
    st.title("Navigation")
    selected = st.sidebar.radio('',
                                ['Introduction',
                                 'About',
                                 'View Raw Data',
                                 'Heart Disease Prediction',
                                 'Diabetes Prediction',
                                 "Parkinson's Prediction",
                                 'Conclusion'])
# ##############################################################################################################################
heart = heart()
parkinsons = parkinsons()
diabetes = diabetes()
# ##############################################################################################################################
if selected == 'Introduction':
    st.title("Introduction")
    st.write("To Be Added")
# ##############################################################################################################################
if selected == 'About':
    st.title("About")
    st.write("To Be Added")
# ##############################################################################################################################
if selected == 'View Raw Data':
    st.title("View Raw Data")
    disease = st.radio('Select Disease', ['Heart', 'Parkinsons', 'Diabetes'])

    # Display data based on selected disease
    if disease == 'Heart':
        st.subheader('Heart Data:')
        st.write(heart)

    if disease == 'Parkinsons':
        st.subheader("Parkinson's Data:")
        st.write(parkinsons)

    if disease == 'Diabetes':
        st.subheader('Diabetes Data:')
        st.write(diabetes)
# ##############################################################################################################################
if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', value=None)
        
    with col2:
        sex = st.number_input('Sex', value=None)
        
    with col3:
        cp = st.number_input('Chest Pain types', value=None)
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure', value=None)
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl', value=None)
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl', value=None)
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results', value=None)
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved', value=None)
        
    with col3:
        exang = st.number_input('Exercise Induced Angina', value=None)
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise', value=None)
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment', value=None)
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy', value=None)
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', value=None)
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    
# ##############################################################################################################################
if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.number_input('Glucose Level')
    
    with col3:
        BloodPressure = st.number_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.number_input('Skin Thickness value')
    
    with col2:
        Insulin = st.number_input('Insulin Level')
    
    with col3:
        BMI = st.number_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.number_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
# ##############################################################################################################################
if selected == "Parkinson's Prediction":
    st.title("Parkinson's Prediction")
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.number_input('MDVP:RAP')
        
    with col2:
        PPQ = st.number_input('MDVP:PPQ')
        
    with col3:
        DDP = st.number_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.number_input('MDVP:APQ')
        
    with col4:
        DDA = st.number_input('Shimmer:DDA')
        
    with col5:
        NHR = st.number_input('NHR')
        
    with col1:
        HNR = st.number_input('HNR')
        
    with col2:
        RPDE = st.number_input('RPDE')
        
    with col3:
        DFA = st.number_input('DFA')
        
    with col4:
        spread1 = st.number_input('spread1')
        
    with col5:
        spread2 = st.number_input('spread2')
        
    with col1:
        D2 = st.number_input('D2')
        
    with col2:
        PPE = st.number_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
# ##############################################################################################################################
if selected == 'Conclusion':
    st.title("Conclusion")
    st.write("To Be Added")