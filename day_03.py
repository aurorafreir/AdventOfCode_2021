"""
Code for day 3 of the 2021 Advent of Code challenge :)
"""

# SYSTEM IMPORTS

# THIRD PARTY IMPORTS

# LOCAL APPLICATION IMPORTS


def read_input():
    # Read input file
    input_data = open("day_03_input", "r")

    cleaned_data = []

    for item in input_data:
        line = item.split("\n")[0]
        cleaned_data.append(line)


    # Output the cleaned data
    return cleaned_data

def power_consumption_p1():

    data = read_input()
    count = 0

    split_added = [0,0,0,0,0,0,0,0,0,0,0,0]

    for line in data:
        for index, i in enumerate(line):
            split_added[index] = split_added[index] + int(i)

        count = count + 1

    gamma_binary_output = [0,0,0,0,0,0,0,0,0,0,0,0]
    epsilon_binary_output = gamma_binary_output[:]

    for index, i in enumerate(split_added):
        if i >= (count/2):
            gamma_binary_output[index] = 1
            epsilon_binary_output[index] = 0
        else:
            gamma_binary_output[index] = 0
            epsilon_binary_output[index] = 1

    gamma_int_output = int(''.join(str(e) for e in gamma_binary_output), 2)
    epsilon_int_output = int(''.join(str(e) for e in epsilon_binary_output), 2)

    int_output = gamma_int_output * epsilon_int_output

    return int_output

def power_consumption_p2():

    data = read_input()
    count = 0

    split_added = [0,0,0,0,0,0,0,0,0,0,0,0]

    for line in data:
        for index, i in enumerate(line):
            split_added[index] = split_added[index] + int(i)
        count = count + 1

    oxygen_binary_output = [0,0,0,0,0,0,0,0,0,0,0,0]
    co2_binary_output = oxygen_binary_output[:]

    for index, i in enumerate(split_added):
        if i >= (count/2):
            oxygen_binary_output[index] = 1
            co2_binary_output[index] = 0
        else:
            oxygen_binary_output[index] = 0
            co2_binary_output[index] = 1

    oxygen_data = read_input()
    for index_h in range(12):
        for index_v, line in enumerate(oxygen_data):
            if line[index_h] == oxygen_binary_output[index_h]:
                pass
            else:
                oxygen_data.pop(index_v)
    print(oxygen_data)
                    

    # int_output = oxygen_binary_output * co2_binary_output

    # return int_output

print("day_03_part01 result: {}".format(power_consumption_p1()))
print("day_03_part02 result: {}".format(power_consumption_p2()))
