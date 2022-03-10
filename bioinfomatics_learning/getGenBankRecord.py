# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/3/10  15:24 
# 名称：getGenBankRecord.PY
# 工具：PyCharm
from Bio import Entrez

Entrez.email = "liuhaorantony@163.com"
handle = Entrez.efetch(db='nucleotide', id='EU490707', rettype='fasta')  # rettype='gb'
print(handle.read())
handle.close()
