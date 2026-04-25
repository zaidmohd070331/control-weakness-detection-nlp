#preprocess.py
#Text cleaning and NLP preprocessing pipeline for audit log data

import pandas as pd
import spacy
import re

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """Remove special characters and lowercase text."""
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower().strip()

def lemmatize(text):
    """Lemmatize text using spaCy."""
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop])

def preprocess_dataframe(df, text_col='assessment_text'):
    df['cleaned_text'] = df[text_col].apply(clean_text)
    df['lemmatized_text'] = df['cleaned_text'].apply(lemmatize)
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/sample_audit_logs.csv")
    df = preprocess_dataframe(df)
    print(df[['control_id', 'lemmatized_text']].head())
