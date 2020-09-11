"""
File: complement.py
Name: Calvin Chen
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    First, user enter a DNA strand.
    Second, print out the complement of DNA strand.
    """
    dna = str(input('Please give me a DNA strand and I\'ll find the complement: '))
    dna = dna.upper()
    print('The complement of ' + dna + ' is ' + build_complement(dna))


def build_complement(dna):
    """
    Loop the character in DNA. Concatenating the complement character in ans list.

    :param dna: string, the strand we need to complement.
    :return: ans: string, the complement strand of DNA sequence.
    """
    ans = ''
    for nucleotide in dna:
        if nucleotide == 'A':
            ans += 'T'
        elif nucleotide == 'T':
            ans += 'A'
        elif nucleotide == 'G':
            ans += 'C'
        else:
            ans += 'G'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
