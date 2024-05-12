-- CREATE A NEW EXTERNAL TABLE FROM GCS DATA
-- BigQuery is unable to determine the size/rows of an external table because the data iteself is not inside BigQuery

CREATE OR REPLACE EXTERNAL TABLE `projectID.dataSet.tableName`
OPTIONS (
  format = 'CSV',
  uris = ['gs://bucketName/folderName/files_*.csv']
);

SELECT * FROM projectID.dataSet.tableName LIMIT 10;

-- PARTITIONING
-- partitioning can improve query performance by reducing amount of data scanned
-- certain columns are often used for filtering
-- data is partitioned by the selected columns
-- BigQuery will be able to compute the size/rows of the table

-- create a partitioned table
CREATE OR REPLACE TABLE `projectID.dataSet.tableName_partitioned`
PARTITION BY
  DATE(date_column) AS
SELECT * FROM projectID.dataSet.tableName;