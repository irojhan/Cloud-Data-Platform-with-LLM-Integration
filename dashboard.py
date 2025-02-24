import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import logging
from pyspark.sql import SparkSession

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_cleaned_data(parquet_path: str) -> pd.DataFrame:
    logging.info(f"Loading cleaned data from {parquet_path}...")
    # For demonstration, we use Spark to read the parquet file and convert to Pandas DataFrame.
    spark = SparkSession.builder.appName("LoadCleanedData").getOrCreate()
    df = spark.read.parquet(parquet_path)
    # In this dataset, assume we have a "tweet_created" field (or use a simulated date)
    # For demo purposes, we create a fake date column.
    import pyspark.sql.functions as F
    df = df.withColumn("tweet_date", F.current_date())
    pdf = df.toPandas()
    spark.stop()
    return pdf

def create_dashboard_figure(df: pd.DataFrame):
    logging.info("Creating dashboard figure...")
    # For demonstration, we aggregate tweet sentiment scores by date.
    # Since our dataset doesn’t include computed sentiment scores, we simulate a trend.
    if 'tweet_date' not in df.columns:
        df['tweet_date'] = pd.to_datetime('today')
    df_grouped = df.groupby('tweet_date').size().reset_index(name='tweet_count')
    fig = px.line(df_grouped, x="tweet_date", y="tweet_count", title="Tweet Volume Over Time")
    return fig

# Initialize Dash app
app = dash.Dash(__name__)

# Load data from the parquet output of the ETL step
parquet_path = "/tmp/cleaned_tweets_data"  # Ensure this matches the output in data_ingestion_online.py
df = load_cleaned_data(parquet_path)
fig = create_dashboard_figure(df)

app.layout = html.Div(children=[
    html.H1(children="Airline Tweets Sentiment Dashboard"),
    dcc.Graph(id="sentiment-graph", figure=fig),
    html.Div(children="This dashboard displays the tweet volume over time, derived from the cleaned airline sentiment dataset."),
])

if __name__ == '__main__':
    logging.info("Starting Dash server...")
    app.run_server(debug=True)
