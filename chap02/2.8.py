# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.18

import random


def rend(time):
    """
    每隔time小时将车从A地搬一半到B地
    返回B地未租到车的可能性ratio_b%
    函数中有设置全局变量
    :param time: 搬运时间间隔
    :return: B地未租到车的可能性ratio_b%
    """
    random.seed()
    n = 500000
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

        if i % time == 0:
            trans = num_a//2
            num_a -= trans
            num_b += trans

    ratio_a = no_bike_count_a / customer_a * 100
    ratio_b = no_bike_count_b / customer_b * 100
    return ratio_b


print('>>>>>模拟过程约需要10s-30s.')
t = 550  # 搬运时间间隔，粗略测试后设置为550。
ratio_b_temp = 0  # break前一次的ratio_b值
while True:
    rend(t)  # 进行一次实验 这次实验的时间间隔设为t
    if ratio_b > 5:
        ratio_b = ratio_b_temp
        t -= 1
        break
    else:
        t += 1
        ratio_b_temp = ratio_b

print(f"每隔{t}小时转移一次为宜。")
print(f"A地想租车人数{customer_a},未租到人数{no_bike_count_a}, 未租到比例{ratio_a:0.2f}%")
print(f"B地想租车人数{customer_b},未租到人数{no_bike_count_b}, 未租到比例{ratio_b:0.2f}%")
