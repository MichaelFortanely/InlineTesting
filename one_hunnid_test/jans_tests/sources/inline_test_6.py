# Inline Test # 6
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/31/23

import random

# type: string manipulation

# purpose: convert a random 8-bit binary number to hex by
# dividing the work in 2 equal 4-bit numbers 

for iter in range(10):
    # generate random binary number
    bin_num = ""
    for digit in range(8):
        bin_num = bin_num + str(random.randint(0, 1))

    # convert to hex
    l_bit = str(hex(int(bin_num[0:4], 2)))
    r_bit = str(hex(int(bin_num[4:8], 2)))
    print("0b"+ bin_num + " -> " + "0x" + l_bit[2] + r_bit[2])
