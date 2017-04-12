import unittest
import requests
import fixtures
import binascii

from pycoinpit import Account
from pycoinpit import Client
from pycoinpit import Rest
from freezegun import freeze_time

from sinon import sinon

g = sinon.init(globals())


class AuthTest(unittest.TestCase):
    def test_get_info(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.info)
        coinpit_me = Client(fixtures.private_key)
        info = coinpit_me.rest.get("/all/info")
        stub.restore()
        self.assertEqual(info, fixtures.info)

    def test_no_auth_connect(self):
        coinpit_me = Client()
        with self.assertRaises(ValueError):
            coinpit_me.connect()

    def test_auth(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.auth_info)
        coinpit_me = Client(fixtures.private_key)
        coinpit_me.connect()
        stub.restore()
        self.assertEqual(coinpit_me.account.server_pub_key, fixtures.server_pub_key)
        self.assertEqual(coinpit_me.account.shared_secret, binascii.unhexlify(fixtures.shared_secret))

    @freeze_time("2016-01-07 08:07:29.511")
    def test_auth_headers(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.auth_info)
        account=Account(fixtures.private_key, fixtures.server_pub_key)
        rest = Rest(fixtures.base_url, account)
        headers = rest.get_headers(fixtures.method, fixtures.uri, fixtures.body)
        stub.restore()
        self.assertEqual(headers, fixtures.headers)


if __name__ == '__main__':
    unittest.main()
