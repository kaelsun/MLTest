library(RODBC);
channel <- odbcConnect("mysql odbc", uid="root", pwd="******");
sqlTables(channel);
active <- sqlFetch(channel, "point_active_100");
hist(active$active, prob = F, breaks = 100);#画分布图，变换参数
