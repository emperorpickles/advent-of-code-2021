'''
Day 2: Dive!
'''


def follow_course(course):
    '''Returns final horizontal position multiplied by final depth'''
    hoizontal_pos = 0
    depth = 0
    aim = 0

    for move in course:
        direction, speed = move.split()
        speed = int(speed)

        match direction:
            case 'forward':
                hoizontal_pos += speed
                depth += aim * speed
            case 'up':
                aim -= speed
            case 'down':
                aim += speed
        # print(f'position: {hoizontal_pos}, depth: {depth}, aim: {aim}')
    return hoizontal_pos * depth


def main(input_file):
    '''Read input file and call helper functions'''
    lines = []
    with open(input_file, 'r', encoding='utf8') as file:
        lines = file.readlines()

    final_pos = follow_course(lines)
    print(f'final position * depth: {final_pos}')


if __name__ == '__main__':
    main('input.txt')
