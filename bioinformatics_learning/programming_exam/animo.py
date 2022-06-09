# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/6/1  20:11 
# 名称：animo.PY
# 工具：PyCharm
import re


class Animo:
	def __init__(self, seq: str, name: str = None, species: str = None):
		self.seq = seq
		self.name = name
		self.species = species
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
	
	def _animo_convert(self) -> str:  # 将序列转换为单个字母的氨基酸序列
		if self.is_animo():
			if self.seq.isupper() is False:  # 转换三个字母为一个字母
				animo_seq = self.three_to_one()
				return animo_seq
		else:
			raise "请检查氨基酸输入是否正确！"
	
	def is_animo(self) -> bool:  # 序列是否为氨基酸
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
	
	def one_to_three(self) -> str:  # 一位变三位
		try:
			triple = [self.animo_three[self.animo_one.index(i)] for i in self.seq]
		except Exception:
			raise "请检查氨基酸输入是否正确！格式为：‘LWTLH’"
		return ''.join(triple)
	
	def three_to_one(self) -> str:  # 三位变一位
		try:
			split = re.findall(r'.{3}', self.seq)  # 分割为三个三个一组
			single = [self.animo_one[self.animo_three.index(i)] for i in split]
		except Exception:
			raise "请检查氨基酸输入是否正确！格式为：‘LeuTrpThrLeuHis’"
		return ''.join(single)
	
	def calculate_percent(self) -> str:  # 计算酸碱氨基酸所占比例
		alk: int = 0
		acid: int = 0
		for animo in self._animo_convert():
			if animo == 'R' or animo == 'K' or animo == 'H':
				alk += 1
			elif animo == 'D' or animo == 'E':
				acid += 1
		return f"酸性氨基酸占比{acid / len(self.seq)}，碱性氨基酸占比{alk / len(self.seq)}"
	
	def calculate_length(self) -> str:  # 计算序列长度
		animo_seq = self._animo_convert()
		return f"多肽有{len(animo_seq)}个氨基酸组成"
	
	def calculate_Mr(self) -> str:  # 计算相对分子量
		animo_seq = self._animo_convert()
		value: int = len(animo_seq) * 128 - (18 * (len(animo_seq) - 1))
		return f"多肽相对分子量为{value}"
	
	def calculate_num(self) -> dict:  # 计算序列各个氨基酸含量
		animo_dict = {}
		for animo in self._animo_convert():
			animo_dict[animo] = animo_dict.get(animo, 0) + 1
		return animo_dict
	
	def __str__(self):
		return f"名称：{self.name}  物种：{self.species}"


if __name__ == '__main__':
	animo1 = Animo('AspLeuTrpThrGluArgArgLeuHisPro', name='bZIP', species='human')
	print(animo1)
	print(animo1.is_animo())
	print(animo1.three_to_one())
	print(animo1.calculate_percent())
	print(animo1.calculate_length())
	print(animo1.calculate_num())
	print(animo1.calculate_Mr())
	# animo2 = Animo('RKDEEERRKKDDLWTLHP')
	# print(animo2.one_to_three())
	# print(animo2.percent())
	# print(animo2.calculate())
	# animo3 = Animo('LWTLHpda')
	# print(animo3.calculate())
	# animo4 = Animo('LeuTRPThrLeHis')
	# print(animo4.calculate())
	...

'''
animo1 = Animo('AspLeuTrpThrGluArgArgLeuHisPro', name='bZIP', species='human')
print(animo1)
print(animo1.is_animo())
print(animo1.three_to_one())
print(animo1.calculate_percent())
print(animo1.calculate_length())
print(animo1.calculate_num())
print(animo1.calculate_Mr())

运行结果：
名称：bZIP  物种：human
True
DLWTERRLHP
酸性氨基酸占比0.06666666666666667，碱性氨基酸占比0.1
多肽有10个氨基酸组成
{'D': 1, 'L': 2, 'W': 1, 'T': 1, 'E': 1, 'R': 2, 'H': 1, 'P': 1}
多肽相对分子量为1118

输入错误氨基酸序列
animo3 = Animo('LWTLHpda')
print(animo3.calculate_Mr())

Traceback (most recent call last):
  File "E:/Code/bioinformatics/bioinformatics_learning/animo.py", line 103, in <module>
    print(animo3.calculate())
  File "E:/Code/bioinformatics/bioinformatics_learning/animo.py", line 90, in calculate
    raise "请检查氨基酸输入是否正确！"
TypeError: exceptions must derive from BaseException

'''
