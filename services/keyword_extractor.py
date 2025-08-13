import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

def extract_keywords(text, num_keywords=5):
    """
    Extract keywords from the given text.
    
    Args:
        text (str): The text to extract keywords from
        num_keywords (int): Number of keywords to extract
        
    Returns:
        dict: A dictionary containing the keywords and related stats
    """
    if not text or len(text.strip()) == 0:
        return {
            "keywords": {},
            "word_count": 0,
            "total_extracted": 0
        }
    
    # Ensure we have NLTK resources
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('punkt')
        nltk.download('stopwords')
    
    # Tokenize and clean text
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    
    # Remove punctuation and stopwords
    cleaned_tokens = [
        word for word in tokens 
        if word not in stop_words and word not in string.punctuation
        and len(word) > 2  # Remove very short words
    ]
    
    # Count word frequencies
    word_counts = Counter(cleaned_tokens)
    
    # Get the most common words
    keywords = dict(word_counts.most_common(num_keywords))
    
    return {
        "keywords": keywords,
        "word_count": len(tokens),
        "total_extracted": len(keywords)
    }