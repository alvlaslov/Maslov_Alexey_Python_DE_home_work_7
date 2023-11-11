import os
from pathlib import Path


def group_rename(*, dir_path: str,
                 new_name: str = '',
                 amount_num: int = 3,
                 in_extension: str,
                 out_extension: str,
                 name_range: tuple):
    if not os.path.isdir(dir_path):
        return f"{dir_path} is'not directory"
    dir_list = os.listdir(dir_path)
    count_file = 1
    rename_file = 0
    for obj in dir_list:
        name, extension = os.path.splitext(obj)
        if extension == in_extension:
            new_file = ''
            if new_name:
                new_file += \
                    f'{name[name_range[0] - 1:name_range[1]]}_{new_name}_'
            else:
                new_file += \
                    f'{name[name_range[0] - 1:name_range[1]]}_'
            new_file += f'{count_file:0>{amount_num}}{out_extension}'
            os.rename(os.path.join(dir_path, obj), os.path.join(dir_path, new_file))
            count_file += 1
    if count_file > 1:
        return f"{count_file - 1} files were rename"