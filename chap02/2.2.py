# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.3.21

n = int(input("请输入一个正整数："))
s = 0
for i in range(1, n+1):
    s += i ** 2

print("平方和为：", s)
