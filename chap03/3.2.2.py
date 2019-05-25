# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.27

import csv


class UserInfo:
    def __init__(self, id_, username, name, gender, Tel, password, mail, rank):
        self.id = id_
        self.username = username
        self.name = name
        self.gender = gender
        self.Tel = Tel
        self.password = password
        self.mail = mail
        self.rank = rank  # 用户级别


filename = 'ex2-1.用户信息.csv'
with open(filename, 'r', encoding='utf-8') as file:
    userls = csv.reader(file)
    next(userls)
    users = []
    for u in userls:
        id_, username, name, gender, Tel, password, mail, rank = u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7]
        user = UserInfo(id_, username, name, gender, Tel, password, mail, rank)
        users.append(user)

vips = []  # 新建用于存放vip用户的列表
for s in users:
    if s.rank == 'VIP':
        vips.append(s)

# 写入到vip.csv文件
with open('vip.csv', 'w', encoding='utf-8') as fw:
    fw.write('id,账号,姓名,性别,电话号码,密码,邮箱,用户级别\n')
    for v in vips:
        fw.write(f'{v.id},{v.username},{v.name},{v.gender},{v.Tel},{v.password},{v.mail},{v.rank}\n')
print('用户信息已写入到[vip.csv]')
