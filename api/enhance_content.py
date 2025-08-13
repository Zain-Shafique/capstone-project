from http.server import BaseHTTPRequestHandler
import json
import time
from api.utils.response_wrapper import make_response
from api.utils.validators import validate_text_input
from api.utils.logger import log_request
from services.content_enhancer import enhance_content

class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_POST(self):
        start_time = time.time()
        
        # Parse the request body
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length == 0:
            response = make_response(400, "Request body is empty")
            self._send_response(response)
            log_request("/api/enhance_content", {}, response, start_time)
            return
            
        request_body = self.rfile.read(content_length)
        try:
            request_data = json.loads(request_body)
        except json.JSONDecodeError:
            response = make_response(400, "Invalid JSON in request body")
            self._send_response(response)
            log_request("/api/enhance_content", {}, response, start_time)
            return
        
        # Validate input
        is_valid, error_message = validate_text_input(request_data)
        if not is_valid:
            response = make_response(400, error_message)
            self._send_response(response)
            log_request("/api/enhance_content", request_data, response, start_time)
            return
        
        # Process the request
        try:
            text = request_data.get('text', '')
            result = enhance_content(text)
            response = make_response(200, "Content enhancement completed successfully", result)
        except Exception as e:
            response = make_response(500, f"Error processing request: {str(e)}")
        
        # Send the response
        self._send_response(response)
        log_request("/api/enhance_content", request_data, response, start_time)
    
    def _send_response(self, response):
        self.send_response(response["statusCode"])
        for header, value in response["headers"].items():
            self.send_header(header, value)
        self.end_headers()
        self.wfile.write(response["body"].encode())