import  tkinter as tk
from tkinter import filedialog
from pathlib import Path

from excel import ExcelConfig, ExcelWriterConfig, ExcelReaderConfig, PdfDownloader
from excel.reader.filters import FilterDefault, FilterDefaultRedownloadEverything

from downloader.urlProcessors import ProcessorMeassureFiles, ProcessorDownloadFiles

class Config():
    sheet_name = "0"

    excel_id_column = "BRnum"
    excel_columns_with_urls = ["Pdf_URL", "Report Html Address"]

    downloaded_file_type = ".pdf"
    download_timout = 10

    max_downloads = 50
    uses_max_download = False

if __name__ == "__main__":
    print("\n\n")

    config = Config()

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    folder_path = str(Path(file_path).parent)

    if 1 < len(folder_path):
        reader_config = ExcelReaderConfig(file_path, config.sheet_name, config.excel_id_column)
        writer_config = ExcelWriterConfig(folder_path, config.downloaded_file_type)
        excel_config = ExcelConfig(reader_config, writer_config)

        #url_processor = ProcessorMeassureFiles(writer_config, config.download_timout)
        url_processor = ProcessorDownloadFiles(writer_config, config.download_timout)

        #filter = FilterDefaultRedownloadEverything(config.downloaded_file_type)
        filter = FilterDefault(writer_config.path_download, config.downloaded_file_type)
        
        max_download = config.max_downloads if config.uses_max_download else -1

        pdf_downloader = PdfDownloader(
            excel_config,
            url_processor,
            filter,
            config.excel_columns_with_urls,
            max_downloads = max_download
            )

        pdf_downloader.download_pdf_files()

        print("")
        url_processor.print_log()

    