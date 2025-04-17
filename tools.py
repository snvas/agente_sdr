from crewai_tools import WebsiteSearchTool, tool

@tool("Sentiment Analysis Tool")
def sentiment_tool(text: str) -> str:
    """Analyzes the sentiment of text."""
    from textblob import TextBlob
    blob = TextBlob(text)
    return "Positive" if blob.sentiment.polarity > 0 else "Negative"

web_search = WebsiteSearchTool()