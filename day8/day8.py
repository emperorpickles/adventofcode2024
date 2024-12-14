'''
Advent of Code 2024: Day 8
'''
import os

def read_input(input_file: str):
    ''''''
    antennas = {}
    input_path = f'{os.path.dirname(os.path.realpath(__file__))}/{input_file}'
    with open(input_path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            line = line.strip()
            for x, char in enumerate(line):
                if char != '.':
                    cords = antennas.get(char, [])
                    antennas[char] = cords + [(x,y)]
        size = (len(lines[0].strip()), len(lines))
    return antennas, size


def print_grid(size, antennas, antinodes):
    rows, cols = size
    for row in range(rows):
        for col in range(cols):
            is_ant = False
            for ant in antennas:
                if (col, row) in antennas[ant]:
                    is_ant = True
                    print(ant, end=' ')
            if is_ant:
                continue
            elif (col, row) in antinodes:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print()


def in_bounds(point):
    x, y = point
    max_x, max_y = size
    if 0 <= x < max_x and 0 <= y < max_y:
        return True
    return False


def find_antinodes(points, antinodes, harmonic = False):
    if len(points) == 1:
        return antinodes
    current_point = points.pop(0)
    x1, y1 = current_point
    for next_point in points:
        x2, y2 = next_point
        offset_x, offset_y = x2 - x1, y2 - y1
        an1 = (x1 - offset_x, y1 - offset_y)
        an2 = (x2 + offset_x, y2 + offset_y)
        if harmonic:
            while in_bounds(an1):
                antinodes.add(an1)
                an1 = (an1[0] - offset_x, an1[1] - offset_y)
            while in_bounds(an2):
                antinodes.add(an2)
                an2 = (an2[0] + offset_x, an2[1] + offset_y)
        else:
            if in_bounds(an1):
                antinodes.add(an1)
            if in_bounds(an2):
                antinodes.add(an2)
    return find_antinodes(points, antinodes, harmonic)


def part_one(antennas):
    unique_antinodes = set()
    for antenna in antennas:
        antinodes = find_antinodes(list(antennas[antenna]), set())
        unique_antinodes.update(antinodes)
    print_grid(size, antennas, unique_antinodes)
    print(f'Number of unique antinodes: {len(unique_antinodes)}')


def part_two(antennas):
    unique_antinodes = set([antenna for points in antennas.values() for antenna in points])
    for antenna in antennas:
        antinodes = find_antinodes(list(antennas[antenna]), set(), True)
        unique_antinodes.update(antinodes)
    print_grid(size, antennas, unique_antinodes)
    print(f'Number of unique antinodes: {len(unique_antinodes)}')


if __name__ == '__main__':
    input_data, size = read_input('input.txt')

    part_one(input_data)
    part_two(input_data)

