import pickle
import pandas as pd
import numpy as np
import streamlit as st
import base64

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
    st.image('image/img1.jpeg')
    st.markdown("***In the realm of biomedical informatics and healthcare, the development of predictive models for heart disease holds profound significance. With heart disease being a leading cause of mortality worldwide, the ability to accurately predict its occurrence enables timely interventions and personalized treatment strategies, thereby potentially saving lives and reducing healthcare costs. Leveraging machine learning techniques, such as classification algorithms and deep learning architectures, researchers and clinicians can harness vast amounts of patient data encompassing demographics, medical history, biomarkers, and imaging studies to construct robust predictive models. These models not only aid in risk assessment but also contribute to our understanding of the complex interplay of factors underlying cardiovascular health. Moreover, the integration of advanced informatics technologies facilitates the translation of these models into clinical practice, empowering healthcare professionals with decision support tools for proactive patient management. As we navigate the era of precision medicine, the synergy between machine learning, biomedical informatics, and healthcare promises transformative advancements in the prevention and treatment of heart disease, ushering in an era of personalized and proactive cardiovascular care.***")
    st.markdown("***Biomedical informatics serves as the bridge between healthcare and technology, leveraging computational methods to extract actionable insights from biomedical data. By integrating information technology, computer science, and healthcare, biomedical informatics plays a pivotal role in the development and implementation of predictive models for heart disease prediction. Through sophisticated data processing techniques, such as data mining, natural language processing, and predictive modeling, biomedical informatics researchers can uncover hidden patterns within clinical datasets, enabling the creation of robust predictive models that aid in risk stratification and decision-making.***")
    st.markdown("***The application of predictive models in healthcare holds immense promise for improving patient outcomes and optimizing resource utilization. In the context of heart disease, predictive models can assist healthcare providers in identifying individuals at high risk of developing cardiovascular complications, allowing for targeted interventions aimed at preventing disease progression. By analyzing a diverse array of patient characteristics and historical data, these models can generate personalized risk profiles for each individual, guiding clinicians in tailoring treatment plans and lifestyle recommendations to suit their specific needs.***")
# ##############################################################################################################################
if selected == 'About':
    st.title("About")
    st.image('image/img2.jpeg')
    st.markdown("***In the field of biomedical informatics and healthcare, the integration of machine learning techniques into predictive models holds immense potential for the early detection and management of both heart disease and Parkinson's disease. By leveraging vast datasets encompassing patient demographics, medical history, lifestyle factors, and genetic predispositions, these models strive to forecast the likelihood of developing these debilitating conditions. Through sophisticated algorithms, they sift through complex patterns within the data, enabling healthcare professionals to identify individuals at increased risk. In the case of heart disease, predictive models aid in risk stratification, allowing for timely interventions and personalized treatment plans tailored to individual needs. Similarly, in Parkinson's disease, these models can help predict the progression of symptoms, enabling early intervention strategies that may slow down the disease's advancement. By empowering clinicians with actionable insights, these predictive models revolutionize clinical decision-making, enhancing diagnostic accuracy and optimizing resource allocation in healthcare settings. As research continues to refine and validate these models, they hold the promise of transforming the landscape of cardiovascular and neurological care, ushering in an era of precision medicine that prioritizes early intervention and personalized treatment approaches for better patient outcomes.***")
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
        age = st.number_input('Age')
    with col2:
        sex = st.number_input('Sex : Male=0,Female=1')
    with col3:
        cp = st.number_input('Chest Pain types: typical angina=0, atypical angina=1, non-anginal=2, asymptomatic=3')
    with col1:
        trestbps = st.number_input('Resting Blood Pressure in mm Hg')
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results: normal=0, stt abnormality=1, lv hypertrophy=2')
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.number_input('Exercise Induced Angina :True =1,False=0')
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy (0-3)')
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

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
    st.markdown("***In conclusion, the amalgamation of machine learning, biomedical informatics, and healthcare holds immense promise in advancing predictive models for both heart disease and Parkinson's disease. Through the integration of diverse datasets and sophisticated algorithms, these models facilitate early detection, risk stratification, and personalized interventions, thereby revolutionizing clinical decision-making and optimizing patient care. In the case of heart disease, predictive models enable healthcare providers to identify individuals at heightened risk, allowing for timely interventions and tailored treatment plans that mitigate the burden of cardiovascular ailments. Similarly, in Parkinson's disease, these models offer insights into disease progression, aiding in the implementation of proactive strategies to manage symptoms and improve quality of life for patients. As research continues to refine and validate these predictive models, they hold the potential to reshape the landscape of cardiovascular and neurological care, ushering in an era of precision medicine that prioritizes preventive measures and personalized treatment approaches. By harnessing the power of data-driven insights, predictive models pave the way for more effective healthcare delivery, ultimately leading to better outcomes and improved patient well-being in the realm of both heart disease and Parkinson's disease.***")