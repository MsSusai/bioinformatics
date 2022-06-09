# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/6/8  21:10 
# 名称：fasta分析长度与画图.PY
# 工具：PyCharm
from Bio import SeqIO
import matplotlib.pyplot as plt

seq_length: dict = {"0-1000": 0,
                    "1000-1500": 0,
                    "1500-2000": 0,
                    "2000-2500": 0,
                    "2500-3000": 0,
                    "3000-3500": 0,
                    "3500-4000": 0,
                    "4000-4500": 0,
                    "4500-5000": 0,
                    ">5000": 0, }

for seq in SeqIO.parse(r"E:\资料\计算机\生物信息学\Arabidopsis thaliana\GCF_000001735.4_TAIR10.1_rna.fna", "fasta"):
	if 0 <= len(seq.seq) < 1000:
		seq_length['0-1000'] += 1
	elif 1000 <= len(seq.seq) < 1500:
		seq_length['1000-1500'] += 1
	elif 1500 <= len(seq.seq) < 2000:
		seq_length['1500-2000'] += 1
	elif 2000 <= len(seq.seq) < 2500:
		seq_length['2000-2500'] += 1
	elif 2500 <= len(seq.seq) < 3000:
		seq_length['2500-3000'] += 1
	elif 3000 <= len(seq.seq) < 3500:
		seq_length['3000-3500'] += 1
	elif 3500 <= len(seq.seq) < 4000:
		seq_length['3500-4000'] += 1
	elif 4000 <= len(seq.seq) < 4500:
		seq_length['4000-4500'] += 1
	elif 4500 <= len(seq.seq) < 5000:
		seq_length['4500-5000'] += 1
	elif len(seq.seq) >= 5000:
		seq_length['>5000'] += 1

fig = plt.figure(figsize=(15, 10))
plt.bar(seq_length.keys(), seq_length.values(), color='purple', align='center')
plt.grid(True)
plt.tick_params(axis='x', labelsize=13)
plt.tick_params(axis='y', labelsize=15)
plt.ylabel("count", fontsize=20)
plt.xlabel("sequence length(bp)", fontsize=20)

plt.savefig('bar.png')
