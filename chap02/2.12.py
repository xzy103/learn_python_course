# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.23


nums = range(1, 10)
for d in nums:
    for e in nums:
        for f in nums:
            for g in nums:
                if (10*d+e)*(10*f+g) == (10*e+d)*(10*g+f) and len({d, e, f, g}) == 4:
                    print('d e f g分别为：', d, e, f, g)


'''
from itertools import product
nums = range(1, 10)
for d, e, f, g in product(nums, nums, nums, nums):
    if (10 * d + e) * (10 * f + g) == (10 * e + d) * (10 * g + f) and (d != e != f != g):
        print('defg分别为：', d, e, f, g)
'''
