import re
from inline import Here

text = "This is a sentence with multiple words and numbers 1234567890."
num = 10

# 1. String manipulation: reverse text
result = text[::-1]
print("Reversed text: ", result)

# 2. Regex: match all words starting with "s"
result = re.findall(r"\bs\w+", text)
Here().given(text, "sword sewn orange clock start pass closure").check_eq(result, ['sword', 'sewn', 'start'])
print("Words starting with 's': ", result)
