from ..abstract import AbsFilterBasic
from pandas import DataFrame, Series
import glob
import os.path

class FilterExistingFiles(AbsFilterBasic):
    def __init__(self, folder_path:str, file_type:str) -> None:       
        self._file_type:str = file_type.lower().replace(".","")
        self._folder_path:str = folder_path

    @property
    def folder_path(self) -> str:
        return self._folder_path
        
    @property
    def file_type(self) -> str:
        return self._file_type

    def get_filter(self, data_frame: DataFrame) -> Series:

        file_expression = "*." + self.file_type
        path_name = os.path.join(self.folder_path, file_expression)
        downloaded_files = glob.glob(path_name)

        return data_frame.index.isin(downloaded_files)
