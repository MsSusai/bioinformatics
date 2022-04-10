# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/4/10  16:44 
# 名称：movefile.PY
# 工具：PyCharm
import shutil
import os

datasets_path = r"C:\Users\sosai\Desktop\HSP70\datasets"
nucleotide_path = r"C:\Users\sosai\Desktop\HSP70\HSP70_sequence\nucleotide"
protein_path = r"C:\Users\sosai\Desktop\HSP70\HSP70_sequence\protein"

for dataset_name in os.listdir(datasets_path):
    nucleotide_seq = datasets_path + fr"\{dataset_name}" + r"\ncbi_dataset\data\gene.fna"
    protein_seq = datasets_path + fr"\{dataset_name}" + r"\ncbi_dataset\data\protein.faa"
    shutil.copyfile(nucleotide_seq, nucleotide_path + fr"\{dataset_name}.fasta")
    shutil.copyfile(protein_seq, protein_path + fr"\{dataset_name}.fasta")
