import json
import time
from datetime import datetime

def log_request(route, request_body, response, start_time=None):
    """
    Logs information about a request.
    
    Args:
        route (str): The API route that was accessed
        request_body (dict): The request body
        response (dict): The response
        start_time (float, optional): Start time of request processing
    """
    end_time = time.time()
    processing_time = round((end_time - start_time) * 1000, 2) if start_time else None
    
    log_entry = {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "route": route,
        "status": response.get("statusCode", 0),
        "processing_time_ms": processing_time
    }
    
    # In a real application, you would write this to a log file or service
    # For Vercel, logs are automatically collected and viewable in the dashboard
    print(json.dumps(log_entry))