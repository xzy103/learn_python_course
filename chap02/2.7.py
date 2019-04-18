# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.2

import random


def get_normol(mean, dev):
    """
    产生一个非负、服从正态分布的随机数
    :param mean: 正态分布的均值
    :param dev: 正态分布的标准差
    :return: 产生的随机数
    """
    if mean <= 0 or dev <= 0:
        raise RuntimeError("Mean and dev must be positive!")
    result = random.normalvariate(mean, dev)
    return max(0, result)


random.seed()
stable_cost = 50000  # 固定成本
sale_mean, sale_dev = 100000, 25000  # 销量的均值 方差
cost_mean, cost_dev = 5, 1  # 单位成本 均值 方差
price_mean, price_dev = 10, 2  # 价格 均值 方差
rate_mean, rate_dev = 0.1, 0.02  # 利率 均值 方差

n = 100000
count = 0
profits = 0
for i in range(n):
    sale = get_normol(sale_mean, sale_dev)
    price = get_normol(price_mean, price_dev)
    cost = get_normol(cost_mean, cost_dev)
    rate = get_normol(rate_mean, rate_dev)
    profit = sale*((price/(1+rate))-cost)-stable_cost
    if profit > 0:
        count += 1
        profits += profit

print(f"该项目盈利的可能性为{count/n*100:.2f}%，盈利的期望值为{profits/n:.2f}元。")
