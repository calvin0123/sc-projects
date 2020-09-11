"""
File: Milestone1.py
Name: Calvin Chen
-----------------------
This file is to test the code for 
babyname.py milestone 1

"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.
    :param name_data: dict, dict holding name data
    :param year: str, the year of the data entry to add
    :param rank: str, the rank of the data entry to add
    :param name: str, the name of the data entry to add
    :return: name_data: dict, dict holding name data
    """
    # Add name to dict
    if name not in name_data:
        name_data[name] = {}
        name_data[name][year] = rank
    else:
        # Add new information to each name
        if year in name_data[name]:
            if int(name_data[name][year]) < int(rank):
                return name_data
            else:
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank

    return name_data


def test3():
    name_data = {'Kylie': {'2010': '57'},'Sammy': {'1980':'451','1990': '200'}}
    add_data_for_name(name_data, '1990', '100', 'Sammy')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #

def test1():
    name_data = {'Kylie':{'2010':'57'}, 'Nick':{'2010':'37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')



def test3():
    name_data = {'Kylie': {'2010': '57'},'Sammy': {'1980':'451','1990': '200'}}
    add_data_for_name(name_data, '1990', '100', 'Sammy')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test4():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    add_data_for_name(name_data, '2000', '108', 'Kate')
    add_data_for_name(name_data, '1990', '100', 'Sammy')
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()
