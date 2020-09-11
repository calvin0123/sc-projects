"""
File: weather_master.py
Name: Calvin Chen
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


constant = -100


def main():
	"""
	pre-condition: enter all the temperature
	post-condition: answer the highest, lowest, average, and cold day(3) of the given temperature
	"""
	print('stanCode \"Weather Master 4.0!"')
	temp = int(input('Next Temperature: (or ' + str(constant) + ' to quit)? '))
	maximum = temp
	minimum = temp
	counts = 1
	cold = 0
	total = temp
	avg = total / counts

	if temp == constant:
		print('No temperature were entered.')
	else:
		while temp != constant:
			if temp < 16:
				cold += 1
			temp = int(input('Next Temperature: (or ' + str(constant) + ' to quit)? '))
			if temp != constant:
				total += temp
				counts += 1
				avg = total / counts
				if maximum < temp:
					maximum = temp
				if minimum > temp:
					minimum = temp

		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(avg))
		print(str(cold) + ' cold days(s)')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
