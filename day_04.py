"""
Code for day 4 of the 2021 Advent of Code challenge :)
"""

# SYSTEM IMPORTS

# THIRD PARTY IMPORTS

# LOCAL APPLICATION IMPORTS


def read_input():
    # Read input file
    input_data = open("day_04_input", "r")

    cleaned_input = []
    for item in input_data:
        line = item.split("\n")[0]
        if line:
            cleaned_input.append(line)
        else:
            cleaned_input.append("_")


    # Output the cleaned data
    return cleaned_input

def bingo_p1():
    data = read_input()

    for i in data:
        print(i)

    return data

def bingo_p2():
    data = read_input()


bingo_p1()

# print("day_04_part01 result: {}".format(bingo_p1()))
# print("day_04_part02 result: {}".format(bingo_p2()))
