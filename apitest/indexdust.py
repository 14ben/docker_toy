from elasticsearch import Elasticsearch

# Create an instance of Elasticsearch client
es = Elasticsearch()

# Index mapping definition
index_mapping = {
    "mappings": {
        "properties": {
            "data_time": {"type": "date"},  # Assuming data_time is in datetime format
            "pm25_value": {"type": "float"},
            "pm10_value": {"type": "float"}
            # Add other fields here if needed
        }
    }
}

# Create the index with the specified mapping
index_name = "dust"  # Replace "dust" with your desired index name
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=index_mapping)

# Now you can insert data into the "dust" index as shown in the previous code

