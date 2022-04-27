# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/4/27  9:43 
# 名称：exam.R
# 工具：PyCharm
# 1.1
# array1 <- array(1:15)
# print(array1[5])
# print(array1[3:5])
# print(array1[c(1, 3, 5, 7)])

# 1.2
# array2 <- array(1:30, dim = c(5, 6))
# print(array2[4,])

# 1.3
# data1 <- rnorm(20, 5, 4)
# print(sort(c(mean(data1), max(data1), min(data1)), decreasing = TRUE))
# print(sort(c(mean(data1), max(data1), min(data1))))

# 1.4
# data1 <- runif(20, -15, 15)
# write.csv(data1, "runif.csv")

# 2 T检验
# sugar <- read.csv("R_learning/exam/data/sugar.txt", header = FALSE)
# result1 <- t.test(sugar, mu = 500)
# print(result1)

# 3 方差分析
# rabbit <- data.frame(
#   sleep_time = c(6.2, 6.1, 6.0, 6.3, 6.1, 5.9, 6.3, 6.5, 6.7, 6.6, 7.1, 6.4,
#                  6.8, 7.1, 6.6, 6.8, 6.9, 6.6, 5.4, 6.4, 6.2, 6.3, 6.0, 5.9),
#   drag = gl(4, 6, 24, labels = c("A1", "A2", "A3", "A4")), # 四组，一组六个
#   food = gl(2, 3, 24, labels = c("B1", "B2"))) # 两组，一组三个
# rabbit_aov <- aov(sleep_time ~ drag + food + drag:food, data = rabbit)
# summary(rabbit_aov)

# 4 画图
cars <- read.table("R_learning/exam/data/cars.txt", header = TRUE)
png("Auto.png")
cars_data <- t(as.matrix(cars))
rownames(cars_data) <- NULL

barplot(cars_data,
        names.arg = c("car", "truck", "suv"),
        col = c(1, 2, 3),
        beside = TRUE,
        ylim = c(0, 20),
        ylab = "Total",
        main = "Autos")
legend("topright",
       c("Mon", "Tue", "Wed", "Thu", "Fri"),
       col = c(1, 2, 3, 4, 5),
       cex = 0.7,
       horiz = TRUE)
dev.off()

# 5 数据整理
# grade <- read.csv("R_learning/exam/data/grade.csv")
# name <- read.csv("R_learning/exam/data/name.csv")
# new_file <- merge(name, grade, by.x = "name", by.y = "ID", all.y = TRUE)
# write.csv(new_file, "grade2.csv")

# 6 线性回归
# pressure <- read.csv("R_learning/exam/data/pressure.csv")
# pdf("pressure.pdf")
# plot(pressure$F, pressure$log100)
# line <- lm(log100 ~ F, data = pressure)
# abline(line$coefficients,col = "red")
# dev.off()

