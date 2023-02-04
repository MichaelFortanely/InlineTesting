# Inline Test # 7
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/31/23

import re
import random

# type: regex

# purpose: Use regex to see if number is HEX, given 2 random
# hex-digits

hex_dig = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l"]

for iter in range(10):
    # generate random hex
    left_bit = hex_dig[random.randint(0, 21)]
    right_bit = hex_dig[random.randint(0, 21)]
    hex_str = left_bit + right_bit
    print(hex_str + ": " + str(True if re.search("[0-9a-f][0-9a-f]", hex_str) else False) + "\n")