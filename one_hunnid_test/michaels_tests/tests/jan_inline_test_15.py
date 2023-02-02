# Inline Test # 15
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 2/1/23

import sys
import re
from inline import Here

# type: regex

# purpose: implement the "strip" method with regex

# simulate input
input_list = sys.argv[1:]

words = ["   hello", " world ", "hi       i", "waddup", " hello world"]

for iter in range(len(words)):
    print("'" + re.sub("^ *| *$","",words[iter]) + "'")
    # verify
    Here().given(input_list, words).check_eq(re.sub("^ *| *$", "", words[iter]), words[iter].strip())