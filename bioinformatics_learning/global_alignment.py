# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/3/27  22:29 
# 名称：global_alignment.PY
# 工具：PyCharm
from Bio import pairwise2
from Bio import SeqIO

seq1 = SeqIO.read(open(r"C:\Users\sosai\Desktop\ZFP182 orthologue\sequence (3).txt"), 'fasta')
seq2 = SeqIO.read(open(r"datasets\AY286474.fasta"), 'fasta')
# print(seq2)
# print("-----------------")
# print(seq1)
alignment = pairwise2.align.globalxx(seq1, seq2)
print(pairwise2.format_alignment(*alignment[0]))
