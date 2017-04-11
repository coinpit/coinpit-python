import json
import requests
import time

import crypto

methods = {}
methods['GET']     = requests.get
methods['POST']    = requests.post
methods['PUT']     = requests.put
methods['DELETE']  = requests.delete
methods['PATCH']   = requests.patch
methods['OPTIONS'] = requests.options

class Rest(object):

    def __init__(self, base_url, account=None):
        self.base_url = base_url
        self.account = account

    def get(self, url):
        if url.startswith("/all/") or url.startswith("/auth/"):
            return self.server_call(url)
        return self.auth_server_call("GET", url)

    def server_call(self, url, headers={'Accept': 'application/json'}):
        try:
            return requests.get(self.base_url + url, headers=headers).json()
        except Exception as err:
            print "Error calling {} \n {}".format(self.base_url + url, err)

    def auth_server_call(self, method, url, body=None):
        assert self.account is not None, "Call to server requiring auth needs account"
        try:
            parsed_body = None if body is None else json.loads(body)
            header_body = None if parsed_body is None else json.dumps(parsed_body, separators=(',', ':'))
            headers = self.get_headers(method, url, header_body)
            method = methods[method]
            return method(url=self.base_url + url, json=parsed_body, headers=headers).json()
        except Exception as err:
            print "Error on Auth call {} \n {}".format(self.base_url + url, err)

    def get_headers(self, method, url, body):
        nonce = str(long(time.time() * 1000))
        headers = crypto.get_headers(self.account.user_id, self.account.shared_secret, nonce, method, url, body)
        return headers
