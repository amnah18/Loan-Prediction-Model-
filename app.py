# save this as app.py
from flask import Flask, request, render_template, send_from_directory
import pickle
import numpy as np
import os

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index.html')
def home1():
    return render_template("index.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/privacy.html')
def privacy():
    return render_template("privacy.html")

@app.route('/prediction.html')
def prediction():
    return render_template("prediction.html")


@app.route('/predict.html', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        #1 Gender
        Gender = request.form['Gender']
        #2 Married
        Married = request.form['Married']
        #3 Dependents
        Dependents = request.form['Dependents']
        #4 Education
        Education = request.form['Education']
        #5 Self_Employeed
        Self_Employed = request.form['Self_Employed']
        #6 ApplicantIncome
        ApplicantIncome = request.form['ApplicantIncome']
        #7 CoapplicantIncome 
        CoapplicantIncome = request.form['CoapplicantIncome']
        #8 Loan_Amount
        LoanAmount = request.form['LoanAmount']
        #9 Loan_Amount_Term
        Loan_Amount_Term = request.form['Loan_Amount_Term']
        #10 Credit_History 
        Credit_History = request.form['Credit_History']
        #11 Property_Area
        Property_Area = request.form['Property_Area']
        
        #Gender
        if(Gender == "Male"):
            Gender = 1
        else:
            Gender = 0
            
        #Married
        if(Married == "Yes"):
            Married = 1
        else:
            Married = 0
            
        #Dependents
        if(Dependents=="0"):
            Dependents=0
        elif(Dependents=="1"):
            Dependents=1
        elif(Dependents=="2"):
            Dependents=2
        elif(Dependents=="3+"):
            Dependents=4
            
        #Education
        if(Education == "Graduated"):
            Education = 1
        else:
            Education = 0
            
        #Self_Employed
        if(Self_Employed == "Yes"):
            Self_Employed = 1
        else:
            Self_Employed = 0
            
        
        #Credit_History
        if(Credit_History == 0.0):
            Credit_History = 0.0
        else:
            Credit_History = 0.1
            
        #Property_Area
        if(Property_Area == "Urban"):
            Property_Area = 2
        elif(Property_Area == "Rural"):
            Property_Area = 0
        else:
            Property_Area = 1
            
        #Calling model
        prediction = model.predict([[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]])
        
        message = f"This is the variable: {prediction}"
        print(message)
        
        #Loan Status Condition
        if(prediction=="0"):
            prediction="No"
        elif(prediction=='1'):
            prediction="Yes"
        else:
            prediction="Invalid"
            
        return render_template("predict_txt.html", prediction_text=format(prediction))
    
    
    else:
        return render_template("prediction.html")

if __name__ == '__main__':
    app.run(debug=True)