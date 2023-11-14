# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# @Time    : 2023/11/14 13:20
# @Author  : Correct-Z
# @Blog    ：

import allure
import pytest
import requests,jsonpath

class Test_CreateOrder:

    @pytest.fixture()
    def test_CreateOrder(self,global_variable):

        payloads = '{"createTime":1699941171000,"warehouseId":"","clientUserId":584983,"orderType":"EGG_BUY","shippingFee":0,"sellOrderItems":[{"skuOrgId":197872,"standardPrice":"590.58","salesPriceWithoutVat":"551.94","goodsName":"QUARTER OUTSIDEMOULDING SUB-ASSY","availableStock":8041,"quantity":1,"eggSku":"756060K020","activityId":null,"activityGoodsSkuId":null,"discountJson":null,"activityDiscount":0,"isComplimentary":false}],"remark":"","platform":"","priceIdentityId":1,"paymentChannelCode":null,"shipId":"SH584983_1","mobile":"170657844","contact":"test gps","province":"Bangkok","stateId":1001,"city":"Bang Bon","cityId":41050,"district":"Khlong Bang Bon","districtId":70180,"address":"杭州市余杭区仓前街道","shippingFeeInvoice":0,"postCode":"10150","companyName":"test gps","detailAddress":"杭州市余杭区仓前街道","expectedDelivery":3,"activityDisAmount":0,"orderAmount":"590.58","shippingCouponAmount":0,"couponDiscount":0,"myCouponIdList":[],"eggPaymentMethodInteger":5}'
        url = global_variable().test_ip + '/platform/oms/order/createOrder'
        response = requests.post(url,json = payloads, headers = global_variable().headers, token = global_variable().token).json()
        sellorderId = jsonpath.jsonpath(response.json(), "$..sellOrderId")

        with allure.step("验证响应状态码"):
            assert response.status_code == 200

        return sellorderId

