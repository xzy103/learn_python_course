# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.23


ROOSTER = 5  # 公鸡的单价
HEN = 3  # 母鸡的单价
CHICK = 1/3  # 鸡雏的单价

money = 100
rooster = hen = chick = 0  # 三种鸡数量的初值

for r in range(money//ROOSTER):
    for h in range(money//HEN):
        for c in range(int(money/CHICK)):
            if r*ROOSTER+h*HEN+c*CHICK == 100 and r+h+c == 100:
                print(f'买公鸡{r}只，母鸡{h}只，鸡雏{c}只')
