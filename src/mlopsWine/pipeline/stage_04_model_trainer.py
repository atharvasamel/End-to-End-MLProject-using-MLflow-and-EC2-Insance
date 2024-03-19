from mlopsWine.config.configuration import configration_manager
from mlopsWine.components.model_trainer import ModelTrainer
from mlopsWine import logger
from pathlib import Path


STAGE_NAME = "Model Training STAGE"

class ModelTrainerTrainingPipepline:
    def __init__(self):
        pass

    def main(self):
        config = configration_manager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = ModelTrainerTrainingPipepline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx=================x")
    except Exception as e:
        logger.exception(e)
        raise e