# Inline Test # 3
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/31/23

import random

# type: bit manipulation

# purpose: multiply a binary number by 2

bin_dig = ["1", "0"]
for iter in range(10):
    # generate a response
    bin_num = "1"
    for digit in range(3):
        bin_num = bin_num + str(bin_dig[random.randint(0, 1)])
    res = bin(int(bin_num, 2) << 1)
    print("Response: " + "0b" + bin_num + " * 0b10 = " + str(res))

    # expected answer
    ans = bin(int(bin_num, 2) * 2)
    print("Answer: " + "0b" + bin_num + " * 0b10 = " + str(ans) + "\n")
