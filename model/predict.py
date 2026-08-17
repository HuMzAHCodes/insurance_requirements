import pickle
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)


# this is manual, but MLflow can track model versions
MODEL_VERSION = "1.0.0"


def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])
    output = model.predict(input_df)[0]
    return output