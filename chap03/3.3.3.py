# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.27


import csv


class Score:
    def __init__(self, id_, name, class_, math, literature, sum_):
        self.id = id_
        self.name = name
        self.class_ = class_
        self.math = math
        self.literature = literature
        self.sum = sum_  # 总分属性


filename = 'ex2-2.scores.csv'
with open(filename, 'r', encoding='utf-8') as fr:
    scorels = csv.reader(fr)
    next(scorels)
    scores = []
    for s in scorels:
        id_, name, class_, math, literature = s[0], s[1], s[2], s[3], s[4]
        sum_ = int(math) + int(literature)  # 总分 = 数学成绩 + 语文成绩
        score = Score(id_, name, class_, math, literature, str(sum_))
        scores.append(score)

# 写入到 含总分成绩.csv 文件
with open('含总分成绩.csv', 'w', encoding='utf-8') as fw:
    fw.write('学号,姓名,班级,数学,语文,总分\n')
    for s in scores:
        fw.write(f'{s.id},{s.name},{s.class_},{s.math},{s.literature},{s.sum}\n')
print('成绩信息已写入到[含总分成绩.csv]')
