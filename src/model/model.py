from joblib import load
from xgboost.sklearn import XGBClassifier
import pandas as pd

# Singleton to load the classifier
clf: XGBClassifier = None

# Class meaning
CLASSES = {
    0: "Normal",
    1: "Leve",
    2: "Moderado",
    3: "Severo",
    4: "Extremadamente severo"
}


# Auxiliary functions
def load_classifier():
    """
    Load the classifier from the joblib data
    """
    global clf
    if clf is None:
        clf = load('./data/model.joblib')


def predict(data: pd.DataFrame):
    """
    Predict a diagnosis based on the data
    :param data: DASS score
    :return: Prediction result
    """
    # Load the classifier if it is needed
    load_classifier()
    result = clf.predict(data)
    probabilities = [round(float(i), 3) for i in clf.predict_proba(data)[0]]
    classes_names = CLASSES.values()
    return {
        "level": int(result[0]),
        "meaning": CLASSES[result[0]],
        "probabilities": dict(zip(classes_names, probabilities))
    }
