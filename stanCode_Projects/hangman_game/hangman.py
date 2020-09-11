"""
File: hangman.py
Name: Calvin Chen
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    First, we return random_word to the ans and know how many lens is the ans.
    Second, start guess the word and play game!
    Third, if you guess the wrong alphabet, you minus 1 life and guess again.
    Fourth, if you guess the right alphabet, you will keep guessing and the
    right alphabet will replace '-'.
    Fifth, if you died or win the game(guess the right word), end the loop.
    """
    ans = random_word()
    turns = N_TURNS
    guess = ''
    first = ''
    for i in range(len(ans)):
        first += '-'
    print('The words looks like: ' + first)
    print('You have ' + str(turns) + ' guesses left')

    while guess != ans and turns != 0:
        input_ch = input('Your guess: ')
        input_ch = input_ch.upper()

        if len(input_ch) == 1 and input_ch.isalpha():
            if input_ch not in ans:

                turns -= 1
                if turns != 0 and len(guess) != len(first):
                    print('There is no ' + input_ch + '\'s' + ' in the word.')
                    print('The words looks like: ' + first)
                    print('You have ' + str(turns) + ' guesses left.')

                if turns != 0 and len(guess) == len(first):
                    print('There is no ' + input_ch + '\'s' + ' in the word.')
                    print('The words looks like: ' + guess)
                    print('You have ' + str(turns) + ' guesses left.')

            else:

                for i in range(len(ans)):
                    ch = ans[i]
                    if input_ch == ch and len(guess) == len(first):
                        guess_right = ''
                        guess_right += guess[:i]
                        guess_right += ans[i]
                        guess_right += guess[i + 1:]
                        guess = guess_right

                    if input_ch == ch and len(guess) != len(first):
                        guess += first[:i]
                        guess += ans[i]
                        guess += first[i + 1:]

                if guess != ans:
                    print('You are correct!')
                    print('The word looks like: ' + guess)
                    print('You have ' + str(turns) + ' guesses left.')
        else:
            print('illegal format.')

    if guess == ans:
        print('You are correct!')
        print('You win!!')
        print('The word was: ' + ans)

    else:
        print('There is no ' + input_ch + '\'s' + ' in the word.')
        print('You are completely hung : (')
        print('The word was: ' + ans)




def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
