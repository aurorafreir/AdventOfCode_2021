"""
Code for day 1 of the 2021 Advent of Code challenge :)
"""

# SYSTEM IMPORTS

# THIRD PARTY IMPORTS

# LOCAL APPLICATION IMPORTS


def read_input():
    # Read input file
    input_data = open("day_02_input", "r")

    cleaned_data = {}
    for index, item in enumerate(input_data):
        # Re-output each of the items to cleaned_data as an cleaned set of dictionary values
        line = item.split("\n")[0]
        # Clean and split the line variable to get the movement type and value for each line
        movement = line.split(" ")[0]
        value = int(line.split(" ")[1])
        # Add the data to it's own dictionary key and value
        cleaned_data[index] = movement, value

    # Output the cleaned data
    return cleaned_data

def check_position_output_p1():
    data = read_input()

    horizontal = 0
    depth = 0

    for index, items in data.items():

        if items[0] == "forward":
            horizontal = horizontal + items[1]

        elif items[0] == "down":
            depth = depth + items[1]
        else: # UP
            depth = depth - items[1]

    final_output = horizontal * depth

    return final_output


def check_position_output_p2():
    data = read_input()

    horizontal = 0
    depth = 0
    aim = 0

    for index, items in data.items():

        if items[0] == "forward":
            horizontal = horizontal + items[1]
            depth = depth + (aim * items[1])

        elif items[0] == "down":
            aim = aim + items[1]
        else: # UP
            aim = aim - items[1]

    final_output = horizontal * depth

    return final_output


print("day_02_part01 result: {}".format(check_position_output_p1()))
print("day_02_part02 result: {}".format(check_position_output_p2()))
