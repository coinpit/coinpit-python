from pycoinpit import Rest
import pycoinpit
import unittest
import fixtures
from sinon import sinon
import requests
g = sinon.init(globals())

class RestTest(unittest.TestCase):
    def test_get_unauth(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.info)
        client = pycoinpit.Client(fixtures.private_key)
        rest_client = Rest(client)
        info = rest_client.get("/all/info")
        stub.restore()
        self.assertEqual(info, fixtures.info.json())

    def test_get_auth(self):
        client = pycoinpit.Client(fixtures.private_key)
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        stubc = sinon.stub(client, "get_server_pubkey")
        stubc.returns(fixtures.auth_info.json()['serverPublicKey'])
        rest_client = Rest(client)
        info = rest_client.get("/account")
        stub.restore()
        stubc.restore()
        self.assertEqual(info, fixtures.account.json())

if __name__ == '__main__':
    unittest.main()
