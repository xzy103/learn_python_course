# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.28


import csv


class Score:
    def __init__(self, id_, name, class_, math, literature):
        self.id = id_
        self.name = name
        self.class_ = class_
        self.math = math
        self.literature = literature


filename = 'ex2-2.scores.csv'
with open(filename, 'r', encoding='utf-8') as fr:
    scorels = csv.reader(fr)
    next(scorels)
    scores = []
    for s in scorels:
        id_, name, class_, math, literature = s[0], s[1], s[2], s[3], s[4]
        score = Score(id_, name, class_, math, literature)
        scores.append(score)


# 顺序查找法
def find_by_name1(scores, name_key):
    """
    在scores这个对象列表中查找name等于name_key的元素
    :param scores: scores对象列表
    :param name_key: 要查找的name关键字
    :return: 该用户的信息对象，没有找到返回-1
    """
    for i in range(len(scores)):
        if scores[i].name == name_key:
            return scores[i]
    return -1


# 折半查找法
def find_by_name2(scores, name_key):
    """
    在scores这个对象列表中查找name等于name_key的元素
    :param scores: scores对象列表
    :param name_key: 要查找的name关键字
    :return: 该用户的信息对象，没有找到返回-1
    """
    start, end = 0, len(scores) - 1
    while start <= end:
        mid = (start+end)//2
        s = scores[mid]
        if s.name == name_key:
            return s
        elif s.name < name_key:
            start = mid+1
        else:
            end = mid-1
    return -1


name = input('请输入要查找的学生姓名：')
uinfo = find_by_name1(scores, name)
if uinfo == -1:
    print(f'找不到姓名为{name}的学生')
else:
    print('顺序查找的结果为↓')
    print(f'id:{uinfo.id}\nname:{uinfo.name}\nclass:{uinfo.class_}\nmath:{uinfo.math}\nliterature:{uinfo.literature}')


uinfo = find_by_name2(scores, name)
if uinfo == -1:
    print(f'找不到姓名为{name}的学生')
else:
    print('二分查找的结果为↓')
    print(f'id:{uinfo.id}\nname:{uinfo.name}\nclass:{uinfo.class_}\nmath:{uinfo.math}\nliterature:{uinfo.literature}')
