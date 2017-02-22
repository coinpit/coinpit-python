import unittest
import requests
import fixtures
import binascii
import pycoinpit

from sinon import sinon
g = sinon.init(globals())

@unittest.skip('not yet ready')
class OrdersTest(unittest.TestCase):
    def test_create_orders(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        info = coinpit_me.create_orders(fixtures.create_orders)
        stub.restore()
        self.assertEqual(info, fixtures.created_orders.json())

    def test_update_orders(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        info = coinpit_me.update_orders(fixtures.update_orders)
        stub.restore()
        self.assertEqual(info, fixtures.patched.json())

    def test_cancel_orders(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        info = coinpit_me.cancel_orders(fixtures.cancel_orders)
        stub.restore()
        self.assertEqual(info, fixtures.patched.json())

    def test_cancel_all_orders(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        info = coinpit_me.cancel_all_orders()
        stub.restore()
        self.assertEqual(info, fixtures.cancel_all)

    def test_patch_orders(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        info = coinpit_me.patch_orders(fixtures.patch_orders)
        stub.restore()
        self.assertEqual(info, fixtures.patched.json())

    def test_get_open_orders(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        info = coinpit_me.get_open_orders(fixtures.open_orders)
        stub.restore()
        self.assertEqual(info, fixtures.patched.json())

    def test_get_closed_orders(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        info = coinpit_me.get_closed_orders(fixtures.closed_orders)
        stub.restore()
        self.assertEqual(info, fixtures.patched.json())

    def test_get_cancelled_orders(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        info = coinpit_me.get_cancelled_orders(fixtures.cancelled_orders)
        stub.restore()
        self.assertEqual(info, fixtures.patched.json())

if __name__ == '__main__':
    unittest.main()
