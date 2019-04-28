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


def read_csv(filename='ex2-1.用户信息.csv'):
    """
    从csv文件中读取用户信息以账号为关键字存入字典
    :param filename: 文件名
    :return: 以账号为关键字的字典
    """
    usersdict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        userls = csv.reader(file)
        next(userls)
        for u in userls:
            id, username, name, gender, Tel, password, mail, rank = u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7]
            user = UserInfo(id, username, name, gender, Tel, password, mail, rank)
            usersdict[username] = user
    return usersdict


id_ = input("请输入要查找的账号：")
usersdict = read_csv()
if id_ in usersdict:
    s = usersdict[id_]
    print(s.id, s.username, s.name, s.gender, s.Tel, s.password, s.mail, s.rank)

ranks = set()
values = usersdict.values()
for s in values:
    ranks.add(s.rank)
print(f'共有有{len(ranks)}种用户级别，即', ranks)
