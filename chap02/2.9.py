# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.22


n = int(input('请输入行数：'))  # 行数

for i in range(n):
    print(' '*(n-i-1), end='')
    for j in range(i*2+1):
        print('*', end='')
    print()

