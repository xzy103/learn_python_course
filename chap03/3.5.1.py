# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.27


import csv


class Inventory:
    def __init__(self, id_, name, amount, type_):
        self.id = id_
        self.name = name
        self.amount = amount
        self.type = type_  # 商品类型


filename = 'ex2-4.inventory.csv'
with open(filename, 'r', encoding='utf-8') as fr:
    inventoryls = csv.reader(fr)
    next(inventoryls)
    inventory = []
    for i in inventoryls:
        id_, name, amount, type_ = i[0], i[1], i[2], i[3]
        inv = Inventory(id_, name, amount, type_)
        inventory.append(inv)

print('商品ID,商品名称,实际库存量,商品类别')
for i in inventory:
    print(f'{i.id},{i.name},{i.amount},{i.type}')
