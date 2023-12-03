from flask import Flask,render_template,request
import numpy as np
import pickle

with open("Loan_Predicted.pkl",'rb') as f:
    model = pickle.load(f)
#create an object instance
app = Flask(__name__)
@app.route('/saketh')
def check():
    return "Codegnan is in NBKR"
@app.route('/') #by default methods = ['GET']
def new():
    return render_template("index.html")
@app.route('/predict',methods=['POST'])
def predict():
    applicant_income = int(request.form['applicant_income'])
    coapplicant_income = int(request.form['coapplicant_income'])
    loan_amount = int(request.form['loan_amount'])
    loan_term = int(request.form['loan_term'])
    gender = int(request.form['gender'])
    married = int(request.form['married'])
    dependents = int(request.form['dependents'])
    education = int(request.form['education'])
    self_employed = int(request.form['self_employed'])
    credit_history = int(request.form['credit_history'])
    property_area = int(request.form['property_area'])
    input_data = np.array([[applicant_income,coapplicant_income,
                            loan_amount,loan_term,gender,married,dependents,
                            education,self_employed,
                            credit_history,property_area]])
    predicted_price = model.predict(input_data)[0]
    
    if predicted_price == 1:
        prediction = 'Loan will be approved'
    else:
        prediction = 'Loan will be rejected'
    
    return render_template('index.html', prediction = prediction)

app.run()
