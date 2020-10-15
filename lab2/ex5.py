import copy
from typing import List


def zero_diagonal(matrix: List[List[int]]) -> List[List[int]]:
    modified = copy.deepcopy(matrix)

    for i in range(len(matrix)):
        modified[i][i] = 0

    return modified


if __name__ == '__main__':
    print(zero_diagonal([
        [1, 2, 3, 4] for i in range(4)
    ]))
