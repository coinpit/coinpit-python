import json


class Result:
    def __init__(self):
        pass

    def json(self):
        return {"BTCUSD7G24": {"vol24H": {"qty": 0, "btc": 0, "instrument": "BTCUSD7G24"}, "indexPrice": 1008},
                "BTC1"      : {"vol24H": {"qty": 0, "btc": 0, "instrument": "BTC1"}, "indexPrice": 1008},
                "BTCUSD7G17": {"vol24H": {"qty": 0, "btc": 0, "instrument": "BTCUSD7G17"}, "indexPrice": 1008}}


class AuthResult:
    def __init__(self):
        pass

    def json(self):
        return {'serverPublicKey': '0303f8731f3fa6e0eaf26435819172696cc2ad0751ccea2bebf89eb9c0622349d0',
                'userid'         : 'mwXrQZ2Lct5c1XHdDXni8NWyJv9v95u6EK'}


class AccountResult:
    def __init__(self):
        pass

    def json(self):
        return {'displayMargin': 0, 'positions': {}, 'userid': 'mwXrQZ2Lct5c1XHdDXni8NWyJv9v95u6EK', 'margin': 0,
                'orders'       : {'BTCUSD7G24': {}, 'BTC1': {}, 'BTCUSD7G17': {}}, 'accountMargin': 0}


info = Result()
private_key = "cMm46vhtEuWkY68SFzZ7wNmH3T7to3AogMbW9koXzSeKChvAzvnv"
server_pub_key = "0303f8731f3fa6e0eaf26435819172696cc2ad0751ccea2bebf89eb9c0622349d0"
shared_secret = "29dbd87c4cff080a464e2ea9b00050a7d9bc3f067c466f1c21a0cb1b0528bf46"
method = "POST"
uri = "/api/greetings"
body = json.dumps({"key": "key", "value": "value"}, separators=(',', ':'))
nonce = "2016-01-07 08:07:29.511",
headers = {'Accept'       : 'application/json',
           'Authorization': 'HMAC mwXrQZ2Lct5c1XHdDXni8NWyJv9v95u6EK:ec07768e88249056fae10ed223a6fbc70112b581a79a416bb796a0815df20be5',
           'Nonce'        : '1452154049511'}
auth_info = AuthResult()
account = AccountResult()
cancel_all = ["1"]

rest_get_info = {"BTCUSD7G24": {"vol24H": {"instrument": "BTCUSD7G24", "btc": 111.83523126, "qty": 242}, "indexPrice": 1114.5}, "BTC1": {"vol24H": {"instrument": "BTC1", "btc": 2.0439, "qty": 2}, "indexPrice": 1114.5}, "BTCUSD7H03": {"vol24H": {"instrument": "BTCUSD7H03", "btc": 0, "qty": 0}, "indexPrice": 1114.5}}
