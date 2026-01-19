# Spam Email Detection Model

[![Python Version](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![API Status](https://img.shields.io/badge/API-live-brightgreen)](https://spam-email-api-ece2.onrender.com/docs)
[![Deployed on Render](https://img.shields.io/badge/deployed%20on-Render-46E3B7)](https://render.com)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A machine learning API for detecting spam emails and messages using TF-IDF vectorization and Logistic Regression. Built with FastAPI and deployed on Render.

## 🎬 API in Action

![API Demo](video/main.gif)

**What you're seeing:**
- Interactive API testing via Swagger UI
- Real-time spam classification with confidence scores
- Simple integration with any application

## 🎯 Overview

This project implements a machine learning solution using TF-IDF vectorization and Logistic Regression to automatically identify and filter spam emails with high accuracy. The model is deployed as a REST API, making it simple to integrate spam detection capabilities into any application or workflow.

## ✨ Key Features

- **High-Accuracy Classification**: Trained Logistic Regression model with optimized performance
- **TF-IDF Vectorization**: Efficient text-to-vector transformation
- **REST API**: Fast, scalable API with JSON responses
- **Interactive Documentation**: Built-in Swagger UI for easy testing
- **Real-time Predictions**: Instant spam classification with confidence scores
- **Production Ready**: Deployed on reliable cloud infrastructure
- **Windows Desktop App**: Native application for easy access

## 🚀 Quick Start

### Using the Live API

The API is live and ready to use! No installation required.

**Base URL**: `https://spam-email-api-ece2.onrender.com`

**Interactive Docs**: [https://spam-email-api-ece2.onrender.com/docs](https://spam-email-api-ece2.onrender.com/docs)

#### Example with cURL

```bash
curl -X POST "https://spam-email-api-ece2.onrender.com/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "email_text": "Congratulations! You have won $1,000,000! Click here to claim now!",
    "return_confidence": true
  }'
```

#### Example with Python

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

## 💻 Windows Desktop Application

Download the SpamCheck desktop application for Windows x64 systems.

**Repository**: [https://github.com/mosesamwoma/SpamCheck-app](https://github.com/mosesamwoma/SpamCheck-app)

**Download**: [Latest Release](https://github.com/mosesamwoma/SpamCheck-app/releases)

**Features:**
- 🖥️ Native Windows UI with familiar controls
- 📋 Easy copy & paste functionality
- ⚡ Fast performance and quick analysis
- 🔒 Secure API communication

**System Requirements:** Windows 10/11 (64-bit), 4GB RAM, Internet connection

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

Visit the [interactive API documentation](https://spam-email-api-ece2.onrender.com/docs) to test endpoints directly in your browser.

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

## 🛠️ Technology Stack

**Core Technologies:**
- Python 3.13
- FastAPI
- Uvicorn

**Machine Learning:**
- scikit-learn (Logistic Regression, TF-IDF Vectorizer)
- pandas
- numpy

**NLP:**
- nltk

**Deployment:**
- Render (Cloud platform)

## 🔮 Future Improvements

- [ ] Add API key authentication
- [ ] Implement rate limiting
- [ ] Add batch email processing
- [ ] Test additional classifiers (Naive Bayes, SVM)
- [ ] Add usage analytics dashboard
- [ ] Implement Redis caching

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Moses Amwoma**

- 🐙 GitHub: [@mosesamwoma](https://github.com/mosesamwoma)
- 💼 LinkedIn: [Moses Amwoma](https://linkedin.com/in/moses-amwoma)
- 📧 Email: [mosesamwoma@gmail.com](mailto:mosesamwoma@gmail.com)

## 📞 Contact & Support

- 📧 **Email**: [mosesamwoma@gmail.com](mailto:mosesamwoma@gmail.com)
- 💼 **LinkedIn**: [Moses Amwoma](https://linkedin.com/in/moses-amwoma-74735a324)
- 📚 **API Docs**: [Interactive Documentation](https://spam-email-api-ece2.onrender.com/docs)
- 🐛 **Report Issues**: [GitHub Issues](https://github.com/mosesamwoma/spam-email-detection-model/issues)

---

## ⭐ Support This Project

If you find this project helpful:

- ⭐ Star the repository
- 🍴 Fork it for your own projects
- 🐛 Report bugs
- 💡 Suggest features
- 🚀 Use the API in your applications

---

## 📥 Quick Links

| Platform | Link | Status |
|----------|------|--------|
| 🌐 **API** | [Try Now](https://spam-email-api-ece2.onrender.com/docs) | ✅ Live |
| 💻 **Windows App** | [Download](https://github.com/mosesamwoma/SpamCheck-app/releases) | ✅ Available |
| 📖 **Documentation** | [API Docs](https://spam-email-api-ece2.onrender.com/docs) | ✅ Live |

---

**Made with ❤️ by Moses Amwoma**

*Building intelligent solutions for a safer digital world*

[![Try the API](https://img.shields.io/badge/Try%20the%20API-Now-brightgreen?style=for-the-badge)](https://spam-email-api-ece2.onrender.com/docs)
[![Download App](https://img.shields.io/badge/Download%20App-Windows-0078D4?style=for-the-badge)](https://github.com/mosesamwoma/SpamCheck-app/releases)
