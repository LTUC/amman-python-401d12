# simple hashing function

def hash(text):
    return sum(ord(c) for c in text)

# print(hash("Hello"))

def hash2(text):
    return sum(ord(c) for c in text) % 10

# print(hash2("Hello"))

def salt(text, salt='salt'):
    return hash(text + salt)

# print(salt("Hello"))

####################################################################

# symmetric encryption

def caesar(text, shift=3):
    return ''.join(chr(ord(c) + 3) for c in text)

# print(caesar("ABC"))

def uncaesar(cipher, shift=3):
    return ''.join(chr(ord(c) - 3) for c in cipher)

# print(uncaesar("DEF"))

#################################################################

# Assymmetric encryption (RSA)

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
 

def generate_key_pair():

    key = RSA.generate(1024) # 1024 bit
    return key

key_pair = generate_key_pair()

# print("public key : ", str(key_pair.publickey().exportKey()))
# print("private key : ", str(key_pair.exportKey()))

public_key = key_pair.publickey().exportKey()

def encrypt_msg(msg, public_key):
    cipher = PKCS1_OAEP.new(public_key)

    enc_msg = cipher.encrypt(msg)
    return enc_msg

print(encrypt_msg(b"Hello", key_pair.publickey()))
enc_text = encrypt_msg(b"Hello", key_pair.publickey())

def decrypt_msg(cipher_text, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    plain_text = cipher.decrypt(cipher_text)

    return plain_text

print(decrypt_msg(enc_text,key_pair))


