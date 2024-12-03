'''
Advent of Code 2024: Day 2
'''
import time
import os

def read_input(input_file: str) -> list[str]:
    '''Opens the input file and parses each report, returning a list of reports'''
    input_path = f'{os.path.dirname(os.path.realpath(__file__))}/{input_file}'
    with open(input_path, 'r', encoding='UTF-8') as f:
        reports = f.readlines()
    return reports


def levels_compare(levels: list[int]) -> bool:
    '''Checks if the provided levels only decrease or only increase by steps of 3 or less'''
    # check if levels initially inc or dec or are same
    if levels[0] == levels[1]:
        return False
    inc = levels[0] < levels[1]

    for i, level in enumerate(levels[:-1]):
        if inc and -3 <= level - levels[i+1] <= -1:
            continue
        if not inc and 1 <= level - levels[i+1] <= 3:
            continue
        return False
    return True


def part_one(reports: list[str]):
    '''Part 1: determine if each report is safe or unsafe'''
    safe_cnt = 0
    for report in reports:
        levels = list(map(int, report.split(' ')))

        safe = levels_compare(levels)
        if safe:
            safe_cnt += 1
    print(f'Total number of safe reports: {safe_cnt}')


def part_two(reports: list[str]):
    '''Part 2: determine if each report is safe or unsafe, now with problem dampener'''
    safe_cnt = 0
    for report in reports:
        levels = list(map(int, report.split(' ')))

        # check if levels are safe
        safe = levels_compare(levels)
        if safe:
            safe_cnt += 1
        else:
            # if not safe then try removing elements until it is safe, or no options left
            for i in range(len(levels)):
                dampened_report = list(levels)
                dampened_report.pop(i)
                safe = levels_compare(dampened_report)
                if safe:
                    safe_cnt += 1
                    break
    print(f'Total number of safe reports w/ Problem Dampener: {safe_cnt}')


if __name__ == '__main__':
    start_time = time.time()

    input_data = read_input('input.txt')
    part_one(input_data)
    part_two(input_data)

    end_time = time.time()
    print(f'\nTotal execution time: {(end_time - start_time) * 10**3} ms')
