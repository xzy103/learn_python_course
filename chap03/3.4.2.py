# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.27


import csv


class Contacts:
    def __init__(self, id, name, Tel, mail, unit):
        self.id = id
        self.name = name
        self.Tel = Tel
        self.mail = mail
        self.unit = unit


with open('ex2-3.contacts.csv', 'r', encoding='utf-8') as fr:
    contactsls = csv.reader(fr)
    next(contactsls)
    contacts = []
    for s in contactsls:
        id, name, Tel, mail, unit = s[0], s[1], s[2], s[3], s[4]
        contact = Contacts(id, name, Tel, mail, unit)
        contacts.append(contact)

print('id,姓名,电话,邮箱,单位')
print('以下是所有上海易利生物科技有限公司的联系人')
for s in contacts:
    if s.unit == '上海易利生物科技有限公司':
        print(f'{s.id},{s.name},{s.Tel},{s.mail},{s.unit}')
print()

print('以下是所有使用雅虎邮箱的联系人')
for s in contacts:
    if '@yahoo.com' in s.mail:
        print(f'{s.id},{s.name},{s.Tel},{s.mail},{s.unit}')
print()

# 移动号段 134,135,136,137,138,139,147,150,151,152,157,158,159,182,183,187,188
print('以下是所有使用中国移动手机号的联系人')
for s in contacts:
    if int(s.Tel[:3]) in [134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 182, 183, 187, 188]:
        print(f'{s.id},{s.name},{s.Tel},{s.mail},{s.unit}')
