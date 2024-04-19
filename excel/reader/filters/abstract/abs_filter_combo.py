import abc
from pandas import DataFrame

class AbsFilterCombo(abc.ABC):

    @abc.abstractmethod
    def filter(self, data_frame: DataFrame, filter_column:str) -> DataFrame:
        pass