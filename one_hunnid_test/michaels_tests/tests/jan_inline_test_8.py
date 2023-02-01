# Inline Test # 8
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/31/23

import sys
import re
import random
from inline import Here

# type: bit manipulation

# purpose: use string manipulation to display only even digits
# by replacing all odd digits with 0.

#simulate input
input_list = sys.argv[1:]

for iter in range(10):
    # store answer
    ans_str = ""

    # generate random decimal
    dec_str = ""
    mask_str = ""
    for dig in range(8):
        curr_dig = random.randint(0, 9)
        dec_str = dec_str + str(curr_dig)
        if(curr_dig % 2 == 0):
            ans_str += str(curr_dig)
            mask_str += "f"
        else:
            ans_str += "0"
            mask_str += "0"
    
    dec_num = int(dec_str, 16)
    hex_mask = int(mask_str, 16)
    ans = int(ans_str, 16)

    print("  " + hex(dec_num))
    print("& " + hex(hex_mask))
    print("-----------")
    print("  " + hex(ans))
    print()

    # verify
    Here().given(input_list, dec_str).check_eq(hex(dec_num & hex_mask), hex(ans))