#!/usr/bin/env python

"""Generate a rabbitmq password hash."""

import os
import sys
import hashlib
import binascii

# Test Case:
#   print encode_rabbit_password_hash('CAD5089B', "simon")
#   print decode_rabbit_password_hash('ytUIm8s3AnKsXQjptplKFytfVxI=')
#   print check_rabbit_password('simon','ytUIm8s3AnKsXQjptplKFytfVxI=')
def encode_rabbit_password_hash_raw(salt, password):
    salt_and_password = salt + password
    salted_sha256 = hashlib.sha256(salt_and_password).digest()
    password_hash = salt + salted_sha256
    password_hash = binascii.b2a_base64(password_hash).strip()

    return password_hash.decode('utf-8')


def encode_rabbit_password_hash(salt, password):
    salt_and_password = salt + binascii.hexlify(password.encode('utf-8'))
    salt_and_password = bytearray.fromhex(salt_and_password)
    salted_sha256 = hashlib.sha256(salt_and_password).hexdigest()
    password_hash = bytearray.fromhex(salt + salted_sha256)
    password_hash = binascii.b2a_base64(password_hash).strip().decode('utf-8')
    return password_hash


def main():
    salt = binascii.hexlify(os.urandom(4))
    password = sys.argv[1]

    password_hash = encode_rabbit_password_hash(salt, password)

    #print("salt: %s" % salt)
    #print("pass: %s" % password)
    #print("hash: %s" % password_hash)

    sys.stdout.write(encode_rabbit_password_hash(salt, password))


if __name__ == "__main__":
    sys.exit(main())
