"""
File: similarity.py
Name: Calvin Chen
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    First, enter a long DNA sequence and a short DNA sequence.
    Second, print out the best match.
    """
    long_seq = input('Please give me a DNA sequence to search: ')
    long_seq = long_seq.upper()

    short_seq = input('What DNA sequence would you like to match? ')
    short_seq = short_seq.upper()

    print('The best match is ' + best_match(long_seq, short_seq))


def best_match(long_seq, short_seq):
    """
    First, know the len of long_seq and short_seq, and know how many times the long_seq
    string can loop in order to find out the best match string.
    Second, for each loop we count how many characters that look the same in each sub string(sub the long_seq)
    and assigns the counts to the max_same.
    Third, we return the sub string that includes the most same alphabet to the ans.

    :param long_seq: string, the DNA string that you will find which part is similar to short_seq.
    :param short_seq: string, the DNA string that you want to match.
    :return: ans: string, the best match string in the long_seq DNA string.
    """
    l = len(long_seq)
    s = len(short_seq)
    same = 0
    max_same = 0
    ans = ''

    for i in range(l - s + 1):
        sub_l = long_seq[i:i+s]
        same = 0
        for j in range(s):
            if sub_l[j] == short_seq[j]:
                same += 1
        if same > max_same:
            max_same = same
            ans = sub_l
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
