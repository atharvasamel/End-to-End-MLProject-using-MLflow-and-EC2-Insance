from mlopsWine.constants import *
from mlopsWine.utils.common import read_yaml, create_directories
from mlopsWine.entity.config_entity import DataIngestionConfig

#read all the yaml files.
#and create directories for configration i.e. data ingestion
class configration_manager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH):

            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)
            self.schema = read_yaml(schema_filepath)

            create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
          config = self.config.data_ingestion  #getting the variables stored in config.yaml

          create_directories([config.root_dir])

          data_ingestion_config = DataIngestionConfig(  #only return these variables as defined entity above
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
          )

          return data_ingestion_config