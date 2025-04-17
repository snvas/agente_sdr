from crewai_tools import WebsiteSearchTool
from textblob import TextBlob
from typing import Any
from crewai.tools import BaseTool
class SentimentAnalysisTool(BaseTool):
    name: str = "Sentiment Analysis"
    description: str = "Analyzes the sentiment of text to determine if it's positive or negative."

    def _run(self, text: str) -> str:
        analysis = TextBlob(text)
        sentiment = analysis.sentiment.polarity
        if sentiment > 0:
            return "Positive"
        elif sentiment < 0:
            return "Negative"
        else:
            return "Neutral"

# Initialize tools
web_search = WebsiteSearchTool()
sentiment_tool = SentimentAnalysisTool()