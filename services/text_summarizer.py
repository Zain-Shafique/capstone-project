from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk

def summarize_text(text, num_sentences=3):
    """
    Summarize the given text.
    
    Args:
        text (str): The text to summarize
        num_sentences (int): Number of sentences in the summary
        
    Returns:
        dict: A dictionary containing the summary and related stats
    """
    if not text or len(text.strip()) == 0:
        return {
            "summary": "",
            "original_length": 0,
            "summary_length": 0,
            "reduction_percentage": 0
        }
    
    # Ensure we have NLTK punkt
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    
    # Create parser
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    # Create summarizer
    stemmer = Stemmer("english")
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words("english")
    
    # Generate summary
    summary_sentences = summarizer(parser.document, num_sentences)
    summary = " ".join([str(sentence) for sentence in summary_sentences])
    
    # Calculate statistics
    original_length = len(text)
    summary_length = len(summary)
    
    if original_length > 0:
        reduction_percentage = round(100 - (summary_length / original_length * 100))
    else:
        reduction_percentage = 0
    
    return {
        "summary": summary,
        "original_length": original_length,
        "summary_length": summary_length,
        "reduction_percentage": reduction_percentage
    }