import logging
import os
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_dataset(url: str, local_path: str):
    logging.info(f"Downloading dataset from {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_path, "wb") as f:
            f.write(response.content)
        logging.info(f"Dataset downloaded and saved to {local_path}")
    else:
        logging.error(f"Failed to download dataset. Status code: {response.status_code}")
        raise Exception("Download failed.")

def main():
    # Initialize Spark session
    logging.info("Starting Spark session...")
    spark = SparkSession.builder \
        .appName("OnlineSentimentDataset_ETL") \
        .getOrCreate()

    # URL for the U.S. Airlines Twitter Sentiment dataset
    dataset_url = "https://raw.githubusercontent.com/kolaveridi/kaggle-Twitter-US-Airline-Sentiment-/master/Tweets.csv"
    local_file_path = "/tmp/Tweets.csv"

    # Download the dataset if not already downloaded
    if not os.path.exists(local_file_path):
        download_dataset(dataset_url, local_file_path)
    
    logging.info(f"Reading dataset from {local_file_path}...")
    df = spark.read.csv(local_file_path, header=True, inferSchema=True)

    # Data Cleaning: Trim whitespace for all string columns and drop rows with null tweet text
    logging.info("Cleaning data...")
    clean_df = df.select([trim(col(c)).alias(c) for c in df.columns]).dropna(subset=["text"])

    # Show schema and a sample of the cleaned data
    clean_df.printSchema()
    logging.info("Sample cleaned data:")
    clean_df.show(5)

    # For demonstration, write the cleaned data to a local Parquet directory (simulate loading to BigQuery)
    output_path = "/tmp/cleaned_tweets_data"
    logging.info(f"Writing cleaned data to {output_path}...")
    clean_df.write.mode("overwrite").parquet(output_path)

    logging.info("ETL process complete.")
    spark.stop()

if __name__ == '__main__':
    main()
