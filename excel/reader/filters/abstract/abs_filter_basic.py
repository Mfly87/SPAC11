import abc
from pandas import DataFrame, Series

class AbsFilterBasic(abc.ABC):

    @abc.abstractmethod
    def get_filter(self, data_frame: DataFrame) -> Series:
        pass

    def filter_keep(self, data_frame: DataFrame) -> DataFrame:
        filter = self.get_filter(data_frame)
        return data_frame[filter]

    def filter_remove(self, data_frame: DataFrame) -> DataFrame:
        filter = self.get_filter(data_frame)
        return data_frame[~filter]
