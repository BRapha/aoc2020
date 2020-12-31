#! /usr/bin/env python3

import math


def parse(row):
    bit_string = "".join(map(lambda c: "1" if c in ("B", "R") else "0", row.strip()))
    return int(bit_string, 2)


def read_input(file_name):
    array = []
    with open(file_name) as file:
        for row in file:
            array.append(parse(row))

    return array


# O(n) algorithm based on the observation that to find a missing number
# in an otherwise complete sequence of numbers in random order
# all numbers must be XOR-ed
# and the sequence needs to start at an even number
# and have a length that's a multiple of 4
def find_missing_seat(seat_nums):
    min_num = math.inf
    max_num = 0
    missing_num = 0
    for num in seat_nums:
        missing_num ^= num
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    # min num must be even
    if min_num % 2 == 1:
        min_num = min_num - 1
        missing_num ^= min_num

    # max num must be odd
    if max_num % 2 == 0:
        max_num = max_num + 1
        missing_num ^= max_num

    count = max_num - min_num + 1  # i.e. including boarders

    # count must a multiple of 4
    if count % 4 != 0:  # must be 2 then, because count is even
        missing_num ^= (max_num + 1)
        missing_num ^= (max_num + 2)

    return missing_num


def main():
    seat_nums = read_input("plane_seats.txt")
    highest = max(seat_nums)
    print(f"Highest: {highest}")
    print(f"My seat: {find_missing_seat(seat_nums)}")


if __name__ == "__main__":
    main()
