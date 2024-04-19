from excel import ExcelConfig, ExcelWriterConfig, ExcelReaderConfig, PdfDownloader
from downloader.downloader import DownloadSizeMeassurer, PdfDownloader_test
from pathlib import Path
from excel.reader.filters import FilterDefault, FilterDefaultRedownload

import  tkinter as tk
from tkinter import filedialog


from pandas import DataFrame

print("\n\n")

sheet_name = "0"

excel_id_column = "BRnum"
excel_columns_with_urls = ["Pdf_URL", "Report Html Address"]

downloaded_file_type = ".pdf"
download_timout = 10





root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
folder_path = str(Path(file_path).parent)

if 1 < len(folder_path):
    reader_config = ExcelReaderConfig(file_path, sheet_name, excel_id_column)
    writer_config = ExcelWriterConfig(folder_path, downloaded_file_type)
    excel_config = ExcelConfig(reader_config, writer_config)

    url_processor = PdfDownloader_test(writer_config, download_timout)

    filter = FilterDefaultRedownload(downloaded_file_type)

    pdf_downloader = PdfDownloader(
        excel_config,
        url_processor,
        filter,
        excel_columns_with_urls,
        max_downloads=250
        )

    pdf_downloader.download_pdf_files()
    
    