# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.28


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
    """
    从csv文件中读取用户信息以账号为关键字存入字典
    :param filename: 文件名
    :return: 以账号为关键字的字典
    """
    usersdict = {}  # 定义一个字典
    with open(filename, 'r', encoding='utf-8') as file:
        userls = csv.reader(file)
        next(userls)
        for u in userls:
            id_, username, name, gender, Tel, password, mail, rank = u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7]
            user = UserInfo(id_, username, name, gender, Tel, password, mail, rank)
            usersdict[username] = user  # 字典的键为用户名  值为用户属性
    return usersdict


username = input("请输入要查找的账号：")
readfile = 'ex2-1.用户信息.csv'
usersdict = read_csv(readfile)
if username in usersdict:
    s = usersdict[username]  # 获取字典中键为username的值信息
    print(s.id, s.username, s.name, s.gender, s.Tel, s.password, s.mail, s.rank)
else:
    print('查无此人！')


ranks = set()  # 新建一个集合
values = usersdict.values()  # 获取字典中所有值
for s in values:
    ranks.add(s.rank)  # 将所有值中的等级属性加入到ranks集合中
print(f'共有有{len(ranks)}种用户级别，即{ranks}')
