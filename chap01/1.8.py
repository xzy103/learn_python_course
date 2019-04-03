# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.3.21


def get_tax(income):
    """
    通过收入获取应缴税额
    :param income:收入数额
    :return:应缴个人所得税额
    """
    if income > 85000:
        tax = (income-5000)*0.45-15160
    elif income > 60000:
        tax = (income-5000)*0.35-7160
    elif income > 40000:
        tax = (income-5000)*0.3-4410
    elif income > 30000:
        tax = (income-5000)*0.25-2660
    elif income > 17000:
        tax = (income-5000)*0.2-1410
    elif income > 8000:
        tax = (income-5000)*0.1-210
    elif income > 5000:
        tax = (income-5000)*0.03
    elif income >= 0:
        tax = 0
    else:
        raise ValueError("您的收入数值非法！")
    return tax


income_raw = float(input("请输入税前收入："))
person_tax = get_tax(income_raw)
print(f"您应缴的个人所得税为{round(person_tax, 2)}元。")
