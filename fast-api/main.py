import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import numpy as np
import json
from copy import copy
import pickle
import datetime
from typing import Optional


import fastapi
import pydantic


class ScoreRequest(pydantic.BaseModel):
    input_data: list
    request_id: Optional[str] = None


class Scorer:
    def __init__(self, model_features: list, artefact_path: str):
        """
        model_features: features used in model
        artefact_path: path to model binary
        """
        self.model_features = model_features
        self.model = pickle.load(open(artefact_path, "rb"))

    def create_response(self, input_data: list) -> dict:
        """
        Batch response API:
        
        Args:
            input_dict: dictionary, with input model features as list of dictionaries in key 'input'
            
        Retruns:
            output_dict: dictioanry, with scored inputs as list of dictionaries in key 'output'
            
        """
        output_df = pd.DataFrame(input_data)
        output_df["prediction"] = self.model.predict_proba(
            output_df[self.model_features]
        )[:, 1]
        output_df["prediction_time"] = datetime.datetime.now().strftime(
            "%m/%d/%Y %H:%M:%S"
        )
        return output_df.to_dict(orient="records")


app = fastapi.FastAPI()

SCORER = Scorer(
    model_features=["Male", "Age", "SibSp", "Parch", "Fare",],
    artefact_path="bin/titanic_clf.pkl",
)


@app.get("/")
def index():
    return "Welcome to my classifier API"


@app.post("/score/")
def create_score(score_request: ScoreRequest):
    return SCORER.create_response(score_request.input_data)
