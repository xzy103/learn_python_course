# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.23


import random

s = 0
n = 10  # 实验n次
for t in range(1, n+1):
    i = 0  # 每次实验赌徒进行的赌局次数设为i
    money = 20  # 每次实验赌徒的初始资金为20
    while money != 0:
        i += 1
        random.seed()
        p = random.random()
        money = money-1 if p < 0.5 else money+1
    print(f'第{t}次实验赌了{i}次。')
    s += i  # 多次重复实验i值的总和

avg = s/n  # 平均到每次实验的i值
print(f'平均要赌{round(avg)}次')
