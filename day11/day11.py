'''
Day 11: Dumbo Octopus
'''

import itertools as it
import numpy as np


def part_one(octopuses, steps):
    '''
    Prints the number of flashes that occured after given number of steps
    '''
    flashes = 0
    for step in range(steps):
        octopuses += 1
        flashing = np.where(octopuses > 9)
        flashed = ([], [])

        while len(flashing[0]) > 0:
            flashing = np.where(octopuses > 9)
            flash_indices = list(zip(flashing[0], flashing[1]))
            if len(flash_indices) == 100:
                print(f'full flash occured at step: {step}')
            if len(flash_indices) > 0:
                flashed[0].extend(flashing[0])
                flashed[1].extend(flashing[1])
                for flash in flash_indices:
                    for neighbor in get_neighbors(flash, 10):
                        octopuses[neighbor] += 1
            flashes += len(flashing[0])
            octopuses[flashed] = 0
    print(f'there was a total of {flashes} flashes after {steps} steps')


def part_two(octopuses):
    '''
    Simulates octopus flashes until a full flash occurs
    '''
    full_flash = False
    step = 0

    while not full_flash:
        if np.all(octopuses == np.ravel(octopuses)[0]):
            full_flash = True
            print(f'\nfull flash occured at step: {step}')
            break

        step += 1
        octopuses += 1
        flashing = np.where(octopuses > 9)
        flashed = ([], [])

        while len(flashing[0]) > 0:
            flashing = np.where(octopuses > 9)
            flash_indices = list(zip(flashing[0], flashing[1]))
            if len(flash_indices) > 0:
                flashed[0].extend(flashing[0])
                flashed[1].extend(flashing[1])
                for flash in flash_indices:
                    for neighbor in get_neighbors(flash, 10):
                        octopuses[neighbor] += 1
            octopuses[flashed] = 0


def get_neighbors(point, dim):
    '''
    (-1, 1) (0, 1) (1, 1)
    (-1, 0) (0, 0) (1, 0)
    (-1,-1) (0,-1) (1,-1)
    '''
    indices = set([i for i in it.combinations([-1, 1, 0, 1, -1], 2)])
    neighbors = []
    for index in indices:
        x = point[0] + index[0]
        y = point[1] + index[1]
        if x >= 0 and x < dim and y >= 0 and y < dim:
            neighbors.append((point[0] + index[0], point[1] + index[1]))
    return neighbors


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf-8') as file:
        octopuses = np.array([list(x.strip()) for x in file.readlines()]).astype(np.int8)

    part_one(octopuses.copy(), 100)
    part_two(octopuses.copy())


if __name__ == '__main__':
    main('input.txt')
