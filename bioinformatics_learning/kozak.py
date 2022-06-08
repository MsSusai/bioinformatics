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
	find = re.match("[AT]..ATGG", str(seq.seq)[index - 3:index + 4])
	if find is not None:
		kozak += 1
		print(f">{seq.id}  {kozak}/{gene}  kozak find!  "
		      f"index is {index - 3}-{index + 4}  kozak seq is {find.string}")
print(f"Total kozak are {kozak}, genes are {gene}")

'''
运行结果
.........
>NR_144274.1  10131/53809  kozak find!  index is 102-109  kozak seq is TTCATGG
>NR_144280.1  10132/53815  kozak find!  index is 164-171  kozak seq is TTTATGG
>NR_144284.1  10133/53819  kozak find!  index is 48-55  kozak seq is TTGATGG
>NR_144291.1  10134/53826  kozak find!  index is 35-42  kozak seq is TCGATGG
Total kozak are 10134, genes are 53827
'''
