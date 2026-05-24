import sys
from networksecurity.components.data_ingection import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__ =='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingesetionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingesetionconfig)

        logging.info("Initiate the data ingestion")
        dataingestionartificat=data_ingestion.initiate_data_ingestion()
        print(dataingestionartificat)
    

    except Exception as e:
        raise NetworkSecurityException(e,sys)