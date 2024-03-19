import os
from mlopsWine import logger
from sklearn.model_selection import train_test_split as tts
import pandas as pd
from mlopsWine.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config : DataTransformationConfig):
        self.config = config

    #We can add Data preprocessing tasks here with the train test split.
    #Data cleaning , EDA, encoding , etc.
        
    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train,test = tts(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "Test.csv"),index = False)

        logger.info("Spliited data into train and test")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)