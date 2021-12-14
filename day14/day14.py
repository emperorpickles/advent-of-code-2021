'''
Day 14: Extended Polymerization
'''

from collections import Counter
from math import ceil
import itertools as it


def part_one(template, rules, steps):
    '''
    Prints the score of the polymer string after given number of steps

    Iterates over the entire string for each step, recalculating pairs and new insertions each time
    Slows down significantly once the string grows larger
    '''
    for step in range(steps):
        pairs = get_pairs(template)
        for pair in reversed(pairs):
            rule = rules[pair]
            pos = template.find(pair) + 1
            if pos != -1:
                template = template[:pos] + rule + template[pos:]
    counts = Counter(template).most_common()
    score = counts[0][1] - counts[-1][1]
    print(f'the score after {steps} steps is: {score}')


def part_two(template, rules, steps):
    '''
    Prints the score of the polymer string after given number of steps

    Uses a dictionary of letter pairs to track the number of each pair rather than iterating
    over the entire string
    '''
    # create list of all possible letter pairs
    letters = ''.join(set(rules.values()))
    pair_counts = {}
    for pair in [''.join(i) for i in it.product(letters, repeat=2)]:
        pair_counts[pair] = 0

    # initalize pair counts from template
    for pair in get_pairs(template):
        pair_counts[pair] += 1

    for step in range(steps):
        for pair, value in pair_counts.copy().items():
            if value > 0:
                # get rule for pair and create new pairs after character insertion
                rule = rules[pair]
                new_pairs = [pair[0] + rule, rule + pair[1]]
                pair_counts[pair] -= value
                for new_pair in new_pairs:
                    pair_counts[new_pair] += value

    # get sum of each letter from dict of pair combinations
    num_letters = Counter()
    for pair, count in pair_counts.items():
        num_letters[pair[0]] += count
        num_letters[pair[1]] += count
    for item, count in num_letters.items():
        num_letters[item] = ceil(num_letters[item] / 2)
    counts = num_letters.most_common()
    score = counts[0][1] - counts[-1][1]
    print(f'the score after {steps} steps is: {score}')


def get_pairs(string):
    '''Returns a list of all two letter pairs from given string'''
    return [string[i: i + 2] for i in range(len(string) - 1)]


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf8') as file:
        lines = file.readlines()
        template = lines[0].strip()
        rules = {}
        for line in lines[2:]:
            line = [i for i in line.strip().split(' -> ')]
            rules[line[0]] = line[1]

    part_one(template, rules, 10)
    part_two(template, rules, 40)


if __name__ == '__main__':
    main('input.txt')
