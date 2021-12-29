'''
Day 12: Passage Pathing
'''

from pprint import pprint


def part_one(caves):
    '''
    Creates a dict with each cave as a key and their connections as values
    '''
    paths = cave_traversal(caves, False)
    print(paths)


def part_two(caves):
    '''
    '''
    paths = cave_traversal(caves, True)
    print(paths)


def cave_traversal(caves, can_go_twice):
    '''Return number of possible paths through the given caves'''
    def count_next_paths(node, seen, twice):
        if node.islower():
            seen = seen.union({node})
        num_paths = 0
        for target in caves[node]:
            if target == 'end':
                num_paths += 1
            elif target not in seen:
                num_paths += count_next_paths(target, seen, twice)
            elif target != 'start' and twice:
                num_paths += count_next_paths(target, seen, False)
        return num_paths
    return count_next_paths('start', frozenset(), can_go_twice)


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf8') as file:
        lines = []
        for line in file:
            lines.append(line.strip().split('-'))
    
    caves = {}
    for line in lines:
        if line[0] not in caves:
            caves[line[0]] = [line[1]]
        else:
            caves[line[0]].append(line[1])
        if line[1] not in caves:
            caves[line[1]] = [line[0]]
        else:
            caves[line[1]].append(line[0])

    part_one(caves)
    part_two(caves)


if __name__ == '__main__':
    main('input.txt')
