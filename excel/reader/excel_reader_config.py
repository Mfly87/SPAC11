class ExcelReaderConfig():
    def __init__(self, file_path: str, sheet_name: str, index_column_name: str) -> None:
        self._file_path: str = file_path
        self._sheet_name: str = sheet_name
        self._index_column_name:str = index_column_name

    @property
    def file_path(self) -> str:
        return self._file_path

    @property
    def sheet_name(self) -> str:
        return self._sheet_name
    
    @property
    def index_column_name(self) -> str:
        return self._index_column_name