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

secrets = ["hello", "password", "something", "code", "reply"]

for iter in range(5):
    # expected answer: message to encrypt and decrypt
    secret = secrets[iter]
    key = len(secret)
    print("expected answer: " + secret)

    # loss-less encrypt secret message with key=len(secret)
    message = dec_to_alpha(encrypt(secret))
    print("encrypted message: " + message)
    print("key: " + str(key))

    # decrypt message
    res = dec_to_alpha(decrypt(message, key))
    print("decrypted message: " + res + "\n")

    # verify
    Here().given(input_list, message).check_eq(dec_to_alpha(int(message, 36) >> key), secret)
