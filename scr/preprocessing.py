import re

def clean_text(text: str) -> str:
    """
    Clean a text message:
    - Lowercase
    - Remove URLs
    - Remove punctuation/numbers
    - Remove extra whitespace
    """
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)              # remove punctuation/numbers
    text = re.sub(r"\s+", " ", text).strip()            # remove extra whitespace
    return text
