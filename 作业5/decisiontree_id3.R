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
train_sub = sample(nrow(data),8/10*nrow(data))
train_data = data[train_sub,]
test_data = data[-train_sub,]
#导入数据，并8：2分为训练集和测试集

library(rpart)
#生成决策树
data_decisiontree <- rpart(Q2 ~ Q4+Q5+Q14_6+Q14_2+Q14_3+Q14_10+Q14_12+Q15_13
                           +Q15_2+Q15_8+Q15_5+Q15_11+Q15_7,
                           data = train_data,
                           method="class",
                           parms=list(split="information"))
printcp(data_decisiontree)
#决策树的剪枝及树的剪枝判断
#输出结果
#选择xerror最小的cp值
data_decisiontree_prune <- prune(data_decisiontree, cp=0.010000)

#绘制树图
library(rpart.plot)
rpart.plot(data_decisiontree_prune,branch=1,fallen.leaves=T,
           cex=0.6)

#在测试集上预测
pre_decisiontree <- predict(data_decisiontree_prune,
                            newdata = test_data,
                            type="class")
#将测试集计算所得概率与观测本身取值整合到一起
obs_p_decision_cart = data.frame(prob=pre_decisiontree,
                                 obs=test_data$Q2)
#输出混淆矩阵
table(test_data$Q2,pre_decisiontree,dnn=c("真实值","预测值"))

#绘制ROC图像
library(pROC)
decisiontree_roc <- roc(test_data$Q2,as.numeric(pre_decisiontree))
plot(decisiontree_roc,print.auc=TRUE,auc.polygon=TRUE,
     grid = c(0.1,0.2),grid.col=c("green", "red"), max.auc.polygon=TRUE,auc.polygon.col="skyblue", print.thres=TRUE,main='决策树ID3算法ROC曲线')

