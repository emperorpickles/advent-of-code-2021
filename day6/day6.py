'''
Day 6: Lanternfish
'''

import numpy as np


def part_one(inital_fish, days):
    '''
    Prints the number of fish after x number of days

    Only works for part one, array becomes too large and slow to handle more than ~170 days
    '''
    fish = inital_fish

    for day in range(days):
        reproducing_fish = np.where(fish == 0)
        fish -= 1
        fish[reproducing_fish] = 6
        fish.resize(len(fish) + len(reproducing_fish[0]), refcheck=False)

        if len(reproducing_fish[0]) > 0:
            fish[-(len(reproducing_fish[0])):] = 8
    print(f'After {days} days there will be {len(fish)} fish')


def part_two(intial_fish, days):
    '''
    Prints the number of fish after x number of days

    Main idea found via reddit
    '''
    fish = [intial_fish.count(i) for i in range(9)]
    for i in range(days):
        num = fish.pop(0)
        fish[6] += num
        fish.append(num)
    print(f'After {days} days there will be {sum(fish)} fish')


def main(input_file):
    '''Read input file and call helper functions'''
    intial_fish = np.loadtxt(input_file, dtype=np.uint8, delimiter=',')

    part_one(intial_fish.copy(), 80)
    part_two(intial_fish.tolist(), 256)


if __name__ == '__main__':
    main('input.txt')
