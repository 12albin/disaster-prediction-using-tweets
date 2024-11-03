import pickle
import streamlit as stl
import time
#from sklearn.feature_extraction.text import TfidfVectorizer as tf

stl.title("Disaster tweet identification")
model=pickle.load(open('model.pkl','rb'))

tweet=stl.text_input("enter the tweet")


submit=stl.button("predict")

if submit:
    #start_time=time.time()
    pred=model.predict([tweet])
    #end_time=time.time()
    #stl.write("prediction time taken:",round(end_time-start_time,2),'seconds')
    if pred[0]==0:
        stl.write("Prediction: No warning nagative!")
    else:
        stl.write("Prediction: Disaster warning, Positive!")



