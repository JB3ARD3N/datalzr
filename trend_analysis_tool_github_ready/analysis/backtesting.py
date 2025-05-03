from nlp.sentiment_analysis import analyze_sentiment

def compare_trends(current_data, historical_data):
    current_sentiments = [analyze_sentiment(e[4]) for e in current_data]
    historical_sentiments = [analyze_sentiment(e[4]) for e in historical_data]
    current_avg = sum(current_sentiments) / len(current_sentiments) if current_sentiments else 0
    historical_avg = sum(historical_sentiments) / len(historical_sentiments) if historical_sentiments else 0
    return {
        "current_sentiment_avg": current_avg,
        "historical_sentiment_avg": historical_avg,
        "change": current_avg - historical_avg
    }
