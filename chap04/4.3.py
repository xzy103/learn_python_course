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


def read_csv(filename: str):
    with open(filename, 'r', encoding='utf-8') as fr:
        scorels = csv.reader(fr)
        next(scorels)
        scores = []
        for s in scorels:
            id_, name, class_, math, literature = s[0], s[1], s[2], s[3], s[4]
            score = Score(id_, name, class_, math, literature)
            scores.append(score)
    return scores


def key_total(score):
    return int(score.math)+int(score.literature)


if __name__ == '__main__':
    scores = read_csv(filename='../chap03/ex2-2.scores.csv')
    max_student = max(scores, key=key_total)
    min_student = min(scores, key=key_total)
    print(f'总分最高的同学\n{max_student.__dict__}')
    print(f'总分最低的同学\n{min_student.__dict__}\n')
    print('总分由高到低排序')
    print('学号,姓名,班级,数学,语文')
    scores = sorted(scores, key=key_total, reverse=True)
    for s in scores:
        print(f'{s.id} {s.name} {s.class_} {s.math} {s.literature}')
