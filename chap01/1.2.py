# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.3.21

p = float(input("请输入本金："))
r = float(input("请输入利率（小数）："))
n = int(input("请输入存款年份："))
total = round(p*(1+r)**n, 2)
print("到期总金额为：", total)
