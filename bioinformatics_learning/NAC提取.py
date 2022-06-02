# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/6/2  21:25 
# 名称：NAC提取.PY
# 工具：PyCharm
import re

# anac = open("anac.txt", "w+")
# with open(r"datasets/NAC.txt", "r") as f:
# 	seqa = re.findall("At.{7}", f.read())
# for line in seqa:
# 	anac.write(line + "\n")
# anac.close()
file = open("datasets/newNAC.fasta", "w")

with open("datasets/NAC.fasta", "r") as f:
	a = f.readlines()
	anac1 = re.findall("ANAC[0-9]{3}|anac[0-9]{3}", ''.join(a))
	loc = ''
	i = 0
	for line in a:
		if '>' in line:
			loc = '>' + anac1[i]
			i += 1
			file.write(loc+'\n')
		else:
			file.write(line)
