# Inline Test # 2
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/25/23

import re
import random

# type: regex

# purpose: test valid id with regex, valid id is a 6 character string with one
# of the characters in poss_digits

# keep track of valid id's
count = 0

for iter in range(10):
    # generate an identification number
    id_num = ""
    poss_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'E', 'I', 'O', 'U', 'X', 'Y']
    for digit in range(6):
        id_num = id_num + str(poss_digits[random.randint(0, 16)])

    # is it a valid id
    print(id_num)
    if(True if re.match(r"[^BCDFGHJKLMNPQRSTVWZ]{6}", id_num) else False):
        print("valid identification number\n")
        count += 1

print(str(count) + "/10 valid id's")
