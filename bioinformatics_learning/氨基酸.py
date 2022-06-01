# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/6/1  20:11 
# 名称：animo.PY
# 工具：PyCharm
import re


class Animo:
	def __init__(self, seq: str):
		self.seq = seq
		self.animo = {
			'Gly': 'G', 'Ala': 'A', 'Val': 'V',
			'Leu': 'L', 'Ile': 'I', 'Phe': 'F',
			'Trp': 'W', 'Tyr': 'Y', 'Asp': 'D',
			'Asn': 'N', 'Glu': 'E', 'Lys': 'K',
			'Gln': 'Q', 'Met': 'M', 'Ser': 'S',
			'Thr': 'T', 'Cys': 'C', 'Pro': 'P',
			'His': 'H', 'Arg': 'R',
		}
	
	def one_to_three(self):
		triple = []
		for i in self.seq:
			triple.append(k for k, v in self.animo.items() if v == i)
		return triple
	
	def three_to_one(self):
		split = re.findall(r'.{3}', self.seq)  # 分割为三个三个一组
		single = [self.animo[i] for i in split]
		return ''.join(single)


if __name__ == '__main__':
	animo1 = Animo('LeuTrpThrLeuHisPro')
	print(animo1.three_to_one())
	animo2 = Animo('LWTLHP')
	print(animo2.one_to_three())
