# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/4/28  15:56 
# 名称：Co-expression analysis.PY
# 工具：PyCharm
from scipy.stats import pearsonr

gene1 = [12.1, 40.9, 11.2, 101.4, 56.6, 44.1, 8.1, 388]
gene2 = [17.6, 46.7, 16.4, 94.6, 769.4, 47.8, 12.4, 512]
gene3 = [133, 367, 124, 998.5, 534.1, 341.2, 72.1, 3321.5]
gene4 = [90.1, 187.5, 84.22, 401.1, 3673.3, 167.2, 56.5, 483.1]
pcc1, pvalue1 = pearsonr(gene1, gene2)
pcc2, pvalue2 = pearsonr(gene1, gene3)
pcc3, pvalue3 = pearsonr(gene1, gene4)
pcc4, pvalue4 = pearsonr(gene2, gene3)
pcc5, pvalue5 = pearsonr(gene2, gene4)
pcc6, pvalue6 = pearsonr(gene3, gene4)
print(pcc1, pcc2, pcc3, pcc4, pcc5, pcc6)


def tau(gene):
    n = 0
    for i in gene:
        n += 1 - (i / max(gene))
    return n / (len(gene) - 1)


print(tau(gene1))
print(tau(gene2))
print(tau(gene3))
print(tau(gene4))
