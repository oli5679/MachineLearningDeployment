import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import numpy as np
import json
from copy import copy 
import pickle
import datetime

class Scorer():
    def __init__(self, model_features: list, artefact_path: str):
        '''
        model_features: features used in model
        artefact_path: path to model binary
        '''
        self.model_features = model_features
        self.model =  pickle.load(open(artefact_path,'rb'))
        
    def create_response(self, input_data: list) -> dict:
        '''
        Batch response API:
        
        Args:
            input_dict: dictionary, with input model features as list of dictionaries in key 'input'
            
        Retruns:
            output_dict: dictioanry, with scored inputs as list of dictionaries in key 'output'
            
        '''
        output_df = pd.DataFrame(input_data)
        output_df['prediction'] = self.model.predict_proba(output_df[self.model_features])[:,1]
        output_df['prediction_time'] = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        return output_df.to_dict(orient='records')

SCORER = Scorer(model_features= ['Male', 'Age', 'SibSp',
        'Parch', 'Fare',], artefact_path='bin/titanic_clf.pkl')


TEST_INPUT = [{'Male':0, 'Age':21, 'SibSp':0,
        'Parch':0, 'Fare':21.5,}]

def score(event, context):
    try:
        score_response = SCORER.create_response(event['input'])
        return {
            "statusCode": 200,
            "body": json.dumps(score_response)
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": str(e)
        }


def status(event, context):
    return {
        "statusCode": 200,
        "body": "status OK!"
    }
