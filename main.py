from excel import ExcelConfig, ExcelWriterConfig, ExcelReaderConfig, PdfDownloader
from downloader.downloader import DownloadSizeMeassurer, PdfDownloader_test
from pathlib import Path

from excel.reader.filters import FilterDefault, FilterDefaultRedownload

print("\n\n")

download_folder = str(Path.cwd()) + '\\downloadFolder\\'

path_excel = '/import/GRI_2017_2020.xlsx'
path_excel = str(Path.cwd()) + path_excel

file_type = ".pdf"
columns_with_url = ["Pdf_URL", "Report Html Address"]
ID = "BRnum"

reader_config = ExcelReaderConfig(path_excel, "0", ID)
writer_config = ExcelWriterConfig(download_folder, file_type)
excel_config = ExcelConfig(reader_config, writer_config)

url_processor = DownloadSizeMeassurer(writer_config, 10)

filter = FilterDefaultRedownload(file_type)

pdf_downloader = PdfDownloader(
    excel_config,
    url_processor,
    filter,
    columns_with_url,
    max_downloads=50
    )

pdf_downloader.download_pdf_files()
'''
import easygui
print(easygui.fileopenbox(msg="Open Excel file", title= "Empre"))
'''

'''
import  tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)
'''
