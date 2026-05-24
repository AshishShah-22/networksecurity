from dataclasses import dataclass
import os
import sys

@dataclass
class DataIngestionArtificat:
    trained_file_path:str
    test_file_path:str