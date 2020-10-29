from os import listdir, walk, path


def write_files_no_a(source_directory, target_file):
    files = [file for file in listdir(source_directory)
             if not file.lower().startswith('a')]

    # use a 'with' block for resources which should be closed
    with open(target_file, mode='w') as f:
        for file in files:
            f.write(file + '\n')


def write_files_no_a_recursive(source_directory, target_file):
    """
    Write the full path of every file in source_directory (recursively)
    into target_file
    """
    files = [
        # file
        path.join(root, file)
        for (root, _, files) in walk(source_directory)
        for file in files
        if not file.lower().startswith('a')
    ]

    with open(target_file, mode='w') as f:
        for file in files:
            f.write(file + '\n')


def main():
    write_files_no_a_recursive('/home/limelier/.config', 'ex2.txt')


if __name__ == '__main__':
    main()
