import unittest

import binascii

from pycoinpit import crypto
from tests import fixtures


class CryptoTest(unittest.TestCase):
    def test_shared_secret(self):
        shared_secret = crypto.get_shared_secret(fixtures.server_pub_key, fixtures.private_key)
        self.assertEqual(shared_secret, binascii.unhexlify(fixtures.shared_secret))

    def test_network_key(self):
        network_code = crypto.get_network_code(fixtures.private_key)
        self.assertEqual(network_code, fixtures.network_code)

    def test_auth_headers(self):
        headers = crypto.get_headers(fixtures.user_id, binascii.unhexlify(fixtures.shared_secret), fixtures.nonce,
                                     fixtures.method, fixtures.uri, fixtures.body)
        self.assertEqual(headers, fixtures.headers)

    def test_pub_key(self):
        pub_key = crypto.get_pub_key(fixtures.private_key)
        self.assertEqual(pub_key, fixtures.user_pub_key)

if __name__ == '__main__':
    unittest.main()
