import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

patients_data = []  # This list will store patient data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/collect', methods=['POST'])
def collect():
    # Collect patient data from the form
   
     name = request.form['name']
     age = request.form['age']
     gender = request.form['gender']
     phn=request.form['phn']
     print(request.form)

     
     patient = {'name': name, 'age': age, 'gender': gender,'phn':phn,}
     patients_data.append(patient)
     return render_template('index.html')

@app.route('/display')
def display():
    # Pass the patient data to the template
    return render_template('display.html', patients=patients_data)

if __name__ == '__main__':
    app.run(debug=True)
