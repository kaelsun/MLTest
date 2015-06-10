library(RODBC);
channel <- odbcConnect("mysql odbc", uid="root", pwd="******");
sqlTables(channel);
experiment <- sqlFetch(channel, "runcool_getwellfare_log");
#hist(recharge$success, prob = F, breaks = 1000);#画分布图，变换参数
hist(experiment$remainCount, prob = F, breaks = 1000);#画分布图，变换参数
