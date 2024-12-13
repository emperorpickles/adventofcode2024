'''
Advent of Code 2024: Day 7
'''
import os

def read_input(input_file: str) -> dict:
    ''''''
    eqs = {}
    input_path = f'{os.path.dirname(os.path.realpath(__file__))}/{input_file}'
    with open(input_path, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            test_val, nums = line.split(':')
            nums = list(map(int, nums.strip().split(' ')))
            eqs.update({int(test_val): nums})
    return eqs


def is_valid(test: int, nums: list[int], concat: bool) -> bool:
    if len(nums) == 1:
        return nums[0] == test
    if is_valid(test, [nums[0] + nums[1]] + nums[2:], concat):
        return True
    if is_valid(test, [nums[0] * nums[1]] + nums[2:], concat):
        return True
    if concat and is_valid(test, [int(str(nums[0]) + str(nums[1]))] + nums[2:], concat):
        return True
    return False


def part_one(eqs: dict):
    result = 0
    for test in eqs.keys():
        if is_valid(test, eqs[test], False):
            result += test
    print(f'Calibration result: {result}')


def part_two(eqs: dict):
    result = 0
    for test in eqs.keys():
        if is_valid(test, eqs[test], True):
            result += test
    print(f'Calibration result with concat: {result}')


if __name__ == '__main__':
    input_data = read_input('input.txt')
    part_one(input_data)
    part_two(input_data)

