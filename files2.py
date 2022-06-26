__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os  # 1, 2, 3
import shutil  # 1
import zipfile  # 2


# 1
def clean_cache():
    name = 'cache'
    if os.path.isdir(os.path.join(os.getcwd(),'files', 'cache')):
        shutil.rmtree(os.path.join(os.getcwd(),'files', 'cache'))
    os.makedirs(os.path.join(os.getcwd(),'files', 'cache'))
    return f'{name} is created'


# 2
def cache_zip(zip_path, dr_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dr_path)
    return 'zip is unpacked in folder'


# 3
def cached_files():
    filelist = []
    for file in os.listdir(os.path.join(os.getcwd(),'files', 'cache')):
        filelist.append(os.path.join(os.path.abspath(os.path.join(os.getcwd(),'files', 'cache')), file))
    return filelist


# 4
def find_password(filelist):
    for file in filelist:
        searchfile = open(file, "r")
        for line in searchfile:
            if ("password") in line:
                return line.replace("password: ", "").rstrip('\n')


if __name__ == '__main__':
    dir_path = os.path.join(os.getcwd(),'files', 'cache')
    zip_path = os.path.join(os.getcwd(),'files', 'data.zip')
    print(clean_cache())
    print(cache_zip(zip_path, dir_path))
    print(cached_files())
    print(find_password(cached_files()))
