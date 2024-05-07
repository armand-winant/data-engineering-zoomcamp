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
  project = "astral-pursuit-422621-e6"
  region  = "europe-west3"
}