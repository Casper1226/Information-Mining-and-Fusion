setwd("D:/大三上/交通信息挖掘与融合/作业2")
data_1 <- read.table("training.csv",header=TRUE,sep=",")
total_1 <- glm(case~spd_dif_1min+spd_dif_2min+spd_dif_3min+spd_dif_4min
+vol_dif_1min+vol_dif_2min+vol_dif_3min+vol_dif_4min,data=data_1,
family=binomial())
summary(total_1)
total_2 <- glm(case~spd_dif_1min+spd_dif_4min
+vol_dif_1min+vol_dif_2min,data=data_1,
family=binomial())
summary(total_2)
anova(total_1,total_2,test="Chisq")