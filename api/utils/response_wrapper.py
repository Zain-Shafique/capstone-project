from http.server import BaseHTTPRequestHandler
import json

def make_response(status_code, message, data=None):
    """
    Creates a standardized API response.
    
    Args:
        status_code (int): HTTP status code
        message (str): Response message
        data (any, optional): Response data payload
        
    Returns:
        dict: Standardized response structure
    """
    response = {
        "status": "success" if 200 <= status_code < 300 else "error",
        "message": message,
    }
    
    if data is not None:
        response["data"] = data
        
    return {
        "statusCode": status_code,
        "body": json.dumps(response),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "POST, OPTIONS"
        }
    }

class VercelHandler(BaseHTTPRequestHandler):
    """Base handler for Vercel serverless functions"""
    
    def parse_body(self):
        """Parse JSON body from request"""
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            return {}
            
        request_body = self.rfile.read(content_length)
        try:
            return json.loads(request_body)
        except json.JSONDecodeError:
            return {}