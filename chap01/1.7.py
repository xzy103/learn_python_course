# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.3.21


def which_day(calendar):
    """
    将整数表示的日期拆分为年月日。
    :param calendar: 整数表示的日期
    :return: year, mon, day 分别表示年 月 日
    """
    year = calendar//10000
    mon_day = calendar % (10000*year)
    mon = mon_day//100
    day = mon_day % (100*mon)
    if year <= 0:
        raise ValueError("年份需大于0！")
    if mon not in range(1, 13):
        raise ValueError("月份数值非法！")
    if day not in range(1, 31):
        raise ValueError("日期数值非法！")
    return year, mon, day


date = int(input("请输入日期，例如20190321："))
y, m, d = which_day(date)
print(f"函数返回：{y},{m},{d}")
print(f"{y}年{m}月{d}日")
