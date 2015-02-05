import ast
from pyelasticsearch import ElasticSearch
es = ElasticSearch('http://127.0.0.1:9200')


##set mappings 
#es.delete_index('all-power')
#es.create_index('all-power')


##{"date": "2006-01-01", "usage_amount": "337481.6", "users": "680", 
##"ID": "60371011101", "location": "34.25936072,-118.2881353"}

mapping_usage = {
    "usage" : {
        "properties" : {
            "date" : {"type": "date", "format": "yyyy-MM-dd" },
            "usage_amount"  : {"type": "float" },
            "users" : {"type": "integer"},
            "ID" : {"type": "string"},
            "location" : {"type": "geo_point"}
        }
    }
}


es.put_mapping('all-power', 'usage', mapping_usage)
print es.get_mapping('all-power', 'usage')

## {"mean_temp": "55.94", "location": "34.25936072,-118.2881353", "date": "2006-01-01", 
## "min_temp": "44.96", "ID": "60371011101", "max_temp": "66.92"}

mapping_temp = {
    "temp" : {
        "properties" : {
            "date" : {"type": "date", "format": "yyyy-MM-dd" },
            "mean_temp"  : {"type": "float" },
            "min_temp"  : {"type": "float" },
            "max_temp"  : {"type": "float" },
            "ID" : {"type": "string"},
            "location" : {"type": "geo_point"}
        }
    }
}

es.put_mapping('all-power', 'temp', mapping_temp)
print es.get_mapping('all-power', 'temp')

## {"average_household_income": "75244", "age_6_9": "127", "per_capita_income": "25419", 
## "age_10_14": "293", "age_0_5": "61", "average_rent": "1118.965517", "age_45_54": "558", 
## "median_year_built": "1956", "age_75_84": "36", "Elevation": "423.7", 
## "location": "34.25936072,-118.2881353", "age_55_64": "361", "housing_unit_vacant": "0", 
## "population": "2304", "age_35_44": "267", "age_64_74": "62", "sqmi": "0.17", "housing_unit_total": "756", 
## "ID": "60371011101", "average_family_income": "78457", "age_85_200": "0", "housing_unit_occupied": "756", 
## "age_15_17": "55", "age_18_24": "232", "age_25_34": "252"}

mapping_census = {
	"census" : {

		"properties" : {

			"average_household_income" : {"type": "integer"},
			"per_capita_income" : {"type": "integer"},
			"population" : 	{"type": "integer"},
			"sqmi" : {"type": "float"},
			"age_0_5" : {"type": "integer"},                 
			"age_6_9" : {"type": "integer"},                  
			"age_10_14" : {"type": "integer"},                
			"age_15_17" : {"type": "integer"},                
			"age_18_24" : {"type": "integer"},                
			"age_25_34" : {"type": "integer"},               
 			"age_35_44" : {"type": "integer"},               
 			"age_45_54" : {"type": "integer"},                
 			"age_55_64" : {"type": "integer"},                
 			"age_64_74" : {"type": "integer"},                
 			"age_75_84" : {"type": "integer"}, 
  			"age_85_200" : {"type": "integer"},
			"average_family_income" : {"type": "integer"},
			"housing_unit_total" : {"type": "integer"},
			"housing_unit_occupied" : {"type": "integer"},
			"housing_unit_vacant" : {"type": "integer"},
 			"median_year_built" : {"type": "string"},
			"average_rent" : {"type": "float"},
			"Elevation" : {"type": "float"},
			"ID" : {"type": "string"},
            "location" : {"type": "geo_point"}
		}
	}
}

es.put_mapping('all-power', 'census', mapping_census)
print es.get_mapping('all-power', 'census')


#bulk push data to elasticsearch
jsonFileName = 'CCSC_dataset_and_demo_analysis/full-data/Consumption_Blockgroup_Sharable_Detail_with_Temperatures/all_census.json' 
bulk_data =[ ast.literal_eval(jsonDoc) for jsonDoc in open(jsonFileName).readlines()]
es.bulk_index('all-power', 'census', bulk_data, id_field = 'ID')

jsonFileName = 'CCSC_dataset_and_demo_analysis/full-data/Consumption_Blockgroup_Sharable_Detail_with_Temperatures/all_temp-flat.json' 
bulk_data =[ ast.literal_eval(jsonDoc) for jsonDoc in open(jsonFileName).readlines()]
es.bulk_index('all-power', 'temp', bulk_data)

jsonFileName = 'CCSC_dataset_and_demo_analysis/full-data/Consumption_Blockgroup_Sharable_Detail_with_Temperatures/all_usage-flat.json'
bulk_data =[ ast.literal_eval(jsonDoc) for jsonDoc in open(jsonFileName).readlines()]
for i in [0,100000, 200000,300000]:
	es.bulk_index('all-power', 'usage', bulk_data[i:i+100000])

#es.delete_index('all-power')
