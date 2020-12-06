#! /usr/bin/env python3
import string

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


def is_valid(key, value):

    if key == "byr":
        return len(value) == 4 and value.isdigit() and 1920 <= int(value) <= 2002
    elif key == "iyr":
        return len(value) == 4 and value.isdigit() and 2010 <= int(value) <= 2020
    elif key == "eyr":
        return len(value) == 4 and value.isdigit() and 2020 <= int(value) <= 2030
    elif key == "hgt":
        height = value[:-2]
        unit = value[-2:]
        if unit == "cm":
            return height.isdigit() and 150 <= int(height) <= 193
        else:
            return height.isdigit() and 59 <= int(height) <= 76
    elif key == "hcl":
        return value[0] == "#" and len(value[1:]) == 6 and all(c in string.hexdigits for c in value[1:])
    elif key == "ecl":
        return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    elif key == "pid":
        return len(value) == 9 and value.isdigit()


def is_valid_passport_two(pass_string, required):
    pass_dict = {}
    for field in pass_string.split():
        s = field.split(":")
        pass_dict[s[0]] = s[1]

    for key in required:
        if key not in pass_dict:
            return False
        if not is_valid(key, pass_dict[key]):
            return False

    return True


def is_valid_passport_one(pass_string, required):
    return all(field in pass_string for field in required)


def read_input(file_name):
    array = []

    string = ""
    with open(file_name) as file:
        for row in file:
            if row == '\n':
                array.append(string)
                string = ""
            else:
                string += row + " "

    array.append(string)

    return array


def main():
    passport_strings = read_input("passports.txt")

    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", )

    count = 0
    for passport in passport_strings:
        count += 1 if is_valid_passport_two(passport, required_fields) else 0

    print(count)


if __name__ == "__main__":
    main()
