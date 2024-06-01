{{ config(materialized='view') }}

with source as (

    select * from {{ source('staging', 'yellow_tripdata') }}

),

renamed as (

    select
        vendor_id,
        tpep_pickup_datetime,
        tpep_dropoff_datetime,
        passenger_count,
        trip_distance,
        ratecode_id,
        store_and_fwd_flag,
        pu_location_id,
        do_location_id,
        payment_type,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        improvement_surcharge,
        total_amount,
        congestion_surcharge,
        airport_fee,
        tpep_pickup_year,
        tpep_pickup_month

    from source

)

select * from renamed