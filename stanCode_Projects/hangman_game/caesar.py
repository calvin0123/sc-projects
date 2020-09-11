"""
File: caesar.py
Name: Calvin Chen
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    First, user enter the secret number in order to know the new_alphabet string will move right how
    many times.
    Second, enter the ciphered string.
    Third, print out the deciphered string.
    """
    secret_number = input('Secret number: ')
    ciphered_string = input('What\'s the ciphered string? ')
    ciphered_string = ciphered_string.upper()
    print('The deciphered string is: ' + deciphered(secret_number, ciphered_string))


def deciphered(secret_number, ciphered_string):
    """
    First, we loop the alphabet and create the new alphabet_string by utilizing secret number.
    Second, we find where the position number of each ciphered_string alphabet is in the new alphabet_string.
    Third, we correspond the position number we found with the old alphabet_string position
    number, and print out the alphabet of old alphabet_string position.

    :param secret_number: int, know the new_alphabet string will move right how many times.
    :param ciphered_string: string. The string you want to deciphered.
    :return: ans: string. Deciphered ans.
    """
    new_alphabet = ''
    for i in range(len(ALPHABET)):
        new_alphabet += ALPHABET[i - int(secret_number)]

    ans = ''
    for j in range(len(ciphered_string)):
        alp = new_alphabet.find(ciphered_string[j])
        if alp == -1:
            ans += ciphered_string[j]
        else:
            ans += ALPHABET[alp]

    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
