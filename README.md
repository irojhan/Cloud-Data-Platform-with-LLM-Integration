# Cloud Data Platform with LLM Integration for Sentiment Analysis

## Objective
Develop an end-to-end cloud-based data pipeline that:
- Downloads and cleans a publicly available sentiment dataset.
- Integrates advanced NLP (using a Hugging Face Transformer) for sentiment analysis and text summarization.
- Deploys on Google Cloud Platform (GCP) with data stored in BigQuery.
- Visualizes insights using an interactive Plotly Dash dashboard.
- Implements testing, logging, and monitoring for robust production deployment.

## Scope
- **Data Ingestion:** Use PySpark to download data from an online source (U.S. Airlines Twitter Sentiment) and perform cleaning.
- **Data Processing:** Transform and load data into BigQuery (or simulate this step locally).
- **Cloud Deployment:** Containerize applications with Docker and provision resources with Terraform.
- **NLP Integration:** Process tweet text using Hugging Face models for sentiment analysis and summarization.
- **Dashboard:** Create a real-time dashboard with Plotly Dash that visualizes sentiment trends.
- **Testing & Monitoring:** Set up unit tests (pytest), logging, and integrate Google Cloud Monitoring.

## Deliverables
- ETL pipeline scripts.
- NLP processing modules.
- Interactive dashboard.
- Dockerfile and Terraform scripts for deployment.
- Unit tests and logging configuration.
- Documentation detailing setup and usage.

