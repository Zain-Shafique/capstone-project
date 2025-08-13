# AI Text Analysis Platform

![AI Text Analysis Platform](c:\Users\Zain\Desktop\Capture1.PNG)

A comprehensive text analysis platform that offers multiple AI-powered text processing capabilities through a web API. This project showcases various text processing techniques using Python and is deployed on Railway.app.

## 🔗 Live Demo

[View Live Demo]()

## ✨ Features

- **📊 Sentiment Analysis**: Analyze the emotional tone of text using TextBlob
- **📝 Text Summarization**: Generate concise summaries from longer texts
- **🔑 Keyword Extraction**: Extract the most important terms from your content
- **✏️ Content Enhancement**: Improve readability with transition phrases
- **🌐 Language Translation**: Translate text between multiple languages

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3 with modern styling features
- Vanilla JavaScript with animations

### Backend
- Python 3.10
- Flask web framework
- Railway.app deployment

### Libraries
- TextBlob for sentiment analysis
- Sumy for text summarization
- NLTK for natural language processing
- Deep-Translator for language translation

## 📁 Project Structure

```
text-analysis-platform/
├── app.py                  # Main Flask application
├── Procfile                # Railway deployment configuration
├── .gitignore              # Git ignore file
├── public/                 # Static frontend assets
│   ├── index.html
│   ├── about.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── services/               # Core text processing functionality
│   ├── __init__.py
│   ├── sentiment_analyzer.py
│   ├── text_summarizer.py
│   ├── keyword_extractor.py
│   ├── content_enhancer.py
│   └── translator.py
├── requirements.txt        # Python dependencies
└── README.md
```

## 📚 API Endpoints Documentation

| Endpoint | Method | Description | Request Body | Response |
|----------|--------|-------------|--------------|----------|
| `/api/analyze_sentiment` | POST | Analyzes sentiment of text | `{ "text": "your text here" }` | Sentiment polarity, category, and subjectivity |
| `/api/summarize` | POST | Creates a summary of text | `{ "text": "your text here", "num_sentences": 3 }` | Summarized text with stats |
| `/api/extract_keywords` | POST | Extracts key terms from text | `{ "text": "your text here", "num_keywords": 5 }` | Top keywords with frequencies |
| `/api/enhance_content` | POST | Improves readability | `{ "text": "your text here" }` | Enhanced text with transition phrases |
| `/api/translate` | POST | Translates text between languages | `{ "text": "your text here", "to_lang": "de" }` | Translated text and language details |

## 🚀 Setup and Installation

### Prerequisites
- Python 3.9+ (3.10 recommended)
- Git

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Zain-Shafique/capstone-project.git
   cd text-analysis-platform
   ```

2. **Create a virtual environment**:
   ```bash
   # Windows
   py -3.10 -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3.10 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download required NLTK data**:
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('averaged_perceptron_tagger')"
   ```

5. **Run the application locally**:
   ```bash
   python app.py
   ```

## ⚠️ Limitations

- Free text processing libraries have usage limitations
- Some language detection and translation may be less accurate for uncommon languages
- Processing very long texts may take longer due to server constraints
- NLTK data needs to be downloaded for keyword extraction to work properly

## 🔮 Future Enhancements

- User accounts to save analysis history
- More advanced text analysis features (entity recognition, topic modeling)
- Batch processing for multiple texts
- Additional translation languages
- Plagiarism detection
- Text readability scoring

## 📊 Project Statistics

- **Last Updated**: 2025-08-13 12:35:09
- **Version**: 1.0.0
- **Status**: Active

---












# AI Text Analysis Platform

A comprehensive text analysis platform that offers multiple AI-powered text processing capabilities through serverless API endpoints. This project showcases various text processing techniques using Python and is deployed on Vercel's serverless architecture.

## 🔗 Live Demo

[View Live Demo](https://test-analysis-platform-8dmvjw8sr-zains-projects-b17c21ef.vercel.app)

## ✨ Features

- **📊 Sentiment Analysis**: Analyze the emotional tone of text using TextBlob
- **📝 Text Summarization**: Generate concise summaries from longer texts
- **🔑 Keyword Extraction**: Extract the most important terms from your content
- **✏️ Content Enhancement**: Improve readability with transition phrases
- **🌐 Language Translation**: Translate text between multiple languages

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3 with modern styling features
- Vanilla JavaScript with animations

### Backend
- Python 3.10 serverless functions
- Vercel serverless deployment

### Libraries
- TextBlob for sentiment analysis
- Sumy for text summarization
- NLTK for natural language processing
- Deep-Translator for language translation

## 📁 Project Structure

```
text-analysis-platform/
├── api/                    # Serverless API endpoints
│   ├── analyze_sentiment.py
│   ├── extract_keywords.py
│   ├── summarize.py
│   ├── enhance_content.py
│   ├── translate.py
│   └── utils/              # Shared utilities
│       ├── __init__.py
│       ├── response_wrapper.py
│       ├── validators.py
│       └── logger.py
├── public/                 # Static frontend assets
│   ├── index.html
│   ├── about.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── services/               # Core text processing functionality
│   ├── __init__.py
│   ├── sentiment_analyzer.py
│   ├── text_summarizer.py
│   ├── keyword_extractor.py
│   ├── content_enhancer.py
│   └── translator.py
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python version specification
├── vercel.json             # Vercel configuration
└── README.md
```

## 📚 API Endpoints Documentation

| Endpoint | Method | Description | Request Body | Response |
|----------|--------|-------------|--------------|----------|
| `/api/analyze_sentiment` | POST | Analyzes sentiment of text | `{ "text": "your text here" }` | Sentiment polarity, category, and subjectivity |
| `/api/summarize` | POST | Creates a summary of text | `{ "text": "your text here", "num_sentences": 3 }` | Summarized text with stats |
| `/api/extract_keywords` | POST | Extracts key terms from text | `{ "text": "your text here", "num_keywords": 5 }` | Top keywords with frequencies |
| `/api/enhance_content` | POST | Improves readability | `{ "text": "your text here" }` | Enhanced text with transition phrases |
| `/api/translate` | POST | Translates text between languages | `{ "text": "your text here", "to_lang": "es" }` | Translated text and language details |

## 🚀 Setup and Installation

### Prerequisites
- Python 3.9+ (3.10 recommended)
- Node.js and npm (for Vercel CLI)
- Git

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Zain-Shafique/text-analysis-platform
   cd text-analysis-platform
   ```

2. **Create a virtual environment**:
   ```bash
   # Windows
   py -3.10 -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3.10 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download required NLTK data**:
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('averaged_perceptron_tagger')"
   ```

5. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

6. **Run locally**:
   ```bash
   vercel dev
   ```

## 📝 Usage Examples

### Example: Sentiment Analysis

```javascript
// Example: Sentiment Analysis request
fetch('/api/analyze_sentiment', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    text: "I absolutely love this amazing product!"
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

Example response:

```json
{
  "status": "success",
  "message": "Sentiment analysis completed successfully",
  "data": {
    "polarity": 0.8,
    "category": "Strongly Positive",
    "subjectivity": 0.75
  }
}
```

### Example: Text Summarization

```javascript
fetch('/api/summarize', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    text: "Your long text here...",
    num_sentences: 3
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## ⚠️ Limitations

- Free text processing libraries have usage limitations
- Some language detection and translation may be less accurate for uncommon languages
- Processing very long texts may take longer due to serverless function constraints
- NLTK data needs to be downloaded for keyword extraction to work properly

## 🔮 Future Enhancements

- User accounts to save analysis history
- More advanced text analysis features (entity recognition, topic modeling)
- Batch processing for multiple texts
- Additional translation languages
- Plagiarism detection
- Text readability scoring

## 📊 Project Statistics

- **Last Updated**: 2025-08-12 17:00:41
- **Version**: 1.0.0
- **Status**: Active

---
