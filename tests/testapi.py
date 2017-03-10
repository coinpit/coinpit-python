import unittest
import requests
import fixtures
import pycoinpit

from sinon import sinon

g = sinon.init(globals())


class OrdersTest(unittest.TestCase):

    def test_get_open_orders(self):
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.auth_info)
        coinpit_me.connect()
        stub.restore()
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.orders)
        info = coinpit_me.get_orders(fixtures.instrument)
        stub.restore()
        self.assertEqual(info, fixtures.orders.json())

    @unittest.skip('not yet ready')
    def test_create_orders(self):
        # stub = sinon.stub(requests, "get")
        # stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        coinpit_me.connect()
        info = coinpit_me.create_orders(fixtures.create_orders)
        # stub.restore()
        self.assertEqual(info, fixtures.created_orders.json())

    @unittest.skip('not yet ready')
    def test_update_orders(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        info = coinpit_me.update_orders(fixtures.update_orders)
        stub.restore()
        self.assertEqual(info, fixtures.patched.json())

    @unittest.skip('not yet ready')
    def test_cancel_orders(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        info = coinpit_me.cancel_orders(fixtures.cancel_orders)
        stub.restore()
        self.assertEqual(info, fixtures.patched.json())

    @unittest.skip('not yet ready')
    def test_cancel_all_orders(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        info = coinpit_me.cancel_all_orders()
        stub.restore()
        self.assertEqual(info, fixtures.cancel_all)

    @unittest.skip('not yet ready')
    def test_patch_orders(self):
        stub = sinon.stub(requests, "get")
        stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        info = coinpit_me.patch_orders(fixtures.patch_orders)
        stub.restore()
        self.assertEqual(info, fixtures.patched.json())

    @unittest.skip('not yet ready')
    def test_get_closed_orders(self):
        # stub = sinon.stub(requests, "get")
        # stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        coinpit_me.connect()
        info = coinpit_me.get_orders(fixtures.instrument, "closed")
        # stub.restore()
        self.assertEqual(info, fixtures.orders.open_orders())

    @unittest.skip('not yet ready')
    def test_get_cancelled_orders(self):
        # stub = sinon.stub(requests, "get")
        # stub.returns(fixtures.account)
        coinpit_me = pycoinpit.Client(fixtures.private_key)
        coinpit_me.connect()
        info = coinpit_me.get_orders(fixtures.instrument, "cancelled")
        # stub.restore()
        self.assertEqual(info, fixtures.orders.open_orders())


if __name__ == '__main__':
    unittest.main()
