# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.5.15


def func(n, count=0):
    if n == 1:
        return 1, count

    count += 1
    if n % 2:
        n = 3*n+1
    else:
        n /= 2
    return func(n, count)


num = int(input('请输入一个自然数：'))
result, count = func(num)
print(f'使用角谷定理，经过{count}次运算，结果为{result}')
