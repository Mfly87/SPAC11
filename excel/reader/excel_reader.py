import pandas as pd
from pandas import DataFrame
from .excel_reader_config import ExcelReaderConfig

class ExcelReader():
    def __init__(self, config:ExcelReaderConfig) -> None:
        self._config:ExcelReaderConfig = config

    @property
    def config(self) -> ExcelReaderConfig:
        return self._config
    
    def get_excel_data_frame(self) -> DataFrame:
        return pd.read_excel(
            self.config.file_path, 
            sheet_name = self.config.sheet_name, 
            index_col = self.config.index_column_name
            )