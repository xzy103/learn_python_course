# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.20


import csv


class Contacts:
    def __init__(self, id_, name, Tel, mail, unit):
        self.id = id_
        self.name = name
        self.Tel = Tel
        self.mail = mail
        self.unit = unit  # 工作单位


class Infos:
    def __init__(self, name, Tel, mail):
        self.name = name
        self.Tel = Tel
        self.mail = mail


def read_csv(filename: str):
    with open(filename, 'r', encoding='utf-8') as fr:
        contactsls = csv.reader(fr)
        next(contactsls)
        contacts = []
        for s in contactsls:
            id_, name, Tel, mail, unit = s[0], s[1], s[2], s[3], s[4]
            contact = Contacts(id_, name, Tel, mail, unit)
            contacts.append(contact)
    return contacts


def filter_unit(obj):
    return obj.unit == unit_name


def map_names(obj):
    return obj.name


def map_info(obj):
    return Infos(name=obj.name, Tel=obj.Tel, mail=obj.mail)


unit_name = input('请输入要查询的公司全称：')  # unit_name的作用域是全局的
contacts = read_csv(filename='../chap03/ex2-3.contacts.csv')
units = list(filter(filter_unit, contacts))  # 筛选后的公司列表
namels = list(map(map_names, units))  # 指定公司所有人姓名列表
infos = list(map(map_info, units))
print(f"{unit_name}所有人的姓名为：\n{' '.join(namels)}\n")
print('该公司所有人的<姓名> <手机号> <邮箱>如下')
for s in infos:
    print(s.name, s.Tel, s.mail)
