import unittest
import requests
import fixtures
from pycoinpit import Client

from sinon import sinon
g = sinon.init(globals())

class ProtectedTest(unittest.TestCase):
    def test_get_account(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = Client(fixtures.private_key)
        stubc = sinon.stub(coinpit_me, "get_server_pubkey")
        stubc.returns(fixtures.auth_info.json()['serverPublicKey'])
        info = coinpit_me.get_account()
        stub.restore()
        stubc.restore()
        self.assertEqual(info, fixtures.account.json())

if __name__ == '__main__':
    unittest.main()
