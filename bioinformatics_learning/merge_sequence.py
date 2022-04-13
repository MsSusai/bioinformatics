# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/4/13  22:13 
# 名称：merge_sequence.PY
# 工具：PyCharm
import os

nucleotide_path = r"C:\Users\sosai\Desktop\HSP70\HSP70_sequence\nucleotide"
protein_path = r"C:\Users\sosai\Desktop\HSP70\HSP70_sequence\protein"

merge_file = open("merge.fasta", "w")
for seq_name in os.listdir(nucleotide_path):
    file = open(nucleotide_path + fr"\{seq_name}", "r")
    merge_file.write(file.read())
    file.close()
merge_file.close()

for seq_name in os.listdir(protein_path):
    file = open(protein_path + fr"\{seq_name}", "r")
    merge_file.write(file.read())
    file.close()
merge_file.close()
