import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # remove erroneous data
    data = data.loc[(data.trip_distance > 0) & (data.passenger_count > 0), :]

    # rename columns for consistency    
    data.rename(columns={
        'VendorID': 'vendor_id',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id'
    }, inplace=True)

    # standardize column name
    data.vendor_id = data.vendor_id.astype(pd.Int64Dtype())
    data.ratecode_id = data.ratecode_id.astype(pd.Int64Dtype())
    data.pu_location_id = data.pu_location_id.astype(pd.Int64Dtype())
    data.do_location_id = data.do_location_id.astype(pd.Int64Dtype())
    data.passenger_count = data.passenger_count.astype(pd.Int64Dtype())
    data.payment_type = data.payment_type.astype(pd.Int64Dtype())
    data.trip_type = data.trip_type.astype(pd.Int64Dtype())

    # create columns for partitioning
    data['lpep_pickup_year'] = data.lpep_pickup_datetime.dt.year
    data['lpep_pickup_month'] = data.lpep_pickup_datetime.dt.month

    year, month = kwargs['execution_date'].strftime("%Y-%m").split('-')
    data = data.loc[(data.lpep_pickup_year == int(year)) & (data.lpep_pickup_month == int(month)), :]

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
