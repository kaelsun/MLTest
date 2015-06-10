library(RODBC);
channel <- odbcConnect("mysql odbc", uid="root", pwd="******");
sqlTables(channel);
all <- sqlFetch(channel, "point_recharge");
max <- sqlFetch(channel, "point_recharge_max");
#hist(max$max, prob = T, breaks = 1000);#画分布图
#plot(ecdf(max$max), xlab = "maximum of money per user single time",main = "Cumulative Distribution Function of point max");#累积分布图
#plot(max$max, all$amount);#总支付和单次最大支付关系图
plot(all$amount, max$max);#总支付和单次最大支付关系图
