# Inline Test # 7
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/31/23

import sys
import re
import random
from inline import Here

# type: regex

# purpose: Use regex to see if number is HEX

#simulate input
input_list = sys.argv[1:]

hex_dig = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l"]
for iter in range(10):

    # generate random hex
    left_bit = hex_dig[random.randint(0, 21)]
    right_bit = hex_dig[random.randint(0, 21)]
    hex_str = left_bit + right_bit
    print(hex_str + ":")

	# expected answer
    ans = True
    try:
        num = int(left_bit + right_bit, 16)
    except:
        ans = False

    # verify
    print(True if re.search("[0-9a-f][0-9a-f]", hex_str) else False)
    Here().given(input_list, hex_dig).check_eq(True if re.search("[0-9a-f][0-9a-f]", hex_str) else False, ans)
