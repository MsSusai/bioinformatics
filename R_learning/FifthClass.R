# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/4/13  9:49 
# 名称：FifthClass.R
# 工具：PyCharm
# 创建dataframe
# mydata <- data.frame(x1 = c(2, 2, 6, 4),
#                      x2 = c(3, 4, 2, 8))
# # dataframe添加列，列运算
# mydata$sum <- mydata$x1 + mydata$x2
# mydata$mean <- (mydata$x1 + mydata$x2) / 2
# print(mydata)
# # 方法二
# mydata <- transform(mydata,
#                     sum = x1 + x2,
#                     mean = (x1 + x2) / 2)
# # 移除，赋值为空
# mydata$mean <- NULL

# data <- data.frame(A = c(1:4), B = c("小明", "小王", "小李", "小张"))
# gg <- c(2, 1, 4, 3)
# data[order(gg)]

chinaIUCN <- read.csv("R_learning/data/chinaIUCN.csv")
gao <- read.csv("R_learning/data/gao.csv")
mergeFrame <- merge(x = chinaIUCN,
                    y = gao,
                    by.x = "species",
                    by.y = "name",)
write.csv(mergeFrame, "R_learning/data/mergeFrame1.csv")

