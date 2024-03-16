'''
Predictor class manages the endpoint preprocessing, inference and postprocessing of the models.
'''
import os
import sys
import time
import logging
import joblib
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder, StandardScaler 
sys.modules['sklearn.externals.joblib'] = joblib
from sklearn.externals.joblib import dump, load
from src.api.model.delivery_duration import DeliveryDuration
from src.api.model.delivery_duration_response import DeliveryDurationResponse


class Predictor:

    def __init__(self, app_config) -> None:
        logging.info("Initializing predictor class")
        self.model_delivery_duration  = xgb.XGBRegressor()
        self.model_delivery_duration.load_model(os.getenv('MODEL_DELIVERY_DURATION'))
        self.scaler_delivery_duration = load(os.getenv('SCALER_DELIVERY_DURATION'))
        logging.info("Loaded delivery duration forecasting model")

    def predict_delivery_duration(self, sample_delivery_duration: DeliveryDuration):
        '''
        Predict delivery duration time
        '''
        start_processing = time.time()
        logging.info(f'Starting predicting delivery duration: {sample_delivery_duration.id}')
        dict_sample = sample_delivery_duration.dict()
        dict_sample_values = list(dict_sample.values())
        sample_scaled = self.scaler_delivery_duration.transform([dict_sample_values[1:]])
        predicted_delivery_duration = self.model_delivery_duration.predict(sample_scaled)
        response = DeliveryDurationResponse(duration_time=predicted_delivery_duration[0])
        logging.info(f'Response delivery duration {response}: {sample_delivery_duration.id}')
        logging.info(f'Processing time delivery duration  {time.time()- start_processing}: {sample_delivery_duration.id}')
        return response
        