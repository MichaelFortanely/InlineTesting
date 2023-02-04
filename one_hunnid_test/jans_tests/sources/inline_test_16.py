# Inline Test # 17
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 2/2/23

import random

# type: string manipulation

# purpose: string manipulation implementation of the "rjust" method

for iter in range(10):
    # generate random string
    rand_len = random.randint(1, 10)
    letters = [chr(97 + random.randint(0, 25)) for i in range(rand_len)]
    word = "".join(letters)

    # right justification of 10
    print("'" + " "*(10-len(word)) + word + "'")
    