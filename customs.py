#! /usr/bin/env python3


def count_questions_any(group):
    answers_any = set(c for c in group if not c.isspace())
    return len(answers_any)


def count_questions_all(group):
    individual_answers = group.split()
    first = individual_answers[0]
    answers_all = tuple(c for c in first if all(c in pers for pers in individual_answers))
    return len(answers_all)


def read_input(file_name):
    array = []

    group = ""
    with open(file_name) as file:
        for row in file:
            if row == "\n":
                array.append(group)
                group = ""
            else:
                group += row + " "

    array.append(group)

    return array


def main():
    groups = read_input("customs_forms.txt")
    print(sum(count_questions_all(group) for group in groups))


if __name__ == "__main__":
    main()
