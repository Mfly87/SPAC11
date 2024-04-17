from pandas import DataFrame
from ..abstract import AbsFilterCombo
from ..basic import FilterNan, FilterNull, FilterExistingFiles, FilterEndsWith

class FilterNotDownloadedInColumn(AbsFilterCombo):

    def __init__(self, download_folder_path:str, file_type:str, column_name:str) -> None:
        self._filter_null = FilterNan(column_name)
        self._filter_nan = FilterNull(column_name)
        self._filter_existing = FilterExistingFiles(download_folder_path, file_type)
        self._filter_ends_with = FilterEndsWith(column_name, file_type)

    @property
    def filter_null(self):
        return self._filter_null

    @property
    def filter_nan(self):
        return self._filter_nan

    @property
    def filter_existing(self):
        return self._filter_existing

    @property
    def filter_ends_with(self):
        return self._filter_ends_with

    def filter(self, data_frame: DataFrame) -> DataFrame:
        data_frame = self.filter_nan.filter_remove(data_frame)
        data_frame = self.filter_null.filter_remove(data_frame)
        data_frame = self.filter_ends_with.filter_keep(data_frame)

        #data_frame = self.filter_existing.filter_remove(data_frame)

        return data_frame