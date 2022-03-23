# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/3/18  16:46 
# 名称：blast.PY
# 工具：PyCharm
# Blast ZFP182 protein sequence with biopython NCBIWWW
from Bio.Blast import NCBIWWW

ZFP182_protein_result = NCBIWWW.qblast('blastp', 'nr', 'AAP42461', format_type='xml')
with open('datasets/AAP42461.xml', 'w') as f:
    f.write(ZFP182_protein_result.read())
