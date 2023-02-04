# Inline Test # 6
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/31/23

import sys
import re
import random
from inline import Here

# type: string manipulation

# purpose: convert a random 8-bit binary number to hex by
# dividing the work in 2 equal 4-bit numbers 

#simulate input
input_list = sys.argv[1:]

bin_dig = ["0", "1"]
for iter in range(10):
    # generate random binary number
    bin_num = ""
    for digit in range(8):
        bin_num = bin_num + str(bin_dig[random.randint(0, 1)])

    # convert to hex
    left_bit = str(hex(int(bin_num[0:4], 2)))
    right_bit = str(hex(int(bin_num[4:8], 2)))
    res_hex = "0x" + left_bit[2] + right_bit[2]
    print("0b"+ bin_num + " -> " + res_hex)

    # verify
    Here().given(input_list, bin_dig).check_eq(res_hex, str(hex(int(bin_num, 2))))

# expected answer

