# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.27


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

info1_sum_math = info1_sum_literture = count = 0
for score in scores:
    if score.class_ == '信管1班':  # 仅针对满足条件的对象操作
        count += 1
        info1_sum_math += float(score.math)
        info1_sum_literture += float(score.literature)

info1_avg_math = info1_sum_math/count  # 信管1班数学平均成绩
info1_avg_literture = info1_sum_literture/count  # 信管1班语文平均成绩

print(f'信管1班数学平均成绩是{info1_avg_math:.2f}，语文平均成绩是{info1_avg_literture:.2f}。')
