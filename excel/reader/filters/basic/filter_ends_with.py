from ..abstract import AbsFilterBasic
from pandas import DataFrame, Series

class FilterEndsWith(AbsFilterBasic):
    
    def __init__(self, column_name:str, ending_string:str) -> None:
        self._column_name = column_name
        self._ending_string = ending_string

    @property
    def ending_string(self):
        return self._ending_string

    @property
    def column_name(self):
        return self._column_name

    def get_filter(self, data_frame: DataFrame) -> Series:
        return data_frame[self.column_name].str.endswith(self.ending_string)
