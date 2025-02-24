import pytest
from nlp_processing import analyze_sentiment, summarize_text

def test_analyze_sentiment_positive():
    text = "I absolutely love this airline!"
    result = analyze_sentiment(text)
    # Ensure that the result contains a sentiment label that indicates positivity
    assert result[0]['label'].upper() in ["POSITIVE", "POS"]

def test_summarize_text_length():
    long_text = (
        "Traveling can be a stressful experience when flights are delayed and services are lacking. "
        "However, a well-managed airline can turn the experience around and ensure customer satisfaction."
    )
    summary = summarize_text(long_text, max_length=40, min_length=20)
    summary_text = summary[0]['summary_text']
    word_count = len(summary_text.split())
    assert 20 <= word_count <= 40

if __name__ == '__main__':
    pytest.main()
