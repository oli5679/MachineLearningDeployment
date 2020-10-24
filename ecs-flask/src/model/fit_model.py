import pandas as pd
import lightgbm as lgb
import pickle
import shap
import numpy as np

TARGET_COL = "arrears_target"

INPUT_PATH = "bin/market-invoice-data.csv"

OUTPUT_CLASSIFIER_BIN_PATH = "bin/market-invoice-lgb.pkl"

DROP_COLS = [
    "Trade ID",
    "Seller ID",
    "Trade Type",
    "Expected Payment Date",
    "Settlement Date",
    "In Arrears",
    "In Arrears on Date",
    "Crystallised Loss Date",
    "Payment State",
    "Crystallised Loss",
    "Advance Date",
]

def main():
    raw = pd.read_csv(INPUT_PATH).drop(columns=DROP_COLS)
    y = raw[TARGET_COL]
    X = raw.drop(columns=[TARGET_COL])
    X_dum = pd.get_dummies(X)
    model = lgb.LGBMClassifier()
    model.fit(X_dum, y)
    pickle.dump(model, open(OUTPUT_CLASSIFIER_BIN_PATH, "wb"))

    print("example record")
    print("----------------------")
    print(X_dum.head(1).to_dict(orient="records"))


if __name__ == "__main__":
    main()
