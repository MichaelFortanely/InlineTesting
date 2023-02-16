from inline import Here


def num_to_hex(num): # 1
	return "0x%x" % num


def num_to_bin(num): # 2
	return bin(num)


def bin_str_to_int(bin_str): # 3
	return int(bin_str[2:], 2)
	
	
def hex_str_to_int(hex): # 4
	return int(hex[2:], 16)
	
	
def hex_str_to_bin_str(hex_str): # 5
	return num_to_bin(hex_str_to_int(hex_str))

# String Manipulation
# 1 
num = 0
hex = num_to_hex(num)

# 2
num = 5
binary = num_to_bin(num)
Here().given(num, 19).check_eq(binary, '0b10011')
