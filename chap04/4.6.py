# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.29


import csv


class UserInfo:
    def __init__(self, id_, username, name, gender, Tel, password, mail, rank):
        self.id = id_
        self.username = username  # 用户名
        self.name = name  # 用户姓名
        self.gender = gender
        self.Tel = Tel
        self.password = password
        self.mail = mail
        self.rank = rank  # 用户等级


def read_csv(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        userls = csv.reader(file)
        next(userls)
        users = []
        for u in userls:
            id_, username, name, gender, Tel, password, mail, rank = u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7]
            user = UserInfo(id_, username, name, gender, Tel, password, mail, rank)
            users.append(user)
    return users


def filter_mail(obj):
    return 'hotmail' in obj.mail


def filter_vip(obj):
    return 'VIP' in obj.rank


users = read_csv(filename='../chap03/ex2-1.用户信息.csv')  # 相对路径
hotmails = list(filter(filter_mail, users))
vips = list(filter(filter_vip, hotmails))
print(f'使用hotmail邮箱的用户个数为{len(hotmails)}，其中vip用户个数为{len(vips)}')
