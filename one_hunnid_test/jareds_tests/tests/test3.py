from inline import Here


# 2220 Minimum Bit Flips to Convert Number
def min_bit_flips(start: int, goal: int) -> int:
    # 1. Bit Manipulation: Checking if 'xor' is correct for the function
    exor = start ^ goal
    Here().given(start, 7).given(goal, 10).check_eq(exor, 13)
    count = 0
    while exor:
		# 2 Bit Manipulation: Checking 'and' with lower neighbor
        exor = exor & (exor - 1)
        Here().given(exor, 13).check_eq(exor, 12)
        count += 1
    return count


x = 0
start = 1
goal = 2

# 3 Bit Manipulation: Checking minBitFlips function
x = min_bit_flips(start, goal)
Here().given(start, 7).given(goal, 10).check_eq(x, 3)

# 4 Bit Manipulation: Makes even numbers odd
x = x | 1
Here().given(x, 2).check_eq(x, 3)

# 5 Bit Manipulation: DeMorgan checker
a = 1
b = -1
demorgan = ~(a | b) == (~a & ~b)
Here().given(a, 42).given(b, 69).check_eq(demorgan, True)