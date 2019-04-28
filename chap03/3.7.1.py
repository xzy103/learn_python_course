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


def find_min(users, start, end):
    """
    找到从users[start]到users[end]中邮箱最小的下标
    :param users: 用户对象列表
    :param start: 开始下标
    :param end: 结束下标
    :return: 最小邮箱的下标
    """
    min = start
    for i in range(start, end):
        if users[i].mail < users[min].mail:
            min = i
    return min


def select_sort(users):
    """
    选择排序
    :param users: 需要排序的对象列表
    :return: None
    """
    n = len(users)
    for i in range(n):
        t = find_min(users, i, n)
        users[i], users[t] = users[t], users[i]


if __name__ == "__main__":
    with open('ex2-1.用户信息.csv', 'r', encoding='utf-8') as file:
        userls = csv.reader(file)
        next(userls)
        users = []
        for u in userls:
            id, username, name, gender, Tel, password, mail, rank = u[0], u[1], u[2], u[3], u[4], u[5], u[6], u[7]
            user = UserInfo(id, username, name, gender, Tel, password, mail, rank)
            users.append(user)

    select_sort(users)
    print('邮箱, id, 账号, 姓名, 性别, 电话号码, 密码, 用户级别')
    for s in users:
        print(s.mail, s.id, s.username, s.name, s.gender, s.Tel, s.password, s.rank)
