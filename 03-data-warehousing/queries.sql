-- CREATE A NEW EXTERNAL TABLE FROM GCS DATA
CREATE OR REPLACE EXTERNAL TABLE 'projectID.dataSet.tableName'
OPTIONS (
  format = 'CSV',
  uris = ['gs://bucketName/folderName/files_*.csv']
)