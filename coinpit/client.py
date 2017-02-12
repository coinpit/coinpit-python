import requests
import binascii
import pybitcointools
import pyelliptic

class Client(object):

    def __init__(self, key=None):
        self.testnet_base_url = "https://live.coinpit.me/api/v1"
        self.livenet_base_url = "https://live.coinpit.io/api/v1"
        self.private_key = key
        self.user_pub_key = None
        if(self.private_key == None):
            return
        if (self.private_key[0] == 'K' or self.private_key[0] == 'L'):
            self.base_url = self.livenet_base_url
            self.network_code = 0
        else:
            self.base_url = self.testnet_base_url
            self.network_code = 111

    def connect(self):
        if (self.user_pub_key):
            return
        if (self.private_key == None):
            raise ValueError('Private key needs to be set for protected endpoints')

        self.user_pub_key = pybitcointools.privtopub(self.private_key)
        auth_info = self.server_call("/auth/" + self.user_pub_key)
        print "auth_info {}".format(auth_info)
        self.server_pub_key = auth_info['serverPublicKey']
        self.get_shared_secret()

    def get_shared_secret(self):
        pub_key_bytes        = binascii.unhexlify(self.server_pub_key)
    	uncompressed_user_key   = binascii.unhexlify(pybitcointools.decompress(self.user_pub_key))
    	uncompressed_server_key = binascii.unhexlify(pybitcointools.decompress(self.server_pub_key))
    	user_priv_key_bin       = binascii.unhexlify(pybitcointools.encode_privkey(self.private_key, 'hex', self.network_code))
    	self.user               = pyelliptic.ECC(privkey=user_priv_key_bin, pubkey=uncompressed_user_key, curve='secp256k1')
    	self.shared_secret      = self.user.get_ecdh_key(uncompressed_server_key)

    def info(self):
        return self.server_call("/all/info")

    def server_call(self, url, headers={'Accept': 'application/json'}):
        try:
            return requests.get(self.base_url + url, headers).json()
        except Error as err:
            print "Error calling " + self.base_url + url + "\n" + err
