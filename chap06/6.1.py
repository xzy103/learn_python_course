# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.5.15


def find_min(lst, n):
    if n == 1:
        return lst[0]
    m = find_min(lst, n-1)
    if m < lst[n-1]:
        return m
    else:
        return lst[n-1]


lst = [56, 23, 98, 64, 24, 91, 81, 13, 75]
m = find_min(lst, len(lst))
print(f"最小值为{m}")
