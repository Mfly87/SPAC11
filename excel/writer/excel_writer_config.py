import os

class ExcelWriterConfig():
    def __init__(self, path_folder: str, file_type: str) -> None:
        if file_type[0] != ".":
            file_type = "." + file_type
        
        self._file_type = file_type

        self._path_folder = path_folder
        
        self._path_download = path_folder + '\\downloads\\'
        self.create_sub_folders(self.path_download)

        self._path_log = path_folder + '\\log\\'
        self.create_sub_folders(self.path_log)

    @property
    def path_folder(self) -> str:
        return self._path_folder
    @property
    def path_download(self) -> str:
        return self._path_download
    @property
    def path_log(self) -> str:
        return self._path_log
    
    @property
    def file_type(self) -> str:
        return self._file_type
    
    def create_sub_folders(self, path: str):
        try:
            os.mkdir(path)
        except FileExistsError:
            pass