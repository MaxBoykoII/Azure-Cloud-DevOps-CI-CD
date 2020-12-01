import pandas as pd
from flask import Blueprint, request
from flask_restx import Api, Resource
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

predict_blueprint = Blueprint("predict", __name__)
api = Api(predict_blueprint)


def scale(payload):
    """Scales Payload"""
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict


class Predict(Resource):
    def post(self):
        """Performs an sklearn prediction
        input looks like:
                {
        "CHAS":{
        "0":0
        },
        "RM":{
        "0":6.575
        },
        "TAX":{
        "0":296.0
        },
        "PTRATIO":{
        "0":15.3
        },
        "B":{
        "0":396.9
        },
        "LSTAT":{
        "0":4.98
        }
        result looks like:
        { "prediction": [ 20.35373177134412 ] }
        """

        try:
            clf = joblib.load("boston_housing_prediction.joblib")
        except Exception:
            return "Model not loaded"

        json_payload = request.json
        inference_payload = pd.DataFrame(json_payload)
        scaled_payload = scale(inference_payload)
        prediction = list(clf.predict(scaled_payload))

        return {"prediction": prediction}, 201


api.add_resource(Predict, "/predict")
