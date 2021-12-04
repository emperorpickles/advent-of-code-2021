'''
Day 3: Binary Diagnostic
'''

import time


def one_most_common(binary_list):
    '''Returns list where true if 1 appears the most in each position'''
    bit_occurances = [0] * len(binary_list[0].strip())
    for binary in binary_list:
        for i, val in enumerate(binary.strip()):
            if val == '1':
                bit_occurances[i] = bit_occurances[i] + 1

    most_ones = list(map(lambda x: True if x >= len(
        binary_list) / 2 else False, bit_occurances))
    return most_ones


def power_consumption_decode(most_ones):
    '''Returns power consumption in decimal form'''
    gamma_binary = ''
    epslion_binary = ''
    for bit in most_ones:
        if bit:
            gamma_binary += '1'
            epslion_binary += '0'
        else:
            gamma_binary += '0'
            epslion_binary += '1'
    return binary_to_int(gamma_binary) * binary_to_int(epslion_binary)


def life_support_decode(binary_list):
    '''Returns the life support rating'''
    oxygen_gen = list(binary_list)
    co2_scrub = list(binary_list)

    for i in range(12):
        oxygen_ones = one_most_common(oxygen_gen)
        oxygen_gen = bit_check(oxygen_gen, oxygen_ones[i], i)
        if len(oxygen_gen) == 1:
            break

    for i in range(12):
        co2_ones = one_most_common(co2_scrub)
        co2_scrub = bit_check(co2_scrub, not co2_ones[i], i)
        if len(co2_scrub) == 1:
            break

    return binary_to_int(oxygen_gen[0]) * binary_to_int(co2_scrub[0])


def bit_check(binaries, match, index):
    '''Filters a list based on the value of the bit at a given index'''
    temp_list = []
    if match:
        bit = '1'
    else:
        bit = '0'

    for item in binaries:
        if item[index] == bit:
            temp_list.append(item)

    if len(temp_list) == 0:
        return binaries

    return temp_list


def binary_to_int(binary):
    '''converts a binary string into an int in decimal form'''
    return int(binary, 2)


def main(input_file, output):
    '''Read input file and call helper functions'''

    with open(input_file, 'r', encoding='utf8') as file:
        lines = []
        for line in file:
            lines += [line.strip()]

    most_ones = one_most_common(lines)

    power_consumption = power_consumption_decode(most_ones)
    if output:
        print(f'power consumption: {power_consumption}')

    life_support = life_support_decode(lines)
    if output:
        print(f'life support rating: {life_support}')


if __name__ == '__main__':
    start = time.time()
    for iteration in range(0, 100):
        main('input.txt', False)
    end = time.time()
    print(f'\nexecution time of 100 iterations in ms: {(end - start) * 1000}')
