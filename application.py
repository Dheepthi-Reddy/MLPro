from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# creating a Flask app
application  = Flask(__name__)      # entry point to the app

app = application   #creating a variable for the app
print("In app.py...")

# Route to home page

@app.route('/')
def index():
    print("Calling index")
    return render_template('index.html')

# making predictions
@app.route('/predictdata', methods = ['GET', 'POST'])   #Creating a end point that supports both GET and POST methods

def predict_datapoint():

    print("Calling predict_datapoint")

    if request.method == 'GET':

        return render_template('home.html')
    
    else:

        data = CustomData(

            gender =  request.form.get('gender'),                    
            race_ethnicity =  request.form.get('race_ethnicity'),
            parental_level_of_education =  request.form.get('parental_level_of_education'),
            lunch =  request.form.get('lunch'),
            test_preparation_course =  request.form.get('test_preparation_course'),
            reading_score =  float(request.form.get('reading_score')),
            writing_score = float(request.form.get('writing_score'))

        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df, "47 printing data frame")      # to print the prediction dataframe
        print("Before Prediction...")

        predict_pipeline = PredictPipeline()

        print("Mid Prediction...")

        results = predict_pipeline.predict(pred_df)

        print("After Prediction...")

        return render_template('home.html', results=results[0])
    
    
if __name__ == "__main__":

    app.run(host = "0.0.0.0")
