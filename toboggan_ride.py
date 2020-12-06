#! /usr/bin/env python3


def get_num_trees(gridmap, colsteps, rowsteps):
    col = 0
    row = 0
    cols = len(gridmap[0])
    count = 0
    while row < len(gridmap):
        count += 1 if gridmap[row][col] == "#" else 0
        col += colsteps
        col %= cols-1
        row += rowsteps

    return count


def read_input(file_name):
    array = []
    with open(file_name) as file:
        for row in file:
            array.append(row)

    return array


def main():
    gridmap = read_input("tree_grid.txt")
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    res = 1
    for slope in slopes:
        trees = get_num_trees(gridmap, slope[0], slope[1])
        res *= trees

    print(res)


if __name__ == "__main__":
    main()
