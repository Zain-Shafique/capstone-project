document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const inputText = document.getElementById('inputText');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const options = document.querySelectorAll('.option');
    const resultsSection = document.getElementById('resultsSection');
    const loader = document.getElementById('loader');
    const resultsContent = document.getElementById('resultsContent');
    
    // Language code mapping for translation
    const languageMapping = {
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
    };
    
    let selectedOption = null;
    
    // Add animation class to options with delay
    options.forEach((option, index) => {
        setTimeout(() => {
            option.style.animation = `fadeIn 0.5s forwards`;
            option.style.opacity = '1';
        }, index * 100);
        
        option.addEventListener('click', function() {
            options.forEach(opt => opt.classList.remove('selected'));
            this.classList.add('selected');
            selectedOption = this.dataset.type;
            
            // Show a little bounce animation when selected
            this.animate([
                { transform: 'scale(1)' },
                { transform: 'scale(1.05)' },
                { transform: 'scale(1)' }
            ], {
                duration: 300,
                easing: 'ease-in-out'
            });
        });
    });
    
    // Analyze button click handler
    analyzeBtn.addEventListener('click', function() {
        const text = inputText.value.trim();
        
        if (!text) {
            showError('Please enter some text to analyze');
            return;
        }
        
        if (!selectedOption) {
            showError('Please select an analysis type');
            return;
        }
        
        // Show results section and loader
        resultsSection.style.display = 'block';
        loader.style.display = 'flex';
        resultsContent.innerHTML = '';
        
        // Scroll to results with smooth animation
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        
        // Button click animation
        this.classList.add('clicked');
        setTimeout(() => this.classList.remove('clicked'), 300);
        
        // Prepare request data
        const requestData = { text };
        
        // Add option-specific parameters
        switch (selectedOption) {
            case 'summarize':
                const numSentences = document.getElementById('numSentences').value;
                requestData.num_sentences = parseInt(numSentences);
                break;
            case 'keywords':
                const numKeywords = document.getElementById('numKeywords').value;
                requestData.num_keywords = parseInt(numKeywords);
                break;
            case 'translate':
                const targetLangElement = document.getElementById('targetLang');
                let targetLang = targetLangElement.value;
                
                // Convert language name to code if needed
                if (targetLang.toLowerCase() in languageMapping) {
                    targetLang = languageMapping[targetLang.toLowerCase()];
                }
                
                requestData.to_lang = targetLang;
                requestData.from_lang = 'auto';
                break;
        }
        
        // Make API request
        fetch(`/api/${getEndpoint(selectedOption)}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestData)
        })
        .then(response => response.json())
        .then(data => {
            loader.style.display = 'none';
            
            if (data.status === 'error') {
                showError(data.message);
                return;
            }
            
            // Display results based on the selected option
            displayResults(selectedOption, data.data);
        })
        .catch(error => {
            loader.style.display = 'none';
            showError('An error occurred while processing your request');
            console.error('Error:', error);
        });
    });
    
    // Get the correct endpoint based on the selected option
    function getEndpoint(option) {
        switch (option) {
            case 'sentiment':
                return 'analyze_sentiment';
            case 'summarize':
                return 'summarize';
            case 'keywords':
                return 'extract_keywords';
            case 'enhance':
                return 'enhance_content';
            case 'translate':
                return 'translate';
            default:
                return '';
        }
    }
    
    // Display error message
    function showError(message) {
        resultsSection.style.display = 'block';
        loader.style.display = 'none';
        resultsContent.innerHTML = `
            <div class="error-message">
                <p><i class="fas fa-exclamation-circle"></i> ${message}</p>
            </div>
        `;
    }
    
    // Display results based on the selected option
    function displayResults(option, data) {
        let resultHTML = '';
        
        switch (option) {
            case 'sentiment':
                resultHTML = createSentimentResult(data);
                break;
            case 'summarize':
                resultHTML = createSummaryResult(data);
                break;
            case 'keywords':
                resultHTML = createKeywordsResult(data);
                break;
            case 'enhance':
                resultHTML = createEnhancementResult(data);
                break;
            case 'translate':
                resultHTML = createTranslationResult(data);
                break;
        }
        
        resultsContent.innerHTML = resultHTML;
        
        // Add staggered animation to result cards
        const resultCards = document.querySelectorAll('.result-card');
        resultCards.forEach((card, index) => {
            card.style.animationDelay = `${index * 0.15}s`;
        });
    }
    
    // Create sentiment analysis result HTML
    function createSentimentResult(data) {
        let sentimentClass = '';
        let sentimentIcon = '';
        
        switch (data.category) {
            case 'Strongly Positive':
                sentimentClass = 'sentiment-strongly-positive';
                sentimentIcon = '<i class="fas fa-laugh-beam"></i>';
                break;
            case 'Positive':
                sentimentClass = 'sentiment-positive';
                sentimentIcon = '<i class="fas fa-smile"></i>';
                break;
            case 'Neutral':
                sentimentClass = 'sentiment-neutral';
                sentimentIcon = '<i class="fas fa-meh"></i>';
                break;
            case 'Negative':
                sentimentClass = 'sentiment-negative';
                sentimentIcon = '<i class="fas fa-frown"></i>';
                break;
            case 'Strongly Negative':
                sentimentClass = 'sentiment-strongly-negative';
                sentimentIcon = '<i class="fas fa-angry"></i>';
                break;
        }
        
        return `
            <div class="result-card">
                <h4><i class="fas fa-chart-line"></i> Sentiment Analysis Results</h4>
                <div class="metadata">
                    <div class="meta-item">
                        <strong>Polarity:</strong> ${data.polarity.toFixed(2)}
                    </div>
                    <div class="meta-item">
                        <strong>Subjectivity:</strong> ${data.subjectivity.toFixed(2)}
                    </div>
                </div>
                <div class="result-content">
                    <p>The text has a <span class="sentiment-indicator ${sentimentClass}">${sentimentIcon} ${data.category}</span> sentiment.</p>
                    <p>Interpretation:</p>
                    <ul>
                        <li><strong>Polarity</strong> ranges from -1 (negative) to 1 (positive).</li>
                        <li><strong>Subjectivity</strong> ranges from 0 (objective) to 1 (subjective).</li>
                    </ul>
                </div>
            </div>
        `;
    }
    
    // Create text summarization result HTML
    function createSummaryResult(data) {
        return `
            <div class="result-card">
                <h4><i class="fas fa-file-alt"></i> Text Summarization Results</h4>
                <div class="metadata">
                    <div class="meta-item">
                        <strong><i class="fas fa-text-width"></i> Original Length:</strong> ${data.original_length} characters
                    </div>
                    <div class="meta-item">
                        <strong><i class="fas fa-compress-alt"></i> Summary Length:</strong> ${data.summary_length} characters
                    </div>
                    <div class="meta-item">
                        <strong><i class="fas fa-percentage"></i> Reduction:</strong> ${data.reduction_percentage}%
                    </div>
                </div>
                <div class="result-content">
                    <p><strong>Summary:</strong></p>
                    <p>${data.summary}</p>
                </div>
            </div>
        `;
    }
    
    // Create keyword extraction result HTML
    function createKeywordsResult(data) {
        const keywordsHTML = Object.entries(data.keywords)
            .map(([keyword, count]) => `<span class="keyword-tag"><i class="fas fa-tag"></i> ${keyword} (${count})</span>`)
            .join('');
        
        return `
            <div class="result-card">
                <h4><i class="fas fa-key"></i> Keyword Extraction Results</h4>
                <div class="metadata">
                    <div class="meta-item">
                        <strong><i class="fas fa-font"></i> Total Words:</strong> ${data.word_count}
                    </div>
                    <div class="meta-item">
                        <strong><i class="fas fa-tags"></i> Keywords Extracted:</strong> ${data.total_extracted}
                    </div>
                </div>
                <div class="result-content">
                    <p><strong>Top Keywords:</strong></p>
                    <div class="keywords-list">
                        ${keywordsHTML}
                    </div>
                </div>
            </div>
        `;
    }
    
    // Create content enhancement result HTML
    function createEnhancementResult(data) {
        return `
            <div class="result-card">
                <h4><i class="fas fa-pen-fancy"></i> Content Enhancement Results</h4>
                <div class="metadata">
                    <div class="meta-item">
                        <strong><i class="fas fa-text-width"></i> Original Length:</strong> ${data.original_length} characters
                    </div>
                    <div class="meta-item">
                        <strong><i class="fas fa-expand-alt"></i> Enhanced Length:</strong> ${data.enhanced_length} characters
                    </div>
                    <div class="meta-item">
                        <strong><i class="fas fa-edit"></i> Changes Made:</strong> ${data.changes_made}
                    </div>
                </div>
                <div class="result-content">
                    <p><strong>Enhanced Text:</strong></p>
                    <p>${data.enhanced_text}</p>
                </div>
            </div>
        `;
    }
    
    // Create translation result HTML
    function createTranslationResult(data) {
        // Prepare display name for target language
        let displayTargetLang = data.target_language;
        for (const [name, code] of Object.entries(languageMapping)) {
            if (code === data.target_language) {
                displayTargetLang = name.charAt(0).toUpperCase() + name.slice(1);
                break;
            }
        }
        
        return `
            <div class="result-card">
                <h4><i class="fas fa-language"></i> Translation Results</h4>
                <div class="metadata">
                    <div class="meta-item">
                        <strong><i class="fas fa-globe"></i> Source Language:</strong> ${data.source_language}
                    </div>
                    <div class="meta-item">
                        <strong><i class="fas fa-globe-americas"></i> Target Language:</strong> ${displayTargetLang} (${data.target_language})
                    </div>
                    <div class="meta-item">
                        <strong><i class="fas fa-text-width"></i> Original Length:</strong> ${data.original_length} characters
                    </div>
                </div>
                <div class="result-content">
                    <p><strong>Translated Text:</strong></p>
                    <p>${data.translated_text}</p>
                </div>
            </div>
        `;
    }
    
    // Add some UI interactions
    inputText.addEventListener('focus', function() {
        this.style.boxShadow = '0 0 0 3px rgba(67, 97, 238, 0.2)';
    });
    
    inputText.addEventListener('blur', function() {
        this.style.boxShadow = 'inset 0 1px 3px rgba(0, 0, 0, 0.1)';
    });
});