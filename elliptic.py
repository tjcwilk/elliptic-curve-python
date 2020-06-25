#!/usr/bin/env python3

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec


class Ellyptic:

    def __init__(self):
        self.private_key = False
        self.public_key = False


    def ping(self):
        print("Pong!")


    def generate_private_key(self):
        self.private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
        print("-> Public Key Generated");


    def get_private_key(self):
        return self.private_key.private_numbers().private_value


    def sign_data(self, data):
        signature = self.private_key.sign( data, ec.ECDSA( hashes.SHA256() ) )
        print("-> Signature Created")
        return signature



if __name__ == "__main__":

    ellyptic = Ellyptic()
    ellyptic.generate_private_key()
    print("-> Private Key: %d" % ellyptic.get_private_key())

    signature_DER_encoded_bytes = ellyptic.sign_data(b"Hello world!");
    print("-> Signature: %s" % signature_DER_encoded_bytes)

