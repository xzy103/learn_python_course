# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.3.21


def discount(money):
    """
    根据购物金额得出折扣方式以及计算折扣价
    :param money: 购物金额
    :return: 折扣方式及折扣价
    """
    # 满减方式的价格
    if money >= 200:
        pay_sub = money-30
    elif money > 0:
        pay_sub = money
    else:
        raise ValueError("金额不能小于零！")

    # 折扣方式的价格
    pay_sale = money*0.9

    # 两种方式进行对比
    if pay_sale < pay_sub:
        return '打9折', round(pay_sale, 2)
    else:
        return '满200减30', round(pay_sub, 2)


if __name__ == '__main__':
    money_raw = float(input("请输入购物金额："))
    way, pay = discount(money_raw)
    print(way, pay, sep='，')
