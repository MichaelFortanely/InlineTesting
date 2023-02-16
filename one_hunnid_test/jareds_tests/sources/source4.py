import re
#from inline import Here

# 1 Regex: finds 3 letter words
text = "This is filler text."
matches = re.findall(r'\b\w{3}\b' , text)
#Here().given(text, "The quick brown fox jumps over the lazy dog.").check_eq(matches, ['The', 'fox', 'the', 'dog'])

# 2 Regex: replaces '= (' with '= document.querySelector(' for html files
example_list_from_file = ['const button = ("#button");',
                          'const icon = ("#button > i");',
                          'const audio = ("audio");']
str_output = []
for i in range(len(example_list_from_file)):
    str_output.append(re.sub(r'(?is)=.\(', '= document.querySelector(', example_list_from_file[i]))
#   Here().given(i, 0).given(example_list_from_file[0], 'const button = ("#button");').check_eq(str_output[0], 'const button = document.querySelector("#button");')

# 3 Regex: finds 5 letter words starting with a and ending with e
pattern = ''
matched = []
word_list = []
matched = list(filter(re.compile(pattern).match, word_list))	
#Here().given(pattern, '^a...e$').given(word_list,
#                                        ['aback',
#                                        'abase',
#                                        'abate',
#                                        'abbot',
#                                        'abhor',
#                                        'abide',
#                                        'abled',
#                                        'abuse',
#                                        'above']).check_eq(matched, ['abase', 'abate', 'abide', 'abuse', 'above'])


# 4 Regex: Searches if a or b is in the text
find = re.search(pattern, text)
#Here().given(pattern, "^a|b").given(text, 'cdefg').check_eq(find, None)

# 5 Regex: Splits string into list at first found number
result = re.split(pattern, text, 1)
#Here().given(pattern, '\d+').given(text, 'There are 99 problems, this could be 1.').check_eq(result, ['There are ', ' problems, this could be 1.'])