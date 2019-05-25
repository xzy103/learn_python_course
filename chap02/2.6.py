# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.3.28

import math

a = float(input("请输入a值："))  # a是全局变量


def f(x):
    return x**3-a


def f_derivative(x):
    return 3*x**2


ep = 0.000000000001  # 设定精度
xk = xk1 = 1

while True:
    xk1 = xk
    try:
        xk = xk1 - f(xk1)/f_derivative(xk1)
    except ZeroDivisionError:
        xk = 0
    if math.fabs(xk - xk1) < ep:
        break

print(f"实数{a}的立方根是{xk}")
