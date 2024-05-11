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
    data = data.loc[(data.passenger_count > 0) & (data.trip_distance > 0), :]

    # create a date column for partitioning
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data['lpep_pickup_year'] = data['lpep_pickup_datetime'].dt.year
    data['lpep_pickup_month'] = data['lpep_pickup_datetime'].dt.month
    data['lpep_pickup_day'] = data['lpep_pickup_datetime'].dt.day

    # rename columns for consistency
    data.rename(columns={
        'VendorID': 'vendor_id',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id'
    }, inplace=True)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert 'vendor_id' in output.columns
    assert output.loc[output.passenger_count <= 0, :].shape[0] == 0
    assert output.loc[output.trip_distance <= 0, :].shape[0] == 0
