#! /usr/bin/env python3


def read_input(file_name):
    array = []
    with open(file_name) as expenses:
        for row in expenses:
            array.append(int(row))

    return array


def two_sum(array, target, excluded_i=-1):
    seen = set()
    for i in range(len(array)):
        if i == excluded_i:
            continue

        num = array[i]
        complement = target-num
        if complement in seen:
            return complement*num
        else:
            seen.add(num)

    return None


def three_sum(array, target):
    for i in range(len(array)):
        num = array[i]
        rest = target-num
        res = two_sum(array, rest, i)
        if res is not None:
            return res * num


def main():
    nums = read_input("expenses.txt")
    target = 2020
    res = three_sum(nums, target)
    print(res)


if __name__ == "__main__":
    main()
