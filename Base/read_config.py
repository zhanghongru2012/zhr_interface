import configparser
import os

'''
1. 这个文件是用来读取config.ini文件的公共类
2. 类名：ReadConfig
3. 核心标准库：configparser
4. 涉及函数/方法：os、configparser、join
'''

# 首先读取当前路径，然后利用当前路径去拼接config.ini的相对路径，以后自己写脚本时候都尽量使用相对路径
now_dir = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(now_dir, "config.ini")


class ReadConfig:
    def __init__(self):
        # 初始化configparser.ConfigParser()--->重定义为 cf，方便使用
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)

    # 获取config.ini文件
    def get_gonfig(self, section, key):
        '''
        :param section:config.ini文件[]中的部分
        :param key: 所选section中的字段名
        :return: 返回key对应的字段值
        '''
        values = self.cf.get(section, key)
        return values

    # 写入config.ini文件的方法
    def set_config(self, section, key, value):
        '''

        :param section:同上个方法
        :param key: 同上个方法
        :param value: 同上个方法
        '''
        fb = open(config_path, 'w')
        self.cf.set(section, key, value)
        self.cf.write(fb)