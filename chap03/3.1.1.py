# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.26


n = int(input("请输入一个正整数："))
lst_a = []
for i in range(1, n+1):
    lst_a.append(i)
print('lst_a is', lst_a)


lst_b = [0]*n
for i in range(n):
    lst_b[i] = i+1
print('lst_b is', lst_b)


lst_c = []
for i in lst_a:
    if i % 2 == 0:
        lst_c.append(i)
print('lst_c is', lst_c)
