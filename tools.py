from crewai.tools import BaseTool
from textblob import TextBlob
from crewai_tools import SerperDevTool
from typing import Any

class SentimentAnalysisTool(BaseTool):
    name: str = "sentiment_analysis"
    description: str = "Analyzes the sentiment of text to ensure positive and engaging communication."
    return_direct: bool = True

    def _run(self, text: str) -> str:
        # Using TextBlob for sentiment analysis
        analysis = TextBlob(text)
        
        # Get polarity score (-1 to 1)
        polarity = analysis.sentiment.polarity
        
        # Classify sentiment
        if polarity > 0.3:
            return "muito positivo"
        elif polarity > 0:
            return "positivo"
        elif polarity == 0:
            return "neutro"
        elif polarity > -0.3:
            return "negativo"
        else:
            return "muito negativo"

    async def _arun(self, text: str) -> str:
        raise NotImplementedError("This tool does not support async")

# Initialize tools
web_search = SerperDevTool()
web_search.name = "web_search"  # Override the name to match the YAML configuration
sentiment_tool = SentimentAnalysisTool() 