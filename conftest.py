# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# @Time    : 2023/11/14 10:59
# @Author  : Correct-Z
# @Blog    ：

import pytest
import requests,jsonpath
from data.config_env import *

@pytest.fixture()
def login():
    url = test_ip + '/platform/admin/auth/login'
    payloads = '{"username":"huh1chn","password":"OANodhrzy6QLqZ2gtTBUyg==","loginSource":"ERP"}'
    response = requests.post(url, json=payloads, headers=headers).json
    token = jsonpath.jsonpath(response, "$..token")

    return token

@pytest.fixture()
def global_variable():
    '''全局变量配置'''
    variable = {
        'test_ip': test_ip,
        'headers': headers,
        'token': login()
    }
    return variable
