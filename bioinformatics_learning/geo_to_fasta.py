# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/5/25  20:56 
# 名称：geo_to_fasta.PY
# 工具：PyCharm
file = open(r"datasets/geo.txt", "r")
output_file = open("geo.fasta", "a+")
mode = int(input("请选择模式[1]或[2]\n"
                 "1：保留read长度大于给定参数的序列\n"
                 "2：只保留一定序列长度的read\n"))
i = 0
j = 1

while True:
    if mode == 1:
        seq_length = int(input("选择模式1，请输入要保留序列的长度：\n"))
        break
    elif mode == 2:
        seq_length = int(input("选择模式2，请输入要保留序列的长度：\n"))
        break
    else:
        print("请检查模式选择输入是否正确！")
        mode = int(input("请选择模式[1]或[2]\n"
                         "1：保留read长度大于给定参数的序列\n"
                         "2：只保留一定序列长度的read\n"))
if mode == 1:
    for line in file:
        if i >= 4:
            seq = line.split('\t')
            sequence = seq[0]
            length = int(seq[1])
            count = int(seq[2])
            if length > seq_length:
                output_file.write(">read_" + str(j) + "@" + str(count) + '\n')
                output_file.write(sequence + '\n')
                j += 1
        else:
            i += 1
elif mode == 2:
    for line in file:
        if i >= 4:
            seq = line.split('\t')
            sequence = seq[0]
            length = int(seq[1])
            count = int(seq[2])
            if length == seq_length:
                output_file.write(">read_" + str(j) + "@" + str(count) + '\n')
                output_file.write(sequence + '\n')
                j += 1
        else:
            i += 1
file.close()
output_file.close()
