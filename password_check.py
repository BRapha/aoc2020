#! /usr/bin/env python3


class Rule:
    def __init__(self, lower, upper, char):
        self.lower = lower
        self.upper = upper
        self.char = char


def extract_rule(line):
    parts = line.split()
    bounds = parts[0].split("-")
    return Rule(int(bounds[0]), int(bounds[1]), parts[1].strip(":"))


def extract_pw(line):
    return line.split()[-1]


def read_input(file_name):
    array = []
    with open(file_name) as file:
        for row in file:
            rule = extract_rule(row)
            pw = extract_pw(row)
            array.append((rule, pw))

    return array


def is_valid_pw_one(combo):
    rule: Rule = combo[0]
    pw = combo[1]

    count = 0
    for c in pw:
        count += 1 if c == rule.char else 0

    return rule.lower <= count <= rule.upper


def is_valid_pw_two(combo):
    rule: Rule = combo[0]
    pw = combo[1]
    at_lower = pw[rule.lower-1] == rule.char
    at_upper = pw[rule.upper-1] == rule.char

    return at_lower ^ at_upper


def count_valid_pws(array):
    count = 0
    for combo in array:
        count += 1 if is_valid_pw_two(combo) else 0

    return count


def main():
    array = read_input("passwords.txt")
    print(count_valid_pws(array))


if __name__ == "__main__":
    main()
