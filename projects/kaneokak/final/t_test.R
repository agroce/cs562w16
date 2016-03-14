# R script for a two-sample t test with equal variance
# type "Rscript t_test.R" on terminal
# make sure t_test.R, insert.txt, and remove.txt are located in a same directory
# insert.txt and remove.txt for each list are in /saving_result

filename <- "insert.txt"
#filename <- "remove.txt"
data <- read.table(filename)
AVLTree <- data$V1
RBTree <- data$V2
t.test(AVLTree, RBTree, var.equal=T)
