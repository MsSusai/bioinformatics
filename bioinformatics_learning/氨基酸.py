# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/6/1  20:11 
# 名称：animo.PY
# 工具：PyCharm
import re


class Animo:
	def __init__(self, seq: str):
		self.seq = seq
		# self.animo = {
		# 	'Gly': 'G', 'Ala': 'A', 'Val': 'V',
		# 	'Leu': 'L', 'Ile': 'I', 'Phe': 'F',
		# 	'Trp': 'W', 'Tyr': 'Y', 'Asp': 'D',
		# 	'Asn': 'N', 'Glu': 'E', 'Lys': 'K',
		# 	'Gln': 'Q', 'Met': 'M', 'Ser': 'S',
		# 	'Thr': 'T', 'Cys': 'C', 'Pro': 'P',
		# 	'His': 'H', 'Arg': 'R',
		# }
		self.animo_three = ['Gly', 'Ala', 'Val', 'Leu',
		                    'Ile', 'Phe', 'Trp', 'Tyr',
		                    'Asp', 'Asn', 'Glu', 'Lys',
		                    'Gln', 'Met', 'Ser', 'Thr',
		                    'Cys', 'Pro', 'His', 'Arg']
		self.animo_one = ['G', 'A', 'V', 'L',
		                  'I', 'F', 'W', 'Y',
		                  'D', 'N', 'E', 'K',
		                  'Q', 'M', 'S', 'T',
		                  'C', 'P', 'H', 'R']
	
	def is_animo(self) -> bool:
		flag = True
		if self.seq.isupper() is False:
			split = re.findall(r'.{3}', self.seq)  # 分割为三个三个一组
			for i in split:
				if i.lower().title() in self.animo_three:
					continue
				else:
					flag = False
					break
		else:
			if self.seq.isupper() is True:
				for i in self.seq:
					if i in self.animo_one:
						continue
					else:
						flag = False
						break
		return flag
	
	def one_to_three(self) -> str:
		try:
			triple = [self.animo_three[self.animo_one.index(i)] for i in self.seq]
		except Exception:
			raise "请检查氨基酸输入是否正确！格式为：‘LWTLH’"
		return ''.join(triple)
	
	def three_to_one(self) -> str:
		try:
			split = re.findall(r'.{3}', self.seq)  # 分割为三个三个一组
			single = [self.animo_one[self.animo_three.index(i)] for i in split]
		except Exception:
			raise "请检查氨基酸输入是否正确！格式为：‘LeuTrpThrLeuHis’"
		return ''.join(single)
	
	def percent(self) -> str:
		alk: int = 0
		acid: int = 0
		if self.is_animo():
			if self.seq.isupper() is False:  # 转换三个字母为一个字母
				self.seq = self.three_to_one()
			for animo in self.seq:
				if animo == 'R' or animo == 'K' or animo == 'H':
					alk += 1
				elif animo == 'D' or animo == 'E':
					acid += 1
			return f"酸性氨基酸占比{acid / len(self.seq)}，碱性氨基酸占比{alk / len(self.seq)}"
		else:
			raise "请检查氨基酸输入是否正确！"
	
	def calculate(self) -> str:
		if self.is_animo():
			if self.seq.isupper() is False:  # 转换三个字母为一个字母
				self.seq = self.three_to_one()
			value: int = len(self.seq) * 128 - (18 * (len(self.seq) - 1))
			return f"多肽有{len(self.seq)}个氨基酸组成，相对分子量为{value}"
		else:
			raise "请检查氨基酸输入是否正确！"


if __name__ == '__main__':
	animo1 = Animo('AspLeuTrpThrGluArgArgLeuHisPro')
	print(animo1.three_to_one())
	print(animo1.percent())
	print(animo1.calculate())
	# animo2 = Animo('RKDEEERRKKDDLWTLHP')
	# print(animo2.one_to_three())
	# print(animo2.percent())
	# print(animo2.calculate())
	# animo3 = Animo('LWTLHpda')
	# print(animo3.calculate())
	# animo4 = Animo('LeuTRPThrLeHis')
	# print(animo4.calculate())
