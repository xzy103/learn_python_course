# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.26


class User:
    def __init__(self, name, times):
        self.name = name
        self.times = times


def premiun(user):
    """
    计算用户的费率
    :param user: 用户对象
    :return: 费率
    """
    if user.times == 0:
        p = 0.85
    elif user.times == 1:
        p = 1.0
    elif user.times == 2:
        p = 1.25
    elif user.times == 3:
        p = 1.5
    elif user.times == 4:
        p = 1.75
    elif user.times >= 5:
        p = 2.0
    else:
        raise ValueError('您的输入有误！')
    return p


users = []
print('>>>>>录入用户信息')
while True:
    name = input('请输入用户姓名<回车结束录入>：')
    if name == '':
        break
    times = int(input('请输入上年出险次数：'))
    user = User(name, times)
    users.append(user)


print('用户\t费率')
for u in users:
    print(f'{u.name}\t{premiun(u):.0%}')
