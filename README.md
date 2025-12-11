# Spam Email Detection Model

[![Python Version](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![API Status](https://img.shields.io/badge/API-live-brightgreen)](https://spam-email-api-ece2.onrender.com/docs)
[![Deployed on Render](https://img.shields.io/badge/deployed%20on-Render-46E3B7)](https://render.com)
[![Status](https://img.shields.io/badge/status-in%20development-orange)](https://github.com/mosesamwoma/spam-email-detection-model)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A machine learning project for detecting spam emails and messages using a TF-IDF vectorizer and a classification model. **Now with a live REST API!**

> **⚠️ Project Status:** This project is currently under active development. The API is live and functional, but source code, documentation, and test suites are still being finalized.

## 📊 Current Status

- ✅ **Trained Model**: Classification model is trained and deployed
- ✅ **TF-IDF Vectorizer**: Vectorizer is trained and available
- ✅ **REST API**: Live and accessible at [https://spam-email-api-ece2.onrender.com](https://spam-email-api-ece2.onrender.com/docs)
- 🚧 **Source Code**: Currently being developed
- 🚧 **Test Suite**: Unit tests in progress

## 🎯 Overview

Email spam detection is a critical component of modern email systems. This project implements a machine learning model using TF-IDF vectorization and classification algorithms to automatically identify and filter spam emails and messages.

The model is now deployed as a REST API, making it easy to integrate spam detection into your applications!

## ✨ Features

- **Text Preprocessing**: Advanced cleaning and normalization of text data
- **TF-IDF Vectorization**: Efficient text representation for machine learning
- **Spam Classification**: Machine learning model for accurate spam detection
- **REST API**: Easy-to-use API for real-time spam detection
- **Interactive Documentation**: Swagger UI for testing endpoints
- **Modular Design**: Easily extensible architecture for future improvements
- **Performance Metrics**: Evaluation with accuracy, precision, recall, and F1-score

## 🚀 Quick Start - Using the API

### Live API Endpoint

The API is live and ready to use! No installation required for API access.

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
print(f"Confidence: {result['confidence']}")
```

## 📡 API Documentation

### Endpoints

#### POST `/api/v1/predict`
Classify an email or message as spam or ham (not spam).

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
  "timestamp": "2025-12-11T10:30:00Z"
}
```

**Parameters:**
- `email_text` (string, required): The email or message text to classify
- `return_confidence` (boolean, optional): Whether to include confidence score (default: true)

**Response Fields:**
- `prediction` (string): Either "spam" or "ham"
- `confidence` (float): Confidence score between 0 and 1
- `timestamp` (string): ISO 8601 formatted timestamp

#### GET `/health`
Health check endpoint to verify API status.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-12-11T10:30:00Z"
}
```

### Try It Out!
Visit the interactive API documentation at [https://spam-email-api-ece2.onrender.com/docs](https://spam-email-api-ece2.onrender.com/docs) to test the endpoints directly in your browser.

## 💻 Local Development

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/mosesamwoma/spam-email-detection-model.git
   cd spam-email-detection-model
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API locally**
   ```bash
   uvicorn api.app:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Access the API**
   - API: http://localhost:8000
   - Interactive Docs: http://localhost:8000/docs

## 🛠️ Technologies Used

- **Python 3.13**: Core programming language
- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running the API
- **scikit-learn**: Machine learning library
  - Logistic Regression for classification
  - TF-IDF Vectorizer for feature extraction
  - Train-test split and cross-validation
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **nltk**: Natural Language Toolkit for text preprocessing
- **matplotlib & seaborn**: Data visualization
- **pytest**: Testing framework
- **Render**: Cloud platform for deployment

## 🔮 Future Improvements

- [ ] **Complete Source Code**: Finalize preprocessing and training scripts
- [ ] **Complete Test Suite**: Implement comprehensive unit tests
- [x] **REST API Integration**: Build API for real-time spam detection ✅
- [ ] **Web Interface**: Simple dashboard for email classification
- [ ] **Batch Processing**: Support for multiple email classification
- [ ] **Ensemble Modeling**: Implement ensemble methods for improved accuracy
  - Voting Classifier (Logistic Regression + Naive Bayes + SVM)
  - Random Forest
  - Gradient Boosting (XGBoost/LightGBM)
  - Stacking methods
- [ ] **Model Comparison**: Test with Naive Bayes and SVM
- [ ] **Hyperparameter Tuning**: Optimize model performance
- [ ] **Extended Testing**: Increase test coverage
- [ ] **Multi-language Support**: Detect spam in different languages
- [ ] **Rate Limiting**: Add API rate limiting for production use
- [ ] **Authentication**: Implement API key authentication
- [ ] **Caching**: Add response caching for improved performance

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Moses Amwoma**
- GitHub: [@mosesamwoma](https://github.com/mosesamwoma)
- LinkedIn: [Moses Amwoma](https://linkedin.com/in/moses-amwoma-74735a324)
- Email: [mosesamwoma@gmail.com](mailto:mosesamwoma@gmail.com)
- Project Link: [https://github.com/mosesamwoma/spam-email-detection-model](https://github.com/mosesamwoma/spam-email-detection-model)

## 🙏 Acknowledgments

- Dataset source: [Kaggle - Spam Email Dataset](https://www.kaggle.com/)
- Inspired by email spam detection research and best practices
- Thanks to the open-source community for the amazing tools
- Deployed on [Render](https://render.com) for reliable cloud hosting

## 📞 Contact & Support

Have questions, suggestions, or interested in collaboration? I'd love to hear from you!

- 📧 **Email**: [mosesamwoma@gmail.com](mailto:mosesamwoma@gmail.com)
- 💼 **LinkedIn**: [Moses Amwoma](https://linkedin.com/in/moses-amwoma-74735a324)
- 🐙 **GitHub**: [@mosesamwoma](https://github.com/mosesamwoma)
- 🌐 **API Docs**: [Interactive Documentation](https://spam-email-api-ece2.onrender.com/docs)

---

## ⭐ Support This Project

If you find this project valuable, please consider:

- ⭐ **Star** the repository to show your support
- 🍴 **Fork** it to build upon for your own projects
- 📢 **Share** it with others who might benefit
- 🐛 **Report issues** to help improve the project
- 🤝 **Contribute** by submitting pull requests
- 🚀 **Use the API** in your applications

Every star and contribution helps make this project better!

---

<div align="center">

**Made with ❤️ by Moses Amwoma**

*Building intelligent solutions for a safer digital world*

**[Try the API Now](https://spam-email-api-ece2.onrender.com/docs)**

</div>
