library(RODBC);
channel <- odbcConnect("mysql", uid="root", pwd="******");
sqlTables(channel);
#recharge <- sqlFetch(channel, "point_recharge_success_30");
recharge <- sqlFetch(channel, "point_recharge_fail_100");
#hist(recharge$success, prob = F, breaks = 1000);#画分布图，变换参数
hist(recharge$fail, prob = F, breaks = 1000);#画分布图，变换参数


