# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.5.15


from pathlib import Path
from easygraphics import dialog as dlg


def find_in_dir(path):
    results = []
    for entry in path.iterdir():  # 遍历目录中的所有条目
        if entry.is_dir():  # 如果是子目录
            results0 = find_in_dir(entry)  # 递归在子目录中查找
            results.extend(results0)  # 将查找结果并入结果集
        if entry.is_file():  # 如果是文件
            if entry.name.endswith('.xls') or entry.name.endswith('.xlsx'):
                results.append(str(entry.resolve()))  # 找到一个，加入结果集
    return results


print('(递归方式)查找一个文件夹下的所有表格文件')
dir_path = dlg.get_directory_name("请选择文件夹")
dir = Path(dir_path)
results = find_in_dir(dir)
for file in results:
    print(file)
