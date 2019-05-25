# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.28


import csv


class Contacts:
    def __init__(self, id_, name, Tel, mail, unit):
        self.id = id_
        self.name = name
        self.Tel = Tel
        self.mail = mail
        self.unit = unit  # 工作单位


filename = 'ex2-3.contacts.csv'
with open(filename, 'r', encoding='utf-8') as fr:
    contactsls = csv.reader(fr)
    next(contactsls)
    contacts = []
    for s in contactsls:
        id_, name, Tel, mail, unit = s[0], s[1], s[2], s[3], s[4]
        contact = Contacts(id_, name, Tel, mail, unit)
        contacts.append(contact)


# 顺序查找法
def find_by_mail1(contacts, mail_key):
    """
    在contacts这个对象列表中查找mail等于mail_key的元素
    :param contacts: contacts对象列表
    :param mail_key: 要查找的mail关键字
    :return: 该用户的信息对象，没有找到返回-1
    """
    for i in range(len(contacts)):
        if contacts[i].mail == mail_key:
            return contacts[i]
    return -1


# 折半查找法
def find_by_mail2(contacts, mail_key):
    """
    在contacts这个对象列表中查找mail等于mail_key的元素
    :param contacts: contacts对象列表
    :param mail_key: 要查找的mail关键字
    :return: 该用户的信息对象，没有找到返回-1
    """
    start, end = 0, len(contacts) - 1
    while start <= end:
        mid = (start+end)//2
        s = contacts[mid]
        if s.mail == mail_key:
            return s
        elif s.mail < mail_key:
            start = mid+1
        else:
            end = mid-1
    return -1


fmail = input('请输入要查找的联系人邮箱：')
uinfo = find_by_mail1(contacts, fmail)
if uinfo == -1:
    print(f'找不到邮箱为{fmail}的联系人')
else:
    print('顺序查找的结果为↓')
    print(f'id:{uinfo.id}\nname:{uinfo.name}\nTel:{uinfo.Tel}\nmail:{uinfo.mail}\nunit:{uinfo.unit}\n')


uinfo = find_by_mail2(contacts, fmail)
if uinfo == -1:
    print(f'找不到邮箱为{fmail}的联系人')
else:
    print('二分查找的结果为↓')
    print(f'id:{uinfo.id}\nname:{uinfo.name}\nTel:{uinfo.Tel}\nmail:{uinfo.mail}\nunit:{uinfo.unit}')
