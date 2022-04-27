# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/4/25  16:03 
# 名称：practice.R
# 工具：PyCharm
# 第一题
array1 <- array(1:15)
print(array1[5])
print(array1[3:5])
print(array1[c(1, 3, 5, 7)])

# # 第二题
# data1 <- rnorm(10, 4, 4)
# print(sort(c(mean(data1), max(data1), min(data1))))
# print(sort(c(mean(data1), max(data1), min(data1)), decreasing = TRUE))
#
# # 第三题
# scan1 <- scan()
# matrix1 <- matrix(scan1, 4, 5)
# print(c(matrix1[, 1], matrix1[, 3], matrix1[, 5]))
#
# # 第四题
# rabbit <- data.frame(
#   sleep_time = c(6.2, 6.1, 6.0, 6.3, 6.1, 5.9, 6.3, 6.5, 6.7, 6.6, 7.1, 6.4,
#                  6.8, 7.1, 6.6, 6.8, 6.9, 6.6, 5.4, 6.4, 6.2, 6.3, 6.0, 5.9),
#   drag = gl(4, 6, 24, labels = c("A1", "A2", "A3", "A4")), # 四组，一组六个
#   food = gl(2, 3, 24, labels = c("B1", "B2"))) # 两组，一组三个
# rabbit_aov <- aov(sleep_time ~ drag + food, data = rabbit)
# summary(rabbit_aov)
#
# # 第五题
# stu.df <- read.csv("stu.data.csv")
# stu.df$armlegL <- stu.df$arml + stu.df$legl
# stu.df$armlegL[c(2, 5, 7, 10)] <- NA
# stu.df$armlegL <- NULL
# is.numeric(stu.df$Grade)
# summary(stu.df$Grade)
# stu.df$Grade <- as.factor(stu.df$Grade)
# summary(stu.df$Grade)
# library(plyr)
# arrange(stu.df, age, -weight)
# df1A <- stu.df[1:20,]
# df1B <- stu.df[-1:-20,]
# df1 <- rbind(df1A, df1B)
# df2A <- stu.df[, 1:6]
# df2B <- stu.df[, -2:-6]
# df2 <- merge(df2A, df2B, by = "ID")
# df3 <- subset(stu.df, age > 20 & Grade < 3)
# mean(stu.df$weight); max(stu.df$height)



