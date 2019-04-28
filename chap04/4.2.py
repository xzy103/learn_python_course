# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.28


import csv


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


def read_csv(filename: str):
    with open(filename, 'r', encoding='utf-8') as file:
        userls = csv.reader(file)
        next(userls)
        users = []
        for u in userls:
            id, username, name, gender, Tel, password, mail, rank = u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7]
            user = UserInfo(id, username, name, gender, Tel, password, mail, rank)
            users.append(user)
    return users


def key_username(user):
    return user.username


def key_mail(user):
    return user.mail


if __name__ == '__main__':
    users = read_csv(filename='../chap03/ex2-1.用户信息.csv')
    print('按账号排序...')
    print('id, 账号, 姓名, 性别, 电话号码, 密码, 邮箱, 用户级别')
    users = sorted(users, key=key_username)
    for s in users:
        print(s.id, s.username, s.name, s.gender, s.Tel, s.password, s.mail, s.rank)

    print()
    print('按邮箱排序...')
    users = sorted(users, key=key_mail)
    for s in users:
        print(s.id, s.username, s.name, s.gender, s.Tel, s.password, s.mail, s.rank)
