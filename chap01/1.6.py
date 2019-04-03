# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.3.21

from math import sqrt


def area(a, b, c):
    """
    用海伦公式计算任意三角形的面积。
    :param a: a边长
    :param b: b边长
    :param c: c边长
    :return: 三角形面积
    """
    p = (a+b+c)/2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    return s


len1 = float(input("请输入第一条边的长度："))
len2 = float(input("请输入第二条边的长度："))
len3 = float(input("请输入第三条边的长度："))

if min(len1, len2, len3) <= 0:
    raise ValueError("边长需为正数！")
if sum([len1, len2, len3]) <= 2*max(len1, len2, len3):
    raise ValueError("两边之和小于等于第三边！")

result = area(len1, len2, len3)
print(f'三角形的面积为：{round(result, 3)}')
