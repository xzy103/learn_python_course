# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.3.21

p = float(input("请输入本金："))
r = float(input("请输入利率(小数)："))
n = int(input("请输入存款年份："))

for i in range(1, n+1):
    interest = p*r  # 当年新增利息
    p += interest  # 当年年末账户余额
    print(f"第{i:^3}年的新增利息为{interest:<8.2f} 账户总金额为{p:<8.2f}")
