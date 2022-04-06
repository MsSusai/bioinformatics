# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/4/6  9:46 
# 名称：FouthClass.R
# 工具：PyCharm

# 对一批涂料进行研究，确定搅拌速度对杂质含量的影响
rate <- c(20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42)
impurity <- c(8.4, 9.5, 11.8, 10.4, 13.3, 14.8, 13.2, 14.7, 16.4, 16.5, 18.9, 18.5)
plot(impurity ~ rate)
reg <- lm(impurity ~ rate)
abline(reg, col = "red")
summary(reg)

# Vasishth’s Height Example
samp <- c(53.56797, 60.12001, 59.857, 63.5358, 62.0039, 61.80454, 64.3353, 61.38428, 60.05831, 65.93938, 57.21961)
t.test(samp, mu = 64)
t.test(samp, mu = 64,alternative = "less")
t.test(samp, mu = 64,alternative = "greater")

# 两正态总体参数检验
x<-c(20.5, 19.8, 19.7, 20.4, 20.1, 20.0, 19.0, 19.9)
y<-c(20.7, 19.8, 19.5, 20.8, 20.4, 19.6, 20.2)
t.test(x, y, var.equal=TRUE)

# 单因子方差分析
X <- c(25.6, 22.2, 28.0, 29.8, 24.4, 30.0, 29.0, 27.5, 25.0, 27.7, 23.0, 32.2, 28.8, 28.0, 31.5, 25.9, 20.6, 21.2, 22.0, 21.2) #数据
A <- factor(rep(1:5, each = 4)) #分组
#输出 A=(1 1 1 1 2 2 2 2 3 3 3 3 ……5 5 5 5）
miscellany <- data.frame(X, A) #拼接
aov.mis <- aov(X ~ A, data = miscellany) #进行anova
summary(aov.mis)
plot(miscellany$X ~ miscellany$A)

# 双因子方差分析
juice <- data.frame(
  X = c(0.05, 0.46, 0.12, 0.16, 0.84, 1.30, 0.08, 0.38, 0.4, 0.10, 0.92, 1.57, 0.11, 0.43, 0.05, 0.10, 0.94, 1.10, 0.11, 0.44, 0.08, 0.03, 0.93, 1.15),
  A = gl(4, 6),
  B = gl(6, 1, 24))
juice.aov <- aov(X ~ A + B, data = juice)
summary(juice.aov)

# 有交互作用的方差分析
rats <- data.frame(
  Time = c(0.31, 0.45, 0.46, 0.43, 0.82, 1.10, 0.88, 0.72, 0.43, 0.45,
           0.63, 0.76, 0.45, 0.71, 0.66, 0.62, 0.38, 0.29, 0.40, 0.23,
           0.92, 0.61, 0.49, 1.24, 0.44, 0.35, 0.31, 0.40, 0.56, 1.02,
           0.71, 0.38, 0.22, 0.21, 0.18, 0.23, 0.30, 0.37, 0.38, 0.29,
           0.23, 0.25, 0.24, 0.22, 0.30, 0.36, 0.31, 0.33),
  Toxicant = gl(3, 16, 48, labels = c("I", "II", "III")),
  Cure = gl(4, 4, 48, labels = c("A", "B", "C", "D")))

rats.aov<-aov(Time~Toxicant*Cure, data=rats)
summary(rats.aov)

