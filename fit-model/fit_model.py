import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import numpy as np
import joblib
import sklearn2pmml
import pickle

from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType


"""
Fitting binary classifier to predict survival of titanic passangers. Using:
     - Male - is gender = 'Male'
     - Age - age at time of journey in years
     - SibSp - Num. siblings and spouces aboard
     - Parch - Num. parents and children aboard
     - Fare - Cost of fare
     
This is just a toy model, little effort is made to develop a good one!
"""

MODEL_FEATURES = [
    "Male",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
]

DATA_PATH = "data/titanic.csv"
ARTEFACT_PATH = "bin/titanic_clf"


def main():
    """
    Fits the model and creates model artefacts (binary, PMML and onnx)
    """
    # Load the data
    # Run curl command to download if you don't already have it
    # curl https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/fa71405126017e6a37bea592440b4bee94bf7b9e/titanic.csv > data/titanic.csv

    data = pd.read_csv(DATA_PATH)

    # Fit model
    data["Male"] = (data.Sex == "male").astype(int)
    y = data["Survived"]
    X = data[MODEL_FEATURES]
    gbdt_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(missing_values=np.nan, strategy="mean")),
            ("gbdt_clf", GradientBoostingClassifier()),
        ]
    )
    gbdt_pipeline.fit(X, y)

    # Save artefacts
    data["prediction"] = gbdt_pipeline.predict_proba(X)[:, 1]
    pickle.dump(gbdt_pipeline, open(f"{ARTEFACT_PATH}.pkl", "wb"))
    sklearn2pmml.sklearn2pmml(
        sklearn2pmml.make_pmml_pipeline(gbdt_pipeline),
        f"{ARTEFACT_PATH}.pmml",
        with_repr=True,
    )
    initial_type = [("float_input", FloatTensorType([None, 4]))]
    data.to_csv(f"{ARTEFACT_PATH}_test_cases.csv", index=False)


if __name__ == "__main__":
    main()
