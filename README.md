# control-weakness-detection-nlp
NLP pipeline to detect &amp; prioritise internal control weaknesses from audit logs | spaCy · Scikit-learn · Power BI
# 🔍 Internal Control Weakness Detection using NLP & ML

> Automated identification and severity prioritisation of internal control weaknesses from audit logs and control assessment text — directly replicating the mandate of a Chief Controls Office (CCO) analytics function.

---

## 📌 Business Problem

In large financial institutions, internal audit teams generate thousands of control assessment records. Manually identifying, categorising, and prioritising control weaknesses is time-consuming and inconsistent. This project automates that process using NLP and machine learning — enabling faster triage, consistent severity classification, and MI-ready reporting for control owners and senior management.

---

## 🎯 Objectives

- Automatically detect and categorise control gaps from unstructured audit text
- Classify weaknesses by severity: **Critical / High / Medium / Low**
- Surface trends by business area and recurrence in a Power BI dashboard
- Produce structured assessment reports suitable for compliance stakeholders

---

## 🏗️ Project Architecture

```
Raw Audit Text → Preprocessing → NLP Pipeline → Classification Model → Severity Scoring → Power BI Dashboard
```

---

## 🔬 Methodology

### 1. Data
- Synthetic audit log and control assessment text (generated to replicate real CCO documentation structure)
- Fields: control_id, business_area, assessment_text, finding_type, date

### 2. NLP Pipeline (spaCy)
- Text cleaning, tokenisation, lemmatisation
- Named Entity Recognition for control-specific entities
- Topic modelling to identify control gap categories

### 3. Text Classification (Scikit-learn)
- TF-IDF vectorisation
- Multi-class classifier: Logistic Regression / Random Forest
- Categories: Process Gap | People Risk | System Failure | Policy Breach | Data Integrity

### 4. Severity Scoring Model
- Multi-class output: Critical / High / Medium / Low
- Features: finding type, frequency, business area risk weight, recurrence score
- Enables triage-ready prioritisation aligned to CCO framework logic

### 5. MI Reporting
- Power BI dashboard: control weakness trends by severity, business area, and recurrence
- Structured assessment report documenting methodology, assumptions, and findings

---

## 📊 Results

| Metric | Score |
|---|---|
| Classification Accuracy | XX% |
| Weighted F1 Score | XX |
| Critical Finding Recall | XX% |

---

## 🛠️ Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.10 |
| NLP | spaCy, NLTK, TF-IDF |
| Modelling | Scikit-learn |
| Visualisation | Power BI, Matplotlib, Seaborn |
| Reporting | Structured MI Report (PDF) |

---

## 📂 Repository Structure

```
├── data/                         # Synthetic audit log samples
├── notebooks/                    # EDA, modelling, evaluation notebooks
├── src/                          # Modular Python scripts
│   ├── preprocess.py             # Text cleaning & NLP pipeline
│   ├── model.py                  # Classification model
│   └── scoring.py                # Severity scoring logic
├── reports/                      # MI report & dashboard screenshots
└── README.md
```

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/zaidmohd070331/control-weakness-detection-nlp.git

# Install dependencies
pip install -r requirements.txt

# Run preprocessing
python src/preprocess.py

# Run model training
python src/model.py

# Open notebooks for full walkthrough
jupyter notebook notebooks/
```

---

## 💡 Key Takeaways

- Demonstrates end-to-end NLP pipeline design for a banking controls use case
- Severity scoring logic mirrors real CCO triage workflows
- MI report output structured for non-technical compliance stakeholders
- Directly applicable to Controls Analytics & Insight functions in financial institutions


