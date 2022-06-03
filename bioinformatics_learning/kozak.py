# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/6/3  16:52 
# 名称：kozak.PY
# 工具：PyCharm

# 寻找拟南芥kozak序列
from Bio import SeqIO
import re

for seq in SeqIO.parse(r"E:\资料\计算机\生物信息学\Arabidopsis thaliana\GCF_000001735.4_TAIR10.1_rna.fna", "fasta"):
	find = re.findall("[AG]..ATGG", str(seq.seq))
	print(seq.id, len(find))

'''
运行结果


'''
