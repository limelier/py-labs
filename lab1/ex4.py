# UpperCamelCase -> snake_case
from string import ascii_uppercase


def convert(string: str) -> str:
    for letter in ascii_uppercase:
        string = string.replace(letter, "_" + letter.lower())
    return string.lstrip("_")


if __name__ == '__main__':
    print(convert("HelloThereWorld"))
