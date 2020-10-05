import re
from typing import Optional


def first_number(string: str) -> Optional[int]:
    number_match = re.search(r'0|([1-9]\d*)', string)
    # 0, or any non-zero digit and any digits following it
    if number_match is None:
        return None
    else:
        return int(number_match.group(0))


if __name__ == '__main__':
    print(first_number("ana are 123mere"))

