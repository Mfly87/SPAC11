from pandas import DataFrame

class ExcelWriter():
    
    def write_file(self, folder_path: str, dictionary: dict[str,any], index_name:str):
        df = DataFrame(dictionary).T
        _write_path = folder_path + "log.xlsx"
        df.to_excel(_write_path, index = True, index_label = index_name)