# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.23


"""
2.15分解质因数方法简介
获取一个正整数
遍历小于这个数的每一个正整数，判断是否为其因数
找到一个因数后更新这一整数为 整数除以因数(while loop)
"""

n = int(input('请输入一个正整数：'))
m = n  # 找到一个因数i后，m /= i，m的初值设为0
a = 0  # 用来暂存因数

for i in range(2, n):
    for j in range(2, m):
        if n % i == 0 and i != a:
            while m % i == 0:
                m = int(m/i)  # while用来过滤重复的因数
            a = i
            print(a, end=' ')

if a == 0:
    print('您输入的数没有因数')
