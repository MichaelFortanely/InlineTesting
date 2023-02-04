# Inline Test # 12
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 2/1/23

import random

# type: string manipulation

# purpose: evaluate the string of a single-operator expression,
# where the expression can be "+", "-", "*", "/", "%", and "^".

op = {'+': lambda x, y: x + y,
      '*': lambda x, y: x * y,
      '-': lambda x, y: x - y,
      '/': lambda x, y: x / y,
      '%': lambda x, y: x % y,
      '^': lambda x, y: x ^ y}

sym = ["+", "*", "-", "/", "%", "^"]

for iter in range(10):

    # generate random expression
    opr = sym[random.randint(0, 3)]
    num1 = random.randint(0, 9)
    low_bound = 0
    if(opr == "/"):
        low_bound = 1
    num2 = random.randint(low_bound, 9)

    # print
    print(str(num1) + " " + opr  + " " + str(num2) + " = " + str(op[opr](num1, num2)))
