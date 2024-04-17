from ..abstract import AbsFilterBasic
from pandas import DataFrame

class FilterNan(AbsFilterBasic):
    
    def __init__(self, column_name:str) -> None:
        self._column_name = column_name

    @property
    def column_name(self):
        return self._column_name

    def get_filter(self, data_frame: DataFrame) -> DataFrame:
        return data_frame[self.column_name].isna() == True