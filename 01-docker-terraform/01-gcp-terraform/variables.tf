variable "project_id" {
  description = "Project ID"
  default = "astral-pursuit-422621-e6"
}

variable "project_location" {
  description = "Project location"
  default = "EU"
}

variable "project_region" {
  description = "Project region"
  default = "europe-west3"
}

variable "bq_dataset_name" {
  description = "my BigQuery dataset name"
  default = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "my GCS bucket name"
  default = "astral-pursuit-422621-e6-terra-bucket"
}

variable "gcs_bucket_storage_class" {
  description = "my GCS bucket class"
  default = "STANDARD"
}