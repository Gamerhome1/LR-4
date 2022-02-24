import os


def userpath():
    while True:
        path1 = input("Введите путь до папки: ")
        if os.path.exists(path1):
            break
        else:
            print("Это не путь, либо путь некорректен")
    return path1


def get_file_sizes(folder_path):
    result = {}
    for path, folders, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(path, file)
            file_size = os.path.getsize(file_path)
            result[file_path] = file_size
    return result


def get_duplicates(d):
    result = {}
    for path, size in d.items():
        name = os.path.basename(path)
        if (name, size) in result:
            result[(name, size)].append(path)
        else:
            result[(name, size)] = [path]
    return {k: v for k, v in result.items() if len(v) > 1}


def get_results(d):
    for k, v in d.items():
        print(k)
        print('\n'.join(['\t' + i for i in v]))
        print()


if __name__ == '__main__':
    print(get_results(get_duplicates(get_file_sizes(userpath()))))
