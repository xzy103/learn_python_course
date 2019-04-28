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


with open('ex2-1.用户信息.csv', 'r', encoding='utf-8') as file:
    userls = csv.reader(file)
    next(userls)
    users = []
    for u in userls:
        id, username, name, gender, Tel, password, mail, rank = u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7]
        user = UserInfo(id, username, name, gender, int(Tel), password, mail, rank)
        users.append(user)


def find_by_name(users, name_key):
    """
    在users这个对象列表中查找name等于name_key的元素
    :param users: users对象列表
    :param name_key: 要查找的name关键字
    :return: 该用户的信息对象，没有找到返回-1
    """
    for i in range(len(users)):
        if users[i].name == name_key:
            return users[i]
    return -1


def find_by_Tel(users, Tel_key):
    """
    在users这个对象列表中查找Tel等于Tel_key的元素
    :param users: users对象列表
    :param name_key: 要查找的Tel关键字
    :return: 该用户的信息对象，没有找到返回-1
    """
    start, end = 0, len(users)-1
    while start <= end:
        mid = (start+end)//2
        s = users[mid]
        if s.Tel == Tel_key:
            return s
        elif s.Tel < Tel_key:
            start = mid+1
        else:
            end = mid-1
    return -1


name = input('请输入要查找的用户姓名：')
uinfo = find_by_name(users, name)
if uinfo == -1:
    print(f'找不到姓名为{name}的用户')
else:
    print(f'id:{uinfo.id} username:{uinfo.username} name:{uinfo.name} gender:{uinfo.gender} '
          f'Tel:{uinfo.Tel} password:{uinfo.password} mail:{uinfo.mail} rank:{uinfo.rank}')


Tel = int(input('请输入要查找的用户电话号码：'))
uinfo = find_by_Tel(users, Tel)
if uinfo == -1:
    print(f'找不到电话号码为{Tel}的用户')
else:
    print(f'id:{uinfo.id} username:{uinfo.username} name:{uinfo.name} gender:{uinfo.gender} '
          f'Tel:{uinfo.Tel} password:{uinfo.password} mail:{uinfo.mail} rank:{uinfo.rank}')

