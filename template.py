'''
Day X:
'''

import numpy as np


def part_one():
    '''
    '''


def part_two():
    '''
    '''


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf8') as file:
        lines = []
        for line in file:
            lines.append([i.split(',') for i in line.strip().split(' -> ')])
    lines = np.loadtxt(input_file, dtype=np.uint8, delimiter=',')

    part_one()
    part_two()


if __name__ == '__main__':
    main('input.txt')
