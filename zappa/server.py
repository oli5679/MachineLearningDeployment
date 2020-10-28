
import flask
import sklearn
import json 
import pickle
import pandas as pd 
import numpy as np
import datetime

app = flask.Flask(__name__)

MODEL_LOCAL_PATH = 'bin/titanic_clf.pkl'

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


@app.route('/', methods=['GET'])
def healthcheck():
    data = {
        "statusCode": 200,
        "body": "status OK!"
    }
    return flask.json.dumps(data)

@app.route('/', methods=['POST'])
def index():
    payload = json.loads(flask.request.get_data().decode('utf-8'))
    print(payload)
    response = SCORER.create_response(payload['input'])
    return json.dumps(response)