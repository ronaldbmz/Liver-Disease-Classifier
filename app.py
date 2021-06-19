from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import TextField,SubmitField,IntegerField,SelectField,DecimalField
from wtforms.validators import NumberRange

import numpy as np  
from tensorflow.keras.models import load_model
import joblib
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import OneHotEncoder 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
import dill


def return_prediction(model,scaler,sample_json):
    
    # For larger data features, you should probably write a for loop
    # That builds out this array for you
    
    input_values = [list(sample_json.values())]
    print("list of values",input_values)
    
    input_values = scaler.transform(input_values)
    print("after scaler",input_values)
    
    classes = np.array(['Cirrhosis', 'Few Septa', 'Many Septa', 'Portal Fibrosis'])
    
    class_ind = model.predict_classes(input_values)
    
    return classes[class_ind][0]



app = Flask(__name__)
# Configure a secret SECRET_KEY
app.config['SECRET_KEY'] = 'mysecretkey'


# REMEMBER TO LOAD THE MODEL AND THE SCALER!
model = load_model("liver_disease_model.h5")
scaler = joblib.load("liver_disease_scaler.pkl")

#input_values = [[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 12, 23.0, 2300.0, 9200000.0, 12.0, 2300.0, 23.0, 23.0, 32299.999999999996]]

#input_values = scaler.transform(input_values)


# Now create a WTForm Class
class Form(FlaskForm):
    
    gender = SelectField(u'Gender', choices=[('Female', 'Female'), ('Male', 'Male')])
    fever = SelectField(u'Fever', choices=[('No', 'No'), ('Yes', 'Yes')])
    vomit = SelectField(u'Vomiting', choices=[('No', 'No'), ('Yes', 'Yes')])
    headache = SelectField(u'Headache', choices=[('No', 'No'), ('Yes', 'Yes')])
    diarrhea = SelectField(u'Diarrhea', choices=[('No', 'No'), ('Yes', 'Yes')])
    fatigue = SelectField(u'Fatigue', choices=[('No', 'No'), ('Yes', 'Yes')])
    jaundice = SelectField(u'Jaundice', choices=[('No', 'No'), ('Yes', 'Yes')])
    epigastric = SelectField(u'Epigastric Pain', choices=[('No', 'No'), ('Yes', 'Yes')])
    age = IntegerField('Age')
    bmi = TextField('BMI')
    wbc = TextField('WBC (in thousands)')
    rbc = TextField('RBC (in millions')
    hgb = TextField('HGB')
    plat = TextField('Platelets (in thousands)')
    ast = TextField('AST')
    alt = TextField('ALT')
    rna = TextField('RNA Base (in thousands)')
    

    submit = SubmitField('Analyze')



@app.route('/', methods=['GET', 'POST'])
def index():

    # Create instance of the form.
    form = Form()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.
        
        session['gender'] = form.gender.data
        session['fever'] = form.fever.data
        session['vomit'] = form.vomit.data
        session['headache'] = form.headache.data
        session['diarrhea'] = form.diarrhea.data
        session['fatigue'] = form.fatigue.data
        session['jaundice'] = form.jaundice.data
        session['epigastric'] = form.epigastric.data
        session['age'] = form.age.data
        session['bmi'] = float(form.bmi.data)
        session['wbc'] = float(form.wbc.data) *1000
        session['rbc'] = float(form.rbc.data) *1000000
        session['hgb'] = float(form.hgb.data)
        session['plat'] = float(form.plat.data) *1000
        session['ast'] = float(form.ast.data)
        session['alt'] = float(form.alt.data)
        session['rna'] = float(form.rna.data) *1000

        return redirect(url_for("prediction"))


    return render_template('home.html', form=form)


@app.route('/prediction')
def prediction():

    content = {}
    
    if session['gender'] == 'Female':
        content['Gender_Female'] = 1
        content['Gender_Male'] = 0
    else:
        content['Gender_Female'] = 0
        content['Gender_Male'] = 1
        
    if session['fever'] == 'No':
        content['Fever_Absent'] = 1
        content['Fever_Present'] = 0
    else:
        content['Fever_Absent'] = 0
        content['Fever_Present'] = 1
    
    if session['vomit'] == 'No':
        content['Vomting_Absent'] = 1
        content['Vomting_Present'] = 0
    else:
        content['Vomting_Absent'] = 0
        content['Vomting_Present'] = 1
        
    if session['headache'] == 'No':
        content['Headache_Absent'] = 1
        content['Headache_Present'] = 0
    else:
        content['Headache_Absent'] = 0
        content['Headache_Present'] = 1
    
    if session['diarrhea'] == 'No':
        content['Diarrhea_Absent'] = 1
        content['Diarrhea_Present'] = 0
    else:
        content['Diarrhea_Absent'] = 0
        content['Diarrhea_Present'] = 1
    
    if session['fatigue'] == 'No':
        content['Fatigue_Absent'] = 1
        content['Fatigue_Present'] = 0
    else:
        content['Fatigue_Absent'] = 0
        content['Fatigue_Present'] = 1
    
    if session['jaundice'] == 'No':
        content['Jaundice_Absent'] = 1
        content['Jaundice_Present'] = 0
    else:
        content['Jaundice_Absent'] = 0
        content['Jaundice_Present'] = 1
    
    if session['epigastric'] == 'No':
        content['Epigastric_Absent'] = 1
        content['Epigastric_Present'] = 0
    else:
        content['Epigastric_Absent'] = 0
        content['Epigastric_Present'] = 1
    
    content['age'] = session['age']
    content['bmi'] = session['bmi']
    content['wbc'] = session['wbc']
    content['rbc'] = session['rbc']
    content['hgb'] = session['hgb']
    content['plat'] = session['plat']
    content['ast'] = session['ast']
    content['alt'] = session['alt']
    content['rna'] = session['rna']
    
    print("content",content)
    print("model",model)
    print("scaler",scaler)
    results = return_prediction(model=model,scaler=scaler,sample_json=content)
    
    print(results)

    return render_template('prediction.html',results=results)


if __name__ == '__main__':
    app.run(debug=False,port= 5000)