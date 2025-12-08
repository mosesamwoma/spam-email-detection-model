from src.utils import plot_confusion_matrix, print_classification_metrics

def test_print_classification_metrics():
    y_true = ["spam", "ham", "spam"]
    y_pred = ["spam", "ham", "ham"]
    print_classification_metrics(y_true, y_pred)

def test_plot_confusion_matrix():
    y_true = ["spam", "ham", "spam"]
    y_pred = ["spam", "ham", "ham"]
    plot_confusion_matrix(y_true, y_pred, labels=["ham", "spam"])
