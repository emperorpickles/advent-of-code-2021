'''
Day 5: Hydrothermal Venture
'''

import math
import numpy as np


def update_field(pts, field):
    '''Returns field after updating with given line'''
    slope = get_slope(pts[0], pts[1])

    pts = sorted(pts, key=(lambda x: x[0]) if slope is not None else (lambda x: x[1]))
    pt_1, pt_2 = pts[0], pts[1]
    dist = abs(pt_1[0] - pt_2[0]) if slope is not None else abs(pt_1[1] - pt_2[1])

    for i in range(dist + 1):
        x_offset = i if slope is not None else 0
        y_offset = slope if slope is not None else int(
            math.copysign(1, (pt_2[1] - pt_1[1])))
        field[pt_1[0] + x_offset][pt_1[1] + (i * y_offset)] += 1


def get_slope(pt_1, pt_2):
    '''Returns the slope of the line between two points. Returns None if line is vertical'''
    return int((pt_2[1] - pt_1[1]) / (pt_2[0] - pt_1[0])) if (pt_2[0] - pt_1[0]) else None


def part_one(vent_lines):
    '''Prints the number of points with at least two overlapping horizontal or vertical lines'''
    size = np.max(vent_lines)
    field = np.zeros((size + 1, size + 1))

    for line in vent_lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            update_field(line, field)
    print(len(field[field > 1]))


def part_two(vent_lines):
    '''Prints the number of points with at least two overlapping lines, including diagonals'''
    size = np.max(vent_lines)
    field = np.zeros((size + 1, size + 1))

    for line in vent_lines:
        update_field(line, field)

    np.savetxt('field.txt', field, fmt='%d')
    print(len(field[field > 1]))


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf8') as file:
        lines = []
        for line in file:
            lines.append([i.split(',') for i in line.strip().split(' -> ')])
        vent_lines = np.array(lines, dtype=int)

    part_one(vent_lines)
    part_two(vent_lines)


if __name__ == '__main__':
    main('input.txt')
