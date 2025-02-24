provider "google" {
  project = "project-4"
  region  = "us-central1"
}

resource "google_storage_bucket" "raw_data_bucket" {
  name     = "twitt_us_airline"
  location = "US"
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id                  = "twitt_us_airline"
  location                    = "US"
  delete_contents_on_destroy  = true
}
