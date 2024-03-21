import os
from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from mlopsWine.entity.config_entity import ModelEvaluationConfig
from mlopsWine.utils.common import save_json

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):
        rmse = float(np.sqrt(mean_squared_error(actual,pred)))
        mae = float(mean_absolute_error(actual, pred))
        r2 = float(r2_score(actual,pred))
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis = 1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predicted_quantites = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_quantites)

            scores = {"rsme" : rmse, "mae" : mae, "r2" : r2}
            save_json(path = Path(self.config.metric_file_name), data = scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rsme" ,rmse)
            mlflow.log_metric("mae" ,mae)
            mlflow.log_metric("r2_score" ,r2)
            
            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")