# set working directory
#setwd("C:/Users/bro16639/OneDrive/OneDrive - Texas Tech University/Research/Projects/TransmissionSwitching/code/R")

# packages
library(arules)
#library(xgboost)

# read in data
data_filename <- "/Users/mdridwanrahman/Desktop/Research/congestion_data_4_19.csv"
mydata <- read.csv(data_filename, header = FALSE)


# set column info
colnames(mydata) <- c('Scenario',
                      'SwitchNum',
                      paste0('pd',1:118),
                      paste0('lmp',1:118),
                      paste0('dual_g',1:19),
                      paste0('bc',1:186),
                      paste0('z',1:186),
                      'cost',
                      'SwitchId'
                      )


# drop rows with all zeros
mydata <- mydata[rowSums(mydata[])>0,]

# drop rows 

# drop demand vectors
mydata <- mydata[,-c(3:120)]


# lmps are 1 if they exceed 1, 0 otherwise
mydata[,grepl("lmp", names(mydata))] <- as.integer(mydata[,grepl("lmp", names(mydata))] >= 1)

# generator upper bound duals are 1 if they are strictly less than 0, 0 otherwise
mydata[,grepl("dual_g", names(mydata))] <- as.integer(mydata[,grepl("dual_g", names(mydata))] < 0)

# branch capacities are 1 if they are strictly 0, 0 otherwise
mydata[,grepl("bc", names(mydata))] <- as.integer(mydata[,grepl("bc", names(mydata))] == 0)

# z's seem to be writing our weird, round to 4 decimal places
mydata[,grepl("z", names(mydata))] <- round(mydata[,grepl("z", names(mydata))], 4)

# drop first two and last two columns
mydata <- mydata[,-which(colnames(mydata) == "Scenario")]
mydata <- mydata[,-which(colnames(mydata) == "SwitchNum")]
mydata <- mydata[,-which(colnames(mydata) == "cost")]
#mydata <- mydata[,-which(colnames(mydata) == "SwitchId")]

# drop columns with all zeros
mydata <- mydata[,colSums(mydata[])>0]

# xgboost testing
#train.data  <- as.matrix(mydata[1:36000,1:283], sparse = TRUE)
#train.label <- as.factor(mydata[1:36000,284])
#test.data <- as.matrix(mydata[36001:45042,1:283], sparse = TRUE)
#test.label <- as.factor(mydata[36001:45042,284])

#xgb.train <- xgb.DMatrix(data=train.data, label = train.label)
#xgb.test <- xgb.DMatrix(data=test.data, label=test.label)
#num_class <- length(unique(train.label))
#params = list(
#  booster="gbtree",
#  eta=0.001,
#  max_depth=5,
#  gamma=3,
#  subsample=0.75,
#  colsample_bytree=1,
#  objective="multi:softprob",
#  eval_metric="mlogloss",
#  num_class=num_class
#)
#xgb.fit=xgb.train(
#  params=params,
#  data=xgb.train,
#  nrounds=10000,
#  early_stopping_rounds=10,
#  watchlist=list(val1=xgb.train,val2=xgb.test),
#  verbose=0
#)


#pred <- predict(xgb, test.data)

#oof_pred <- data.frame(pred)


# cast as a matrix for apriori
mydata <- as.matrix(mydata)

# make some rules (parameters here are TBD)
myrules <- apriori(mydata, parameter = list(support = 0.1,
                                            confidence = 0.95,   # started with 0.8 
                                            minlen = 2,
                                            maxlen = 4,
                                            maxtime = 30))

z.rules <- subset(myrules, items %pin% "z153")

inspect(sort(z.rules, by = "lift"))
