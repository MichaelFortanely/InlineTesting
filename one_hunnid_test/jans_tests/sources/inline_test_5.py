# Inline Test # 5
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/31/23

import random

# type: string manipulation

# purpose: determine whether a password is acceptable,
# i.e. if the password has at least one letter

poss_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'X', 'Y']
for iter in range(10):
	# generate an identification number
	password = ""
	for digit in range(6):
		password = password + str(poss_digits[random.randint(0, 11)])

	# determine if it's safe password
	print(password + ":")
	if(password.isdecimal()):
		print("acceptable password - good combination!")
	else:
		print("unacceptable password - all digits :(")

	# expected answer
	ans = True
	try:
		num = int(password)
	except:
		ans = False

	print("")
