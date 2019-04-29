# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.29


def sum_square(x, y):
    return pow(x, 2)+pow(y, 2)


def str_sum_square(x, y):
    return f'{x}的平方加上{y}的平方等于{pow(x, 2)+pow(y, 2)}'


a = [i for i in range(1, 11)]
b = [i for i in range(2, 21, 2)]

c = map(sum_square, a, b)
print(list(c))

c = map(str_sum_square, a, b)
print(list(c))
