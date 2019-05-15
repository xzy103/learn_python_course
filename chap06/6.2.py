# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.5.15

import csv


class Score:
    def __init__(self, id_, name, class_, math, literature):
        self.id = id_
        self.name = name
        self.class_ = class_
        self.math = int(math)
        self.literature = int(literature)


with open('../chap03/ex2-2.scores.csv', 'r', encoding='utf-8') as fr:
    scorels = csv.reader(fr)
    next(scorels)
    scores = []
    for s in scorels:
        id_, name, class_, math, literature = s[0], s[1], s[2], s[3], s[4]
        score = Score(id_, name, class_, math, literature)
        scores.append(score)


def find_max(students, n):
    if n == 1:
        return students[0]
    temp = find_max(students, n-1)
    if temp.math + temp.literature > students[n-1].math+students[n-1].literature:
        return temp
    else:
        return students[n-1]


student = find_max(scores, len(scores))
print(f'总分最高的同学是{student.name},他的总分是{student.math+student.literature}分。')
