# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/6/3  20:31 
# 名称：基因文件格式转换.PY
# 工具：PyCharm
import sys
from Bio import SeqIO


class FileConvert:
	def __init__(self, length: int = None):
		self.file_path = sys.argv[1]
		self.output_path = sys.argv[2]
		self.length = length
	
	def seq_to_fasta(self, normalized=False):
		seq_dict: dict = {}  # 储存对应序列出现次数
		i: int = 1  # 计数
		output_file = open(self.output_path, "w")
		with open(self.file_path, "r") as f:
			for line in f:
				seq_dict[line] = seq_dict.get(line, 0) + 1  # 没有则创造，有则+1
		# 如果没有长度筛选要求
		if self.length is None:
			print("正在将序列文件转换为FASTA文件...")
			if normalized:  # 如果序列读数要均一化
				total_reads = sum(seq_dict.values())  # 序列读数总数
				for k, v in seq_dict.items():
					output_file.write(
						">read_" + str(i) + "@" + str(v) +
						f"_NormalizedValue:{v / total_reads}" + '\n')
					output_file.write(k)
					i += 1
			else:  # 序列读数不用均一化
				for k, v in seq_dict.items():
					output_file.write(">read_" + str(i) + "@" + str(v) + '\n')
					output_file.write(k)
					i += 1
		# 如果有长度筛选要求
		elif self.length is not None:
			print(f"正在将{self.length}bp长度的序列转换为FASTA文件...")
			if normalized:  # 如果序列读数要均一化
				total_reads = sum(seq_dict.values())  # 序列读数总数
				for k, v in seq_dict.items():
					if self.length == len(k):
						output_file.write(
							">read_" + str(i) + "@" + str(v) +
							f"_NormalizedValue:{v / total_reads}" + '\n')
						output_file.write(k)
						i += 1
			else:  # 序列读数不用均一化
				for k, v in seq_dict.items():
					if self.length == len(k):
						output_file.write(">read_" + str(i) + "@" + str(v) + '\n')
						output_file.write(k)
						i += 1
		output_file.close()
	
	def fasta_to_seq(self):
		output_file = open(self.output_path, "w")
		print("正在将fasta文件转换为纯序列文件...")
		for seq in SeqIO.parse(self.file_path, 'fasta'):
			output_file.write(str(seq.seq) + '\n')
		output_file.close()
	
	def geo_to_fasta(self):
		i: int = 0  # 为了跳过geo文件的前四行注释
		j: int = 1  # 对序列进行编号
		output_file = open(self.output_path, 'w')
		with open(self.file_path, 'r') as f:
			if self.length is None:  # 如果没有长度筛选要求
				print("正在将geo序列转换成FASTA文件...")
			elif self.length is not None:  # 如果有长度筛选要求
				print(f"正在将长度大于{self.length}bp的geo序列转换成FASTA文件...")
			for line in f:
				if i >= 4:
					seq = line.split('\t')
					sequence = seq[0]  # 核酸序列
					length = int(seq[1])  # 序列长度
					count = int(seq[2])  # 序列读数
					if self.length is None:  # 没有长度筛选要求
						output_file.write(">read_" + str(j) + "@" + str(count) + '\n')
						output_file.write(sequence + '\n')
						j += 1
					elif length > self.length:  # 长度筛选要求大于某长度
						output_file.write(">read_" + str(j) + "@" + str(count) + '\n')
						output_file.write(sequence + '\n')
						j += 1
				else:
					i += 1
		output_file.close()
	
	def fasta_to_geo(self):
		seq_dict: dict = {}
		output_file = open(self.output_path, "w")
		print("正在将fasta文件转换为geo文件...")
		for seq in SeqIO.parse(self.file_path, 'fasta'):
			seq_dict[seq.seq] = seq_dict.get(seq.seq, 0) + 1
		output_file.write("SEQUENCE\tLENGTH\tCOUNT\n")
		for k, v in seq_dict.items():
			output_file.write(f"{str(k)}\t{len(k)}\t{v}\n")
		output_file.close()
	
	def seq_to_geo(self):
		seq_dict: dict = {}
		output_file = open(self.output_path, "w")
		with open(self.file_path, "r") as f:
			print("正在将纯序列文件转换为geo文件...")
			for seq in f:
				seq_dict[seq] = seq_dict.get(seq, 0) + 1
		output_file.write("SEQUENCE\tLENGTH\tCOUNT\n")
		for k, v in seq_dict.items():
			output_file.write(f"{k}\t{len(k)}\t{v}\n")
		output_file.close()
	
	def geo_to_seq(self):
		i: int = 0  # 为了跳过geo文件的前四行注释
		output_file = open(self.output_path, 'w')
		with open(self.file_path, 'r') as f:
			print("正在将geo文件转换为纯序列文件...")
			for line in f:
				if i >= 4:
					seq = line.split('\t')
					sequence = seq[0]  # 核酸序列
					count = int(seq[2])  # 序列读数
					output_file.write(f"{sequence}\n" * count)
				else:
					i += 1
		output_file.close()
	
	def genbank_to_fasta(self):
		flag: bool = False
		output_file = open(self.output_path, 'w') # 打开新建fasta文件准备写入
		with open(self.file_path, 'r') as f: # 打开gb文件，准备读取序列信息并写入fasta文件
			for line in f:
				if line[0:9] == 'ACCESSION': # 如果是ACCESSION行，则写入fasta文件作为序列标题
					output_file.writelines('>' + line.split()[1] + '\n')
				elif line[0:6] == 'ORIGIN': # 如果是ORIGIN行，代表是序列
					flag = True
				elif flag is True:
					s = line.split() # 通过空格符（空格 换行 制表）对字符串进行切片
					if s: # 非空切片字符打印
						# 去掉列表首个元素（数字序号）后，连接所有元素即为完整序列按行写入fasta文件
						seq = ''.join(s[1:])
						output_file.writelines(seq.upper() + '\n')
		output_file.close()
	
	def gff3_to_gtf(self):
		for line in sys.stdin.readlines():
			# skip comment lines that start with the '#' character
			if line[0] != '#':
				# split line into columns by tab
				data = line.strip().split('\t')
				
				# parse the transcript/gene ID. I suck at using regex, so I usually just do a series of splits.
				transcriptID = data[-1].split('transcript_id')[-1].split(';')[0].strip()[1:-1]
				geneID = data[-1].split('gene_id')[-1].split(';')[0].strip()[1:-1]
				
				# replace the last column with a GFF formatted attributes columns
				# I added a GID attribute just to conserve all the GTF data
				data[-1] = "ID=" + transcriptID + ";GID=" + geneID
				
				# print out this new GFF line
				print("\t".join(data))


if __name__ == '__main__':
	test1_seq = FileConvert()
	# test2_geo = FileConvert()
	# test3_genbank = FileConvert()
	test1_seq.geo_to_seq()
	# test2_geo.geo_to_fasta()
	# test3_genbank.genbank_to_fasta()
	...

'''
test1_seq = FileConvert()
test1_seq.seq_to_fasta()
运行结果：
>read_1@1
TCGCTTGGTGCAGATCGGGAC
>read_2@2
TGACAGAAGAGAGTGAGCAC
>read_3@2
TTGACAGAAGAGAGTGAGCAC
>read_4@1
TGACAGAAGAGAGTGAGCAC

test1_seq = FileConvert()
test1_seq.seq_to_fasta(normalized=True)
运行结果：
>read_1@1_NormalizedValue:0.16666666666666666
TCGCTTGGTGCAGATCGGGAC
>read_2@2_NormalizedValue:0.3333333333333333
TGACAGAAGAGAGTGAGCAC
>read_3@2_NormalizedValue:0.3333333333333333
TTGACAGAAGAGAGTGAGCAC
>read_4@1_NormalizedValue:0.16666666666666666
TGACAGAAGAGAGTGAGCAC


test1_seq = FileConvert(21)
test1_seq.seq_to_fasta()
运行结果：
>read_1@2
TGACAGAAGAGAGTGAGCAC

test1_seq = FileConvert()
test1_seq.fasta_to_seq()
运行结果：
TCGCTTGGTGCAGATCGGGAC
TGACAGAAGAGAGTGAGCAC
TTGACAGAAGAGAGTGAGCAC
TTGACAGAAGAGAGTGAGCAC
TGACAGAAGAGAGTGAGCAC
TGACAGAAGAGAGTGAGCAC


test1_seq = FileConvert(21)
test1_seq.seq_to_fasta(normalized=True)
运行结果：
>read_1@2_NormalizedValue:0.3333333333333333
TGACAGAAGAGAGTGAGCAC


test2_geo = FileConvert()
test2_geo.geo_to_fasta()
运行结果：
>read_1@178813
TCGCTTGGTGCAGATCGGGAC
>read_2@161703
TGACAGAAGAGAGTGAGCAC
>read_3@75782
TTGACAGAAGAGAGTGAGCAC
>read_4@20166
TGAAGCTGCCAGCATGATCTGA
>read_5@7516
TGAAGCTGCCAGCATGATCTA

test1_seq = FileConvert()
test1_seq.fasta_to_geo()
运行结果：
SEQUENCE	LENGTH	COUNT
TCGCTTGGTGCAGATCGGGAC	21	1
TGACAGAAGAGAGTGAGCAC	20	3
TTGACAGAAGAGAGTGAGCAC	21	2


test2_geo = FileConvert(21)
test2_geo.geo_to_fasta()
运行结果：
>read_1@20166
TGAAGCTGCCAGCATGATCTGA


test1_seq = FileConvert()
test1_seq.geo_to_seq()
运行结果：
TCGCTTGGTGCAGATCGGGAC
TGACAGAAGAGAGTGAGCAC
TGACAGAAGAGAGTGAGCAC
TGACAGAAGAGAGTGAGCAC
TTGACAGAAGAGAGTGAGCAC
TTGACAGAAGAGAGTGAGCAC

test3_genbank = FileConvert()
运行结果：
>NM_213806
ATGCAGCAGCCCTTCAATTACCCATACCCCCAAATCTTCTGGGTGGACAGCAGTGCTACC
TCTCCCTGGGCCTCCCCAGGCTCAGTCTTCCCCTGTCCAGCTTCTGTGCCAGGAAGGCCA
GGGCAAAGGAGGCCACCACCACCACCGCCGCCACCGCCACCACCACCAACACTCCTGCCA
TCAAGACCGCTGCCTCCACTGCCACCGCCATCTCTGAAGAAGAAGAGGGACCACAATGCA
GGCCTGTGTCTCCTTGTGATGTTCTTCATGGTTCTGGTGGCCCTGGTTGGATTGGGGCTG
GGGATGTTTCAGCTCTTCCACCTACAGAAGGAGCTGACTGAACTCAGAGAGTCTGCCAGC
CAAAGGCATACAGAATCATCTTTGGAGAAGCAAATAGGTCACCCCAATCTACCCTCTGAG
AAAAAGGAGCTGAGAAAAGTGGCCCACTTAACAGGCAAGCCTAACTCAAGATCCATCCCT
CTGGAATGGGAAGACACCTATGGAATTGCCTTGGTCTCTGGGGTGAAGTATATGAAGGGC
AGCCTTGTGATCAATGACACTGGGCTGTATTTTGTGTATTCCAAAGTGTACTTCCGGGGT
CAGTACTGCAACAACCAGCCCCTGAGTCACAAGGTATACACAAGGAACTCTAGGTATCCC
CAGGACCTGGTGCTGATGGAGGGAAAGATGATGAACTATTGCACTACTGGCCAAATGTGG
GCCCGCAGCAGCTACCTGGGGGCTGTGTTCAATCTCACCAGCGCTGACCATTTATATGTC
AACGTATCTGAGCTCTCTCTGGTCAATTTTGAGGAATCTAAGACATTTTTTGGCTTATAT
AAGCTCTGA
'''
