'''
Day 1: Sonar Sweep Depth Measurement
'''


def prev_increases(lines):
    '''Returns number of times a line is greater than the previous line'''
    increases = 0
    prev_line = 0

    for line in lines:
        if line > prev_line:
            increases += 1
        prev_line = line

    return increases


def three_measure_window(lines):
    '''Creates blocks of three measurements and compares the sums of adjacent blocks'''
    increases = 0
    prev_window = sum(lines[0:3])

    for w_start in range(1, len(lines) - 2):
        window = sum(lines[w_start: w_start + 3])
        if window > prev_window:
            increases += 1
        prev_window = window

    return increases


def main(input_file):
    '''Run through input file counting depth increases'''

    with open(input_file, 'r', encoding='utf8') as file:
        lines = []
        for line in file:
            lines += [int(i) for i in line.split()]

    single_measurements = prev_increases(lines)
    print(f'Single line comparison: {single_measurements} increases')

    window_measurements = three_measure_window(lines)
    print(f'Three line window comparison: {window_measurements} increases')


if __name__ == '__main__':
    main('input.txt')
