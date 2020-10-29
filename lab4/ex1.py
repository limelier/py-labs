from os.path import splitext
from os import listdir


def unique_extensions(directory):
    contents = listdir(directory)
    exts = {splitext(file)[1].lstrip('.') for file in contents}
    exts.discard('')
    return sorted(exts)


def main():
    print(unique_extensions('/home/limelier'))


if __name__ == '__main__':
    main()

