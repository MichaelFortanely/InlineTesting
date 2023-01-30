import re
from inline import Here

text = "This is a sentence with multiple words and numbers 1234567890."

# 1. Match all letters in the text
result = re.findall(r"[a-zA-Z]", text)
Here().given(text, "This is a senten6767684763463737667367637ce with mult697278768373865456468465316546iple words and numbers 123454646546546498464567890.").check_eq(result, ['T', 'h', 'i', 's', 'i', 's', 'a', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', 'w', 'i', 't', 'h', 'm', 'u', 'l', 't', 'i', 'p', 'l', 'e', 'w', 'o', 'r', 'd', 's', 'a', 'n', 'd', 'n', 'u', 'm', 'b', 'e', 'r', 's'])
print("Letters: ", result)
# 2. Match all digits in the text
result = re.findall(r"\d", text)
Here().given(text, "1234hflasjkfhlkasjflhflashdflasdfhuaisdfiafbbljvbif").check_eq(result, ['1', '2', '3', '4'])
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
Here().given(text, "apple watch banana bugs eye frozen constitution a June").check_eq(result, ['bugs', 'June'])
print("Words of length 4: ", result)

# 7. Replace all whitespaces with "-"
result = re.sub(r"\s", "-", text)
print("Text with whitespaces replaced: ", result)

# 8. Replace all "is" with "was"
result = re.sub(r"is", "was", text)
Here().given(text, "This sentence is in the tense originally. WOW What was that! That is cool.").check_eq(result, "Thwas sentence was in the tense originally. WOW What was that! That was cool.")
print("Text with 'is' replaced: ", result)

# 9. Split text by " " (whitespace)
result = re.split(r"\s", text)
print("Text split by whitespace: ", result)