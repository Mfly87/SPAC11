class ExcelWriterConfig():
    def __init__(self, file_path: str, file_type: str) -> None:
        self._file_path: str = file_path

        if file_type[0] != ".":
            file_type = "." + file_type
        
        self._file_type: str = file_type

    @property
    def file_path(self) -> str:
        return self._file_path
    
    @property
    def file_type(self) -> str:
        return self._file_type