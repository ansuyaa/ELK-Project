import csv
import json
from datetime import datetime

def convert(csvFileName, fieldNames):
	jsonFileName = csvFileName.split('.')[0] + '.json'
	csvFile = open(csvFileName, 'r')
	jsonFile = open(jsonFileName, 'w')

	reader = csv.DictReader(csvFile, fieldNames)
	for row in reader:
		json.dump(row, jsonFile)
		jsonFile.write('\n')

def convert_nested(csvFileName, dates):
	jsonFileName = csvFileName.split('.')[0] + '.json'
	jsonFile = open(jsonFileName, 'w')
	n_dates = len(dates)

	with open(csvFileName) as f:
		lis=[line.split() for line in f]

		for x in lis:
			l = x[0].split(",")
			row = dict()
			i_row = 1
			j_row = n_dates + 1
			row['ID'] = l[0]
			usage_users = []
			while i_row <= n_dates :
				usage_users_dict = dict()
				usage_users_dict["date"] = dates[i_row - 1]
				usage_users_dict["usage_amount"] = l[i_row]
				usage_users_dict["users"] = l[j_row]
				usage_users.append(usage_users_dict)
				i_row = i_row + 1
				j_row = j_row + 1
			row['usage'] = usage_users
			json.dump(row, jsonFile)
			jsonFile.write('\n')

def convert_nested_flattened(csvFileName, dates):
	jsonFileName = csvFileName.split('.')[0] + '-flat.json'
	jsonFile = open(jsonFileName, 'w')
	n_dates = len(dates)

	with open(csvFileName) as f:
		lis=[line.split() for line in f]

		for x in lis:
			l = x[0].split(",")
			i_row = 1
			j_row = n_dates + 1
			while i_row <= n_dates :
				row = dict()
				row['ID'] = l[0]
				row["date"] = dates[i_row - 1]
				row["usage_amount"] = l[i_row]
				row["users"] = l[j_row]
				json.dump(row, jsonFile)
				jsonFile.write('\n')
				i_row = i_row + 1
				j_row = j_row + 1


fieldNames = ( 'ID', 'Unspecified' , 'Commercial_Unspecified' , 'Hotel' , 'Mixed_Commercial' ,
	'Mixed_Commercial/Residential' , 'Department_Store' , 'Neighborhood_Store' , 'Low_Office' ,
	'High_Office' , 'Hospital' , 'Church' , 'School' , 'Warehouse' , 'Heavy_Industrial' , 'Other' ,
	'Multi_Family_Small' , 'Single_Family' , 'Multi_Family_Large' , 'Condo' , 'Parking' , 'Vacant' )
csvFileName = 'CCSC_dataset_and_demo_analysis/Building_Type_Land_Percentage-1.csv'
convert(csvFileName, fieldNames)


fieldNames = ( 'ID' , 'population' , 'pop_white' , 'pop_african_american' , 'pop_indian_native' , 'pop_asian' ,
	'pop_hawaiian_pacific_islander' , 'pop_other_race' , 'pop_multi_race' , 'median_age' , 'median_age_male' , 
	'median_age_female' , 'occupied_units' , 'occupied_units_owner' , 'occupied_units_renter' , 'median_year_built' , 'per_capita_income' )
csvFileName = 'CCSC_dataset_and_demo_analysis/Census_Noised-1.csv'
convert(csvFileName, fieldNames)

#convert string to JSON datetime format
#str(datetime(2006,1,1)).replace(' ','T')
#'2006-01-01T00:00:00'
dates = [ str(datetime(year,month,1)).replace(' ','T') for year in [2006,2007,2008, 2009, 2010, 2011] for month in [1,2,3,4,5,6,7,8,9,10,11,12] ]
csvFileName = 'CCSC_dataset_and_demo_analysis/Consumption-1.csv'
convert_nested_flattened(csvFileName, dates)
