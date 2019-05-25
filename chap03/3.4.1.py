# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.4.27


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

print('id,姓名,电话,邮箱,单位')
for s in contacts:
    print(f'{s.id},{s.name},{s.Tel},{s.mail},{s.unit}')
print(f'联系人的数量是{len(contacts)}')
