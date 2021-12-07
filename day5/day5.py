'''
Day 5: Hydrothermal Venture
'''

import numpy as np


def update_field(pt_1, pt_2, field):
    '''Returns field after updating with given line'''
    start_x, start_y = min(pt_1[0], pt_2[0]), min(pt_1[1], pt_2[1])
    end_x, end_y = max(pt_1[0], pt_2[0]), max(pt_1[1], pt_2[1])

    if pt_1[0] == pt_2[0]:
        for i in range(start_y, end_y + 1):
            field[start_x][i] += 1
    elif pt_1[1] == pt_2[1]:
        for i in range(start_x, end_x + 1):
            field[i][start_y] += 1
    else:
        # diagonals - not working
        x_dist = pt_2[0] - pt_1[0]
        y_dist = pt_2[1] - pt_1[1]

        x_dir = 1 if x_dist > 0 else -1
        y_dir = 1 if y_dist > 0 else -1

        x_range = range(0, x_dist + x_dir, x_dir)
        y_range = range(0, y_dist + y_dir, y_dir)

        print(pt_1)

        for i in x_range:
            field[pt_1[0] + i][pt_1[1] +
                               (i * y_dir if x_dir != -1 else i)] += 1


def part_one(vent_lines):
    '''Prints the number of points with at least two overlapping horizontal or vertical lines'''
    size = np.max(vent_lines)
    field = np.zeros((size + 1, size + 1))

    for line in vent_lines:
        # [[ 72 504], [422 154]]
        start, end = line[0], line[1]
        if start[0] == end[0] or start[1] == end[1]:
            update_field(start, end, field)
    print(len(field[field > 1]))


def part_two(vent_lines):
    '''Prints the number of points with at least two overlapping lines, including diagonals'''
    size = np.max(vent_lines)
    field = np.zeros((size + 1, size + 1))

    for line in vent_lines:
        # [[ 72 504], [422 154]]
        start, end = line[0], line[1]
        update_field(start, end, field)
    # update_field([72, 504], [422, 154], field)
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
