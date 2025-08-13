import nltk
import random
from nltk.tokenize import sent_tokenize

def enhance_content(text):
    """
    Enhance the given text by adding transition phrases.
    
    Args:
        text (str): The text to enhance
        
    Returns:
        dict: A dictionary containing the enhanced text and related stats
    """
    if not text or len(text.strip()) == 0:
        return {
            "enhanced_text": "",
            "original_length": 0,
            "enhanced_length": 0,
            "changes_made": 0
        }
    
    # Ensure we have NLTK punkt
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    
    # Transition phrases to add readability
    transition_phrases = [
        "Furthermore, ",
        "In addition, ",
        "Moreover, ",
        "Similarly, ",
        "Likewise, ",
        "For instance, ",
        "To illustrate, ",
        "Specifically, ",
        "As a result, ",
        "Consequently, ",
        "Therefore, ",
        "Hence, ",
        "In contrast, ",
        "On the other hand, ",
        "However, ",
        "Nevertheless, ",
        "In conclusion, ",
        "To summarize, "
    ]
    
    # Split text into sentences
    sentences = sent_tokenize(text)
    
    # Skip enhancement if text is too short
    if len(sentences) < 3:
        return {
            "enhanced_text": text,
            "original_length": len(text),
            "enhanced_length": len(text),
            "changes_made": 0
        }
    
    # Enhance selected sentences
    enhanced_sentences = sentences.copy()
    changes_made = 0
    
    # Skip the first sentence and enhance approximately every third sentence
    for i in range(1, len(sentences), 3):
        if i < len(sentences):
            # Don't add transitions to very short sentences
            if len(sentences[i].split()) > 4:
                # Choose a random transition phrase
                transition = random.choice(transition_phrases)
                
                # Add transition at the beginning of the sentence
                # If it starts with uppercase, preserve it
                if sentences[i][0].isupper():
                    # Handle case where first word might be a proper noun
                    first_char = sentences[i][0]
                    rest_of_sentence = sentences[i][1:]
                    enhanced_sentences[i] = transition + first_char + rest_of_sentence
                else:
                    # For lowercase starts, capitalize the transition and keep the sentence as is
                    enhanced_sentences[i] = transition + sentences[i]
                
                changes_made += 1
    
    # Join sentences back into text
    enhanced_text = " ".join(enhanced_sentences)
    
    return {
        "enhanced_text": enhanced_text,
        "original_length": len(text),
        "enhanced_length": len(enhanced_text),
        "changes_made": changes_made
    }