'''
Day 8: Seven Segment Search
'''

from collections import Counter
import numpy as np


def part_one(lines):
    '''
    Prints the number of times that the digits: 1, 4, 7, or 8 appears
    '''
    outs = [i[1] for i in lines]
    occrs = dict(Counter([len(i) for line in outs for i in line]).most_common())
    total = occrs[2] + occrs[4] + occrs[3] + occrs[7]
    print(f'Occurances of digits 1, 4, 7, and 8: {total}')


def part_two():
    '''
    -- in progress --
    cgaed gcdbfa gcfaed gfcde gadfceb(8) cdbfeg acg(7) eacf(4) eabgd ca(1) | agc efcgbd cag eacf

    A: acg, B: eacf, C: ca, D: eacf, E: gadfceb, F: , G: gadfceb
    '''
    signals = np.array(['cgaed', 'gcdbfa', 'gcfaed', 'gfcde',
                        'gadfceb', 'cdbfeg', 'acg', 'eacf', 'eabgd', 'ca'])
    lengths = np.vectorize(len)
    one = signals[lengths(signals) == 2][0]
    four = signals[lengths(signals) == 4][0]
    seven = signals[lengths(signals) == 3][0]
    eight = signals[lengths(signals) == 7][0]
    print(one, four, seven, eight)

    a_seg = remove_chars(seven, one)
    print(a_seg)


def remove_chars(string, to_remove):
    for character in to_remove:
        string = string.replace(character, '')
    return string


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf8') as file:
        lines = []
        for line in file:
            lines.append([i.split(' ') for i in line.strip().split(' | ')])

    part_one(lines)
    part_two()


if __name__ == '__main__':
    main('input.txt')
