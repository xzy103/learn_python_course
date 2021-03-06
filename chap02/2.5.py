# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.3.28

rate = 0.03  # 年利率
balance = 20574  # 每年交的保费
for age in range(1, 31):
    deposit = 0  # 存款现金流 初始设为0
    interest = balance * rate
    if 0 <= age <= 10:
        deposit += 20574
    if 5 <= age <= 30:
        deposit += -1500
    if 15 <= age <= 24:
        deposit += -15000
    if age in (18, 21, 24):
        deposit += -15000
    if age == 30:
        deposit += -50000
    balance += deposit + interest

    print(f"{age:<2}岁时，账户余额为{balance:.2f}")
