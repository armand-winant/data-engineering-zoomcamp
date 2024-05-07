terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.28.0"
    }
  }
}

provider "google" {
  credentials = ".keys/my-creds.json"
  project     = "astral-pursuit-422621-e6"
  region      = "europe-west3"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "astral-pursuit-422621-e6-terra-bucket"
  location      = "EU"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "demo-dataset" {
  dataset_id    = "demo_dataset"
  friendly_name = "test"
  description   = "This is a test description"
  location      = "EU"
}