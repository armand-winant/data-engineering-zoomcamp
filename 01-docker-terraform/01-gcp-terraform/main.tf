terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.28.0"
    }
  }
}

provider "google" {
  project = "data-engineering-zoomcamp-armandwinant"
  region  = "europe-west3"
}