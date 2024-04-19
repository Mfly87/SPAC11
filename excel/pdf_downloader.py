from .reader.filters import AbsFilterCombo
from .reader import ExcelReader
from .writer import ExcelWriter
from .excel_config import ExcelConfig

from downloader.urlProcessors.abs_url_processor import AbsUrlProcessor

from pandas import DataFrame

class PdfDownloader():
    def __init__(self, excel_config: ExcelConfig, processor: AbsUrlProcessor, filter: AbsFilterCombo, columns_with_url: list[str], *, max_downloads:int = -1) -> None:
        self._excel_config = excel_config
        self._filter = filter

        self._processor = processor
        self._columns_with_url = columns_with_url

        self._max_downloads = max_downloads
    
    def download_pdf_files(self) -> None:
        data_frame: DataFrame = self._get_data_frame()
        self._process_columns(data_frame)
        self._write_pdf()

    def _get_data_frame(self) -> DataFrame:
        print("Reading excel file")

        _reader_config = self._excel_config.excel_reader_config
        excel_reader = ExcelReader(_reader_config)
        data_frame = excel_reader.get_excel_data_frame()

        if 0 < self._max_downloads:
            data_frame = data_frame[:self._max_downloads]

        return data_frame

    def _process_columns(self, data_frame: DataFrame) -> None:
        for i, _column_url in enumerate(self._columns_with_url):
            print("")
            print("Processing column %i/%i: '%s'" % (i+1, 
                                               len(self._columns_with_url), 
                                               _column_url
                                               ))

            data_frame_filtered = self._filter.filter(data_frame, _column_url)

            if 0 < len(data_frame_filtered):
                self._processor.process_url(data_frame_filtered, _column_url)
            else:
                print("Nothing to process")

    def _write_pdf(self) -> None:
        print("")
        print("Writing results")
        _index_name = self._excel_config._excel_reader_config.index_column_name
        _download_path = self._excel_config._excel_writer_config.path_log
        _log = self._processor.log

        writer = ExcelWriter()
        writer.write_file(_download_path, _log, _index_name)

        print("")
        print("Done")