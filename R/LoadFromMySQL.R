#library(RODBC);
channel <- odbcConnect("mysql odbc", uid="root", pwd="******");
sqlTables(channel);
recharge <- sqlFetch(channel, "point_recharge_1000");
#recharge <- sqlFetch(channel, "point_recharge");
#summary(recharge);#概览
#hist(recharge$amount, prob = T);#画分布图
hist(recharge$amount, prob = F, breaks = 100);#画分布图，变换参数
#plot(ecdf(recharge$amount), xlab = "total amount of money per user",main = "Cumulative Distribution Function of point recharge");#累积分布图
#library(sROC);
#plot(kCDF(recharge$amount), type = "l", lwd = 10);
#ks.test(recharge$amount, "pgamma", 1);



