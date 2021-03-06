#!/usr/bin/env python

import sys
import string
import os

def main():
	number = sys.argv[1]

	number = number.replace("-", "")
	number = number.replace(")", "")
	number = number.replace("(", "")

	for char in number:
		if char not in string.digits:
			print("Error: non-number characters detected in phone number")
			return

	if len(number) < 10:
		print("Error: phone number is not long enough.")
		return
	elif len(number) == 10:
		number = "+1"+number

	elif len(number) == 11:
		number = "+"+number

	else:
		print("Error: phone number is too long.")
		return

	#read file
	numberFile = open(os.path.join(os.path.expanduser('~'),"frosti/alertSrc/user_register/phone.txt"), 'r')
	lines = numberFile.readlines()
	numberFile.close()

	#open file for overwriting
	numberFile = open(os.path.join(os.path.expanduser('~'),"frosti/alertSrc/user_register/phone.txt"), 'w')

	#boolean set to true if matching number is found. Triggers 'number not found' message
	found = False
	
	for line in lines:
		if number not in line:
			#rewrite file
			numberFile.write(line)
		else:
			found = True
			#skip number to be deleted
			print("Phone number "+number+" has been deleted from our phone records!")

	if not found:
		print("Phone number "+number+" was not found in our records (no changes made to file)")

main()
