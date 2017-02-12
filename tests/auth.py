import unittest
from sinon import sinon
import requests
import fixtures
import binascii

from coinpit.client import Client
g = sinon.init(globals())

class AuthTest(unittest.TestCase):
    def test_get_info(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.info)
        coinpit_me = Client(fixtures.private_key)
        info = coinpit_me.info()
        self.assertEqual(info, fixtures.info.json())

    def test_no_auth_connect(self):
        coinpit_me = Client()
        with self.assertRaises(ValueError):
            coinpit_me.connect()

    def test_auth(self):
        coinpit_me = Client(fixtures.private_key)
        coinpit_me.connect()
        self.assertEqual(coinpit_me.server_pub_key, fixtures.server_pub_key)
        self.assertEqual(coinpit_me.shared_secret, binascii.unhexlify(fixtures.shared_secret))

if __name__ == '__main__':
    unittest.main()
