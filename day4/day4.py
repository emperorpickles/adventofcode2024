'''
Advent of Code 2024: Day 4
'''

import os
from typing import Tuple


def read_input(input_file: str) -> list[str]:
    '''Opens the input file and returns the contents'''
    input_path = f'{os.path.dirname(os.path.realpath(__file__))}/{input_file}'
    with open(input_path, 'r', encoding='UTF-8') as f:
        content = f.readlines()
    return content

def recur_search(dir: Tuple[int, int], pos: Tuple, itr: int) -> bool:
    '''Recursively searches in a direction for the next char in XMAS'''
    if any(val < 0 for val in pos):
        return False
    if itr == 3 and input_data[pos[0]][pos[1]] == 'S':
        return True
    try:
        if input_data[pos[0]][pos[1]] == target[itr]:
            next_pos = tuple(a + b for a, b in zip(pos, dir))
            return recur_search(dir, next_pos, itr+1)
    except IndexError:
        return False
    return False


def part_one(content: list[str]):
    '''Part 1: find number of occurances of XMAS'''
    xmas_cnt = 0
    for y, row in enumerate(content):
        for x in range(len(row)-1):
            if content[y][x] != 'X': continue
            for dir in dirs:
                xmas = recur_search(dir, (y,x), 0)
                if xmas:
                    xmas_cnt += 1
    print(f'Total number of XMAS occurances: {xmas_cnt}')


def part_two(content: list[str]):
    '''Part 2: find number of occurances of MAS in X shapes'''
    mas_cnt = 0
    for y, row in enumerate(content[:-2], 1):
        for x in range(1, len(row)-2):
            if content[y][x] != 'A': continue
            fwd_slash = content[y+1][x+1] + content[y-1][x-1]
            bck_slash = content[y+1][x-1] + content[y-1][x+1]
            if 'M' in fwd_slash and 'S' in fwd_slash and 'M' in bck_slash and 'S' in bck_slash:
                mas_cnt += 1
    print(f'Total number of MAS occurances: {mas_cnt}')


if __name__ == '__main__':
    input_data = read_input('input.txt')

    target = 'XMAS'
    dirs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

    part_one(input_data)
    part_two(input_data)

