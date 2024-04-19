from pandas import DataFrame
from ..abstract import AbsFilterCombo
from ..basic import FilterNan, FilterNull, FilterEndsWith

class FilterDefaultRedownload(AbsFilterCombo):

    def __init__(self, file_type:str) -> None:
        self._file_type = file_type
        
    def filter(self, data_frame: DataFrame, filter_column:str) -> DataFrame:

        _filter_null = FilterNan(filter_column)
        _filter_nan = FilterNull(filter_column)

        _filter_ends_with = FilterEndsWith(filter_column, self._file_type)

        data_frame = _filter_nan.filter_remove(data_frame)
        data_frame = _filter_null.filter_remove(data_frame)
        data_frame = _filter_ends_with.filter_keep(data_frame)

        return data_frame