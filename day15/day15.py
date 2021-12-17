'''
Day 15: Chiton
'''

import bisect
import numpy as np


class Path():
    '''Path class that holds the current position and total risk value of the path'''

    def __init__(self, pos, total_risk) -> None:
        self.pos = pos
        self.total_risk = total_risk


def part_one(cave):
    '''Prints the total risk of the lowest risk path through the cave'''
    print(cave_traversal(cave))


def cave_traversal(cave):
    '''pretty slow'''
    start = (0, 0)
    end = (cave.shape[0] - 1, cave.shape[1] - 1)

    eval_queue = [Path(start, 0)]
    visited = []

    while len(eval_queue) > 0:
        # pull lowest risk (first) node from queue
        current_node = eval_queue.pop(0)
        if current_node.pos == end:
            return current_node.total_risk
        if current_node.pos not in visited:
            # track already visited nodes
            visited.append(current_node.pos)
            # get neighbors
            for pos in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                new_pos = tuple(map(lambda x, y: x + y, current_node.pos, pos))
                if new_pos[0] in range(0, end[0] + 1) and new_pos[1] in range(0, end[1] + 1):
                    # add new node into correctly sorted position in queue
                    bisect.insort(eval_queue, Path(new_pos, current_node.total_risk +
                                  cave[new_pos]), key=lambda i: i.total_risk)


def part_two():
    '''
    '''


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf8') as file:
        cave = np.array([list(x.strip()) for x in file.readlines()]).astype(np.int8)

    part_one(cave)
    part_two()


if __name__ == '__main__':
    main('input.txt')
