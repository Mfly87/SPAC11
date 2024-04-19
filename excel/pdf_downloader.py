from .reader.filters import AbsFilterCombo
from .reader import ExcelReader, ExcelReaderConfig
from .writer import ExcelWriterConfig
from .excel_config import ExcelConfig

from downloader.downloader.abs_url_processor import AbsUrlProcessor

class PdfDownloader():
    def __init__(self, excel_config: ExcelConfig, processor: AbsUrlProcessor, filter: AbsFilterCombo, columns_with_url: list[str], *, max_downloads:int = -1) -> None:
        self._excel_config = excel_config
        self._filter = filter

        self._processor = processor
        self._columns_with_url = columns_with_url

        self._max_downloads = max_downloads
    
    def download_pdf_files(self):
        _reader_config = self._excel_config.excel_reader_config

        print("Reading excel file")

        excel_reader = ExcelReader(_reader_config)
        data_frame = excel_reader.get_excel_data_frame()

        if 0 < self._max_downloads:
            data_frame = data_frame[:self._max_downloads]

        for i, _column_url in enumerate(self._columns_with_url):

            print("Processing '%s' (%i/%i)" % (_column_url, i+1, len(self._columns_with_url)))

            data_frame_filtered = self._filter.filter(data_frame, _column_url)

            self._processor.download_from_data_frame(data_frame_filtered, _column_url)
        
        self._processor.print_log()