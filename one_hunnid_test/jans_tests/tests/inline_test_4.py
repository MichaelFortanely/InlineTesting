# Inline Test # 4
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/31/23

import sys
from inline import Here

# type: bit manipulation

# purpose: encrypt a message

#simulate input
input_list = sys.argv[1:]

# function 1: convert decimal number to 36
def dec_to_alpha(num):
    base_num = ""
    while num > 0:
        dig = int(num % 36)
        if dig < 10:
            base_num += str(dig)
        else:
            base_num += chr(ord('a') + dig - 10)
        num //= 36
    base_num = base_num[::-1]  #To reverse the string

    return base_num

# function 2: encrypt message with key
def encrypt(secret):
    encryption = int(secret, base=36)
    key = len(secret)
    return encryption << key

def decrypt(message, key):
    decryption = int(message, base=36)
    return decryption >> key


''' Encrypt and Decrypt functions '''

secret = "password"

# expected answer: message to encrypt and decrypt
key = len(secret)
print("expected answer: " + secret)

# loss-less encrypt secret message with key=len(secret)
encoded_msg = encrypt(secret)
message = dec_to_alpha(encoded_msg)
print("encrypted message: " + message)
print("key: " + str(key))

# decrypt message
decoded_msg = decrypt(message, key)
res = dec_to_alpha(decoded_msg)
print("decrypted message: " + res)

# verify
Here().given(secret, "password").given(key, 8).check_eq(encoded_msg >> key, decoded_msg)
