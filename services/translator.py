from deep_translator import GoogleTranslator

def translate_text(text, from_lang='auto', to_lang='en'):
    """
    Translate the given text from one language to another.
    
    Args:
        text (str): The text to translate
        from_lang (str): Source language code (or 'auto' for auto-detection)
        to_lang (str): Target language code
        
    Returns:
        dict: A dictionary containing the translated text and language info
    """
    if not text or len(text.strip()) == 0:
        return {
            "translated_text": "",
            "source_language": from_lang,
            "target_language": to_lang,
            "original_length": 0
        }
    
    # Language code mapping (UI friendly names to ISO codes)
    language_mapping = {
        'english': 'en',
        'german': 'de',
        'spanish': 'es',
        'french': 'fr',
        'italian': 'it',
        'portuguese': 'pt',
        'russian': 'ru',
        'japanese': 'ja',
        'chinese': 'zh-CN',
        'arabic': 'ar',
        'hindi': 'hi'
    }
    
    # Convert language name to code if needed
    if to_lang.lower() in language_mapping:
        to_lang = language_mapping[to_lang.lower()]
    
    # Check if we're actually changing languages
    if to_lang == 'en' and from_lang == 'auto':
        # Skip translation if already in English and source is auto
        return {
            "translated_text": text,
            "source_language": "auto-detected (English)",
            "target_language": "en",
            "original_length": len(text)
        }
    
    try:
        # Perform translation
        translator = GoogleTranslator(source=from_lang, target=to_lang)
        translated_text = translator.translate(text)
        
        # If from_lang was auto, get detected language
        if from_lang == 'auto':
            detected_lang = "auto-detected"
        else:
            detected_lang = from_lang
            
        return {
            "translated_text": translated_text,
            "source_language": detected_lang,
            "target_language": to_lang,
            "original_length": len(text)
        }
    except Exception as e:
        error_message = f"Translation error: {str(e)}"
        print(f"Translation failed: {error_message}")  # Log the error
        
        return {
            "translated_text": error_message,
            "source_language": from_lang,
            "target_language": to_lang,
            "original_length": len(text)
        }