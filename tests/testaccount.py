import unittest

import binascii

import fixtures

from pycoinpit import Account


class AccountTest(unittest.TestCase):
    def test_create_account_with_private_and_server_public_key(self):
        account = Account(fixtures.private_key, fixtures.server_pub_key)
        self.assertEqual(account.private_key, fixtures.private_key)
        self.assertEqual(account.public_key, fixtures.user_pub_key)
        self.assertEqual(account.network_code, fixtures.network_code)
        self.assertEqual(account.user_id, fixtures.user_id)
        self.assertEqual(account.server_pub_key, fixtures.server_pub_key)
        self.assertEqual(account.shared_secret, binascii.unhexlify(fixtures.shared_secret))


if __name__ == '__main__':
    unittest.main()
