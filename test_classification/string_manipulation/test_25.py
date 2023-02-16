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

# 3
binary_str = '0b0101'
num = bin_str_to_int(binary_str)

# 4
hex_str = '0x01'
num = hex_str_to_int(hex_str)
Here().given(hex_str, '0x1f').check_eq(num, 31)
