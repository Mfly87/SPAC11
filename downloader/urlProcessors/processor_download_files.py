from excel.writer.excel_writer_config import ExcelWriterConfig
from .abs_url_processor import AbsUrlProcessor

from urllib import request
from http.client import HTTPResponse

class ProcessorDownloadFiles(AbsUrlProcessor):

    def __init__(self, config: ExcelWriterConfig, timeout: int) -> None:
        super().__init__(config, timeout)

        self._error_log: list[tuple[str,str]] = []
        
    def _get_savefile_path(self, file_name:str) -> str:
        return "".join([
            self.config.path_download, 
            file_name, 
            self.config.file_type
            ])
    
    def _write_log(self, name: str, url: str, response: HTTPResponse) -> None:

        self._set_log_entry(name, "column_downloaded", self.processed_column)
        self._set_log_entry(name, "url", url)

        _file_size = self._get_file_size(response)
        self._set_log_entry(name, "file_size", _file_size)

    def _get_file_size(self, response: HTTPResponse) -> int:
        if "Content-Length" not in response.headers:
            return 0
        try:
            _size = response.headers["Content-Length"]
            return int(_size)
        except:
            return 0

    
    def url_function(self, name_url: tuple[str, str]) -> None:
        _name:str = name_url[0]
        _url:str = name_url[1]

        _save_path:str = self._get_savefile_path(_name)
                
        try:   
            _repsonse: HTTPResponse
            with request.urlopen(_url, timeout=self.timeout) as _repsonse:             

                self._write_log(_name, _url, _repsonse)

                with open(_save_path, 'wb') as f:
                    f.write(_repsonse.read())

        except Exception as e:
            self._set_log_entry(_name, "error", e)
            return

    def print_log(self):
        for _name in self.log:
            _error = self._get_log_entry(_name, "error")
            if _error is None:
                continue
            print(_name)
            print(_error)
            print()