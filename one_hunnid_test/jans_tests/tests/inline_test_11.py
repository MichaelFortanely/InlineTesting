# Inline Test # 11
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 2/1/23

import sys
import random
from inline import Here

# type: string manipulation

# purpose: make a string into a palindrome

# simulate input
input_list = sys.argv[1:]

for iter in range(10):
    word = ""
    for n in range(3):
        # generate word
        ch_idx = random.randint(0, 25)
        word = chr(97 + ch_idx) + word + chr(97 + ch_idx)
    print(word[0:3] + " => " + word)

    # verify
    Here().given(input_list, word).check_eq(word, word[0:3] + "".join(reversed(word[0:3])))