import unittest
from sinon import sinon
import requests
import fixtures
import binascii

from coinpit.client import Client
g = sinon.init(globals())

class ProtectedTest(unittest.TestCase):
    def test_get_account(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = Client(fixtures.private_key)
        info = coinpit_me.get_account()
        print '/account', info
        stub.restore()
        self.assertEqual(info, fixtures.account.json())

if __name__ == '__main__':
    unittest.main()
