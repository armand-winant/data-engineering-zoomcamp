import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/.keys/astral-pursuit-422621-e6-4789763eb8fa.json"

bucket_name = 'de-zoomcamp_nyc-taxi-data'
table_name = 'green_taxi_trips'
root_path = os.path.join(bucket_name, table_name)

@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    table = pa.Table.from_pandas(data)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path = root_path,
        partition_cols = ['lpep_pickup_year', 'lpep_pickup_month', 'lpep_pickup_day'],
        filesystem = gcs
    )


