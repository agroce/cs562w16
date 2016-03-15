data <- read.csv("/Users/Celleria/Documents/course/CS562/Project/dura.csv", header=TRUE)

cdura <- data[,1]
pdura <- data[,2]
dsize <- data[,3]
ssize <- data[,5]


#skip sort
par(mfrow=c(1,2))
plot(dsize,cdura,type="p",pch=20, col="blue", main="Scatter Plot", xlab="Dictionary Size",ylab="Running Time")
plot(ssize,cdura,type="p",pch=20, col="blue", main="Scatter Plot", xlab="String Size",ylab="Running Time")


par(mfrow=c(1,2))
boxplot(cdura~dsize, main="Boxplot for Running Time vs. Dictionary Size", xlab="Dictionary Size",ylab="Running Time")
boxplot(cdura~ssize, main="Boxplot for Running Time vs. String Size", xlab="String Size",ylab="Running Time")


par(mfrow=c(1,2))
avedsize <- aggregate(cdura~dsize, data, mean)
plot(avedsize$dsize, avedsize$cdura, type="p",pch=20, col="blue", main="Scatter Plot for Average", xlab="Dictionary Size",ylab="Running Time")
abline(lm(avedsize$cdura~avedsize$dsize))

avessize <- aggregate(cdura~ssize, data, mean)
plot(avessize$ssize, avessize$cdura, type="p",pch=20, col="blue", main="Scatter Plot for Average", xlab="String Size",ylab="Running Time")
abline(lm(avessize$cdura~avessize$ssize))

model1 <- lm(cdura~ssize+dsize)
summary(model1)
anova(model1)


#sortedcontainers
par(mfrow=c(1,2))
plot(dsize,pdura,type="p",pch=20, col="blue", main="Scatter Plot", xlab="Dictionary Size",ylab="Running Time")
plot(ssize,pdura,type="p",pch=20, col="blue", main="Scatter Plot", xlab="String Size",ylab="Running Time")


par(mfrow=c(1,2))
boxplot(pdura~dsize, main="Boxplot for Running Time vs. Dictionary Size", xlab="Dictionary Size",ylab="Running Time")
boxplot(pdura~ssize, main="Boxplot for Running Time vs. String Size", xlab="String Size",ylab="Running Time")


par(mfrow=c(1,2))
avedsize2 <- aggregate(pdura~dsize, data, mean)
plot(avedsize2$dsize, avedsize2$pdura, type="p",pch=20, col="blue", main="Scatter Plot for Average", xlab="Dictionary Size",ylab="Running Time")
abline(lm(avedsize2$pdura~avedsize2$dsize))

avessize2 <- aggregate(pdura~ssize, data, mean)
plot(avessize2$ssize, avessize2$pdura, type="p",pch=20, col="blue", main="Scatter Plot for Average", xlab="String Size",ylab="Running Time")
abline(lm(avessize2$pdura~avessize2$ssize))

model2 <- lm(pdura~ssize+dsize)
summary(model2)
anova(model2)

#comparison




plot(avedsize$dsize, avedsize$cdura, type="p",pch=20, col="blue", main="Scatter Plot for Average", xlab="Dictionary Size",ylab="Running Time")
abline(lm(avedsize$cdura~avedsize$dsize))

plot(avedsize2$dsize, avedsize2$pdura, type="p",pch=20, col="blue", main="Scatter Plot for Average", xlab="Dictionary Size",ylab="Running Time")
abline(lm(avedsize2$pdura~avedsize2$dsize))




plot(avessize$ssize, avessize$cdura, type="p",pch=20, col="green", main="Scatter Plot for Average", xlab="String Size",ylab="Running Time")
abline(lm(avessize$cdura~avessize$ssize))
plot(avessize2$ssize, avessize2$pdura, type="p",pch=20, col="green", main="Scatter Plot for Average", xlab="String Size",ylab="Running Time")
abline(lm(avessize2$pdura~avessize2$ssize))
