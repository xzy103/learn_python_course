# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.29


import csv
import statistics


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


def filter_class(obj):
    return class_ == obj.class_


def map_literature(obj):
    return float(obj.literature)


def map_math(obj):
    return float(obj.math)


def filter_liter_low(obj):
    return float(obj.literature) < 60


def filter_math_low(obj):
    return float(obj.math) < 60


def math_low_names(obj):
    return obj.name


if __name__ == '__main__':
    class_ = input('请输入要计算的班级：')  # class_的作用域是全局的
    scores = read_csv(filename='../chap03/ex2-2.scores.csv')
    classls = list(filter(filter_class, scores))  # 筛选后的班级列表

    literature = list(map(map_literature, classls))  # 要查询班级的语文成绩列表
    literature_mean = round(statistics.mean(literature), 2)
    math = list(map(map_math, classls))  # 要查询班级的数学成绩列表
    math_mean = round(statistics.mean(math), 2)
    math_lowls = list(map(math_low_names, filter(filter_math_low, classls)))  # 要查询班级的数学不及格同学列表
    liter_lowls = list(filter(filter_liter_low, classls))  # 要查询班级的语文不及格同学对象

    print(f'{class_}的语文平均分是{literature_mean}，数学平均分是{math_mean}')
    print(f'其中语文不及格的人数为：{len(liter_lowls)}')
    print(f'其中数学不及格的同学为：{" ".join(math_lowls) if math_lowls else "(无)"}')
