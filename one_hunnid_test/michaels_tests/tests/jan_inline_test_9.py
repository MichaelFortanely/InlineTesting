# Inline Test # 9
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/31/23

import sys
import re
import random
from inline import Here

# type: string manipulation and regex

# purpose: remove all vowels from a string

# simulate input
input_list = sys.argv[1:]

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

    # verify
    Here().given(input_list, word).check_eq(re.sub("[aeiou]", "", word), ans)
