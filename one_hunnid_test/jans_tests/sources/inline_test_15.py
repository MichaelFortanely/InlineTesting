# Inline Test # 15
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 2/1/23

import re

# type: regex

# purpose: implement the "strip" method with regex

words = ["   hello", " world ", "hi       i", "waddup", " hello world"]

for iter in range(len(words)):
    print("'" + re.sub("^ *| *$","",words[iter]) + "'")
