'''
Advent of Code 2024: Day 9
'''
import os
import time


def read_input(input_file: str) -> str:
    '''Opens the input file, separates the rules and updates, and returns each as lists of strs'''
    input_path = f'{os.path.dirname(os.path.realpath(__file__))}/{input_file}'
    with open(input_path, 'r', encoding='UTF-8') as f:
        lines = [line.strip() for line in f]
    return lines[0]


def consecutive_check(lst, target):
    indices = [i for i, x in enumerate(lst) if x == target]
    return all(indices[i] + 1 == indices[i + 1] for i in range(len(indices) - 1))


def part_one(disk_map):
    blocks = []
    file_id = 0
    for i, item in enumerate(disk_map):
        if i % 2 == 0:
            blocks.extend([str(file_id) for _ in range(0, int(item))])
            file_id += 1
        else:
            blocks.extend(['.' for _ in range(0, int(item))])
    for i in range(1, len(blocks)):
        if blocks[-i] != '.':
            next_free = blocks.index('.')
            blocks[-i], blocks[next_free] = blocks[next_free], blocks[-i]
            if consecutive_check(blocks, '.'):
                break
    checksum = 0
    for i, block in enumerate(blocks[:blocks.index('.')]):
        checksum += i * int(block)
    print(f'Filesystem checksum: {checksum}')


if __name__ == '__main__':
    start_time = time.time()

    input_data = read_input('input.txt')
    part_one(input_data)

    end_time = time.time()
    print(f'\nTotal execution time: {(end_time - start_time) * 10**3} ms')

