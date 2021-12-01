"""
Code for day 1 of the 2021 Advent of Code challenge :)
"""

# SYSTEM IMPORTS

# THIRD PARTY IMPORTS

# LOCAL APPLICATION IMPORTS


def read_input():
    # Read input file
    input_data = open("day_01_input", "r")

    cleaned_data = []
    for item in input_data:
        # Re-output each of the items to cleaned_data as an cleaned int
        cleaned_data.append(int(item.split("\n")[0]))

    # Output the cleaned data
    return cleaned_data


def check_higher_counts_p1():
    count = 0
    prev_number = 99999999999

    input_data = read_input()

    for item in input_data:
        # Check if the current number is higher than the previous number
        if item > prev_number:
            count = count + 1
        # And then overrite the previous number
        prev_number = item

    return count


def check_higher_counts_p2():
    count = 0
    prev_number = 99999999999

    input_data = read_input()

    # Run through each item in the list and enumerate it as well to be used inside of loop
    for index, item in enumerate(input_data):
        # Grab the current item, the next item, and the item after that as an array
        new_items = input_data[index:index+3]
        # And add them together
        new_items_sum = sum(new_items)

        # Check if the summed item is higher than the previous number
        if new_items_sum > prev_number:
            count = count + 1
        # And then overrite the previous number
        prev_number = new_items_sum

    return count


print("day_01_part01 result: {}".format(check_higher_counts_p1()))
print("day_01_part02 result: {}".format(check_higher_counts_p2()))
