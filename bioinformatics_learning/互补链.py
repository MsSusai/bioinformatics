# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/6/1  19:24 
# 名称：互补链.PY
# 工具：PyCharm
class Sequence:
	def __init__(self, seq: str):
		self.seq = seq
	
	def comp(self):
		lib = {
			'N': 'N',
			'A': 'T',
			'T': 'A',
			'C': 'G',
			'G': 'C',
		}
		newSeq = ''
		for i in self.seq:
			newSeq += lib[i]
		return newSeq
	
	def comp_reverse(self):
		lib = {
			'N': 'N',
			'A': 'T',
			'T': 'A',
			'C': 'G',
			'G': 'C',
		}
		newSeq = ''
		for i in self.seq:
			newSeq += lib[i]
		return newSeq[::-1]
	
	def length(self):
		return len(self.seq)
	
	def gc_value(self):
		g = self.seq.count('G')
		c = self.seq.count('C')
		return (g + c) / len(self.seq)
	
	def RNA_to_DNA(self):
		return self.seq.replace('U', 'T')
	
	def DNA_to_RNA(self):
		return self.seq.replace('T', 'U')


if __name__ == '__main__':
	sequence = Sequence("AATTCCGG")
	print(sequence.comp())
	print(sequence.comp_reverse())
	print(sequence.length())
	print(sequence.gc_value())
	print(sequence.RNA_to_DNA())
	print(sequence.DNA_to_RNA())
