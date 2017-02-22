import requests

class Rest(object):
    def __init__(self, client):
        self.client = client

    def get(self, url):
        if(url.startswith("/all/") or url.startswith("/auth/")):
            return self.client.server_call(url)
        return self.client.auth_call("GET", url)
