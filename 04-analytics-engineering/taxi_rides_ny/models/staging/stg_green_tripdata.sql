{{ config(materialized='view') }}

with source as (

    select * from {{ source('staging', 'green_tripdata') }}

),

renamed as (

    select
        {{ dbt_utils.generate_surrogate_key(['vendor_id', 'lpep_pickup_datetime']) }} as trip_id,
        vendor_id,
        lpep_pickup_datetime,
        lpep_dropoff_datetime,
        store_and_fwd_flag,
        ratecode_id,
        pu_location_id,
        do_location_id,
        passenger_count,
        trip_distance,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        ehail_fee,
        improvement_surcharge,
        total_amount,
        payment_type,
        {{ get_payment_type_description('payment_type') }} as payment_type_description,
        trip_type,
        congestion_surcharge,
        lpep_pickup_year,
        lpep_pickup_month

    from source

)

select * from renamed