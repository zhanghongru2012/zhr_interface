# coding=gbk
import xlrd
import time
import json
import configparser
from Base.get_token import *
from Base.read_config import *

'''
1. 核心标准库：xlrd，requests，json
2. 涉及知识点：xlrd，requests，json，读写文件
'''


def interface_check():
    # 设定测试用的文件
    workbook = xlrd.open_workbook('../data/interface.xlsx')
    # 找到所用表格中的sheet名称
    interface_sheet = workbook.sheet_by_name('interfaces')
    # 获取行数（和列数，列数这里都是直接赋值了，没有过多的方法）
    num_nows = interface_sheet.nrows
    num_cols = interface_sheet.ncols
    # 定义请求头，预设两种，一种带token，一种不带token
    headers_without_token = {'Content-Type': 'application/json'}
    headers_token = {'Content-Type': 'application/json', 'token': login()}
    # 读取在config.ini中存好的host
    base_url = ReadConfig().get_gonfig("HTTP", "base_url")
    print(base_url)
    # 核心代码：遍历excel中的接口参数
    for i in range(1, num_nows):
        # 第一列“接口名称”
        interface_name = interface_sheet.row_values(i)[0]
        # 第三列“接口路径”
        path = interface_sheet.row_values(i)[2]
        # 拼接完整接口
        url = base_url + path
        # 第四列“接口传参”
        data = interface_sheet.row_values(i)[3]
        # 第九列“接口请求方式”
        method = interface_sheet.row_values(i)[8]

        # 发送get、post请求
        if method == "get":
            r = requests.get(url=url, params=data)
        else:
            r = requests.post(url=url, headers=headers_token, data=data)
        # 根据请求的返回状态值存档
        if json.dumps(r.status_code) == "200":
            with open('../log/log_success.txt', 'a') as f:
                print(i, ".", interface_name, file=f)
                print("接口请求时间：", time.ctime(), file=f)
                print("URL------->", url, file=f)
                print("RESPONSE-->", r.status_code, r.text, file=f)

        else:
            with open('../log/log_fail.txt', 'a') as f:
                print(i, ".", interface_name, file=f)
                print("接口请求时间：", time.ctime(), file=f)
                print("URL------->", url, file=f)
                print("RESPONSE-->", r.status_code, r.text, file=f)





