set.seed(1);
x<-seq(0,10,length.out=100);
#y<-dgamma(x,1,2);
y<-dgamma(x,1.1,1.2);

plot(x,y,col="red",xlim=c(0,10),ylim=c(0,2),type='l', xaxs="i", yaxs="i",ylab='density',xlab='', ain="The Gamma Density Distribution");

#lines(x,dgamma(x,2,2),col="green");
#lines(x,dgamma(x,3,2),col="blue");
#lines(x,dgamma(x,5,1),col="orange");
#lines(x,dgamma(x,9,1),col="black");

#legend("topright",legend=paste("shape=",c(1,2,3,5,9)," rate=", c(2,2,2,1,1)), lwd=1, col=c("red", "green","blue","orange","black"));