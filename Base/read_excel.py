from .read_config import *
import time
import xlrd


'''
写的一个读写excel的公共类，这个脚本实现没有用到，正在拓展中，可以先忽略
'''


class ReadExcel:
    def __init__(self, section, key, sheet):
        data_path = ReadConfig().get_gonfig(section, key)
        work_book = xlrd.open_workbook(data_path)
        self.sheet = work_book.sheets()[sheet]

    def get_rows(self):
        rows = self.sheet.nrows
        return rows

    def get_col_data(self, col):
        col_data = self.sheet.col_values(col)
        return col_data

    def get_cell_data(self, row, col):
        cell_data = self.sheet.cell(row, col).value
        return cell_data


class WriteExcel:
    def __init__(self, section, key, sheet):
        self.data_path = ReadConfig().get_gonfig(section, key)
        self.work_book =xlrd.open_workbook(self.data_path)
        self.work_sheet =self.work_book.get_sheet(sheet)

    def set_cell(self, row, col, cell):
        self.work_sheet.write(row, col, cell)

    def save_excel(self,filename, format):
        self.time = time.strftime("Y%m%d%H%M%S%", time.localtime())
        self.report = filename + '_' + self.time + format
        self.work_book.save(self.report)


