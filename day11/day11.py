
'''
Advent of Code 2024: Day 9
'''
import enum
import os
import multiprocessing
import time
import numpy as np
import cupy as cp
from numpy._core.multiarray import dtype


def read_input(input_file: str) -> list[int]:
    '''Opens the input file, separates the rules and updates, and returns each as lists of strs'''
    input_path = f'{os.path.dirname(os.path.realpath(__file__))}/{input_file}'
    with open(input_path, 'r', encoding='UTF-8') as f:
        line = f.readline().strip()
    stones = list(map(int, line.split(' ')))
    return stones


def part_one(stones, blinks):
    print(f'Initial arrangement: {stones}')
    for blink in range(blinks):
        stones_updt = stones[:]
        i = 0
        for stone in stones:
            if stone == 0:
                stones_updt[i] = 1
            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                midpoint = len(stone_str) // 2
                stones_updt[i] = int(stone_str[:midpoint])
                stones_updt.insert(i + 1, int(stone_str[midpoint:]))
                i += 1
            else:
                stones_updt[i] = stone * 2024
            i += 1
        stones = stones_updt
        # print(f'After {blink + 1} blinks: {stones}')
    print(f'Number of stones after {blinks} blinks: {len(stones)}')


def check_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        midpoint = len(stone_str) // 2
        return [int(stone_str[:midpoint]), int(stone_str[midpoint:])]
    else:
        return [stone * 2024]


def part_two(stones, blinks):
    stones = {stone: stones.count(stone) for stone in set(stones)}

    for blink in range(blinks):
        new_stones = {}
        for stone in stones.keys():
            updts = check_stone(stone)
            for new_stone in updts:
                new_stones.update({new_stone: stones.get(stone) + new_stones.get(new_stone, 0)})

        stones = new_stones
        print(f'after {blink + 1} blinks: {sum(stones.values())}')
    print(f'number of stones after {blinks} blinks: {sum(stones.values())}')


if __name__ == '__main__':
    start_time = time.time()

    input_data = read_input('input.txt')
    #part_one(input_data, 25)
    part_two(input_data, 75)

    end_time = time.time()
    print(f'\nTotal execution time: {(end_time - start_time) * 10**3} ms')

