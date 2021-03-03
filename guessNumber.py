"""
	Title: Guessing Game
	Author: Diamond Engalan Rivero
	Date: 03/03/2021
"""
from random import randint
import os
import platform
import time

def clearScreen():
	if platform.system() == 'Linux':
		os.system("clear")

	elif platform.system() == 'Windows':
		os.system("cls")

	else:
		
		return 0

def gameTitle():
	print(" __        ___  __   __          __   __              ___")
	print("/ _` |  | |__  /__` /__` | |\ | / _` / _`  /\   |\/| |__ ")
	print("\__> \__/ |___ .__/ .__/ | | \| \__> \__> /~~\  |  | |___")
	print("---------------------------------------------------------")
	print("    [I] - Information | [*] - Status | [!] - Warning")
	print("\t\tAuthor: @onlyme_dias")
	print("\n")

	return 0

def main():
	guessNum = 0
	setDifficulty = ''
	guessLimit = 0
	secretNum = 0

	clearScreen()
	gameTitle()

	# Set difficulty of a game, based on limited guesses. 
	while True:
		clearScreen()
		gameTitle()

		setDifficulty = str(input("[I] Difficulty: [Easy]-[Medium]-[Hard]: "))

		if setDifficulty[0].lower() == 'e' or setDifficulty == 'easy':
			guessLimit = 10
			maxGuesslength = 10
			break

		elif setDifficulty[0].lower() == 'm' or setDifficulty == 'medium':
			guessLimit = 5
			maxGuesslength = 20
			break

		elif setDifficulty[0].lower() == 'h' or setDifficulty == 'hard':
			guessLimit = 3
			maxGuesslength = 30
			break

		else:
			print("[!] Invalid input, Must be e, m or h letters only for difficulties.")

	secretNum = randint(1, maxGuesslength)
	
	# The main Logic of the game
	while guessNum != secretNum and guessLimit > 0:

		while True:
			print("[I] Remaining guess: ", guessLimit)
			guessNum = int(input("[I] Enter your guess number[1 to " + str(maxGuesslength) + "]: "))

			if guessNum < 1:
				clearScreen()
				gameTitle()
				print("[!] Lower than 1 is prohibited.")

			elif guessNum > maxGuesslength:
				print("[!] Higher than a " + str(maxGuesslength) + " is prohibited.")

			elif guessNum < secretNum:
				clearScreen()
				gameTitle()
				print("[*] The Guess is [LOW], try to [HIGHER] your guess.")
				guessLimit -= 1

			elif guessNum > secretNum:
				clearScreen()
				gameTitle()
				print("[*] The Guess is [HIGH], try to [LOWER] your guess.")
				guessLimit -= 1

			elif guessNum == secretNum:
				clearScreen()
				gameTitle()

				print("[I] Correct, you're WINNER!")
				break
			else:
				print("[!]Invalid input, must be a number.")

			if guessLimit < 1:
				break

		if guessLimit != 0:

			# For playing again prompt	
			while True:
				print("[I] Do you want to try again? ")
				print("\t[Yes] or [No]:")
				try_again = str(input("> "))
				try_again.lower()

				if try_again[0] == 'y' or try_again == 'yes':
					main()

				elif try_again[0] == 'n' or try_again == 'no':
					print("[I] Thankyou for playing, Have a nice day!")
					break

				else:
					print("[!] Invalid input, must be a letters/characters")
		else:
			print("[I] LOSE, Empty remaining guess.")
			while True:
				print("[I] Do you want to try again? ")
				print("\t[Yes] or [No]:")
				try_again = str(input("> "))
				try_again.lower()

				if try_again[0] == 'y' or try_again == 'yes':
					main()

				elif try_again[0] == 'n' or try_again == 'no':
					print("[I] Thankyou for playing, Have a nice day!")
					break

				else:
					print("[!] Invalid input, must be a letters/characters")
	return 0

if __name__== '__main__':
	main()