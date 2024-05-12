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

-- partitioning can be done on different data types: time-unit, integer range
-- partitioning should split the data evenly

-- create a partitioned table
CREATE OR REPLACE TABLE `projectID.dataSet.tableName_partitioned`
PARTITION BY
  DATE(date_column) AS
SELECT * FROM projectID.dataSet.tableName;

-- CLUSTERING
-- clustering can further improve cost and query performance
-- clustering order is important as it determines the sorting of the data

CREATE OR REPLACE TABLE `projectID.dataSet.tableName_partitioned`
PARTITION BY DATE(date_column)
CLUSTER BY clusteringColumn AS
SELECT * FROM projectID.dataSet.tableName;


-- the cost benefits of clustering are unknown (unlike partitioning)
-- use clustering when more granularity is required (filtering on multiple columns)
-- use clustering over partitioning when the oartition results in a small amount of data per partition
-- use clustering over partitioning when partitions are modified frequently
