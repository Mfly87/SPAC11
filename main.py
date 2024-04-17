import pandas as pd
from pandas import DataFrame
from pathlib import Path
import urllib

from excel.reader.filters import FilterNotDownloadedInColumn
from excel import ExcelReader

from urllib import request, response, parse

import os.path

import glob

print("\n\n")

download_folder = str(Path.cwd()) + '\\downloadFolder\\'

'''
path_excel = '/import/GRI_2017_2020.xlsx'
path_excel = str(Path.cwd()) + path_excel

file_type = ".pdf"
column_name = "Pdf_URL"
ID = "BRnum"

excel_reader = ExcelReader(path_excel, "0", ID)
data_frame = excel_reader.get_excel_data_frame()

filter_all = FilterNotDownloadedInColumn(download_folder, file_type, column_name)
data_frame = filter_all.filter(data_frame)


count = 0
print("DF_all : %i" % (len(data_frame.index)))

def download_progress_hook(count, blockSize, totalSize):
    print(count, blockSize, totalSize)

def get_file_size(url_link: str):
    request.urlcleanup()
    with request.urlopen(url_link, timeout=1) as url:
        info: dict[str,str] = url.info()
        return info["Content-Length"]


total_size = 0

size_type = ["","K","M","G","T","P"]

size_i = 0
size_lim = 1024

tot = float(len(data_frame.index))

for x, col_id in enumerate(df.index):

    savefile = str(download_folder + str(col_id) + '.pdf')
    try:
        url_link = df.at[col_id,'Pdf_URL']
        
        #request.urlretrieve(url_link, savefile, reporthook=download_progress_hook)
        #request.urlcleanup()
        
        file_size = get_file_size(url_link)
        total_size += file_size
        print(file_size)

        if size_lim < total_size:
            size_lim *= 1024
            size_i += 1
        break

    except:
        pass
    print("%.2f%% - %i - %.2f %sB" % (
        100 * float(x)/tot, 
        x, 
        total_size, 
        size_type[size_i]
        ))

print("\n\n")

print("DONE!")
print(count)

print(total_size)
'''


from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))