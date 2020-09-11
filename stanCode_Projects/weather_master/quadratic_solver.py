"""
File: quadratic_solver.py
Name: Calvin Chen
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	pre-condition: enter a, b, and c
	post-condition: answer of the quadratic and how many roots
	"""
	print("stanCode Quadratic Solver!")
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	disc = b * b - 4 * a * c    # disc = discriminant

	if disc > 0:
		y = math.sqrt(disc)
		root1 = (-b + y) / 2 * a
		root2 = (-b - y) / 2 * a
		print('Two roots: ' + str(root1) + ' , ' + str(root2))
	elif disc == 0:
		root1 = -b / 2 * a
		print('One root: ' + str(root1))
	else:
		print('No real roots')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
