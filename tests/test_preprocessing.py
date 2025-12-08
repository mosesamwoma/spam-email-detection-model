from src.preprocessing import clean_text

def test_clean_text_basic():
    text = "Hello WORLD! Visit http://example.com"
    cleaned = clean_text(text)
    assert cleaned == "hello world visit"
