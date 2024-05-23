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
    # rename columns for consistency  
    data.rename(columns={
        'dropOff_datetime': 'dropoff_datetime',
        'PUlocationID': 'pu_location_id',
        'DOlocationID': 'do_location_id'
    }, inplace=True)

    # standardize column types
    data.pu_location_id = data.pu_location_id.astype(pd.Int64Dtype())
    data.do_location_id = data.do_location_id.astype(pd.Int64Dtype())

    # create columns for partitioning
    data['pickup_year'] = data.pickup_datetime.dt.year
    data['pickup_month'] = data.pickup_datetime.dt.month

    year, month = kwargs['execution_date'].strftime("%Y-%m").split('-')
    year, month = [2019, 2]
    data = data.loc[(data.pickup_year == int(year)) & (data.pickup_month == int(month)), :]

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
