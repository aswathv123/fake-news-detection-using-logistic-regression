from flask import Flask,render_template,request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split 
import re
import string
app=Flask(__name__)

vectorization=TfidfVectorizer(stop_words="english",max_df=0.7)

df=pd.read_csv('manual_testing1.csv')

x=df['text']
y=df['class']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

def manual_testing2(news):
    xv_train=vectorization.fit_transform(x_train)
    xv_test=vectorization.transform(x_test)
    LR=LogisticRegression()
    LR.fit(xv_train,y_train) 
    input_data=[news]
    vectorized_input_data=vectorization.transform(input_data)
    prediction=LR.predict(vectorized_input_data)
    return (prediction[0])

@app.route('/')
def home():
    return render_template('fakenews.html')
@app.route('/predict',methods=["POST"])
def predict():
    if request.method=="POST":
        message=request.form['message']
        pred=manual_testing2(message)
        
        return render_template('fakenews.html',prediction=pred)
    return None
        
if __name__ == '__main__':
   
    app.run(debug=True)



        