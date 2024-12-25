library(foreign)
library(sas7bdat)
library(ggplot2)
library(scatterplot3d)

?t.test
#the test for class
###########向量##########
a1 <- c(1,3,10)
a2 <- c(sin(pi/6),sqrt(9))
a3 <- c("Hello","World","!!")

#当要生成数值和字符串混合的向量时，数值型会被强制转换为字符型
a4 <- c("Hello","New","Year",2018)
a4[4]
mode(a4[4])

#生成排列规则的数值型向量
a5 <- 1:10
a6 <- rep(10,3)
a7 <- seq(1,1.9,0.1)

#如果两个向量长度相同，向量间的运算为向量成员之间的运算结果
a8 <- seq(2,20,2)
a5/a8

#当两个向量的长度不同时，较短的向量成员要循环扩充到较长的向量等长为止
a9 <- c(1,2)
a1*a9

###########数组和矩阵###########
#2维数组
a1 <- 1:10
dim(a1) <- c(2,5)
a1
matrix(1:15,ncol=5,byrow=TRUE)
matrix(1:15,ncol=5,byrow=FALSE)
#3维数组
a2 <- 1:27
dim(a2) <- c(3,3,3)
a2


###########因子###############
fruit <- c(1,1,2,3) 
f_fruit <- factor(fruit,levels=1:3)
as.numeric(f_fruit)
levels(f_fruit)
levels(f_fruit) <- c("apple","banana","orange")
f_fruit


##############列表################
year <- 2018
fruit <- c("apple","banana","orange")
location <- c("北京","上海","南京","厦门",
              "广州","东莞")  #换行，直接敲回车
com <- list(year=year,fruit=fruit,location=location)
com$fruit


#############数据框###################
win <- c(1,2,3,4,7)
lose <- c(2,3,5,1,8)
comb <- data.frame(win,lose)
comb$win
comb[2,2]

###编写函数###
function.name <- function(x,y){
  x+y #表达式
}
function.name(3,4)

##条件语句##
p <- 0.8
if(p<0.5) 
  {print("p<0.5")}
else
{print("p>=0.5")}

#循环
for(i in 1:10) print(i)
i <- 1
while(i<10){
  print(i)
  i <- i+1}


###########外部文件############
data0<-read.csv("C:/Users/WL/Dropbox/time window paper/training.txt",header=T)
data1<-read.csv("C:/Users/WL/Dropbox/time window paper/training.csv",header=T)
data0 <- read.sas7bdat("C:/Users/WL/Dropbox/time window paper/final.sas7bdat")

summary(data)
data0 <- read.csv("C:/Users/WL/Desktop/training.csv",header=T)
summary(data0)
mean(data0$data1.case)
IQR(data0$data1.vol_dif_2min)

##############数据可视化###########
weather.tab <- table(data0$Weather)
barplot(weather.tab,ylim=c(0,900),ylab="计数",col="red",fill=data0$data1.case)
?barplot

hist(data0$data1.spd_dif_1min)
boxplot(data1.spd_dif_1min~data1.case,data=data0,ylab="spd_dif_1min",col="green")
plot(data0$occ_dif_1min,data0$vol_dif_1min)
?plot

x<-runif(50,0,2)
y<-runif(50,0,2)
plot(x,y,main="散点图",xlab="x",ylab="y",col="red")
text(0.6,0.6,"text at (0.6,0.6)")
abline(h=0.6,v=0.6)
qqnorm(x);qqline(x)

#分步绘图
plot(x,y,type='n',xlab="",ylab="",axes=F)#打开绘图窗口，不绘制任何对象
points(x,y)#添加坐标点
axis(1)#添加横轴
axis(at=seq(0.2,1.8,0.2),side=2)#添加纵轴
box()#补齐散点图的边框
title(main="main title",sub="subtitle",xlab="x",ylab="y")#添加标题、
#副标题、横纵轴说明

#原有图形上添加元素
x <- rnorm(100)#生成随机数
hist(x,freq=F,ylim=c(0,0.5))#绘制直方图
curve(dnorm(x),add=T)#添加曲线

#散点图矩阵
df <- data.frame(data0$std_spd_section_1min,data0$spd_dif_1min,data0$occ_dif_1min)
pairs(df)

#三维散点图
scatterplot3d(df,pch=16,type="h")


###########linear regression ##############
a <- lm(data0$spd_dif_1min~data0$occ_dif_1min)
summary(a)




