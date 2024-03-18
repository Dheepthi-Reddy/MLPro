import sys
import pandas as pd
from src.utils import load_object
from src.exception import CustomException

class PredictPipeline:

    print("In PredictPipeline...")

    def __init__(self):
        pass

    def predict(self, features):

        print("In predict method...")
        
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'    #preprocessor for handling categorical features, feature scaling
            model = load_object(file_path = model_path)         #loads the pkl file
            preprocessor = load_object(file_path = preprocessor_path)

            # print(preprocessor)

            #Scaling the data
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)

            return preds
        
        except Exception as e:
            raise CustomException(e, sys)


#CustomData class is to map all the inputs we are giving in the HTML to the backend
class CustomData:
    def __init__(self,
        gender: str,                    #features being used
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        print("In CustomData.....")
        

        # assigining values
        self.gender = gender

        self.race_ethnicity = race_ethnicity
        print(race_ethnicity,"race printing")

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    # this function to return data in the form of dataframe
    def get_data_as_data_frame(self):

        print("In get_data_as_data_frame.......", self)

        try:
            # we are creating a dictionary
            custom_data_input_dict = {
                "gender": [self.gender],                    
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)
