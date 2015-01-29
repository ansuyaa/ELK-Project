import ast
from pyelasticsearch import ElasticSearch
es = ElasticSearch('http://localhost:9200')


##set mappings for timestamp, nested object for consumption type 

es.create_index('power')

mapping_consumption = {
    "consumption" : {
        "_timestamp" : {
            "enabled" : "true",
            "path" : "usage.date"
      	},
        "properties" : {
            "usage" : {
                "type" : "nested",
                "include_in_parent": "true",
                "properties": {
                    "date" : {"type": "date" },
                    "usage_amount"  : {"type": "float" },
                    "users" : {"type": "integer"}
                }
            }
        }

    }
}

es.put_mapping('power', 'consumption', mapping_consumption)
print es.get_mapping('power', 'consumption')

#bulk push data to elasticsearch
jsonFileName = 'CCSC_dataset_and_demo_analysis/Census_Noised-1.json' 
bulk_data =[ ast.literal_eval(jsonDoc) for jsonDoc in open(jsonFileName).readlines()]
es.bulk_index('power', 'census', bulk_data, id_field = 'ID')

jsonFileName = 'CCSC_dataset_and_demo_analysis/Building_Type_Land_Percentage-1.json' 
bulk_data =[ ast.literal_eval(jsonDoc) for jsonDoc in open(jsonFileName).readlines()]
es.bulk_index('power', 'land', bulk_data, id_field = 'ID')

jsonFileName = 'CCSC_dataset_and_demo_analysis/Consumption-1.json'
bulk_data =[ ast.literal_eval(jsonDoc) for jsonDoc in open(jsonFileName).readlines()]
es.bulk_index('power', 'consumption', bulk_data, id_field = 'ID')

#es.delete_index('power')