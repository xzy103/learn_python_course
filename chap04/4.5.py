# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.29


from functools import reduce


print('>>>>>>求解小于n的奇数的立方和')
n = int(input("请输入一个正整数："))
num = [i for i in range(n)]


def map_cube(n):
    return pow(n, 3)


def reduce_odd(lt: list, i):
    if i % 2:
        lt.append(i)
    return lt


odd = reduce(reduce_odd, num, [])
cube = map(map_cube, odd)
sum_cube = sum(cube)
print(f'小于{n}的所有奇数的立方和为{sum_cube}')
