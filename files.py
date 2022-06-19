__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os  # 1, 2, 3
import shutil  # 1
import zipfile  # 2


# 1
def clean_cache():
    name = 'cache'
    dir_path = 'C:/Users/user/Winc/files/cache'
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
    os.makedirs(dir_path)
    return f'{name} is created'


# 2
zip_path = 'C:/Users/user/Winc/files/data.zip'
dir_path = 'C:/Users/user/Winc/files/cache'


def cache_zip(zip_path, dir_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dir_path)
    return 'zip is unpacked in folder'


# 3
def cached_files():
    filelist = []
    for file in os.listdir(dir_path):
        filelist.append(os.path.join(os.path.abspath(dir_path), file))
    return filelist


# 4
filelist = cached_files()


def find_password(filelist):
    for file in filelist:
        searchfile = open(file, "r")
        for line in searchfile:
            if ("password") in line:
                return line.replace("password: ", "").rstrip('\n')


if __name__ == '__main__':
    print(clean_cache())
    print(cache_zip(zip_path, dir_path))
    print(cached_files())
    print(find_password(cached_files()))
