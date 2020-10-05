def vowels(string: str) -> int:
    return len([char for char in string if char.lower() in 'aeiou'])


if __name__ == '__main__':
    print(vowels("AnA ArE mErE'"))
