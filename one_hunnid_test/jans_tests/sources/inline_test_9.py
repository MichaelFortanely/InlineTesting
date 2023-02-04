# Inline Test # 9
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/31/23

import re
import random

# type: string manipulation and regex

# purpose: remove all vowels from a string

for iter in range(10):
    word = ""
    ans = ""
    for n in range(5):
        # generate word
        ch = chr(97 + random.randint(0, 14))
        word += ch

        # add only if char is consonant
        if(not(ch in ('a', 'e', 'i', 'o', 'u'))):
            ans += ch

    print("remove_vowels(\"" + word + "\"):")
    print(re.sub("[aeiou]", "", word) + "\n")
