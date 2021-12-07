'''
Day 7: The Treachery of Whales
'''

import statistics


def part_one(data):
    '''
    Prints the amount of fuel that must be used to align the crabs
    '''
    data_median = statistics.median(data)
    fuel_used = 0
    for i in data:
        fuel_used += abs(i - data_median)
    print(f'total fuel used: {fuel_used}')


def part_two(data):
    '''
    Prints the amount of fuel that must be used to align the crabs

    Brute forces finding best position by calculating fuel use at each position
    '''
    fuel_usages = []
    for target in range(len(data)):
        fuel_used = 0
        for i in data:
            distance = abs(i - target)
            fuel_used += (distance**2 + distance) / 2
        fuel_usages.append({'pos': target, 'fuel': fuel_used})

    lowest_cost = min(fuel_usages, key=lambda x: x['fuel'])
    print(f'lowest fuel cost position: {lowest_cost}')


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf8') as file:
        data = [int(i) for i in file.readline().strip().split(',')]

    part_one(data)
    part_two(data)


if __name__ == '__main__':
    main('input.txt')
