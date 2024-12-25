setwd("D:/大三上/交通信息挖掘与融合/作业4/第四次作业")
library(openxlsx)
data <- read.xlsx("数据集1.xlsx", sheet=2)
library(psych)
fa.parallel(data[42:54], fa="pc", n.iter=100,
            show.legend = FALSE, main = "Scree plot with parallel analysis")
abline(h=1,lwd=1,col="green")
pc <- principal(data[42:54],nfactors = 4, score = TRUE)
pc
head(pc$scores)
round(unclass(pc$weights),4)
