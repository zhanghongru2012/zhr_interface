import requests
from .read_config import ReadConfig


"""
1. 功能A：模拟用户登录获取token备用，为什么要获取token我就不说了
2. 功能B：被测系统的域名写成了活的，手输域名后会写入config.ini，输入域名时需带上协议
3. 核心标准库：requests
4. 涉及知识点：input、requests、for循环、字典等
"""


def input_phone():
    '''
    :return:返回输入的电话号
    '''
    phone = input("请输入电话号码：")
    return phone


def input_password():
    '''
    :return:返回输入的密码
    '''
    password = input("请输入密码----：")
    return password


def login():
    # 输入主域名
    input_host = input("请输入主域名（带http/https）：")
    # 把输入的主域名写入config.ini
    ReadConfig().set_config("HTTP", "base_url", input_host)
    # 把base_url重新赋值
    base_url = ReadConfig().get_gonfig("HTTP", "base_url")
    # 以下为模拟登陆过程
    url = base_url + "/v2.0/login/index"
    headers = {"Content-Type": "X-WWW-FORM-URLENCODED"}
    data = {"phone": input_phone(),
            "password": input_password(),
            "dev_type": 4}
    r = requests.post(url=url, headers=headers, data=data)
    # 遍历登录接口的返回值，找到token并存下
    for token_key, token_value in r.headers.items():
        if token_key == "token":
            return(token_value)

            # print(token_value)

# login()

