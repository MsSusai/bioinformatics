# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/3/23  9:42 
# 名称：SecondClass.R
# 工具：PyCharm
# data1 <- c(1, 2, 3, 4)
# data2 <- c(TRUE, FALSE, TRUE)
# data3 <- c('aa', 'bb', 'cc')
# data4 <- rep(2:5, times = 4) # 重复函数
# data5 <- seq(from = 3, to = 21, by = 3) # 序列函数
# data6 <- rep(c(1,2,5),times=c(5,10,5))
# print(data1)
# print(data2)
# print(data3)
# print(data4)
# print(data5)
# data1 <- data1[-1] # -表示去除第几个数
# print(data1)

# a <- 1:12
# a <- matrix(a, nrow = 3, ncol = 4, byrow = T) # 生成矩阵
# dim(a) <- c(2, 6) # 矩阵重新塑形

x1 <- c(10, 13, 45, 26, 23, 12)
x2 <- c(20, 65, 32, 32, 27, 87)
x <- data.frame("weight" = x1, "fee" = x2)
