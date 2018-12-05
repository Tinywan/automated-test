#!/usr/bin/python3

# *------------------------------------------------------------
# |  Author: Tinywan(ShaoBo Wan)
# |  DateTime: 2018/12/4 14:20
# |  Mail: 756684177@qq.com
# |  Desc: Python 支付Demo ，要求 Python 版本 3.5 及以上
# *-------------------------------------------------------------*/

import time
import json
from urllib import request, parse
from hashlib import md5
from selenium import webdriver

class PayDemo:
    gateway_url = 'https://pay.hongnaga.com/api/gateway'
    mch_id = '12001'
    mch_key = "0d8cee92eed880b379fde0b78cbdc173"

    # 支付请求
    def request(self, method, content):
        data = {
            'method': method,
            'version': '1.0',
            'timestamp': int(time.time()),
            'content': json.dumps(content),
            'mch_id': self.mch_id
        }
        sign = self.__sign(data)
        if not sign:
            return "签名失败"

        data['sign'] = sign
        b_data = parse.urlencode(data).encode('utf-8')
        res = self.curl_post(self.gateway_url, b_data)
        return json.loads(res)  # return 将json对象转换为python字典

    # 签名
    def __sign(self, param):
        if 'sign' in param:
            del param['sign']

        tmp_list = []
        sort_keys = sorted(param)  # 对keys 排序
        for k in sort_keys:
            tmp_list.append("%s=%s" % (k, param[k]))
        # 拼接key
        sign_str = "&".join(tmp_list)+"&key="+self.mch_key  
        # print("Sign-Str " + sign_str)
        sign_md5 = md5(sign_str.encode('utf-8')).hexdigest()
        # print("Sign " + sign_md5)
        return sign_md5

    # Get 请求
    def curl_get(self, url):
        request_obj = request.Request(url)
        response_obj = request.urlopen(request_obj)
        html_code = response_obj.read().decode('utf-8')
        return html_code

    # POST 请求
    def curl_post(self, url, data, headers={}):
        request_obj = request.Request(url, data, headers)
        response_obj = request.urlopen(request_obj)
        html_code = response_obj.read().decode('utf-8')
        return html_code


# 请求配置参数
method = "shop.payment.aliWap"
pay = PayDemo()
content = {
    'total_fee': '1',
    'goods': 'H5-test',
    'order_sn': int(time.time()),
    'client': 'web',
    'notify_url': 'http://www.baidu.com/notify_url',
    'return_url': 'http://www.baidu.com/return_url'
}

dict_data = pay.request(method, content)
print(dict_data)

if not dict_data['success']:
    exit("接口请求失败，错误消息："+dict_data['message'])

# 打开支付页面
drive = webdriver.Chrome()
drive.get(dict_data['data']['pay_url'])
