import subprocess
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from time import time
import argparse

# user = "root"
# password = "root"
# host = "localhost"
# port = 5431
# db = "ny_taxi"

# local_filename = "ny_taxi_data.parquet"
# url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"


# fetch_command = f"curl -s -o {local_filename} {url}"
# subprocess.run(fetch_command.split())
# parquet_file = pq.ParquetFile(local_filename)

# engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

# for i, batch in enumerate(parquet_file.iter_batches(batch_size=100000, use_pandas_metadata=True), 1):
#   t_start = time()
#   df = batch.to_pandas()
#   df.to_sql('yellow_taxi_trips', con=engine, if_exists='append', index=False)
#   print(f"Upload complete: {df.shape[0]} rows uploaded in {(time() - t_start):.3f} seconds.")


def main(params):
  user = params.user
  password = params.password
  host = params.host
  port = params.port
  db = params.db
  table = params.table
  url = params.url

  local_filename = "output.parquet"
  # url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"

  fetch_command = f"curl -s -o {local_filename} {url}"
  subprocess.run(fetch_command.split())
  parquet_file = pq.ParquetFile(local_filename)

  engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

  for i, batch in enumerate(parquet_file.iter_batches(batch_size=100000, use_pandas_metadata=True), 1):
    t_start = time()
    df = batch.to_pandas()

    upload_method = 'replace' if i == 1 else 'append'
    df.to_sql(table, con=engine, if_exists=upload_method, index=False)
    print(f"Upload complete: {df.shape[0]} rows uploaded in {(time() - t_start):.3f} seconds.")
  
  delete_command = f"rm -f {local_filename}"
  subprocess.run(delete_command.split())


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Ingest Parquet data to Postgres')

  parser.add_argument('--user', help='Username for postgres')
  parser.add_argument('--password', help='User password for postgres')
  parser.add_argument('--host', help='Postgres host')
  parser.add_argument('--port', help='Postgres port number')
  parser.add_argument('--db', help='postgres DB')
  parser.add_argument('--schema', help='postgres schema')
  parser.add_argument('--table', help='Postgres table')
  parser.add_argument('--url', help='URL of Parquet data file')

  args = parser.parse_args()

  main(args)