def words(string: str) -> int:
    return len(string.split(' '))


if __name__ == '__main__':
    print(words('I have Python exam'))
