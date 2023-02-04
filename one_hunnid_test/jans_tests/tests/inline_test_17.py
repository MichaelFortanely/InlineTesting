# Inline Test # 17
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 2/2/23

import sys
import re
from inline import Here

# type: regex

# purpose: regex-based implementation of the "title" function

# simulate input
input_list = sys.argv[1:]

# function: 
def uppcase(match):
    arr = match.span()
    return match.group(1).upper() + match.string[arr[0]+2:arr[1]]

# Album: The New Abnormal - The Strokes
titles = ["not the same anymore", "ode To the Mets", "Why Are Sundays So Depressing",
          "brooklyn bridge", "Eternal summer", "the adults are talking", "selfless",
          "at the Door", "bad decisions"]

for iter in range(len(titles)):
    # generate title
    print(re.sub(r'( [a-z])[a-z]*', uppcase, " "+titles[iter]).strip())

    # verify
    Here().given(input_list, titles).check_eq(re.sub(r'( [a-z])[a-z]*', uppcase, " "+titles[iter])[1:], titles[iter].title())