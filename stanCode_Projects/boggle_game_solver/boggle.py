"""
File: boggle.py
Name: Calvin Chen
----------------------------------------
This program plays the 4x4 boggle game.
This program recursively finds all the word that
more than four alphabets and terminates when input
string is not alphabet or input string is more than
one character.

If you correctly implement this program,
you should see number of word in below.

	* Input = [f y c l   -> 21 words
			i o m g
			o r i l
			h j h u]

"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global Variable
python_list = []					# This list stores all the word from dictionary.


def main():
	"""
	This function reads the dictionary, makes user input the alphabet, turns all the alphabet
	into lower case, and checks when to continue the game.
	"""
	read_dictionary()
	# Store the input alphabet into a list which is a 2x2 matrix
	check_lst = []

	# Control whether the character append on list or not.
	key = True
	for i in range(1, 5):
		letter_str = str(input(f'{i} row of letters: '))
		letter_list = str_manipulation(letter_str).split()
		key = decide_play(letter_list)
		# Condition controls that whether user should still input the character.
		if key:
			check_lst.append(letter_list)
		else:
			print('Illegal Input')
			break

	# Condition controls play boggle game or not.
	if len(check_lst) == 4:
		boggle(check_lst)


def str_manipulation(s):
	"""
	This function turns all the alphabet into lower case.
	----------------------------------------------------------------------------
	:param s: (str) the word that user input.
	:return: ans (str), the word with the lower case.
	"""
	ans = ''
	for ch in s:
		if ch.isupper():
			ans += ch.lower()
		else:
			ans += ch
	return ans


def decide_play(lst):
	"""
	This function will return the boolean to control whether user should continue the game.
	----------------------------------------------------------------------------
	:param lst: (list) a list stores the input alphabet.
	:return: (bool) if the input character is alphabet and if only one character is in the string.
	"""
	if len(lst) == 4:
		for char in lst:
			if char.isalpha() and len(char) == 1:
				pass
			else:
				return False
		return True
	else:
		return False


def boggle(lst):
	"""
	This function loops each alphabet in the list and inputs that alphabet
	into the helper function to find the word in the boggle game.
	----------------------------------------------------------------------------
	:param lst: (list) a list that stores all the input alphabet in a 2x2 matrix.
	:return: None.
	"""
	# First, loop over each char in grip(2x2 matrix)
	control_list = []
	ans_lst = []
	for r in range(len(lst)):
		for c in range(len(lst)):
			look_up_char = lst[r][c]  # That alphabet
			boggle_helper(lst, look_up_char, control_list, ans_lst, c, r)

	print(f'There are {len(ans_lst)} words in total.')


def boggle_helper(lst, current, control_list, ans_lst, c, r):
	"""
	This function first receives the current word, which is the alphabet in the lst,
	and prints the word, the word started by that alphabet only, in the boggle game by
	using the backtracking method.
	----------------------------------------------------------------------------
	:param lst: (list), a list that stores all the alphabet.
	:param current: (string), each alphabet that we need to run in the boggle game
					and will update in each time when we run boggle_helper function.
	:param c: (int), column of the grip / each character in each list of the list
	:param r: (int), row of the grip / each index in the lst.
	:return: None.
	"""
	# Read the neighbor alphabets around that alphabet
	around_lst = neighbor_char(c, r)

	if not has_prefix(current):
		return
	# Base Case
	if len(current) >= len(lst) and current in python_list:

		if current not in ans_lst:
			print(f'Found \"{current}"')
			ans_lst.append(current)

		# Keep looping the neighbor alphabet and backtracking to find
		# if there is still word in Boggle game.
		for position in around_lst:
			# If that position(tuple) is in the control_list. Do not add that alphabet
			if position in control_list:
				pass
			else:
				control_list.append((c, r))
				boggle_helper(lst, current + lst[position[1]][position[0]], control_list, ans_lst, c=position[0], r=position[1])
				control_list.pop()
	# Recursion
	else:
		# Loop over that position's alphabet
		for position in around_lst:
			# if that position(tuple) is in the control_list. Do not add that alphabet
			if position in control_list:
				pass
			else:
				control_list.append((c, r))
				boggle_helper(lst, current + lst[position[1]][position[0]], control_list, ans_lst, c=position[0], r=position[1])
				control_list.pop()


def neighbor_char(c, r):
	"""
	This function will return all the neighboring alphabet position by taking
	the point we needed and then ignoring the point outside the zone.
	----------------------------------------------------------------------------
	:param c: (int) the columns index position in the grid(list) (c, r)
	:param r: (int) the row index position in the grid(list) (c, r)
	:return: neighbor_lst (list) the point around that alphabet and showed by (c, r)
	"""
	# Create a list to store needed point
	neighbor_lst = []
	# Create all the point we needed
	grid = [(c - 1, r - 1), (c, r - 1), (c + 1, r - 1),
			(c - 1, r), (c + 1, r),
			(c - 1, r + 1), (c, r + 1), (c + 1, r + 1)]
	# Loop over each point and Set the condition to control the point we needed
	for i in range(len(grid)):
		if grid[i][0] == -1 or grid[i][0] == 4 or grid[i][1] == -1 or grid[i][1] == 4:
			pass
		else:
			neighbor_lst.append(grid[i])
	return neighbor_lst


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global python_list
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			python_list.append(line)


def has_prefix(sub_s):
	"""
	This function returns the boolean to explore the word quickly.
	---------------------------------------------------------------------------
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global python_list
	for word in python_list:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
