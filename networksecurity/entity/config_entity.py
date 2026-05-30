from datetime import datetime
import os
from networksecurity.constants import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFICAT_DIR)


class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%S")
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFICAT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.timestamp:str = timestamp


class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_directory :str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_NAME
        )
        self.ingested_directory : str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTION_DIR
        )
        self.artifact_directory : str = os.path.join(
            self.feature_store_directory,
            training_pipeline.FILE_NAME
        )
        self.train_file_path : str = os.path.join( 
            self.ingested_directory,
            training_pipeline.TRAIN_FILE_NAME,       
        )
        self.test_file_path : str = os.path.join(
            self.ingested_directory,
            training_pipeline.TEST_FILE_NAME
        )

        self.collection_name : str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name : str = training_pipeline.DATA_INGESTION_DATABASE_NAME
        self.train_test_split_ratio : float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION  


class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir:str = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALID_NAME)
        self.invalid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_NAME)
        self.valid_train_file_path:str = os.path.join(self.valid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path:str = os.path.join(self.valid_data_dir,training_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path:str = os.path.join(self.invalid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path:str = os.path.join(self.invalid_data_dir,training_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path:str = os.path.join(self.data_validation_dir,
                                                       training_pipeline.DATA_VALIDATION_DRIFT_NAME,
                                                       training_pipeline.DATA_VALIDATION_REPORT_NAME
                                                       )
        

class DataTransformationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_TRANSFORMATION_DIR_NAME)
        self.transfromed_train_file_path:str = os.path.join(self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                            training_pipeline.TRAIN_FILE_NAME.replace("csv","npy"))
        self.transfromed_test_file_path:str = os.path.join(self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
                                                            training_pipeline.TEST_FILE_NAME.replace("csv","npy"))
        self.transfromed_object_file_path:str = os.path.join(self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
                                                            training_pipeline.PREPROCESSING_OBJECT_FILE_NAME,)