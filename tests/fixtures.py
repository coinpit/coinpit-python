class Result:
    def __init__(self):
        pass
    def json(self):
        return {"BTCUSD7G24":{"vol24H":{"qty":0,"btc":0,"instrument":"BTCUSD7G24"},"indexPrice":1008},"BTC1":{"vol24H":{"qty":0,"btc":0,"instrument":"BTC1"},"indexPrice":1008},"BTCUSD7G17":{"vol24H":{"qty":0,"btc":0,"instrument":"BTCUSD7G17"},"indexPrice":1008}}

class AuthResult:
    def __init__(self):
        pass
    def json(self):
        return {'serverPublicKey': '0303f8731f3fa6e0eaf26435819172696cc2ad0751ccea2bebf89eb9c0622349d0', 'userid': 'mwXrQZ2Lct5c1XHdDXni8NWyJv9v95u6EK'} 
info = Result()
private_key = "cMm46vhtEuWkY68SFzZ7wNmH3T7to3AogMbW9koXzSeKChvAzvnv"
server_pub_key = "0303f8731f3fa6e0eaf26435819172696cc2ad0751ccea2bebf89eb9c0622349d0"
shared_secret = "29dbd87c4cff080a464e2ea9b00050a7d9bc3f067c466f1c21a0cb1b0528bf46"
auth_info = AuthResult()
