# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/6/3  20:31 
# 名称：基因文件格式转换.PY
# 工具：PyCharm
import sys


class FileConvert:
	def __init__(self, length: int = None):
		self.file_path = sys.argv[1]
		self.output_path = sys.argv[2]
		self.length = length
	
	def gff3_to_gtf(self):
		pass
	
	def seq_to_fasta(self):
		pass
	
	def geo_to_fasta(self):
		i: int = 0
		j: int = 1
		output_file = open(self.output_path + 'fasta', 'w')
		with open(self.file_path, 'r') as f:
			if self.length is None:
				print("正在将geo序列转换成FASTA文件...")
			elif self.length is not None:
				print(f"正在将长度大于{self.length}的geo序列转换成FASTA文件...")
			for line in f:
				if i >= 4:
					seq = line.split('\t')
					sequence = seq[0]
					length = int(seq[1])
					count = int(seq[2])
					if self.length is None:
						output_file.write(">read_" + str(j) + "@" + str(count) + '\n')
						output_file.write(sequence + '\n')
						j += 1
					elif length > self.length:
						output_file.write(">read_" + str(j) + "@" + str(count) + '\n')
						output_file.write(sequence + '\n')
						j += 1
				else:
					i += 1
		output_file.close()
	
	def genbank_to_fasta(self):
		flag: bool = False
		# 打开新建fasta文件准备写入
		output_file = open(self.output_path + 'fasta', 'w')
		# 打开gb文件，准备读取序列信息并写入fasta文件
		with open(self.file_path, 'r') as f:
			# 逐行扫描
			for line in f:
				# 如果是ACCESSION行，则写入fasta文件作为序列标题
				if line[0:9] == 'ACCESSION':
					output_file.writelines('>' + line.split()[1] + '\n')
				# 如果是ORIGIN行，代表是序列
				elif line[0:6] == 'ORIGIN':
					flag = True
				elif flag is True:
					# 通过空格符（空格 换行 制表）对字符串进行切片
					s = line.split()
					# 非空切片字符打印
					if s:
						# print(s)
						# 去掉列表首个元素（数字序号）后，连接所有元素即为完整序列按行写入fasta文件
						seq = ''.join(s[1:])
						output_file.writelines(seq.upper() + '\n')
		output_file.close()


if __name__ == '__main__':
	pass
