# el nino dataset
elnino = read.table("tao-all2.dat", header=FALSE, na.strings = ".")
head(elnino)
colnames(elnino)= c("obs", "year", "month", "day", "date", "lat",
	"long", "zon.winds", "mer.winds", "humidity", "airTemp", "ssTemp")
elnino = elnino[-1]
#convert to R date format
elnino[,4] = as.Date(as.character(elnino[,4]),"%y%m%d")

head(elnino)
write.table(elnino,"final-elnino.dat", row.names=FALSE, col.names=FALSE)

#remove year, month and day fields
elnino_cut = elnino[c(-1, -2, -3)]
write.table(elnino_cut,"final-elnino-cut.dat", row.names=FALSE, col.names=FALSE)

#to load file to elasticsearch, use logstash

#missing data 
missing=read.table("tao-all2.missing")
head(missing)