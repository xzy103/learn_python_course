# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.5.15

import numpy as np
from numpy import random


def get_normal(mean, dev, n):
    """
    产生n个非负，服从指定正态分布的随机数

    :param mean: 正态分布的均值
    :param dev: 正态分布的标准差
    :return: 产生的随机数数组
    """
    if mean <= 0 or dev <= 0:
        raise ValueError("Mean and dev must be positive！")
    result = random.normal(mean, dev, n)
    return np.where(result > 0, result, 0)


fixed_cost = 50000
sale_mean, sale_dev = 100000, 25000
cost_mean, cost_dev = 5, 1
price_mean, price_dev = 10, 2
rate_mean, rate_dev = 0.1, 0.02

n = 5000000
sale = get_normal(sale_mean, sale_dev, n)
price = get_normal(price_mean, price_dev, n)
rate = get_normal(rate_mean, rate_dev, n)
cost = get_normal(cost_mean, cost_dev, n)
profit = sale * (price-cost) / (1+rate)-fixed_cost  # 盈利=销量*(价格-成本)/(1+利率)-固定成本
count = len(profit[profit >= 0])
print(f"盈利的可能性为{count/n * 100: .2f}%, 盈利的期望值为{round(np.average(profit), 2)}元")
