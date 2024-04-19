from excel.writer.excel_writer_config import ExcelWriterConfig
from .abs_url_processor import AbsUrlProcessor

from urllib import request, error

class PdfDownloader_test(AbsUrlProcessor):

    def __init__(self, config: ExcelWriterConfig, timeout: int) -> None:
        super().__init__(config, timeout)

        self._error_log: list[tuple[str,str]] = []

    def url_function(self, name_url: tuple[str, str]) -> None:
        _name:str = name_url[0]
        _url:str = name_url[1]

        _save_path:str = self.get_savefile_path(_name)
                
        try:   
            _request = request.urlopen(_url, timeout=self.timeout)       
            with open(_save_path, 'wb') as f:
                    f.write(_request.read())
        except Exception as e:
            self._error_log.append((_name, e))
            return

    def print_log(self):
        for _name, _error in self._error_log:
            print(_name)
            print(_error)
            print()
        
    def get_savefile_path(self, file_name:str) -> str:
        return "".join([
            self.config.file_path, 
            file_name, 
            self.config.file_type
            ])