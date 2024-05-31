import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    year_month = kwargs['execution_date'].strftime("%Y-%m")
    year_month = '2024-02'
    url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/fhv_tripdata_{year_month}.parquet'

    return pd.read_parquet(url)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'