'''
Day 9: Smoke Basin
'''

import numpy as np


def part_one(heightmap):
    '''
    Finds all low points and prints the sum of their risk levels
    '''
    risk_sum = 0
    low_points = []
    for y, row in enumerate(heightmap):
        for x, height in enumerate(row):
            if lowest_point(height, x, y, heightmap):
                low_points.append((x, y, height))
                risk_sum += 1 + height
    print(risk_sum)
    return low_points


def part_two(heightmap, low_points):
    '''
    Starting from previously found lowest points recursively expand outwards
    until basin walls are reached
    '''
    basin_sizes = np.zeros(len(low_points))
    visted = []

    def basin_check(point, basin):
        if point[2] == 9 or point in visted:
            return
        basin_sizes[basin] += 1
        visted.append(point)

        neighbors = get_neighbors(point, heightmap)
        for neighbor in neighbors:
            basin_check(neighbor, basin)

    for i, point in enumerate(low_points):
        basin_check(point, i)
    print(np.prod(np.partition(basin_sizes, -3)[-3:]))


def lowest_point(height, x, y, heightmap):
    '''Checks if given point is lower than its neighbors'''
    for i in [-1, 1]:
        dx = (heightmap[y][x+i] if x+i < heightmap.shape[1] and x+i >= 0 else 10) - height
        dy = (heightmap[y+i][x] if y+i < heightmap.shape[0] and y+i >= 0 else 10) - height
        if dx <= 0 or dy <= 0:
            return False
    return True


def get_neighbors(pt, matrix):
    '''Given a point return list of indices for neighboring points'''
    neighbors = []
    for i in [-1, 1]:
        dx = matrix[pt[1]][pt[0]+i] if pt[0]+i < matrix.shape[1] and pt[0]+i >= 0 else None
        dy = matrix[pt[1]+i][pt[0]] if pt[1]+i < matrix.shape[0] and pt[1]+i >= 0 else None
        if dx:
            neighbors.append((pt[0]+i, pt[1], dx))
        if dy:
            neighbors.append((pt[0], pt[1]+i, dy))
    return neighbors


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf-8') as file:
        heightmap = np.array([list(x.strip()) for x in file.readlines()]).astype(np.int8)
    print(heightmap)

    low_points = part_one(heightmap)
    part_two(heightmap, low_points)


if __name__ == '__main__':
    main('input.txt')
