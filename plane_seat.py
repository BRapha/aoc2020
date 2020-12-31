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
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    # In the following steps, the sequence is extended outward to match the algo's criteria;
    # The sequence must not be reduced inward
    # because the missing num could be right next to the sequence's edge.

    # min num must be even
    if min_num % 2 == 1:
        min_num -= 1
        missing_num ^= min_num

    # length (including boundaries) must be a multiple of 4
    while (max_num - min_num + 1) % 4:
        max_num += 1
        missing_num ^= max_num

    return missing_num


def main():
    seat_nums = read_input("plane_seats.txt")
    highest = max(seat_nums)
    print(f"Highest: {highest}")
    print(f"My seat: {find_missing_seat(seat_nums)}")


if __name__ == "__main__":
    main()
