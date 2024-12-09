'''
Advent of Code 2024: Day 6
'''
import os
import bisect

def read_input(input_file: str):
    ''''''
    rows = {}
    cols = {}
    start = []
    input_path = f'{os.path.dirname(os.path.realpath(__file__))}/{input_file}'
    with open(input_path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            for x, item in enumerate(line):
                if item == '#':
                    row = rows.get(y, [])
                    bisect.insort(row, x)
                    rows.update({y: row})
                    col = cols.get(x, [])
                    bisect.insort(col, y)
                    cols.update({x: col})
                elif item == '^':
                    start = [x, y]
        size = (len(lines[0].strip()), len(lines))
        print(size)
    return start, rows, cols, size


def print_grid(size, highlights, start_position):
    rows, cols = size
    for row in range(rows):
        for col in range(cols):
            if (col, row) == start_position:
                print('S', end=' ')
            elif (col, row) in highlights:
                print('X', end=' ')
            else:
                print('.', end=' ')
        print()


def find_next_stop(direction, pos, blocks):
    print(f'getting moves: {direction}, {pos}, {blocks}')
    match direction:
        case 'UP':
            return next(y for y in reversed(blocks.get(pos[0], [])) if y < pos[1]) + 1
        case 'RIGHT':
            return next(x for x in blocks.get(pos[1], []) if x > pos[0]) - 1
        case 'DOWN':
            return next(y for y in blocks.get(pos[0], []) if y > pos[1]) - 1
        case 'LEFT':
            return next(x for x in reversed(blocks.get(pos[1], [])) if x < pos[0]) + 1


def part_one(start, rows, cols, size):
    '''Part 1'''
    in_bounds = True
    direction = 'UP'
    pos = list(start)
    positions = set()
    while in_bounds:
        if direction == 'UP':
            try:
                stop = find_next_stop(direction, pos, cols)
                moves = abs(pos[1] - stop)
                any(positions.add((pos[0], pos[1] - y)) for y in range(0, moves))
                pos[1] = pos[1] - moves
                direction = 'RIGHT'
            except StopIteration:
                any(positions.add((pos[0], pos[1] - y)) for y in range(0, pos[1] + 1))
                in_bounds = False
        elif direction == 'RIGHT':
            try:
                stop = find_next_stop(direction, pos, rows)
                moves = abs(pos[0] - stop)
                any(positions.add((pos[0] + x, pos[1])) for x in range(0, moves))
                pos[0] = pos[0] + moves
                direction = 'DOWN'
            except StopIteration:
                any(positions.add((pos[0] + x, pos[1])) for x in range(0, size[0] - pos[0]))
                in_bounds = False
        elif direction == 'DOWN':
            try:
                stop = find_next_stop(direction, pos, cols)
                moves = abs(pos[1] - stop)
                any(positions.add((pos[0], pos[1] + y)) for y in range(0, moves))
                pos[1] = pos[1] + moves
                direction = 'LEFT'
            except StopIteration:
                any(positions.add((pos[0], pos[1] + y)) for y in range(0, size[1] - pos[1]))
                in_bounds = False
        elif direction == 'LEFT':
            try:
                stop = find_next_stop(direction, pos, rows)
                moves = abs(pos[0] - stop)
                any(positions.add((pos[0] - x, pos[1])) for x in range(0, moves))
                pos[0] = pos[0] - moves
                direction = 'UP'
            except StopIteration:
                any(positions.add((pos[0] - x, pos[1])) for x in range(0, pos[0] + 1))
                in_bounds = False
    print_grid(size, positions, tuple(start))
    print(f'Number of distinct moves: {len(positions)}')


if __name__ == '__main__':
    input_start, input_rows, input_cols, input_size = read_input('input.txt')
    part_one(input_start, input_rows, input_cols, input_size)
