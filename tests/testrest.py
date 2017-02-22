from pycoinpit import Rest
import unittest
import fixtures
from sinon import sinon
import requests
from pycoinpit import Account

g = sinon.init(globals())


class RestTest(unittest.TestCase):
    def test_get_unauth(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.info)
        rest = Rest(fixtures.base_url)
        info = rest.get("/all/info")
        stub.restore()
        self.assertEqual(info, fixtures.info.json())

    def test_get_auth(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        account = Account(fixtures.private_key, fixtures.server_pub_key)
        rest_client = Rest(fixtures.base_url, account)
        info = rest_client.get("/account")
        stub.restore()
        self.assertEqual(info, fixtures.account.json())


if __name__ == '__main__':
    unittest.main()
