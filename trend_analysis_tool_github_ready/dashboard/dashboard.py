import streamlit as st
from storage.database import fetch_data
from nlp.sentiment_analysis import analyze_sentiment
from nlp.topic_modeling import extract_topics
from analysis.backtesting import compare_trends
import datetime

def run_dashboard():
    st.title("Trend Analysis & Backtesting Tool")

    start = st.date_input("Start Date", datetime.date.today() - datetime.timedelta(days=30))
    end = st.date_input("End Date", datetime.date.today())
    start_ts = datetime.datetime.combine(start, datetime.time.min).timestamp()
    end_ts = datetime.datetime.combine(end, datetime.time.max).timestamp()

    data = fetch_data(start_ts, end_ts)

    if data:
        contents = [d[4] for d in data]
        sentiments = [analyze_sentiment(c) for c in contents]
        st.line_chart(sentiments)
        topics = extract_topics(contents)
        st.write("Extracted Topics:")
        for topic in topics:
            st.text(topic)
    else:
        st.warning("No data available in selected date range.")
