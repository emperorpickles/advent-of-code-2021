'''
Day 3: Binary Diagnostic

Rewritten to make use of numpy and matrices
'''

import collections
import time
import numpy as np


def column_get_common_bit(column):
    '''
    Returns the most common bit in a given column.
    If counts are equal, returns 1
    '''
    most_common = collections.Counter(column).most_common()
    if most_common[0][1] == most_common[1][1]:
        return 1
    return int(most_common[0][0])


def power_consumption_decode(bit_matrix):
    '''Returns power consumption in decimal form'''
    gamma_binary = ''
    epslion_binary = ''
    for column in range(len(bit_matrix[0])):
        common_bit = column_get_common_bit(bit_matrix[:, column])
        gamma_binary += str(common_bit)
        epslion_binary += str(common_bit ^ 1)
    return binary_to_int(gamma_binary) * binary_to_int(epslion_binary)


def life_support_decode(bit_matrix):
    '''Returns the life support rating'''
    oxygen_gen = get_rating(bit_matrix, True)
    co2_scrub = get_rating(bit_matrix, False)

    return binary_to_int(oxygen_gen) * binary_to_int(co2_scrub)


def get_rating(bit_matrix, most_common):
    '''Returns diagnostic rating in binary by filtering on columns common bit'''
    temp_matrix = np.copy(bit_matrix)

    for i in range(len(bit_matrix[0])):
        column = temp_matrix[:, i]
        common_bit = column_get_common_bit(column)

        if most_common:
            temp_matrix = temp_matrix[column == str(common_bit)]
        else:
            temp_matrix = temp_matrix[column == str(common_bit ^ 1)]

        if len(temp_matrix) == 1:
            break
    return ''.join(temp_matrix[0])


def binary_to_int(binary):
    '''converts a binary string into an int in decimal form'''
    return int(binary, 2)


def main(input_file, output):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf-8') as file:
        bits = [list(x.strip()) for x in file.readlines()]
    bit_matrix = np.array(bits)

    power_consumption = power_consumption_decode(bit_matrix)
    if output:
        print(f'power consumption: {power_consumption}')

    life_support = life_support_decode(bit_matrix)
    if output:
        print(f'life support rating: {life_support}')


if __name__ == '__main__':
    start = time.time()
    for iteration in range(0, 100):
        main('input.txt', False)
    end = time.time()
    print(f'\nexecution time of 100 iterations in ms: {(end - start) * 1000}')
