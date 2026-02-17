import spacy
import re

nlp = spacy.load("en_core_web_sm")

def parse_command(text):

    doc = nlp(text.lower())

    intent = "unknown"

    # detect intent
    if any(token.lemma_ in ["add", "buy", "need"] for token in doc):
        intent = "add"

    elif any(token.lemma_ == "remove" for token in doc):
        intent = "remove"

    elif any(token.lemma_ in ["find", "search"] for token in doc):
        intent = "search"

    # quantity
    quantity_match = re.findall(r'\d+', text)
    quantity = int(quantity_match[0]) if quantity_match else 1

    # item extraction (noun detection)
    item = None
    for token in doc:
        if token.pos_ == "NOUN":
            item = token.text

    return intent, item, quantity
