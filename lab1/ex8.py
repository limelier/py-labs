def binary_ones(num: int) -> int:
    # O(log_2(num))
    return bin(num).count('1')


def binary_ones_2(num: int) -> int:
    # O(ones)
    ones = 0
    while num:
        ones += 1
        num = num & (num - 1)
    return ones


"""
    a = 0b100110
    c = 0b100101
    b = 0b100100
    
    b = a & (a - 1)
    
    a & 1
    a >> 1
    
"""

if __name__ == '__main__':
    print(binary_ones_2(24))
