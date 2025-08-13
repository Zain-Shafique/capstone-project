from flask import Flask, request, jsonify, send_from_directory
import os
import sys
import nltk

# Download NLTK data at startup
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
    
try:
    nltk.data.find('taggers/averaged_perceptron_tagger')
except LookupError:
    nltk.download('averaged_perceptron_tagger')

# Add the project root to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our services
from services.sentiment_analyzer import analyze_sentiment
from services.text_summarizer import summarize_text
from services.keyword_extractor import extract_keywords
from services.content_enhancer import enhance_content
from services.translator import translate_text

# Create Flask app
app = Flask(__name__, static_folder="public")

# CORS headers
@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    return response

# Serve static files
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def serve_static(path):
    if path == "":
        path = "index.html"
    return send_from_directory('public', path)

# API endpoints
@app.route('/api/analyze_sentiment', methods=['POST'])
def api_analyze_sentiment():
    try:
        request_data = request.get_json()
        if not request_data or 'text' not in request_data:
            return jsonify({
                "status": "error",
                "message": "Missing required parameter: text"
            }), 400
            
        text = request_data.get('text', '')
        result = analyze_sentiment(text)
        
        return jsonify({
            "status": "success",
            "message": "Sentiment analysis completed successfully",
            "data": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error processing request: {str(e)}"
        }), 500

@app.route('/api/summarize', methods=['POST'])
def api_summarize():
    try:
        request_data = request.get_json()
        if not request_data or 'text' not in request_data:
            return jsonify({
                "status": "error",
                "message": "Missing required parameter: text"
            }), 400
            
        text = request_data.get('text', '')
        num_sentences = request_data.get('num_sentences', 3)
        
        try:
            num_sentences = int(num_sentences)
            if num_sentences < 1:
                num_sentences = 3
        except (ValueError, TypeError):
            num_sentences = 3
            
        result = summarize_text(text, num_sentences)
        
        return jsonify({
            "status": "success",
            "message": "Text summarization completed successfully",
            "data": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error processing request: {str(e)}"
        }), 500

@app.route('/api/extract_keywords', methods=['POST'])
def api_extract_keywords():
    try:
        request_data = request.get_json()
        if not request_data or 'text' not in request_data:
            return jsonify({
                "status": "error",
                "message": "Missing required parameter: text"
            }), 400
            
        text = request_data.get('text', '')
        num_keywords = request_data.get('num_keywords', 5)
        
        try:
            num_keywords = int(num_keywords)
            if num_keywords < 1:
                num_keywords = 5
        except (ValueError, TypeError):
            num_keywords = 5
            
        result = extract_keywords(text, num_keywords)
        
        return jsonify({
            "status": "success",
            "message": "Keyword extraction completed successfully",
            "data": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error processing request: {str(e)}"
        }), 500

@app.route('/api/enhance_content', methods=['POST'])
def api_enhance_content():
    try:
        request_data = request.get_json()
        if not request_data or 'text' not in request_data:
            return jsonify({
                "status": "error",
                "message": "Missing required parameter: text"
            }), 400
            
        text = request_data.get('text', '')
        result = enhance_content(text)
        
        return jsonify({
            "status": "success",
            "message": "Content enhancement completed successfully",
            "data": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error processing request: {str(e)}"
        }), 500

@app.route('/api/translate', methods=['POST'])
def api_translate():
    try:
        request_data = request.get_json()
        if not request_data or 'text' not in request_data:
            return jsonify({
                "status": "error",
                "message": "Missing required parameter: text"
            }), 400
            
        text = request_data.get('text', '')
        from_lang = request_data.get('from_lang', 'auto')
        to_lang = request_data.get('to_lang', 'en')
        
        result = translate_text(text, from_lang, to_lang)
        
        return jsonify({
            "status": "success",
            "message": "Translation completed successfully",
            "data": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error processing request: {str(e)}"
        }), 500

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)