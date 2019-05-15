# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.5.15


import numpy as np


a_1_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a_1_2 = np.arange(10)
print('第1问', a_1_1, a_1_2, sep='\n', end='\n\n')


a_2_1 = np.array([1, 3, 5, 7, 9, 11])
a_2_2 = np.linspace(1, 11, 6)
print('第2问', a_2_1, a_2_2, sep='\n', end='\n\n')


a = np.arange(10)
b = 2 * a + 1
print('第3问', b, end='\n\n')

# 第4问
a = np.arange(1, 11)
b = 2 * a
c = a * a + b * b
print('第4问', c, end='\n\n')


n = int(input('第5问\n请输入一个正整数n:'))
a = np.arange(n)
b = a[a % 2 == True]
c = sum(np.power(b, 3))
print(c)
