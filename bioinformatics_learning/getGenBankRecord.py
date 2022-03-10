# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/3/10  15:24 
# 名称：getGenBankRecord.PY
# 工具：PyCharm
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "liuhaorantony@163.com"
handle = Entrez.efetch(db='nucleotide', id='AY286474', rettype='fasta')  # rettype='gb'
# print(handle.read())
seqRecord = SeqIO.read(handle, format='fasta')
with open('datasets/AY286474.fasta', 'w+') as f:
    f.write(seqRecord.format('fasta'))
handle.close()
