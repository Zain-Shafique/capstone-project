def validate_text_input(request_body):
    """
    Validates if the request body contains valid text input.
    
    Args:
        request_body (dict): The parsed request body
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not request_body:
        return False, "Request body is empty or malformed"
    
    if 'text' not in request_body:
        return False, "Missing 'text' field in request"
    
    text = request_body.get('text', '')
    if not isinstance(text, str):
        return False, "'text' must be a string"
    
    if not text.strip():
        return False, "'text' cannot be empty"
        
    return True, None