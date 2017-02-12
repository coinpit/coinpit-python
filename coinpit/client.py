import requests

class Client(object):

    def __init__(self, key):
        self.testnet_base_url = "https://live.coinpit.me/api/v1"
        self.livenet_base_url = "https://live.coinpit.io/api/v1"
        self.private_key = key
        if (self.private_key[0] == 'K' or self.private_key[0] == 'L'):
            self.base_url = self.livenet_base_url
            self.network_code = 0
        else:
            self.base_url = self.testnet_base_url
            self.network_code = 111

    def info(self):
        try:
            r = requests.get(self.base_url + "/all/info", headers={'Accept': 'application/json'})
            return r.content
        except:
            print "Error calling " + self.base_url + "/all/info" + "\n"
