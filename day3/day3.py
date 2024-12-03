'''
Advent of Code 2024: Day 2
'''
import time
import os
import re

def read_input(input_file: str) -> str:
    '''Opens the input file and returns the contents'''
    content = ''
    input_path = f'{os.path.dirname(os.path.realpath(__file__))}/{input_file}'
    with open(input_path, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            content += line.strip()
    return content


def sum_muls(muls: list[str]) -> int:
    '''For given list of mul() operations, return sum of all operations'''
    mul_total = 0
    for mul in muls:
        num_1, num_2 = tuple(map(int, mul[4:-1].split(',')))
        mul_total += num_1 * num_2
    return mul_total


def part_one(content: str):
    '''Part 1: find valid mul() operators and get total of all operations'''
    muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', content)

    mul_total = sum_muls(muls)
    print(f'Total of all multiplications: {mul_total}')


def part_two(content: str):
    '''Part 2: same as part 1, now checking for do() or dont() statements'''
    filtered_content = ''.join(re.findall(r'do\(\)(.*?)(?:don\'t\(\)|$)', 'do()'+content))
    muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', filtered_content)

    mul_total = sum_muls(muls)
    print(f'Total of all enabled multiplications: {mul_total}')


if __name__ == '__main__':
    start_time = time.time()

    input_data = read_input('input.txt')
    part_one(input_data)
    part_two(input_data)

    end_time = time.time()
    print(f'\nTotal execution time: {(end_time - start_time) * 10**3} ms')
