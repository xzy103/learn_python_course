# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.18

import random


def rend(t):
    random.seed()
    n = 10000
    global customer_a, customer_b, no_bike_count_a, no_bike_count_b, ratio_a, ratio_b
    prob_a, prob_b = 0.3, 0.5  # A地租车可能性 B地租车可能性
    num_a, num_b = 100, 100  # AB两地车的数量
    customer_a, customer_b = 0, 0  # AB两地来租车的人数
    no_bike_count_a, no_bike_count_b = 0, 0  # AB两地没租到车的人数
    for i in range(n):
        want_a = random.uniform(0, 1) <= prob_a
        want_b = random.uniform(0, 1) <= prob_b
        if want_a:
            customer_a += 1
            if num_a > 0:
                num_a -= 1
                num_b += 1
            else:
                no_bike_count_a += 1
        if want_b:
            customer_b += 1
            if num_b > 0:
                num_b -= 1
                num_a += 1
            else:
                no_bike_count_b += 1

        if i % t == 0:
            trans = num_a//2
            num_a -= trans
            num_b += trans

    ratio_a = no_bike_count_a / customer_a * 100
    ratio_b = no_bike_count_b / customer_b * 100
    return ratio_b


t = 1
while rend(t) < 5:
    t += 1

print(f"每隔{t}小时转移一次为宜。")
print(f"A地想租车人数{customer_a},未租到人数{no_bike_count_a}, 未租到比例{ratio_a:0.2f}%")
print(f"B地想租车人数{customer_b},未租到人数{no_bike_count_b}, 未租到比例{ratio_b:0.2f}%")

