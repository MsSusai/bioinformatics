# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/5/30  21:05 
# 名称：基因号处理.PY
# 工具：PyCharm

# 去掉RefSeq基因号后面的.[0-9]
import re

newf = open("datasets/SRR_diff_genenum.txt", "a+")

with open("datasets/SRR_diff_4.csv", 'r') as f:
    find = re.findall("N._[0-9]*\\.[0-9]", f.read())
    for line in find:
        newf.write(line[:-2]+"\n")

newf.close()

