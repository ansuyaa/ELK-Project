#power dataset
power = read.table("All_CCSC_Data_in_one_Table.csv", header=TRUE, na.strings = ".", sep=",")
head(power)
colnames(power)

#to load file to elasticsearch, use logstash
