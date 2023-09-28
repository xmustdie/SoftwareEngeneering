empty, non_empty = 'files/file_empty.txt', 'files/file_with_info.txt'


def read_file(name):
    with open(name, 'r') as file:
        try:
            import os
            if os.stat(name).st_size == 0:
                raise IOError()
            for line in file:
                print(line)
        except IOError:
            print("файл пустой")


read_file(empty)
read_file(non_empty)
