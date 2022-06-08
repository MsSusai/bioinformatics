# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/6/8  19:36 
# 名称：biopython.PY
# 工具：PyCharm
from Bio import SeqIO

for seq in SeqIO.parse('datasets/newNAC.fasta', 'fasta'):
	g = seq.seq.count('G')
	c = seq.seq.count('C')
	print(f"{seq.id}    {len(seq.seq)}    {(g + c) / len(seq.seq)}")
