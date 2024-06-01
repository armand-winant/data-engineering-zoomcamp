{{ codegen.generate_source(
  schema_name='trips_data_all',
  table_names=['green_tripdata', 'yellow_tripdata'],
  include_descriptions=False,
  name='staging',
  include_database=True,
  include_schema=True
) }}