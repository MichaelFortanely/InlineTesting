# Inline Test # ?
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/25/23

import sys
import re
from inline import Here

# type: regex test

# purpose: test regex-based implementation of the split method 

# simulate input
input_list = sys.argv[1:]

# text to "tokenize"
txt = "Have you anything ever had a dream that you, um, you had, your, you- you could, " \
    "you’ll do, you- you wants, you, you could do so, you- you’ll do, you could- " \
    "you, you want, you want him to do you so much you could do anything?"

# parse this text
res = re.findall(r"[- ’A-Za-z]*,|[- ’A-Za-z]*\?", txt)
idx = 0
for tok in res:
	tok = tok.replace(",", "")
	res[idx] = tok
	idx += 1

# expected answer
ans = txt.split(",")

# verify
Here().given(input_list, txt).check_eq(res, ans)