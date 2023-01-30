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

# 3. Bit manipulation: count number of set bits in binary representation of `num`
count = 0
while num:
    count += num & 1
    Here().given(num, 0).check_eq(count, 2)
    num >>= 1
print("Number of set bits: ", count)

# 4. String manipulation: join all words in text using "-"
result = "-".join(text.split())
Here().given(text, "This is is a sentence that was originally split by spaces :)").check_eq(result, "This-is-is-a-sentence-that-was-originally-split-by-spaces-:)")
print("Text joined with '-': ", result)

# 5. Regex: replace all "is" with "was"
result = re.sub("is", "was", text)
print("Text with 'is' replaced: ", result)

# 6. Bit manipulation: toggle the 3rd bit in binary representation of `num`
num = num ^ (1 << (3 - 1))
Here().given(num, 5).check_eq(num, 1)
print("Number after toggling 3rd bit: ", num)

# 7. String manipulation: find the length of text
result = len(text)
Here().given(text, "agfhsfbkagfasifyewb7orewvrtkuybfsd.][kspb,lf][sn;bM<.;WaEMjmBLa1ds'tdzgj").check_eq(result, 72)
print("Length of text: ", result)

# 8. Regex: match all digits in text
result = re.findall(r"\d", text)
print("Digits in text: ", result)

# 9. Bit manipulation: convert `num` to binary representation
result = bin(num)
print("Binary representation of num: ", result)

# 10. String manipulation: split text by " " (whitespace)
result = text.split()
print("Text split by whitespace: ", result)
