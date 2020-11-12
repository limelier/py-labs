# UpperCamelCase -> snake_case
from string import ascii_uppercase
import re


def convert(string: str) -> str:
    for letter in ascii_uppercase:
        string = string.replace(letter, "_" + letter.lower())
    return string.lstrip("_")


def convert_re(string: str) -> str:
    uppercases = re.findall(r'[A-Z]', string)

    for letter in uppercases:
        string = string.replace(letter, "_" + letter.lower())

    return string.lstrip('_')


def convert_re2(string: str) -> str:
    return re.sub(r'[A-Z]', lambda s: '_' + s.group().lower(), string).lstrip('_')


if __name__ == '__main__':
    print(convert_re2('HelloThereWorld'))
