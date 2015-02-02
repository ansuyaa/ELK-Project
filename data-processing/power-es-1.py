import ast
from pyelasticsearch import ElasticSearch
es = ElasticSearch('http://127.0.0.1:9200')


##set mappings for timestamp, nested object for consumption type 
es.create_index('power')

mapping_consumption = {
    "consumption" : {
        "properties" : {
            "date" : {"type": "date" },
            "usage_amount"  : {"type": "float" },
            "users" : {"type": "integer"},
            "ID" : {"type": "string"}
        }
    }
}


es.put_mapping('power', 'consumption', mapping_consumption)
print es.get_mapping('power', 'consumption')

mapping_census = {
	"census" : {

		"properties" : {

			'population' : {"type": "integer"}, 
			'pop_white' : {"type": "integer"}, 
			'pop_african_american' : {"type": "integer"}, 
			'pop_indian_native' : {"type": "integer"}, 
			'pop_asian' : {"type": "integer"},
			'pop_hawaiian_pacific_islander' : {"type": "integer"}, 
			'pop_other_race' : {"type": "integer"}, 
			'pop_multi_race' : {"type": "integer"}, 
			'median_age' : { "type" : "float" }, 
			'median_age_male' : { "type" : "float" }, 
			'median_age_female' : { "type" : "float" }, 
			'occupied_units' : {"type": "integer"}, 
			'occupied_units_owner' : {"type": "integer"}, 
			'occupied_units_renter' : {"type": "integer"}, 
			'median_year_built' : {"type": "integer"}, 
			'per_capita_income' : {"type": "integer"}
		}
	}
}

es.put_mapping('power', 'census', mapping_census)
print es.get_mapping('power', 'census')

mapping_land = {
	"land" : {

		"properties" : {

			'Unspecified' : { "type" : "float" }, 
			'Commercial_Unspecified' : { "type" : "float" }, 
			'Hotel' : { "type" : "float" }, 
			'Mixed_Commercial' : { "type" : "float" },
			'Mixed_Commercial/Residential' : { "type" : "float" }, 
			'Department_Store' : { "type" : "float" }, 
			'Neighborhood_Store' : { "type" : "float" }, 
			'Low_Office' : { "type" : "float" },
			'High_Office' : { "type" : "float" }, 
			'Hospital' : { "type" : "float" }, 
			'Church' : { "type" : "float" }, 
			'School' : { "type" : "float" }, 
			'Warehouse' : { "type" : "float" }, 
			'Heavy_Industrial' : { "type" : "float" }, 
			'Other' : { "type" : "float" },
			'Multi_Family_Small' : { "type" : "float" }, 
			'Single_Family' : { "type" : "float" }, 
			'Multi_Family_Large' : { "type" : "float" }, 
			'Condo' : { "type" : "float" }, 
			'Parking' : { "type" : "float" }, 
			'Vacant' : { "type" : "float" }
		}

	}
	
}

es.put_mapping('power', 'land', mapping_land)
print es.get_mapping('power', 'land')

#bulk push data to elasticsearch
jsonFileName = 'CCSC_dataset_and_demo_analysis/Census_Noised-1.json' 
bulk_data =[ ast.literal_eval(jsonDoc) for jsonDoc in open(jsonFileName).readlines()]
es.bulk_index('power', 'census', bulk_data, id_field = 'ID')

jsonFileName = 'CCSC_dataset_and_demo_analysis/Building_Type_Land_Percentage-1.json' 
bulk_data =[ ast.literal_eval(jsonDoc) for jsonDoc in open(jsonFileName).readlines()]
es.bulk_index('power', 'land', bulk_data, id_field = 'ID')

jsonFileName = 'CCSC_dataset_and_demo_analysis/Consumption-1-flat.json'
bulk_data =[ ast.literal_eval(jsonDoc) for jsonDoc in open(jsonFileName).readlines()]
es.bulk_index('power', 'consumption', bulk_data)

#es.delete_index('power')
