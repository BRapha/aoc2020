#! /usr/bin/env python3


def parse(row):
    bit_string = "".join(map(lambda c: "1" if c in ("B", "R") else "0", row.strip()))
    return int(bit_string, 2)


def read_input(file_name):
    array = []
    with open(file_name) as file:
        for row in file:
            array.append(parse(row))

    return array


def find_my_seat(seat_nums, max_num):
    my_seat = max_num
    for num in seat_nums:
        my_seat = my_seat ^ num

    return my_seat


def main():
    seat_nums = read_input("plane_seats.txt")
    highest = max(seat_nums)
    print(f"Highest: {highest}")
    print(f"My seat: {find_my_seat(seat_nums, highest)}")


if __name__ == "__main__":
    main()
