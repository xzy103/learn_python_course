# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.3.21


def calculate(p, r, n):
    """
    这是计算复利的函数
    :param p: 本金
    :param r: 年利率
    :param n: 计算期数
    :return: 复利本息
    """

    t = round(p * (1 + r) ** n, 2)
    return t


price = float(input("请输入本金："))
rate = float(input("请输入利率(小数)："))
years = float(input("请输入存款年限："))

if price < 0:
    raise ValueError("本金不能为负数！")
if rate < 0:
    raise ValueError("年利率不能为负数！")
if years <= 0:
    raise ValueError("计息期数应为正数！")

total = calculate(price, rate, years)  # 计算含复利的本利和
print(f"到期总金额为：{total}元。")
