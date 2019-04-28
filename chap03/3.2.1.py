# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.26

import csv
from easygraphics import dialog


class UserInfo:
    def __init__(self, id, username, name, gender, Tel, password, mail, rank):
        self.id = id
        self.username = username
        self.name = name
        self.gender = gender
        self.Tel = Tel
        self.password = password
        self.mail = mail
        self.rank = rank


with open('ex2-1.用户信息.csv', 'r', encoding='utf-8') as file:
    userls = csv.reader(file)
    next(userls)
    users = []
    for u in userls:
        id, username, name, gender, Tel, password, mail, rank = u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7]
        user = UserInfo(id, username, name, gender, Tel, password, mail, rank)
        users.append(user)


print('id, 账号, 姓名, 性别, 电话号码, 密码, 邮箱, 用户级别')
for s in users:
    print(s.id, s.username, s.name, s.gender, s.Tel, s.password, s.mail, s.rank)

dialog.show_objects(users, title='用户信息', width=1500, height=900)