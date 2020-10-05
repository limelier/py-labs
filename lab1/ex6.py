def num_palindrome(num: int) -> bool:
    forwards = str(num)
    backwards = forwards[::-1]
    return forwards == backwards


if __name__ == '__main__':
    print(num_palindrome(123454321), num_palindrome(12345))

