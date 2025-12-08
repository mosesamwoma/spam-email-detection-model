import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

def plot_confusion_matrix(y_true, y_pred, labels):
    """
    Plot confusion matrix heatmap for given predictions.
    """
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()

def print_classification_metrics(y_true, y_pred):
    """
    Print accuracy and classification report.
    """
    from sklearn.metrics import accuracy_score
    print("📊 Accuracy:", accuracy_score(y_true, y_pred))
    print("\n📊 Classification Report:")
    print(classification_report(y_true, y_pred))
