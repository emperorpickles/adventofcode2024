
'''
Advent of Code 2024: Day 9
'''
import os
import multiprocessing
import time


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


def process_batch(batch):
    results = []
    for stone in batch:
        if stone == 0:
            results.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            midpoint = len(stone_str) // 2
            results.extend([int(stone_str[:midpoint]), int(stone_str[midpoint:])])
        else:
            results.append(stone * 2024)
    return results


def part_two(stones, blinks, batch_size=100000):
    for blink in range(blinks):
        tasks = [stones[i:i + batch_size] for i in range(0, len(stones), batch_size)]

        new_stones = []
        with multiprocessing.Pool(processes=16) as pool:
            for batch_result in pool.imap_unordered(process_batch, tasks):
                new_stones.extend(batch_result)

        stones = new_stones
        print(f'after {blink + 1} blinks: {len(stones)}')
    print(f'number of stones after {blinks} blinks: {len(stones)}')


if __name__ == '__main__':
    start_time = time.time()

    input_data = read_input('input.txt')
    #part_one(input_data, 25)
    part_two(input_data, 75)

    end_time = time.time()
    print(f'\nTotal execution time: {(end_time - start_time) * 10**3} ms')

