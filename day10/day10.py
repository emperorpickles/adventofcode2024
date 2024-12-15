'''
Advent of Code 2024: Day 10
'''
import os

def read_input(input_file: str):
    ''''''
    height_map = {}
    input_path = f'{os.path.dirname(os.path.realpath(__file__))}/{input_file}'
    with open(input_path, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            line = line.strip()
            for x, height in enumerate(line):
                cords = height_map.get(int(height), [])
                height_map[int(height)] = cords + [(x,y)]
        size = (len(lines[0].strip()), len(lines))
    return height_map, size


def in_bounds(point):
    x, y = point
    max_x, max_y = size
    if 0 <= x < max_x and 0 <= y < max_y:
        return True
    return False


def check_paths(height, pos, height_map, trail=[]):
    if pos not in height_map[height]:
        return []
    elif height == 9:
        return [trail + [pos]]
    trail = trail + [pos]

    neighbors = []
    for offset in [(1,0), (-1,0), (0,1), (0,-1)]:
        neighbor = tuple(a + b for a, b in zip(pos, offset))
        if in_bounds(neighbor):
            neighbors.append(neighbor)

    all_paths = []
    for neighbor in neighbors:
        path = check_paths(height + 1, neighbor, height_map, trail[:])
        all_paths.extend(path)
    return all_paths


def part_one(height_map):
    ''''''
    scores = []
    for start in height_map.get(0):
        paths = check_paths(0, start, height_map)
        summits = set([trail.pop(-1) for trail in paths])
        scores.append(len(summits))
    print(f'Sum of scores for all trailheads: {sum(scores)}')


def part_two(height_map):
    ''''''
    ratings = []
    for start in height_map.get(0):
        paths = check_paths(0, start, height_map)
        ratings.append(len(paths))
    print(f'Sum of scores for all trailheads: {sum(ratings)}')


if __name__ == '__main__':
    input_data, size = read_input('input.txt')

    part_one(input_data)
    part_two(input_data)

