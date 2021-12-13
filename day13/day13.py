'''
Day 13: Transparent Origami
'''

import itertools as it
import numpy as np


def part_one(dots, fold):
    '''
    Prints the number of dots visible after the first fold
    '''
    dots = do_fold(dots, fold)

    print(f'{len(dots)} are visible after the first fold')


def part_two(dots, folds):
    '''
    Prints the eight letters formed after performing all the folds
    '''
    for fold in folds:
        dots = do_fold(dots, fold)

    x_dim = max([i[0] for i in dots]) + 2
    y_dim = max([i[1] for i in dots]) + 1
    field = np.zeros((y_dim, x_dim), dtype=int)

    for dot in dots:
        field[dot[1]][dot[0]] = 1

    letters = np.hsplit(field, 8)
    for letter in letters:
        print()
        print(letter)


def do_fold(dots, fold):
    '''Returns the new dot positions after performing the given fold'''
    for dot in dots:
        if fold['axis'] == 'y' and dot[1] > fold['line']:
            dot[1] = abs(dot[1] - 2 * fold['line'])
        if fold['axis'] == 'x' and dot[0] > fold['line']:
            dot[0] = abs(dot[0] - 2 * fold['line'])
    dots.sort()
    dots = list(dots for dots, _ in it.groupby(dots))
    return dots


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf8') as file:
        data = file.readlines()

    folds = []
    # get the folds from the end of the file
    for line in reversed(data):
        if line == '\n':
            break
        line = line.strip()[11:]
        fold = {'axis': line[0], 'line': int(line[2:])}
        folds.insert(0, fold)

    dots = list([[int(i) for i in x.strip().split(',')] for x in data[:-len(folds)-1]])

    part_one(dots, folds[0])
    part_two(dots, folds)


if __name__ == '__main__':
    main('input.txt')
