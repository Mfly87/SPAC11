from pandas import DataFrame
from ..abstract import AbsFilterCombo
from ..basic import FilterNan, FilterNull, FilterExistingFiles, FilterEndsWith

class FilterDefault(AbsFilterCombo):
    '''
    Skips empty rows\n
    Skips rows with wrong file type\n
    Skips rows that have already been downloaded\n
    '''

    def __init__(self, download_folder_path:str, file_type:str) -> None:
        self._file_type = file_type
        self._filter_existing = FilterExistingFiles(download_folder_path, file_type)
        
    def filter(self, data_frame: DataFrame, filter_column:str) -> DataFrame:

        _filter_null = FilterNan(filter_column)
        _filter_nan = FilterNull(filter_column)

        _filter_ends_with = FilterEndsWith(filter_column, self._file_type)

        data_frame = _filter_nan.filter_remove(data_frame)
        data_frame = _filter_null.filter_remove(data_frame)
        data_frame = _filter_ends_with.filter_keep(data_frame)

        data_frame = self._filter_existing.filter_remove(data_frame)

        return data_frame