# Inline Test # 17
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 2/2/23

import sys
import random
from inline import Here

# type: string manipulation

# purpose: string manipulation implementation of the "rjust" method

# simulate input
input_list = sys.argv[1:]

for iter in range(10):
    # generate random string
    rand_len = random.randint(1, 10)
    letters = [chr(97 + random.randint(0, 25)) for i in range(rand_len)]
    word = "".join(letters)

    # right justification of 10
    print("'" + " "*(10-len(word)) + word + "'")

    # verify
    Here().given(input_list, letters).check_eq(" "*(10-len(word)) + word, word.rjust(10))
