# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.28


import csv


class Inventory:
    def __init__(self, id, name, amount, type_):
        self.id = id
        self.name = name
        self.amount = amount
        self.type = type_


def find_min(invty, start, end):
    """
    找到从invty[start]到invty[end]中邮箱最小的下标
    :param invty: 用户对象列表
    :param start: 开始下标
    :param end: 结束下标
    :return: 最小库存的下标
    """
    min = start
    for i in range(start, end):
        if invty[i].amount < invty[min].amount:
            min = i
    return min


def select_sort(invty):
    """
    选择排序
    :param invty: 需要排序的对象列表
    :return: None
    """
    n = len(invty)
    for i in range(n):
        t = find_min(invty, i, n)
        invty[i], invty[t] = invty[t], invty[i]


if __name__ == '__main__':
    with open('ex2-4.inventory.csv', 'r', encoding='utf-8') as fr:
        inventoryls = csv.reader(fr)
        next(inventoryls)
        inventory = []
        for i in inventoryls:
            id, name, amount, type_ = i[0], i[1], i[2], i[3]
            inv = Inventory(id, name, amount, type_)
            inventory.append(inv)

    select_sort(inventory)
    print('商品ID,商品名称,库存量,商品类别')
    for i in inventory:
        print(f'{i.id},{i.name},{i.amount},{i.type}')
