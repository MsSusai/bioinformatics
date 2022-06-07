# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/6/5  21:34 
# 名称：wheat.PY
# 工具：PyCharm
import pandas as pd
from scipy import stats

wheat = pd.read_csv(r"wheat.CSV", encoding="GBK")
# print(wheat)
data = []
datalist = []

for i in range(0, 600, 6):
	data.append(wheat["height"][i:i + 3])
# print(wheat.describe())

for j in data:
	datalist.append(j.values)
col = [i for i in range(100)]
row = ["one", "two", "three"]
frame = pd.DataFrame(data=datalist, columns=row, index=col)

print(frame)
