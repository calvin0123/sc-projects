"""
File: largest_digit.py
Name: Calvin Chen
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	This function creates a helper function
	to help find the biggest digit.
	-----------------------------------
	:param n: int, number
	:return: int, the biggest digit.
	"""
	# Compared with other int, max_int will update to the biggest
	max_int = 0
	return find_largest_digit_helper(n, max_int)


def find_largest_digit_helper(n, max_int):
	"""
	This function find the biggest int by using the backtracking
	method.
	-----------------------------------
	:param n: (int) number.
	:param max_int: (int) help update the biggest digit in integers.
	:return: ans: (int) the biggest integers.
	"""
	# When int is smaller than zero.
	if n < 0:
		n //= -1
	# Base Case
	if n < 10:
		if n % 10 > max_int:
			max_int = n % 10
		return max_int
	# Recursion
	else:
		current = n % 10
		if current > max_int:
			max_int = current
		ans = find_largest_digit_helper(n // 10, max_int)
		return ans

		# 	ans = find_largest_digit_helper(n // 10, max_int)
		# 	return ans
		# else:
		# 	ans = find_largest_digit_helper(n // 10, max_int)
		# 	return ans

# ----------------------------------
# 	def find_largest_digit_helper(n):
# 		if n < 0:
# 			n //= -1
# 		# Base Case
# 		if n < 10:
# 			return n
# 		Recursion
# 		else:
# 			current = n % 10
# 			ans = find_largest_digit_helper(n // 10)
# 			if ans > current:
#      			max_int = ans
# 			else:
# 				max_int = current
# 			return ans



if __name__ == '__main__':
	main()
