from itertools import chain
from functools import reduce

with open('./forest map.txt') as f:
    forest_map = f.readlines()

forest_map = [list(x.strip()) for x in forest_map]


def trees_encountered(f_map, slope):
    col = 0
    for row in range(slope[0], len(f_map), slope[0]):
        col += slope[1]
        try:
            if f_map[row][col] == '.':
                f_map[row][col] = 'O'
            elif f_map[row][col] == '#':
                f_map[row][col] = 'X'
        except IndexError:
            col = col % 31
            if f_map[row][col] == '.':
                f_map[row][col] = 'O'
            elif f_map[row][col] == '#':
                f_map[row][col] = 'X'

    f_map_flat = list(chain(*f_map))
    return f_map_flat.count('X')


slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
num_trees_encountered = []

for slope in slopes:
    with open('./forest map.txt') as f:
        forest_map = f.readlines()

        forest_map = [list(x.strip()) for x in forest_map]
    num_trees_encountered.append(trees_encountered(forest_map, slope))

print(reduce((lambda x, y: x * y), num_trees_encountered))
