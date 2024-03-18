from mlopsWine.config.configuration import configration_manager
from mlopsWine.components.data_validation import DataValidation
from mlopsWine import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = configration_manager()
        data_validation_config = config.get_datavalidation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>stage {STAGE_NAME} started <<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx===============x")
    except Exception as e:
        logger.exception(e)
        raise e