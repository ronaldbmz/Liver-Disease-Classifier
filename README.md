# Liver-Disease-Classifier

## Introduction:
Liver cirrhosis affects nearly 80 million to 100 million Americans but remains widely misdiagnosed. There are many contributing factors to why, one of the main factors being that it can occur in even the healthiest of individuals. With symptoms that are similar to other illnesses it becomes that much difficult to properly diagnose. The medical community has started making progress in terms of diagnoses but the issue of misdiagnosis still remains. With the disease being so widespread, the number of healthy livers decreases which affects organ donation as well. Our team decided to tackle that problem by creating a tool for doctors to possibly catch liver cirrhosis early on before sending patients through extensive tests and treatments.

## Problem Statement:
Build a deep learning model to predict the type of a liver disease based on the patient’s attributes like Age, BMI, WBC, RBC etc.

### About Data:
The dataset contains the different patients records with 4 types of liver disease. The dataset is used to build a Deep Learning model. Using the following shown key attributes of a patient the model is developed to predict the type of liver disease the patient has:
Here is the sample data and attributes for reference:

![images](Picture1.png)
 
## Steps Performed:
## 1.	Exploratory Data Analysis using visualizations in pandas, matplotlb and seaborn
Performed EDA to understand the distribution of target variable i.e. “class” across the data and across other variables:
### •	Distribution of target variable across the data:
This represents that the given data is almost equally distributed among the 4 types and its not skewed for any one type.
Also, the distribution helps to understand the baseline of the model prediction should be at least 24%. 

### •	Distribution of target variable across WBC and RBC:
The below chart shows that there is no particular relation (direct/indirect) between the type of liver disease and RBC/WBC. 
 
### •	Distribution of target variable across AST and ALT:
Similar like above, here also we can observe that there is no particular relation (direct/indirect) between the type of liver disease and AST/ALT
 
### •	Check for missing values:
Checked the missing values in the data to perform the data cleaning step but noticed that there are no missing values in the data.

## 2.	Preprocessing of data using scikit learn library:
In order to preprocess the data, following are the two main steps that were being performed:

### •	Creating dummy (one-hot encoding) variables: 
For the attributes like “gender”, “fever” etc. because those variables are categorical variables, in order to use them in deep learning model building, these variables are converted into one-hot encoding.
 
### •	Scaling the continuous variables: 
To have the same impact of all continuous variables in the model irrespective of their magnitude, continuous variables are scaled using sci-kit learn scaler function.

## 3.	Train Deep Learning Model:
As a last step of modelling process, following different types of deep learning models were built to analyze their performance and at last the best fit model was saved to host it on Heroku through python flask app:

### Model-1: 
•	Configuration: 25 nodes in start layer, 12 nodes in 1st hidden layer, 6 nodes in 2nd hidden layer and 4 nodes in final layer
•	Performance: Minimum Error – 1.39 and Maximum Error – 1.42

### Model-2: 
•	Configuration: 25 nodes in start layer, 12 nodes in 1st hidden layer, and 4 nodes in final layer
•	Performance: Minimum Error – 1.41 and Maximum Error – 1.45
•	Comparison: Compared to 1st model, in the 2nd version, one less hidden layer was taken and noticed that overall min and max value of error got increased.

### Model-3: 
•	Configuration: 25 nodes in start layer and 4 nodes in final layer
•	Performance: Minimum Error – 1.43 and Maximum Error – 1.49
•	Comparison: Compared to 1st and 2nd model, in the 3rd version, no hidden layer was taken and noticed that overall min and max value of error got increased further.
Therefore, trained model-1 was saved as a final version and being used further in flask app.

## 4.	Built flask app to deploy the trained deep learning model:
Used following libraries from python flask to deploy the model:
•	“FlaskForm” to create a user interactive form where user/patient can enter his/her details which would be used further to predict the type of liver disease.
•	“load_model” library from tensorflow to load the trained/saved deep learning model which was used to predict the type of disease based on the user input values.
•	“joblib” library to load the scaler pickle file to scale the user input data before passing it through the saved model for prediction.
•	“render_template” from flask in order to build the front-end of the application in html files and render them as landing page and final result page.

