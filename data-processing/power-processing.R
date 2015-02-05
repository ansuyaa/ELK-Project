#power dataset
power = read.table("All_CCSC_Data_in_one_Table.csv", header=TRUE, na.strings = ".", sep=",")
head(power)
colnames(power)

building_type_land_per = read.table("Building_Type_Land_Percentage.csv", header=TRUE, na.strings = ".", sep=",")
census_noised = read.table("Census_Noised.csv", header=TRUE, na.strings = ".", sep=",")
consumpiton = read.table("All_CCSC_Data_in_one_Table.csv", header=TRUE, na.strings = ".", sep=",")

all_power = read.table("All_Blockgroup_Data_averaged_by_Month.csv", header=TRUE, na.strings = "0", sep=",")
all_consumption = read.table("Consumption_Blockgroup_Sharable_Detail_with_Temperatures.csv", header=TRUE, na.strings = "0", sep=",")

all_census = all_consumption[,c("BlockgroupID","sqmi","longitude","latitude","population","age_0_5","age_6_9","age_10_14","age_15_17","age_18_24",
	"age_25_34","age_35_44","age_45_54","age_55_64","age_64_74","age_75_84","age_85_200","average_household_income","average_family_income"
	,"per_capita_income","housing_unit_total","housing_unit_occupied","housing_unit_vacant","median_year_built","average_rent","Elevation")]
all_temp = all_consumption[,c(1,5,6,c(29:244))]
all_usage = all_consumption[,c(1,5,6,c(245:388))]

all_census[is.na(all_census)] = 0
all_usage[is.na(all_usage)] = 0
all_temp[is.na(all_temp)]

write.table(all_census, "all_census.csv", row.names = FALSE, sep=",", col.names = FALSE)
write.table(all_temp, "all_temp.csv", row.names = FALSE, sep=",", col.names = FALSE)
write.table(all_usage, "all_usage.csv", row.names = FALSE, sep=",", col.names = FALSE)