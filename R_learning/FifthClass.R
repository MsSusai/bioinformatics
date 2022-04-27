# -*- coding: utf-8 -*-

# 作者：Sosai
# 时间：2022/4/13  9:49 
# 名称：FifthClass.R
# 工具：PyCharm

# 创建dataframe
mydata <- data.frame(x1 = c(2, 2, 6, 4),
                     x2 = c(3, 4, 2, 8))
# dataframe添加列，列运算
mydata$sum <- mydata$x1 + mydata$x2
mydata$mean <- (mydata$x1 + mydata$x2) / 2
print(mydata)
# 方法二
mydata <- transform(mydata,
                    sum = x1 + x2,
                    mean = (x1 + x2) / 2)
# 移除，赋值为空
mydata$mean <- NULL

data <- data.frame(A = c(1:4), B = c("小明", "小王", "小李", "小张"))
gg <- c(2, 1, 4, 3)
data[order(gg)]

# csv操作
chinaIUCN <- read.csv("R_learning/data/chinaIUCN.csv")
gao <- read.csv("R_learning/data/gao.csv")
mergeFrame <- merge(x = chinaIUCN,
                    y = gao,
                    by.x = "species",
                    by.y = "name",)
write.csv(mergeFrame, "R_learning/data/mergeFrame1.csv")


num<-seq(201501,201560)#模拟学号
x1<-round(runif(60,min=80,max=100))#模拟数学分析的成绩服从均匀分布
x2<-round(rnorm(60,mean=80,sd=7))#模拟线性代数的成绩服从正态分布
x3<-round(rnorm(60,mean=83,sd=10))#模拟概率统计的成绩服从正态分布发现有超过100的分数，使用
x3[which(x3>100)]<-100#将超过100的分数重新赋值为100
x<-data.frame(num,x1,x2,x3)

# write.table(x,"grade.txt",append="FALSE",col.names=FALSE,row.names=FALSE)

stem(x$x2)

boxplot(x$x1,x$x2,x$x3)
boxplot(x[2:4],col=c("red","green","blue"),notch=T)#notch决定缺口
boxplot(x$x1,x$x2,x$x3,horizontal=TRUE,axes=TRUE,col=c("red","green","blue"),notch=T)
