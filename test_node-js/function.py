import os

def count_files(directory):
    file_count = 0

    for root,dirs,files in os.walk(directory):
        for file in files:
            file_count += 1

    return file_count

def rename_all_file_in_dir(path_dir,new_name="img",extension=".jpg"):
    i = 1
    for filename in os.listdir(path_dir):
        if os.path.isfile(os.path.join(path_dir, filename)):
            file_path = os.path.join(path_dir, filename)
            new_file_path = os.path.join(path_dir,new_name+str(i)+extension)
            os.rename(file_path, new_file_path)
        i+=1