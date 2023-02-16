from inline import Here

# 151 Reverse Words in a String

s = "hi there"
split_str_list = s.split()

# 1. String Manipulation: checking list reversal
split_str_list.reverse()
Here().given(split_str_list, ['reversed.', 'is', 'This']).check_eq(split_str_list, ['This', 'is', 'reversed.'])
