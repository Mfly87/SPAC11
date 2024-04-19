import abc
from pandas import DataFrame

from excel.writer.excel_writer_config import ExcelWriterConfig
from ..thread_pool_handler import ThreadPoolHandler

class AbsUrlProcessor(abc.ABC):
    
    def __init__(self, config:ExcelWriterConfig, timeout: int) -> None:
        self._config = config
        self._timeout = timeout if 0 < timeout else 9999
        self._log = dict()

        self.processed_column: str = ""

    @property
    def config(self) -> ExcelWriterConfig:
        return self._config
    
    @property
    def timeout(self) -> int:
        return self._timeout
    
    @property
    def log(self) -> dict[dict[str,any]]:
        return self._log

    def _set_log_entry(self, key: str, field:str, value:any) -> None:
        self.log[key][field] = value

    def _get_log_entry(self, key: str, field:str, *, default_value = None) -> any:
        if key in self.log:
            _dict = self.log[key]
            if field in _dict:
                return _dict[field]
            return default_value
        return default_value
        
    def _get_name_url_tuple_list(self, data_frame: DataFrame, column_with_link:str) -> list[tuple[str,str]]:
        _name_url_tuple_list: list[tuple[str, str]] = []

        for _col_id in data_frame.index:
            _url = data_frame.at[
                _col_id,
                column_with_link
                ]
            _name_url_tuple_list.append((_col_id, _url))

        return _name_url_tuple_list

    def process_url(self, data_frame: DataFrame, column_with_link:str):
        self.processed_column = column_with_link

        _name_url_tuple_list: list[tuple[str, str]] = self._get_name_url_tuple_list(
            data_frame, 
            column_with_link
            )
        
        _thread_pool_handler = ThreadPoolHandler()
        _thread_pool_handler.map_unordered(
            self.url_function_base,
            _name_url_tuple_list
        )

    def url_function_base(self, name_url: tuple[str, str]) -> None:
        _name:str = name_url[0]
        _url:str = name_url[1]

        if _name not in self.log:
            self.log[_name] = {
                "url": _url,
                "file_size": 0
            }

        self.url_function(name_url)

    @abc.abstractmethod
    def url_function(self, name_url: tuple[str, str]) -> None:
        pass

    @abc.abstractmethod
    def print_log(self) -> None:
        pass