# Inline Test # ?
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/25/23

import sys
import re
import random
from inline import Here

# type: regex

# purpose: test valid id with regex, valid id is a 6 character string with one
# of the characters in poss_digits

#simulate input
input_list = sys.argv[1:]

for iter in range(10):
    # generate an identification number
    id_num = ""
    poss_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'E', 'I', 'O', 'U', 'X', 'Y']
    for digit in range(6):
        id_num = id_num + str(poss_digits[random.randint(0, 16)])
    print(id_num)

    # verify
    Here().given(input_list, poss_digits).check_true(True if re.match(r"[^BCDFGHJKLMNPQRSTVWZ]{6}", id_num) else False)
