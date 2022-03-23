# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/3/16  9:46 
# 名称：FirstClass.R
# 工具：PyCharm
# x <- c(0:10, 50)
# xmean <- mean(x)
# print(xmean, mean(x, trim = 0, 10))
# print(xmean)

x1 <- c(2, 4, 6, 8, 0)
x2 <- c(1, 3, 5, 7, 9)
print(x1[3])
bind1 <- rbind(x1, x2)
bind2 <- cbind(x1, x2)
print(bind1)
print(bind2)
q()