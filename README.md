# Spam Email Detection Model

[![Python Version](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![API Status](https://img.shields.io/badge/API-live-brightgreen)](https://spam-email-api-ece2.onrender.com/docs)
[![Deployed on Render](https://img.shields.io/badge/deployed%20on-Render-46E3B7)](https://render.com)
[![Status](https://img.shields.io/badge/status-in%20development-orange)](https://github.com/mosesamwoma/spam-email-detection-model)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A machine learning API for detecting spam emails and messages using TF-IDF vectorization and classification algorithms. Built with FastAPI and deployed on Render.

> **⚠️ Project Status:** This project is currently under active development.

## 🎬 API in Action

See the Spam Detection API in action! The demo below shows real-time email classification through the interactive Swagger UI interface.

**What you're seeing:**
- Interactive API testing via Swagger UI
- Real-time spam classification with confidence scores
- Instant JSON responses with predictions
- Simple integration with any application

## 📊 Project Status

- ✅ **Trained Model**: Logistic Regression classifier trained and optimized
- ✅ **TF-IDF Vectorizer**: Feature extraction pipeline deployed
- ✅ **REST API**: Live and production-ready
- ✅ **Interactive Docs**: Swagger UI available for testing
- ✅ **Cloud Deployment**: Hosted on Render with 99.9% uptime
- ✅ **Chrome Extension**: Built and ready for testing (pending Web Store deployment)
- 🚧 **Extended Features**: Authentication and batch processing in development

## 🎯 Overview

Email spam detection is essential for maintaining secure and efficient communication systems. This project implements a machine learning solution using TF-IDF vectorization and Logistic Regression to automatically identify and filter spam emails with high accuracy.

The model is deployed as a REST API, making it simple to integrate spam detection capabilities into any application or workflow. A Chrome extension is also available for browser-based email protection.

## ✨ Key Features

### Core API Features
- **Advanced Text Processing**: Comprehensive cleaning and normalization pipeline
- **TF-IDF Vectorization**: Efficient text-to-vector transformation
- **High-Accuracy Classification**: Trained model with optimized performance metrics
- **REST API**: Fast, scalable API with JSON responses
- **Interactive Documentation**: Built-in Swagger UI for easy testing
- **Real-time Predictions**: Instant spam classification with confidence scores
- **Health Monitoring**: Built-in health check endpoint
- **Production Ready**: Deployed on reliable cloud infrastructure

### Chrome Extension (Coming Soon)
- **Browser Integration**: Seamless email checking directly in your browser
- **One-Click Detection**: Instant spam analysis with a single click
- **Privacy-Focused**: Email content processed securely through the API
- **Visual Feedback**: Clear indicators for spam and legitimate emails
- **Lightweight**: Minimal resource usage for smooth browsing

## 🚀 Quick Start - Using the API

### Live API Endpoint

The API is live and ready to use! No installation or setup required.

**Base URL**: `https://spam-email-api-ece2.onrender.com`

**Interactive Docs**: [https://spam-email-api-ece2.onrender.com/docs](https://spam-email-api-ece2.onrender.com/docs)

### Example Usage

#### Using cURL

```bash
curl -X POST "https://spam-email-api-ece2.onrender.com/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "email_text": "Congratulations! You have won $1,000,000! Click here to claim now!",
    "return_confidence": true
  }'
```

#### Using Python

```python
import requests

url = "https://spam-email-api-ece2.onrender.com/api/v1/predict"
payload = {
    "email_text": "Congratulations! You have won $1,000,000! Click here to claim now!",
    "return_confidence": True
}

response = requests.post(url, json=payload)
result = response.json()

print(f"Prediction: {result['prediction']}")
print(f"Confidence: {result['confidence']:.2%}")
```

## 🔌 Chrome Extension

### Installation (Developer Mode)

The Chrome extension is currently available for testing but not yet published to the Chrome Web Store.

**Repository**: [https://github.com/mosesamwoma/chrome-extension](https://github.com/mosesamwoma/chrome-extension)

#### Manual Installation Steps:

1. **Clone the extension repository**
   ```bash
   git clone https://github.com/mosesamwoma/chrome-extension.git
   cd chrome-extension
   ```

2. **Open Chrome Extensions page**
   - Navigate to `chrome://extensions/`
   - Enable "Developer mode" (toggle in top right)

3. **Load the extension**
   - Click "Load unpacked"
   - Select the cloned extension directory

4. **Start using**
   - The extension icon will appear in your browser toolbar
   - Click it to analyze email text for spam

### Extension Features

- 🎯 **Instant Analysis**: Check emails with one click
- 🔒 **Secure**: All processing via encrypted API calls
- 💡 **Smart Alerts**: Visual indicators for spam detection
- ⚡ **Fast**: Real-time results in seconds
- 🎨 **Clean UI**: Simple, intuitive interface

> **Note**: The extension will be published to the Chrome Web Store soon for easier installation.

## 📡 API Documentation

### Endpoints

#### POST `/api/v1/predict`

Classify an email or message as spam or ham (legitimate).

**Request Body:**
```json
{
  "email_text": "Your email content here",
  "return_confidence": true
}
```

**Response:**
```json
{
  "prediction": "spam",
  "confidence": 0.97,
  "timestamp": "2025-12-12T14:30:00Z"
}
```

**Response Fields:**
- `prediction` (string): Classification result - "spam" or "ham"
- `confidence` (float): Confidence score between 0 and 1
- `timestamp` (string): ISO 8601 formatted timestamp

#### GET `/health`

Health check endpoint to verify API availability.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-12-12T14:30:00Z"
}
```

### Try It Out!

Visit the [interactive API documentation](https://spam-email-api-ece2.onrender.com/docs) to test endpoints directly in your browser with the Swagger UI interface.

## 💻 Local Development

### Prerequisites

- Python 3.8 or higher
- pip package manager
- virtualenv (recommended)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/mosesamwoma/spam-email-detection-model.git
   cd spam-email-detection-model
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API locally**
   ```bash
   uvicorn api.app:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Access the API**
   - API: http://localhost:8000
   - Interactive Docs: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.13**: Primary programming language
- **FastAPI**: Modern, high-performance web framework
- **Uvicorn**: Lightning-fast ASGI server

### Machine Learning
- **scikit-learn**: ML library and algorithms
  - Logistic Regression classifier
  - TF-IDF Vectorizer for feature extraction
  - Model evaluation and validation tools
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing operations

### Natural Language Processing
- **nltk**: Text preprocessing and tokenization

### Browser Integration
- **Chrome Extension**: Native browser integration for seamless email checking

### Testing & Deployment
- **pytest**: Testing framework
- **Render**: Cloud deployment platform

## 🔮 Roadmap & Future Enhancements

### In Development
- [ ] **Chrome Web Store Publishing**: Official extension listing
- [ ] **Batch Processing API**: Support for bulk email classification
- [ ] **API Authentication**: Secure API key-based authentication
- [ ] **Rate Limiting**: Request throttling for production environments

### Planned Features
- [ ] **Enhanced Models**: Ensemble methods and advanced algorithms
  - Voting Classifier (Logistic Regression + Naive Bayes + SVM)
  - Random Forest Classifier
  - Gradient Boosting (XGBoost/LightGBM)
  - Neural network approaches
- [ ] **Model Comparison Dashboard**: Performance metrics across models
- [ ] **Hyperparameter Optimization**: Automated tuning with GridSearch/RandomSearch
- [ ] **Multi-language Support**: Spam detection for non-English emails
- [ ] **Response Caching**: Redis integration for improved performance
- [ ] **Extended Test Coverage**: Comprehensive unit and integration tests
- [ ] **Model Monitoring**: Performance tracking and drift detection
- [ ] **Email Parser Integration**: Automatic header and content extraction
- [ ] **Firefox & Edge Extensions**: Multi-browser support
- [ ] **Extension Analytics**: Usage statistics and detection patterns

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for full details.

## 👤 Author

**Moses Amwoma**

- 🐙 GitHub: [@mosesamwoma](https://github.com/mosesamwoma)
- 💼 LinkedIn: [Moses Amwoma](https://linkedin.com/in/moses-amwoma-74735a324)
- 📧 Email: [mosesamwoma@gmail.com](mailto:mosesamwoma@gmail.com)
- 🔗 API Project: [Spam Email Detection Model](https://github.com/mosesamwoma/spam-email-detection-model)
- 🔗 Extension Project: [Chrome Extension](https://github.com/mosesamwoma/chrome-extension)

## 🙏 Acknowledgments

- Dataset source: [Kaggle Spam Email Dataset](https://www.kaggle.com/)
- Inspired by email security research and industry best practices
- Built with amazing open-source tools and libraries
- Deployed on [Render](https://render.com) for reliable cloud hosting
- Thanks to the ML and NLP communities for continuous innovation

## 📞 Contact & Support

Questions, suggestions, or collaboration opportunities? Let's connect!

- 📧 **Email**: [mosesamwoma@gmail.com](mailto:mosesamwoma@gmail.com)
- 💼 **LinkedIn**: [Moses Amwoma](https://linkedin.com/in/moses-amwoma-74735a324)
- 🐙 **GitHub**: [@mosesamwoma](https://github.com/mosesamwoma)
- 📚 **API Docs**: [Interactive Documentation](https://spam-email-api-ece2.onrender.com/docs)
- 🐛 **Report Issues**: 
  - API: [GitHub Issues](https://github.com/mosesamwoma/spam-email-detection-model/issues)
  - Extension: [GitHub Issues](https://github.com/mosesamwoma/chrome-extension/issues)

---

## ⭐ Support This Project

If you find this project helpful, please consider:

- ⭐ **Star** the repositories to show your appreciation
- 🍴 **Fork** them to build upon for your own projects
- 📢 **Share** them with colleagues and friends
- 🐛 **Report bugs** to help improve quality
- 💡 **Suggest features** for future development
- 🤝 **Contribute** by submitting pull requests
- 🚀 **Use the API** in your applications and projects
- 🔌 **Test the extension** and provide feedback

Your support helps make this project better for everyone!

---

**Made with ❤️ by Moses Amwoma**

*Building intelligent solutions for a safer digital world*

[![Try the API](https://img.shields.io/badge/Try%20the%20API-Now-brightgreen?style=for-the-badge)](https://spam-email-api-ece2.onrender.com/docs)
[![Get Extension](https://img.shields.io/badge/Get%20Extension-GitHub-blue?style=for-the-badge)](https://github.com/mosesamwoma/chrome-extension)
