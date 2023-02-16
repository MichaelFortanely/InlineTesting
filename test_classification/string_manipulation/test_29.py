from inline import Here

text = "This is a string with multiple words and numbers 1234567890."
num = 10

# 1. Convert `num` to binary representation
result = bin(num)
print("Binary representation of num: ", result)

# 2. Count the number of set bits in binary representation of `num`
count = 0
while num:
    count += num & 1
    num >>= 1
print("Number of set bits: ", count)

# 3. Reverse the binary representation of `num`
binary = bin(num)[2:]
result = binary[::-1]
print("Reversed binary representation: ", result)

# 4. Toggle the 3rd bit in binary representation of `num`
num = num ^ (1 << (3 - 1))
print("Number after toggling 3rd bit: ", num)

# 5. Convert the binary representation of `num` to an integer
result = int(binary, 2)
print("Integer representation of binary: ", result)

# 6. Reverse the text
result = text[::-1]
print("Reversed text: ", result)

# 7. Split text by " " (whitespace)
result = text.split()
print("Text split by whitespace: ", result)

# 8. Join all words in text using "-"
result = "-".join(text.split())
print("Text joined with '-': ", result)

# 9. Find the length of text
result = len(text)
print("Length of text: ", result)

# 10. Convert text to uppercase
result = text.upper()
Here().given(text, 'hello').check_eq(result, 'HELLO')
print("Text in uppercase: ", result)

# 11. Convert text to lowercase
result = text.lower()
print("Text in lowercase: ", result)

# 12. Replace all "is" with "was"
result = text.replace("is", "was")
print("Text with 'is' replaced: ", result)

# 13. Split text into individual characters
result = [c for c in text]
