# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/4/20  9:52 
# 名称：SixthClass.R
# 工具：PyCharm
x <- read.table(file = "R_learning/data/numgrade.txt", header = TRUE)
numgrade <- tapply(x$levers, INDEX = x$levers, FUN = length)
barplot(numgrade,
        xlab = "level",
        ylab = "number",
        ylim = c(0, 30)) #对向量画柱形图
barplot(numgrade,
        ylab = "level",
        xlab = "number",
        xlim = c(0, 30),
        names.arg = c("best", "good", "ok")) #对向量画条形图并给出类别标签

numgrade <- table(x$sex, x$levers) #2行3列的矩阵（table可统计数据的频数）
barplot(numgrade,
        col = c(2, 3),
        beside = TRUE,
        xlab = "level",
        ylab = "count",
        ylim = c(0, 20),
        names.arg = c("A", "B", "C"))

legend("topright",
       c("male", "female"),
       pch = c(15, 15),
       col = c(2, 3))
numgrade <- t(numgrade)
barplot(numgrade,
        col = c(4, 5, 6),
        beside = TRUE,
        xlab = "sex",
        ylab = "count",
        ylim = c(0, 20),
        names.arg = c("female", "male"))
legend("topright",
       c("A", "B", "C"),
       pch = c(10, 10, 10, 10),
       col = c(4, 5, 6),
       horiz = TRUE,
       cex = 1)

x <- runif(50, 0, 2)
y <- runif(50, 0, 2)
plot(x, y, main = "graph", xlab = "x", ylab = "y")
text(0.6, 0.6, "text at (0.6,0.6)")
abline(h = 0.6, v = 0.6)

