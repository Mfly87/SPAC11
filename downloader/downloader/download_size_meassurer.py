from excel.writer.excel_writer_config import ExcelWriterConfig
from .abs_url_processor import AbsUrlProcessor

from urllib import request, response, parse
from http.client import HTTPResponse
class DownloadSizeMeassurer(AbsUrlProcessor):

    def __init__(self, config: ExcelWriterConfig, timeout: int) -> None:
        super().__init__(config, timeout)

    def url_function(self, name_url: tuple[str, str]) -> None:
        _name:str = name_url[0]
        _url:str = name_url[1]

        try:
            _file_size = self.get_file_size(_url)
            _file_size = int(_file_size)
        except:
            return
                
        self._set_log_entry(_name, "file_size", _file_size)

        
    
    def get_file_size(self, url_link: str) -> float:
        request.urlcleanup()

        url: HTTPResponse
        with request.urlopen(url_link, timeout=self.timeout) as url:
            info: dict[str,str] = url.info()
            return info["Content-Length"]
        
    def print_log(self) -> None:

        _len = 0
        _sum = 0
        for _name in self.log:
            _size = self._get_log_entry(_name, "file_size")
            _sum += _size
            if 0 < _size:
                _len += 1

        _endig = ["","K","M","G","T","P"]
        while 1024 < _sum:
            _sum /= 1024.0
            del _endig[0]

        print("%i files" % (_len))
        print("Total size: %.2f %sB" % (_sum, _endig[0]) )