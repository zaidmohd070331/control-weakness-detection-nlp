# model.py
# Text classification model for control weakness categorisation

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# ----------------------------
# Load Data
# ----------------------------
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

# ----------------------------
# Train Model
# ----------------------------
def train_model(df, text_col='lemmatized_text', label_col='finding_type'):
    X = df[text_col]
    y = df[label_col]

    # TF-IDF Vectorisation
    vectorizer = TfidfVectorizer(max_features=500, ngram_range=(1, 2))
    X_vec = vectorizer.fit_transform(X)

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X_vec, y, test_size=0.2, random_state=42, stratify=y
    )

    # Model
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    print("=== Classification Report ===")
    print(classification_report(y_test, y_pred))
    print("=== Confusion Matrix ===")
    print(confusion_matrix(y_test, y_pred))

    # Save model and vectorizer
    joblib.dump(model, 'model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')
    print("Model saved as model.pkl")

    return model, vectorizer

if __name__ == "__main__":
    df = pd.read_csv("../data/sample_audit_logs.csv")
    # Note: In practice, run preprocess.py first to get lemmatized_text
    df['lemmatized_text'] = df['assessment_text']  # placeholder
    train_model(df)
