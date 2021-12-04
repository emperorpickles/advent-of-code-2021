'''
Day 4: Giant Squid
'''

import numpy as np


def board_update(board, number):
    '''Updates given board with given number, returns true if resulting board wins'''
    index = np.where(board == number)
    if index:
        board[index] = -1
    if np.any(np.all(board == -1, axis=0)) | np.any(np.all(board == -1, axis=1)):
        return True
    return False


def get_score(board, number):
    '''Returns the score value of given board and number'''
    unmarked_squares = board[board != -1]
    score = np.sum(unmarked_squares) * number
    return score


def part_one(boards, numbers):
    '''Returns the score of the first winning board'''
    winning_board = False
    while not winning_board:
        for number in numbers:
            for board in boards:
                winning_board = board_update(board, number)
                if winning_board:
                    score = get_score(board, number)
                    break
            if winning_board:
                break
    print(score)


def part_two(boards, numbers):
    '''
    Returns the score of the last winning board

    Current method brute forces the issue
    '''
    won_boards = set()
    while len(won_boards) < len(boards):
        for number in numbers:
            for board in boards:
                if np.array2string(board) in won_boards:
                    continue
                won_board = board_update(board, number)
                if won_board:
                    won_boards.add(np.array2string(board))
                    if len(won_boards) == len(boards):
                        print(board)
                        score = get_score(board, number)
                        break
                    continue
        if len(won_boards) == len(boards):
            break
    print(score)


def main(input_file):
    '''Read input file and call helper functions'''
    with open(input_file, 'r', encoding='utf8') as file:
        numbers = [int(i) for i in file.readline().split(',')]
    raw_boards = np.loadtxt(input_file, skiprows=2)

    boards = []
    for board in range(0, len(raw_boards), 5):
        boards.append((raw_boards[board:board+5]))

    part_one(list(boards), numbers)
    part_two(list(boards), numbers)


if __name__ == '__main__':
    main('input.txt')
