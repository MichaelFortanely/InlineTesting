# Inline Test # 13
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 2/1/23

# type: string manipulation

# purpose: implementation of split using rpartition

sent = ["I am who I think I am",
        "I am who you think I am",
        "You are who I think you are",
        "You are who you think you are",
        "I am who I think you think I am",
        "You are who you think I think you are",
        "think",
        "think think"]

for iter in range(len(sent)):
    curr_s = sent[iter]
    print("\"" + curr_s + "\".split(\"think\") ")
    arr_s = []
    while("think" in curr_s):
        part_s = curr_s.rpartition("think")
        curr_s = part_s[0]
        arr_s = [part_s[2]] + arr_s
    arr_s = [curr_s] + arr_s
    print("-> " + str(arr_s) + "\n")
