# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.5.15


def search(a, strat, end):
    mid = (strat+end)//2
    if a[mid] == key:
        return mid  # 返回找到值的下标
    if strat >= end:
        exit('没有找到')

    if a[mid] > key:
        return search(a, strat, mid)
    else:
        return search(a, mid, end)


a = [34, 48, 56, 60, 72, 75, 80, 87, 90, 95, 100]  # 该列表已经按从小到大排序
key = int(input('请输入要查找的值：'))
local = search(a, 0, len(a))
print(f'您要找的值位于列表的第{local+1}个位置。')
