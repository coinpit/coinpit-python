import unittest
from sinon import sinon
import requests
import fixtures

from coinpit.client import Client
g = sinon.init(globals())

class AuthTest(unittest.TestCase):
    def test_get_info(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.info)
        coinpit_me = Client(fixtures.private_key)
        info = coinpit_me.info()
        self.assertEqual(info, fixtures.info.content)

    def test_auth(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
