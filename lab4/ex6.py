from os.path import isfile, isdir, join, getsize
from os import walk
import mmap


def callback_search(target, to_search, callback, follow_links=False):
    """
    Search for a string of bytes in a file or directory (recursively), and return
    a list of files where the string was found.

    Raise a ValueError for targets that are neither file nor directory.

    Call the callback with any exception encountered.

    Use follow_links to control following symlinks (default: False).
    """
    try:
        if isfile(target):
            if getsize(target) == 0:
                return []
            with open(target, "rb") as f:
                # create an iterable from a file
                contents = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                if contents.find(to_search) != -1:
                    return [target]
                else:
                    return []
        elif isdir(target):
            hits = []
            for root, _, files in walk(target, followlinks=follow_links):
                for file in files:
                    hits.extend(callback_search(
                        join(root, file),
                        to_search,
                        callback
                    ))
            return hits
        else:
            raise ValueError('{} is not a directory or file'.format(target))
    except Exception as e:
        callback(e)
        return []


def main():
    res = callback_search('/home/limelier/.config', b'gold = ', print, follow_links=True)
    print(res)


if __name__ == '__main__':
    main()
