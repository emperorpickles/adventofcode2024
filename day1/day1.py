'''
Advent of Code 2024: Day 1
'''
import time
import os

def read_input(input_file: str) -> list[int]:
    '''Opens the input file and parses the left and right columns, returning each as a list'''
    left_list, right_list = [], []
    input_path = f'{os.path.dirname(os.path.realpath(__file__))}/{input_file}'
    with open(input_path, 'r', encoding='UTF-8') as f:
        for line in f:
            line = line.split('   ')
            left_list.append(int(line[0]))
            right_list.append(int(line[1]))
    return left_list, right_list


def part_one(l_list: list[int], r_list: list[int]):
    '''Part 1: finds the total distance between the two lists'''
    l_list.sort()
    r_list.sort()

    dists = [abs(l_list[i] - r_list[i]) for i in range(len(l_list))]
    total_dist = sum(dists)
    print(f'The total distance between lists is: {total_dist}')


def part_two(l_list: list[int], r_list: list[int]):
    '''Part 2: find the similarity score between the two lists'''
    r_counts = {}
    for item in r_list:
        r_counts[item] = r_counts.get(item, 0) + 1

    sim_scores = [x * r_counts.get(x, 0) for x in l_list]
    total_sim = sum(sim_scores)
    print(f'The total similarity score is: {total_sim}')


if __name__ == '__main__':
    start_time = time.time()

    _left_list, _right_list = read_input('input.txt')
    part_one(_left_list, _right_list)
    part_two(_left_list, _right_list)

    end_time = time.time()
    print(f'\nTotal execution time: {(end_time - start_time) * 10**3} ms')
