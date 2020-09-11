"""
File: anagram.py
Name: Calvin Chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variable
python_list = []              # This list stores all the word in dictionary
ans_lst = []                  # This list stores all the anagram.


def main():
    """
    User will enter a word and the function will help find all the
    anagrams. When user enter EXIT constant, user will leave the game.
    """
    global ans_lst
    print('Welcome to stanCode \"Anagram Generator" (or -1 to quit)')
    s = str(input('Finds anagrams for: '))
    read_dictionary()
    while True:
        if s != EXIT:
            find_anagrams(s)
            print(f'{len(ans_lst)} Anagrams: {ans_lst}')
            s = str(input('Finds anagrams for: '))
            ans_lst = []
        else:
            break


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


def find_anagrams(s):
    """
    This function creates a helper function to help find
    all anagrams.
    --------------------------------------------------------------------
    :param s: str, word that user input.
    :return: None.
    """
    find_anagrams_helper(s, '', [])


def find_anagrams_helper(s, current, char_lst):
    """
    This function recursively find all the anagrams for the word
    by using the backtracking method.
    --------------------------------------------------------------------
    :param s: (str), word that user input.
    :param current: (str), the current word in the string, which will update in each stack frame.
    :param char_lst: (list), store the index of the word and check if we have run that char before.
    :return: None.
    """
    global python_list, ans_lst

    # Condition to check if the current is in the dictionary.
    if not has_prefix(current) and len(current) != 0:
        return
    # Base Case
    if len(current) == len(s) and current in python_list:
        if current not in ans_lst:
            print(f'Searching...')
            ans_lst.append(current)
            print(f'Found: {current}')
    # Recursive
    else:
        # Loop over each index in a word and check whether
        # the current index is in the char_lst.
        for i in range(len(s)):
            if i in char_lst:
                pass
            else:
                char_lst.append(i)
                find_anagrams_helper(s, current+s[i], char_lst)
                char_lst.pop()


def has_prefix(sub_s):
    """
    This function returns the boolean to explore the word quickly.
    --------------------------------------------------------------------
    :param sub_s:(str) A substring that is constructed by a word which we lookup
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    global python_list
    for word in python_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
