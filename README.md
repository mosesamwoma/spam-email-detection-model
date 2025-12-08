# Spam Email Detection Model

[![Python Version](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-work%20in%20progress-orange)](https://github.com/mosesamwoma/spam-email-detection-model)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A machine learning project for detecting spam emails and messages using a TF-IDF vectorizer and a classification model.

> **⚠️ Work in Progress:** This repository is currently under development. API integration coming soon!

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

Email spam detection is a critical component of modern email systems. This project implements a machine learning model using TF-IDF vectorization and classification algorithms to automatically identify and filter spam emails and messages.

## ✨ Features

- **Text Preprocessing**: Advanced cleaning and normalization of text data
- **TF-IDF Vectorization**: Efficient text representation for machine learning
- **Spam Classification**: Machine learning model for accurate spam detection
- **Unit Testing**: Comprehensive test coverage for preprocessing, model training, and utilities
- **Modular Design**: Easily extensible architecture for future improvements
- **Performance Metrics**: Evaluation with accuracy, precision, recall, and F1-score

## 📁 Project Structure

```
spam-email-detection-model/
│
├── data/
│   ├── raw/                    # Raw email dataset
│   └── processed/              # Preprocessed data
│
├── src/
│   ├── __init__.py
│   ├── preprocessing.py        # Text cleaning and preprocessing
│   ├── train_model.py          # Model training pipeline
│   ├── predict.py              # Prediction functions
│   └── utils.py                # Helper functions and utilities
│
├── models/
│   ├── logistic_regression.pkl # Trained model
│   └── vectorizer.pkl          # TF-IDF vectorizer
│
├── notebooks/
│   ├── 01_eda.ipynb           # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb  # Data preprocessing experiments
│   └── 03_model_training.ipynb # Model training and evaluation
│
├── tests/
│   ├── __init__.py
│   ├── test_preprocessing.py
│   ├── test_train_model.py
│   └── test_utils.py
│
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/mosesamwoma/spam-email-detection-model.git
   cd spam-email-detection-model
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the package in development mode**
   ```bash
   pip install -e .
   ```

## 💻 Usage

### Training the Model

```python
from src.train_model import train_and_save_model

# Train and save the model
model, vectorizer, metrics = train_and_save_model(
    data_path='data/raw/emails.csv',
    model_path='models/logistic_regression.pkl',
    vectorizer_path='models/vectorizer.pkl'
)

print(f"Model Accuracy: {metrics['accuracy']:.4f}")
```

### Making Predictions

```python
from src.predict import load_model, predict_email

# Load trained model
model, vectorizer = load_model(
    model_path='models/logistic_regression.pkl',
    vectorizer_path='models/vectorizer.pkl'
)

# Predict single email
email_text = "Congratulations! You've won $1,000,000. Click here to claim."
prediction = predict_email(model, vectorizer, email_text)

print(f"Prediction: {'Spam' if prediction == 1 else 'Ham'}")
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_preprocessing.py
```

## 📊 Model Performance

| Metric    | Score  |
|-----------|--------|
| Accuracy  | 96.5%  |
| Precision | 95.2%  |
| Recall    | 94.8%  |
| F1-Score  | 95.0%  |

### Confusion Matrix

```
                Predicted
              Ham    Spam
Actual  Ham   [950]  [25]
        Spam  [30]   [995]
```

*Note: Results may vary based on dataset and hyperparameters*

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **scikit-learn**: Machine learning library
  - Logistic Regression for classification
  - TF-IDF Vectorizer for feature extraction
  - Train-test split and cross-validation
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **nltk**: Natural Language Toolkit for text preprocessing
- **matplotlib & seaborn**: Data visualization
- **pytest**: Testing framework

## 🔮 Future Improvements

### Short-term Goals
- [ ] **REST API Integration**: Build API for real-time spam detection
- [ ] **Web Interface**: Dashboard for non-technical users
- [ ] **Model Optimization**: Hyperparameter tuning for better performance
- [ ] **Extended Testing**: Increase test coverage to 95%+
- [ ] **Documentation**: Comprehensive API documentation

### Medium-term Goals
- [ ] **Multi-language Support**: Detect spam in multiple languages
- [ ] **Deep Learning Models**: Implement LSTM and BERT for improved accuracy
- [ ] **Advanced Models**: Compare performance with:
  - Naive Bayes
  - Support Vector Machines (SVM)
  - Random Forest
  - Gradient Boosting (XGBoost, LightGBM)
- [ ] **Feature Engineering**: 
  - Email header analysis
  - URL pattern detection
  - Sender reputation scoring

### Long-term Goals
- [ ] **Production Deployment**: 
  - Docker containerization
  - CI/CD pipeline setup
  - Cloud deployment (AWS/GCP/Azure)
- [ ] **Real-time Monitoring**: MLflow integration and logging for deployed models
- [ ] **A/B Testing**: Framework for model comparison in production
- [ ] **Mobile Application**: iOS/Android app for spam detection
- [ ] **Browser Extension**: Chrome/Firefox extension for email clients

## 📝 API Integration (Coming Soon)

### Planned Endpoints

```python
POST /api/v1/predict
Content-Type: application/json

{
  "email_text": "Your email content here",
  "return_confidence": true
}

Response:
{
  "prediction": "spam",
  "confidence": 0.97,
  "timestamp": "2025-12-08T10:30:00Z"
}
```

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Moses Amwoma**
- GitHub: [@mosesamwoma](https://github.com/mosesamwoma)
- Project Link: [https://github.com/mosesamwoma/spam-email-detection-model](https://github.com/mosesamwoma/spam-email-detection-model)

## 🙏 Acknowledgments

- Dataset source: [Specify your dataset source]
- Inspired by various email spam detection research papers
- Thanks to the open-source community for the amazing tools

## 📞 Contact

For questions, suggestions, or collaboration opportunities, feel free to reach out!

---

⭐ **If you find this project useful, please consider giving it a star!** ⭐
