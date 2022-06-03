# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/6/3  16:52 
# 名称：kozak.PY
# 工具：PyCharm

# 寻找拟南芥kozak序列
from Bio import SeqIO
import re

kozak: int = 0
gene: int = 0

for seq in SeqIO.parse(r"E:\资料\计算机\生物信息学\Arabidopsis thaliana\GCF_000001735.4_TAIR10.1_rna.fna", "fasta"):
	gene += 1
	index = str(seq.seq).find('ATG')
	# print(str(seq.seq)[index - 3:index + 4])
	find = re.match("[AG]..ATGG", str(seq.seq)[index - 3:index + 4])
	if find is not None:
		kozak += 1
		print(f"{kozak}/{gene}  kozak find!")
print(f"Total kozak are {kozak}, genes are {gene}")

'''
运行结果
.........
9934/53799  kozak find!
9935/53804  kozak find!
9936/53825  kozak find!
Total kozak are 9936, genes are 53827
'''
