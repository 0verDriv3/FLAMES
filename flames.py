"""
	Title: FLAMES Game
	Author: Diamond Engalan Rivero
	Date: 03/02/2021
"""

flames = ["F","L","A","M","E","S"]
removedChar = [] 
removedChar_fixedDup = []
n1p = 0
n2p = 0

name1 = list(str(input("Enter name: ")).replace(" ", "").lower())
name2 = list(str(input("Enter name: ")).replace(" ", "").lower())

if len(name1) and len(name2) > 0:

	# For comparing and removing second name characters in first name characters
	for n1 in name1:
		counter = 0
		for n2 in name2:
			if n1 == n2:
				removedChar.append(name2.pop(counter))
				n2p += 1
			counter += 1

	# Fix duplicated removed Characters
	for char in removedChar:
		if char not in removedChar_fixedDup:
			removedChar_fixedDup.append(char)

	# For comparing first name characters to removed Characters
	for n1 in name1:
		counter = 0
		for remChar in removedChar_fixedDup:
			if n1 == remChar:
				n1p += 1
			counter += 1

	total = n1p + n2p
	flamesValue = total % len(flames)
	
	print("First name result: ", n1p)
	print("Second name result: ", n2p)
	print("Total: ", total)
	print("FLAMES result: ", flames[flamesValue])