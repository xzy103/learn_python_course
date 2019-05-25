# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.27

import csv
from easygraphics import dialog


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

sum_math = sum_literature = 0  # 初始化数学和语文成绩的和
for score in scores:
    sum_math += float(score.math)
    sum_literature += float(score.literature)
avg_math = sum_math/len(scores)  # 数学平均成绩
avg_literature = sum_literature/len(scores)  # 语文平均成绩
print(f'所有同学的数学平均成绩是{avg_math:.2f}，语文平均成绩是{avg_literature:.2f}。')

dialog.show_objects(scores, title='成绩信息', width=1080, height=720)
