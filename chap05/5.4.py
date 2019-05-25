# -*- coding:UTF-8 -*-
# Author:徐熙林-金融162班
# Date:2019.5.15

import pandas as pd

filename = '../chap03/ex2-2.scores.csv'  # 相对路径

with open(filename, mode="r", encoding="utf-8") as file:
    df = pd.read_csv(file)

df["总分"] = df["数学"]+df["语文"]
df.to_csv("./含总分成绩.csv")
