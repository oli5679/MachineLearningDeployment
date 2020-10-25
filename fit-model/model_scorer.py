import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import numpy as np
import json
from copy import copy 
import pickle
import datetime

'''
Simple code to create the api response I would like
'''

class Scorer():
    def __init__(self, model_features: list, artefact_path: str):
        '''
        model_features: features used in model
        artefact_path: path to model binary
        '''
        self.model_features = model_features
        self.model =  pickle.load(open(artefact_path,'rb'))
        
    def create_response(self, input_dict: dict) -> dict:
        '''
        Batch response API:
        
        Args:
            input_dict: dictionary, with input model features as list of dictionaries in key 'input'
            
        Returns:
            output_dict: dictioanry, with scored inputs as list of dictionaries in key 'output'
            
        '''
        output_df = pd.DataFrame(input_dict['input'])
        output_df['prediction'] = self.model.predict_proba(output_df[self.model_features])[:,1]
        output_df['prediction_time'] = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        output_dict = copy(input_dict)
        output_dict['output'] = output_df.to_dict(orient='records')
        return output_dict


if __name__ == '__main__':
    scorer = Scorer(model_features= ['Male', 'Age', 'SibSp',
        'Parch', 'Fare',], artefact_path='../bin/titanic_clf.pkl')
    res = scorer.create_response({'input':[{'Male':0, 'Age':21, 'SibSp':0,
        'Parch':0, 'Fare':21.5,}]})
    print(res)