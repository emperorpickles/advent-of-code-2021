'''
Day 17: Trick Shot
'''

import math


def part_one(target):
    '''
    '''
    n = (target[1][0] * -1) - 1
    print(f'maximum possible height: {n * (n + 1) / 2}')


def part_two():
    '''
    '''


def height_calc(t):
        return (-1 + math.sqrt(1+(8*t)))/2


def shot(vel, target):
    on_target = True
    pos = [0,0]
    x_vel, y_vel = vel
    max_height = 0
    while on_target:
        pos[0] += x_vel
        pos[1] += y_vel
        print(pos)
        max_height = max(max_height, pos[1])
        if pos[0] >= target[0][0] and pos[0] <= target[0][1] \
           and pos[1] >= target[1][0] and pos[1] <= target[1][1]:
            return max_height
        elif pos[0] > target[0][1] or pos[1] < target[1][0]:
            return -1
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 0
        y_vel -= 1


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf8') as file:
        line = file.readline().split(':')[1].split(',')
    target = [[int(j) for j in i.strip()[2:].split('..')] for i in line]

    part_one(target)
    part_two()


if __name__ == '__main__':
    main('input.txt')
