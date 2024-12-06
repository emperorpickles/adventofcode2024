'''
Advent of Code 2024: Day 5
'''
import os
from typing import Tuple

def read_input(input_file: str) -> Tuple[list[str], list[str]]:
    '''Opens the input file, separates the rules and updates, and returns each as lists of strs'''
    input_path = f'{os.path.dirname(os.path.realpath(__file__))}/{input_file}'
    with open(input_path, 'r', encoding='UTF-8') as f:
        lines = [line.strip() for line in f]
    split_indx = lines.index('')
    rules = lines[0:split_indx]
    updates = lines[split_indx+1:]
    return rules, updates


def order_check(rule_ord: dict, nums: list[int], recheck: bool) -> Tuple:
    '''Check if given list of nums follows given rule order, if not swap the misordered nums and check again'''
    for i, updt in enumerate(nums):
        ordr = rule_ord.get(updt, [])
        misordered_check = [x in ordr for x in nums[i:]]
        if any(misordered_check):
            invalid_indx = misordered_check.index(True) + i
            nums[i], nums[invalid_indx] = nums[invalid_indx], nums[i]
            return order_check(rule_ord, nums, True)
    return recheck, nums


def validate_updates(rules: list[str], updates: list[str]) -> Tuple[list[list[int]], list[list[int]]]:
    '''For a given set of order rules and updates, validate that updates follow the order rules'''
    rule_ord = {}
    for rule in rules:
        # Create a dict and for each num, list what nums must appear before it for the update to be valid
        frst, sec = map(int, rule.split('|'))
        befores = rule_ord.get(sec, [])
        befores.append(frst)
        rule_ord[sec] = befores
    valid_updts = []
    fixed_updates = []
    for update in updates:
        nums = list(map(int, update.split(',')))
        rechecked, checked_update = order_check(rule_ord, nums, False)
        if rechecked:
            fixed_updates.append(checked_update)
        else:
            valid_updts.append((checked_update))
    return valid_updts, fixed_updates


def sum_of_mids(vals_list: list[list[int]]) -> int:
    '''Return the sum of the middle values from all lists of values given'''
    mid_sum = 0
    for vals in vals_list:
        mid = len(vals) // 2
        mid_sum += vals[mid]
    return mid_sum


def solver(rules, updates):
    '''find sum of middle numbers for all valid updates'''
    valid_updts, fixed_updates = validate_updates(rules, updates)
    valid_mid_sum = sum_of_mids(valid_updts)
    corrected_mid_sum = sum_of_mids(fixed_updates)
    print(f'Total of midpoints of valid updates: {valid_mid_sum}')
    print(f'Total of midpoints of corrected updates: {corrected_mid_sum}')


if __name__ == '__main__':
    input_rules, input_updates = read_input('input.txt')
    solver(input_rules, input_updates)

