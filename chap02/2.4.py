# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.3.28

i = 0
while True:
    score = int(input("请输入分数(输入-1结束)："))
    if score == -1:
        break
    elif 0 <= score < 60:
        i += 1

print(f"共有{i}人不及格！")
