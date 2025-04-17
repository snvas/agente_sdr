from crewai.tools import BaseTool, SerperDevTool
from textblob import TextBlob
from typing import Any

class WebSearchTool(BaseTool):
    name: str = "Web Search"
    description: str = "Search the web for information about a company or person"

    def _run(self, query: str) -> str:
        search = SerperDevTool()
        return search.run(query)

class SentimentAnalysisTool(BaseTool):
    name: str = "Sentiment Analysis"
    description: str = "Analyze the sentiment of a text"

    def _run(self, text: str) -> str:
        analysis = TextBlob(text)
        sentiment = analysis.sentiment.polarity
        if sentiment > 0:
            return "Positive"
        elif sentiment < 0:
            return "Negative"
        else:
            return "Neutral"

web_search = WebSearchTool()
sentiment_tool = SentimentAnalysisTool() 