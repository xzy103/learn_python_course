# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.28


def factor_sum(n: int):
    """
    找出一个正整数所有因子的和
    :param n: 一个正整数
    :return: 这个正整数所有因子的和
    """
    s = 0
    for i in range(1, n//2+1):
        if n % i == 0:
            s += i
    return s


tip = """提示：(a,b) -> (220,284) 和 (284,220)视为相同的一对\n>>>>>Begin..."""
print(tip)
n = 20000
for i in range(1, n+1):
    result = factor_sum(i)
    if factor_sum(result) == i <= result:
        print('Bingo!Find a pair:', i, result)
print('Done!')
