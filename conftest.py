# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# @Time    : 2023/11/14 10:59
# @Author  : Correct-Z
# @Blog    ：

import pytest
from data.config_data import *


@pytest.fixture()
def login():
    print("登录成功！")


@pytest.fixture()
def global_variable():
    '''全局变量配置'''
    variable = {
        'test_ip': ,
        'downstream_token': ,
        'upstream_token':
    }
    return variable
