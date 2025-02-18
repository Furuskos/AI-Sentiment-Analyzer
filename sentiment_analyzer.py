from textblob import TextBlob

def analyze_sentiment(text):
    """Analyzes the sentiment of a given text."""
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity

    if sentiment > 0:
        return "Positive 😊"
    elif sentiment < 0:
        return "Negative 😡"
    else:
        return "Neutral 😐"

if __name__ == "__main__":
    user_text = input("Enter text to analyze: ")
    print("Sentiment:", analyze_sentiment(user_text))
