# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.28


import csv


class Contacts:
    def __init__(self, id, name, Tel, mail, unit):
        self.id = id
        self.name = name
        self.Tel = Tel
        self.mail = mail
        self.unit = unit


def read_csv(filename: str):
    """
    从csv文件中读取联系人信息分别以邮箱和电话号码为关键字存入字典
    :param filename: 文件名
    :return: 以邮箱和电话号码为关键字的字典
    """
    maildict = {}  # 定义一个字典
    teldict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        contactsls = csv.reader(file)
        next(contactsls)
        for s in contactsls:
            id, name, Tel, mail, unit = s[0], s[1], s[2], s[3], s[4]
            contact = Contacts(id, name, Tel, mail, unit)
            maildict[mail] = contact
            teldict[Tel] = contact
    return maildict, teldict


getinfo = input('请输入要查找人的邮箱或电话号码：')
maildict, teldict = read_csv('ex2-3.contacts.csv')
if getinfo in maildict:
    s = maildict[getinfo]
    print(f'{s.id},{s.name},{s.Tel},{s.mail},{s.unit}')
elif getinfo in teldict:
    s = teldict[getinfo]
    print(f'{s.id},{s.name},{s.Tel},{s.mail},{s.unit}')
else:
    print("查无此人！")


corps = set()
values = maildict.values()
for s in values:
    corps.add(s.unit)
print(f'共有{len(corps)}家公司')
print(corps)  # 公司集合


newdict = {}
contacts = list(values)  # contacts是未经筛选的联系人信息列表，每个联系人的信息是一个对象(类)
for corp in corps:
    lst = []  # 初始化一个空列表用于存放符合要求的联系人(类)信息
    for s in contacts:
        if s.unit == corp:  # 如果这个联系人的单位是这家公司
            lst.append(s)  # s是一个联系人对象(类)
    newdict[corp] = lst  # 键为公司名，值为联系人列表


corpname = input('请输入公司名：')
try:
    names = newdict.get(corpname)
    for name in names:
        print(name.__dict__)
except:
    raise ValueError('查无此公司！')
