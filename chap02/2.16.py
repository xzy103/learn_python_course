# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.26


"""
2.16分解质因数方法简介
获取一个正整数
找到小于这个数的所有质数
在质数中寻找质因数
"""


n = int(input('请输入一个正整数：'))
ls = []
for i in range(2, n//2+1):
    for j in range(2, i//2+1):
        if i % j == 0:
            break  # 如果break，则i不是质数
    if n % i == 0:
        print(i, end=' ')
        # while n % i == 0:
        #     n = int(n/i)
        # print(i, end=' ')







