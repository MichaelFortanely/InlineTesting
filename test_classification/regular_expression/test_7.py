import re
from inline import Here

text = "This is a sentence with multiple words and numbers 1234567890."

# 1. Match all letters in the text
result = re.findall(r"[a-zA-Z]", text)
print("Letters: ", result)
# 2. Match all digits in the text
result = re.findall(r"\d", text)
print("Digits: ", result)

# 3. Match all words starting with "s"
result = re.findall(r"\bs\w+", text)
print("Words starting with 's': ", result)

# 4. Match all words ending with "e"
result = re.findall(r"\w+e\b", text)
print("Words ending with 'e': ", result)

# 5. Match all words containing "o"
result = re.findall(r"\b\w*o\w*\b", text)
Here().given(text, "owl watch banana bugs orange frozen constitution a June").check_eq(result, ['owl', 'orange', 'frozen','constitution'])
print("Words containing 'o': ", result)

# 6. Match all words of length 4
result = re.findall(r"\b\w{4}\b", text)
print("Words of length 4: ", result)

# 7. Replace all whitespaces with "-"
result = re.sub(r"\s", "-", text)
print("Text with whitespaces replaced: ", result)

# 8. Replace all "is" with "was"
result = re.sub(r"is", "was", text)
print("Text with 'is' replaced: ", result)

# 9. Split text by " " (whitespace)
result = re.split(r"\s", text)
print("Text split by whitespace: ", result)
