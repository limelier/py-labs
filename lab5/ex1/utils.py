from math import sqrt, floor


def process_item(num):
    """Return first prime past num."""

    def is_prime_minimal(p):
        """Will only work for odd numbers starting with 3."""
        return not any([p % d == 0 for d in range(3, floor(sqrt(p)), 2)])

    if num < 2:
        return 2

    i = num + 1
    i += 1 - (i % 2)
    while not is_prime_minimal(i):
        i += 2
    return i


def main():
    def input_int():
        while True:
            try:
                num = int(input('Input an integer: '))
                return num
            except ValueError:
                print("That's not an integer.")

    num = input_int()
    print('Bigger prime:', process_item(num))


if __name__ == '__main__':
    main()