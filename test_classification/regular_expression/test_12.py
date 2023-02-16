import re
from inline import Here

# 1 Regex: finds 3 letter words
text = "This is filler text."
matches = re.findall(r'\b\w{3}\b' , text)


# 2 Regex: replaces '= (' with '= document.querySelector(' for html files
example_list_from_file = ['const button = ("#button");',
                          'const icon = ("#button > i");',
                          'const audio = ("audio");']
str_output = []
for i in range(len(example_list_from_file)):
    str_output.append(re.sub(r'(?is)=.\(', '= document.querySelector(', example_list_from_file[i]))
    Here().given(i, 0).given(example_list_from_file[0], 'const button = ("#button");').check_eq(str_output[0], 'const button = document.querySelector("#button");')

# 3 Regex: finds 5 letter words starting with a and ending with e
pattern = ''
matched = []
word_list = []
matched = list(filter(re.compile(pattern).match, word_list))	



# 4 Regex: Searches if a or b is in the text
find = re.search(pattern, text)


# 5 Regex: Splits string into list at first found number
result = re.split(pattern, text, 1)
