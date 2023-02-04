# Inline Test # 14
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 2/1/23

# type: bit manipulation

# purpose: fill a given index with 0's (all numbers
# nearby that are equal to that index are to be filled)

nums = ["3122323312", "3133321223",
        "1233312133", "3222221311",
        "3232331332", "1131133232",
        "3231133311", "1322121111",
        "1111111331", "3112121333"]

ansm = ["00ff000000", "00fff00000",
        "00fff00000", "0fffff0000",
        "0000ff0000", "00000ff000",
        "00000fff00", "000000ffff",
        "fffffff000", "0000000fff"]

idx = [2, 2, 2, 1, 4, 5, 5, 6, 0, 7]

for iter in range(10):
    # fill 0's at index
    curr_n = list(nums[iter])
    mask_idx = idx[iter]
    mask = curr_n[mask_idx]
    while((mask_idx < 10) and (curr_n[mask_idx] == mask)):
        curr_n[mask_idx] = "0"
        mask_idx += 1

    # make list into string
    print("Fill \"" + "".join(curr_n) + "\" at " + str(mask_idx) + " -> " + "".join(curr_n))
