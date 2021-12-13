'''
Day 10: Syntax Scoring
'''

import numpy as np


def part_one(lines):
    '''
    '''
    scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}
    error_score = 0
    for line in lines:
        char = mismatched_pairs(line)
        if char:
            error_score += scoring[char]
    print(error_score)


def part_two():
    '''
    '''


def mismatched_pairs(line):
    mapping = dict(zip('({[<', ')}]>'))
    queue = []
    for char in line:
        if char in mapping:
            queue.append(mapping[char])
        elif not (queue and char == queue.pop()):
            return char
    return None


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf8') as file:
        lines = []
        for line in file:
            lines.append(line.strip())

    part_one(lines)
    part_two()


if __name__ == '__main__':
    main('input.txt')
