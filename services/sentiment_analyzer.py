from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: A dictionary containing sentiment analysis results
    """
    if not text or len(text.strip()) == 0:
        return {
            "polarity": 0,
            "subjectivity": 0,
            "category": "Neutral"
        }
    
    # Create TextBlob object
    blob = TextBlob(text)
    
    # Get polarity and subjectivity
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Determine sentiment category
    if polarity >= 0.5:
        category = "Strongly Positive"
    elif polarity > 0:
        category = "Positive"
    elif polarity == 0:
        category = "Neutral"
    elif polarity > -0.5:
        category = "Negative"
    else:
        category = "Strongly Negative"
    
    return {
        "polarity": polarity,
        "subjectivity": subjectivity,
        "category": category
    }