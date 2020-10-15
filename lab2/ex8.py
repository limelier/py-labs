from typing import List


def f(words: List[str], x: int = 1, flag: bool = True) -> List[List[str]]:
    return [
        list(filter(
            lambda c: (ord(c) % x == 0) == flag,
            string
        ))
        for string in words
    ]


if __name__ == '__main__':
    strings = ['test', 'hello', 'lab002']
    print(f(strings, 2))
    print(f(strings, 2, flag=False))
