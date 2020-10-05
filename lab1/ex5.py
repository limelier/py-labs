def spiral(matrix: [[chr]]) -> str:
    size = len(matrix)
    # if size == 0:
    #     result = ''
    # elif size == 1:
    #     result = matrix[0][0]
    # else:
    result = ''.join(matrix[0])
    result += ''.join([matrix[i][size - 1] for i in range(1, size)])
    result += ''.join(matrix[size - 1][-2::-1])
    result += ''.join(matrix[i][0] for i in range(size - 2, 0, -1))

    if size > 2:
        result += spiral([line[1:-1] for line in matrix[1:-1]])

    return result


if __name__ == '__main__':
    matrix1 = [
        ['a', 'b', 'c', 'd'],
        ['l', 'm', 'n', 'e'],
        ['k', 'p', 'o', 'f'],
        ['j', 'i', 'h', 'g'],
    ]
    matrix2 = [
        ['a', 'b', 'c'],
        ['h', 'i', 'd'],
        ['g', 'f', 'e'],
    ]

    matrix3 = [
        ['f', 'i', 'r', 's'],
        ['n', '_', 'l', 't'],
        ['o', 'b', 'a', '_'],
        ['h', 't', 'y', 'p'],
    ]

    print(spiral(matrix3))
