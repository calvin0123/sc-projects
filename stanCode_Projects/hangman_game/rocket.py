"""
File: rocket.py
Name: Calvin Chen
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 3


def main():
	"""
	Print out the rocket in the size you want.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	Print out the head of rocket.
	First loop will print out each row.
	Later loop will print out each column with '', '/', '\'.
	"""
	for i in range(SIZE):
		print(' ', end='')
		for j in range(i, SIZE-1):
			print(' ', end='')
		for k in range(i + 1):
			print('/', end='')
		for s in range(i + 1):
			print('\\', end='')
		print('')


def belt():
	"""
	Print out the belt of the rocket.
	For loop will print out each column with '='.
	"""
	print('+', end='')
	for i in range(2):
		for j in range(SIZE):
			print('=', end='')
	print('+')


def upper():
	"""
	Print out the upper body of the rocket.
	First for loop will print out each row of the upper body.
	Later for loop will print out each column of the upper body with '.', '/\', and '|'.
	"""

	for i in range(SIZE):
		print('|', end='')
		for j in range((SIZE - 1) - i):
			print('.', end='')
		for k in range(i + 1):
			print('/', end='\\')
		for s in range((SIZE - 1) - i):
			print('.', end='')
		print('|')


def lower():
	"""
	Print out the lower body of the rocket.
	First for loop will print out each row of the lower body.
	Later for loop will print out each column of the lower body with '.', '\/', and '|'.
	"""
	for i in range(SIZE):
		print('|', end='')
		for j in range(i):
			print('.', end='')
		for k in range(i, SIZE):
			print('\\', end='/')
		for s in range(i):
			print('.', end='')
		print('|')

		###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()