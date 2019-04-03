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
cost = 50000  # 固定成本
sale_mean, sale_dev = 100000, 25000
cost_mean, cost_dev = 5, 1
price_mean, price_dev = 10, 2
rate_mean, rate_dev = 0.1, 0.02



