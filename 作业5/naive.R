setwd("D:/大三上/交通信息挖掘与融合/作业5");
getwd();
library(openxlsx)
data <- read.xlsx("数据集1.xlsx", sheet=2)
for(i in 1:nrow(data)) 
{if (data[i,3]==0)
  data[i,3]=0
else if(data[i,3]<3)
  data[i,3]=1
else if(data[i,3]>2)
  data[i,3]=2
}
selectedl = c("Q4","Q5","Q14_3","Q14_2","Q14_6","Q14_10","Q15_13",
              "Q15_2","Q15_5","Q15_7","Q15_8","Q15_11","Q14_12","Q2")
data1=data[selectedl]
train_sub = sample(nrow(data1),8/10*nrow(data1))
train_data = data1[train_sub,]
test_data = data1[-train_sub,]
#导入数据，并8：2分为训练集和测试集


##klaR函数包使用 朴素贝叶斯分类
library(e1071)
library(pROC)
train_data$Q2 <- as.factor(train_data$Q2)
data_model <- naiveBayes(Q2~.,data=train_data,laplace = 1)
#预测结果
test_data$Q4 <- as.factor(test_data$Q4)
test_data$Q5 <- as.factor(test_data$Q5)
data_predict <- predict(data_model,newdata = test_data)


#输出混淆矩阵
table(test_data$Q2,data_predict,dnn=c("真实值","预测值"))
#绘制ROC曲线
naive_roc <- roc(test_data$Q2,as.numeric(data_predict$class))
plot(naive_roc,print.auc=TRUE, auc.polygon=TRUE, grid=c(0.1, 0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='朴素贝叶斯算法ROC曲线 kernel = radial')

