from inline import Here

# 151 Reverse Words in a String

s = "hi there"
split_str_list = s.split()

# 1. String Manipulation: checking list reversal
split_str_list.reverse()

# 2. String Manipulation (join list into string with " ")
result = " ".join(split_str_list)
Here().given(split_str_list, ['This', 'list', 'is', 'now', 'one', 'string.']).check_eq(result, "This list is now one string.")
