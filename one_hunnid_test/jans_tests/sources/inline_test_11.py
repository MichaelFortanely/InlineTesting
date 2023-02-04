# Inline Test # 11
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 2/1/23

import random

# type: string manipulation

# purpose: make a string into a palindrome

for iter in range(10):

    # generate random 3-letter string
    word = ""
    for n in range(3):
        ch_idx = random.randint(0, 25)
        word = chr(97 + ch_idx) + word + chr(97 + ch_idx)

    print("make_palindrome(\"" + word[0:3] + "\") -> " + word)
    