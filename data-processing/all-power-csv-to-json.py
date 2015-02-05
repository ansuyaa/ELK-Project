import csv
import json
from datetime import datetime

def convert(csvFileName, fieldNames):
	jsonFileName = csvFileName.split('.')[0] + '.json'
	csvFile = open(csvFileName, 'r')
	jsonFile = open(jsonFileName, 'w')

	reader = csv.DictReader(csvFile, fieldNames)
	for row in reader:
		row['location'] = row['lat'] + "," + row['long']
		del row['lat']
		del row['long']
		json.dump(row, jsonFile)
		jsonFile.write('\n')

def convert_nested_flattened_2(csvFileName, dates):
	jsonFileName = csvFileName.split('.')[0] + '-flat.json'
	jsonFile = open(jsonFileName, 'w')
	n_dates = len(dates)

	with open(csvFileName) as f:
		lis=[line.split() for line in f]

		for x in lis:
			l = x[0].split(",")
			i_row = 3
			j_row = n_dates + 3
			while i_row <= n_dates :
				row = dict()
				row['ID'] = l[0]
				row['location'] = l[2] + "," + l[1]
				# row['long'] = l[1]
				# row['lat'] = l[2]
				row["date"] = dates[i_row - 3]
				row["usage_amount"] = l[i_row]
				row["users"] = l[j_row]
				json.dump(row, jsonFile)
				jsonFile.write('\n')
				i_row = i_row + 1
				j_row = j_row + 1

def convert_nested_flattened_3(csvFileName, dates):
	jsonFileName = csvFileName.split('.')[0] + '-flat.json'
	jsonFile = open(jsonFileName, 'w')
	n_dates = len(dates)

	with open(csvFileName) as f:
		lis=[line.split() for line in f]

		for x in lis:
			l = x[0].split(",")
			i_row = 3
			j_row = n_dates + 3
			k_row = n_dates * 2 + 3
			while i_row <= n_dates :
				row = dict()
				row['ID'] = l[0]
				row['location'] = l[2] + "," + l[1]
				# row['long'] = l[1]
				# row['lat'] = l[2]
				row["date"] = dates[i_row - 3]
				row["min_temp"] = l[i_row]
				row["max_temp"] = l[j_row]
				row["mean_temp"] = l[k_row]
				json.dump(row, jsonFile)
				jsonFile.write('\n')
				i_row = i_row + 1
				j_row = j_row + 1
				k_row = k_row + 1


fieldNames = ("ID","sqmi","long","lat","population","age_0_5","age_6_9","age_10_14","age_15_17","age_18_24",
	"age_25_34","age_35_44","age_45_54","age_55_64","age_64_74","age_75_84","age_85_200","average_household_income","average_family_income"
	,"per_capita_income","housing_unit_total","housing_unit_occupied","housing_unit_vacant","median_year_built","average_rent","Elevation")
csvFileName = 'CCSC_dataset_and_demo_analysis/full-data/Consumption_Blockgroup_Sharable_Detail_with_Temperatures/all_census.csv'
convert(csvFileName, fieldNames)


#convert string to JSON datetime format
#str(datetime(2006,1,1)).replace(' ','T')
#'2006-01-01T00:00:00'
dates = [ str(datetime(year,month,1)).replace(' 00:00:00','') for year in [2006,2007,2008, 2009, 2010, 2011] for month in [1,2,3,4,5,6,7,8,9,10,11,12] ]
csvFileName = 'CCSC_dataset_and_demo_analysis/full-data/Consumption_Blockgroup_Sharable_Detail_with_Temperatures/all_temp.csv'
convert_nested_flattened_3(csvFileName, dates)

csvFileName = 'CCSC_dataset_and_demo_analysis/full-data/Consumption_Blockgroup_Sharable_Detail_with_Temperatures/all_usage.csv'
convert_nested_flattened_2(csvFileName, dates)


