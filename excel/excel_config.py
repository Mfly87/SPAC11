from .reader import ExcelReaderConfig
from .writer import ExcelWriterConfig

class ExcelConfig():
    def __init__(self, excel_reader_config: ExcelReaderConfig, excel_writer_config: ExcelWriterConfig) -> None:
        self._excel_reader_config = excel_reader_config
        self._excel_writer_config = excel_writer_config

    @property
    def excel_reader_config(self) -> ExcelReaderConfig:
        return self._excel_reader_config
    
    @property
    def excel_writer_config(self) -> ExcelWriterConfig:
        return self._excel_writer_config