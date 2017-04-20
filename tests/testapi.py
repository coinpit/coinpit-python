import unittest
import requests
import fixtures
import pycoinpit

from sinon import sinon

g = sinon.init(globals())


class OrdersTest(unittest.TestCase):

    def setUp(self):
        self.stub = sinon.stub(requests, "get")
        self.stub.onCall(1).returns(fixtures.auth_info)
        self.coinpit_me = pycoinpit.Client(fixtures.private_key)
        self.coinpit_me.connect()

    def tearDown(self):
        self.stub.restore()

    def test_get_open_orders(self):
        self.stub.onCall(2).returns(fixtures.orders)
        info = self.coinpit_me.get_orders(fixtures.instrument)
        self.assertEqual(info, fixtures.orders)

    @unittest.skip('not yet ready')
    def test_create_orders(self):
        info = self.coinpit_me.create_orders(fixtures.create_orders)
        self.assertEqual(info, fixtures.created_orders)

    @unittest.skip('not yet ready')
    def test_update_orders(self):
        info = self.coinpit_me.update_orders(fixtures.update_orders)
        self.assertEqual(info, fixtures.patched)

    @unittest.skip('not yet ready')
    def test_cancel_orders(self):
        info = self.coinpit_me.cancel_orders(fixtures.cancel_orders)
        self.assertEqual(info, fixtures.patched)

    @unittest.skip('not yet ready')
    def test_cancel_all_orders(self):
        info = self.coinpit_me.cancel_all_orders()
        self.assertEqual(info, fixtures.cancel_all)

    @unittest.skip('not yet ready')
    def test_patch_orders(self):
        info = self.coinpit_me.patch_orders(fixtures.patch_orders)
        self.assertEqual(info, fixtures.patched)

    @unittest.skip('not yet ready')
    def test_get_closed_orders(self):
        self.stub.onCall(2).returns(fixtures.closed_orders)
        info = self.coinpit_me.get_orders(fixtures.instrument, "closed")
        self.assertEqual(info, fixtures.orders.closed_orders())

    @unittest.skip('not yet ready')
    def test_get_cancelled_orders(self):
        self.stub.onCall(2).returns(fixtures.cancelled_orders)
        info = self.coinpit_me.get_orders(fixtures.instrument, "cancelled")
        self.assertEqual(info, fixtures.orders.cancelled_orders())


if __name__ == '__main__':
    unittest.main()
