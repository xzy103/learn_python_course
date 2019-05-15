# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.5.15


def judge(s, start, end):
    if start >= end:
        return f'{s}是回文'

    if s[start] == s[end]:
        return judge(s, start+1, end-1)
    else:
        return f'{s}不是回文'


string = input('请输入一个字符串：')
result = judge(string, 0, len(string)-1)
print(result)
