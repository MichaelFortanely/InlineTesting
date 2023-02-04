# Inline Test # 10
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 2/1/2023

import random

# type: string manipulation

# purpose: change the string to upper-case

for iter in range(10):
    word = ""
    res = ""
    for n in range(5):
        # generate word
        ch_idx = random.randint(0, 14)
        word += chr(97 + ch_idx)
        res += chr(65 + ch_idx)
    
    print("\"" + word + "\".upper() -> " + res)
