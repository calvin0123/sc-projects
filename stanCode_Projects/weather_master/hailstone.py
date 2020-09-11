"""
File: hailstone.py
Name: Calvin Chen
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    pre-condition: enter a number
    post-condition: print the process of Hofstadter and the answer of how many steps
    """
    print('This program computes Hailstone sequences.')
    n = int(input('Enter a number: '))
    counts = 0

    if n == 1:
        print('It took 0 steps to reach 1.')
    else:
        while n > 1:
            if n % 2 == 0:
                n1 = n // 2  # n1 == new number when finish calculated
                print(str(n) + ' is even, so I take half: ' + str(n1))
                n = n1
                counts += 1
            else:
                n1 = n * 3 + 1
                print(str(n) + ' is odd, so I make 3n+1: ' + str(n1))
                n = n1
                counts += 1
        print('It took ' + str(counts) + ' steps to reach 1.')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
