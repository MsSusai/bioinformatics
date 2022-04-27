# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/3/30  9:52 
# 名称：ThirdClass.R
# 工具：PyCharm
# 因子
a1 <- c(1,2,3)
factor1 <- as.factor(a1)
print("无序因子：")
print(factor1)
ordered <- as.ordered(a1)
print("有序因子：")
print(ordered)
a<-c("Poor","Improved","Excellent","Poor")
b<-as.factor(a)
levels(b)
levels(b)[1]<-"one"
print(b)


# 条件筛选
vector1 <- seq(from = 2, to = 50, by = 2)
print(vector1[20])
print(c(vector1[10], vector1[15], vector1[20]))
print(vector1[10:20])
print(vector1[vector1 > 40])


boxplot(count ~ spray, data = InsectSprays)
boxplot(count ~ spray, data = InsectSprays, col = "lightgray")

# 读取文件
csv_data <- read.csv("R_learning/data/medical3.csv", header = T)
txt_data <- read.table("R_learning/data/medical3.txt", header = T)
scan_data <- scan("R_learning/data/scan.txt", what = "character", sep = "@", encoding = "GBK")
