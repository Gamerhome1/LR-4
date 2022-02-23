import os

def get_file_sizes(folder_path):
    result={}
    for path,folders,files in os.walk(folder_path):
        for file in files:
            file_path=os.path.join(path, file)
            file_size=os.path.getsize(file_path)
            result[file_path]=file_size
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
    for k,v in d.items():
        print(k)
        print('\n'.join(['\t'+ i for i in v]))
        print()