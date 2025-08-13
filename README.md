# AI Text Analysis Platform

A comprehensive text analysis platform that offers multiple AI-powered text processing capabilities through a web API. This project showcases various text processing techniques using Python and is deployed on Railway.app.

## 🔗 Live Demo

[View Live Demo](https://web-production-f09c.up.railway.app/)

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
├── railway.toml            # Railway specific configuration
├── runtime.txt             # Python version specification
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