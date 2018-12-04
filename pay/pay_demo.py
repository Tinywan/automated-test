#!/usr/bin/python3

import time
import json
from urllib import parse


class PayDemo:

    def request(self, method, data):
        gate_way_url = 'https://网关地址/api/gateway'
        mch_id = '12001'
        data = {
            'mch_id': mch_id,
            'method': method,
            'version': '1.0',
            'timestamp': time.time(),
            'content': json.dumps(data)
        }

    def __sign(self, param):
        if 'sign' in param:
            del param['sign']

        sorted(param)
        mch_key = "121111as2d12a2s1da1das"
        params_str = parse.urld urldecode(http_build_query(param))
        params_str = $params_str . '&key=' . $key
        parse.urlencode(query, doseq=False, safe='',
                        encoding=None, errors=None, quote_via=quote_plus)
