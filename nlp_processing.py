import logging
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize NLP pipelines
logging.info("Initializing NLP pipelines...")
sentiment_analyzer = pipeline("sentiment-analysis")
summarizer = pipeline("summarization")

def analyze_sentiment(text: str):
    logging.info("Analyzing sentiment...")
    result = sentiment_analyzer(text)
    logging.info(f"Sentiment result: {result}")
    return result

def summarize_text(text: str, max_length=50, min_length=25):
    logging.info("Generating summary...")
    result = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    logging.info(f"Summary result: {result}")
    return result

if __name__ == '__main__':
    sample_tweet = "I absolutely love the service of this airline! It was a great experience."
    analyze_sentiment(sample_tweet)

    long_review = (
        "Traveling can be a stressful experience, but when the airline staff are courteous and the flight is comfortable, "
        "it makes a significant difference. Overall, my journey was pleasant and I look forward to flying again."
    )
    summarize_text(long_review)
