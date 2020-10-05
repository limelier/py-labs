def binary_ones(num: int) -> int:
    return bin(num).count('1')


if __name__ == '__main__':
    print(binary_ones(24))
