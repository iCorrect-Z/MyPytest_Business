# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# @Time    : 2023/11/14 16:09
# @Author  : Correct-Z
# @Blog    ：

import allure
import pytest
import requests,jsonpath
from data.config_env import *
from test_CreateBBorder import Test_CreateOrder

class Test_OrderDetail:

    @pytest.fixture()
    def test_OrderDetail(self,login):
        sellOrderId = Test_CreateOrder.test_CreateOrder
        url = (test_ip + '/platform/client/eggSearch/order/detail/%s' % sellOrderId)
        response = requests.get(url, headers = headers, token = login().token).json()
        orderAmount = jsonpath.jsonpath(response, "$..orderAmount")

        with allure.step("验证响应状态码"):
            assert response.status_code == 200

        return orderAmount