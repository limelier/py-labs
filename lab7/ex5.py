import sys
import os
import zipfile


def main():
    if len(sys.argv) != 3:
        print("Usage: {} a_path ext".format(sys.argv[0]))
        return
    _, a_path, ext = sys.argv

    with zipfile.ZipFile("the.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for file in os.listdir(a_path):
            crt_ext = os.path.splitext(file)[-1]
            print(ext, crt_ext)
            if crt_ext == ext:
                z.write(os.path.join(a_path, file))


if __name__ == '__main__':
    main()
