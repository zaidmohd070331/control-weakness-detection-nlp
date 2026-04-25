# scoring.py
# Severity scoring model for prioritising control weaknesses

import pandas as pd

# ----------------------------
# Severity Scoring Logic
# ----------------------------

# Risk weights by business area
BUSINESS_AREA_WEIGHTS = {
    'Payments': 1.5,
    'Credit Risk': 1.4,
    'Compliance': 1.3,
    'Operations': 1.2,
    'Other': 1.0
}

# Finding type base scores
FINDING_TYPE_SCORES = {
    'Policy Breach': 80,
    'System Failure': 75,
    'Process Gap': 60,
    'Data Integrity': 65,
    'People Risk': 50
}

def calculate_severity_score(row):
    """
    Calculate a numeric severity score for each control weakness.
    Score = Base Score x Business Area Weight x Recurrence Multiplier
    """
    base_score = FINDING_TYPE_SCORES.get(row['finding_type'], 50)
    area_weight = BUSINESS_AREA_WEIGHTS.get(row['business_area'], 1.0)
    recurrence = row.get('recurrence_count', 1)
    recurrence_multiplier = 1 + (0.1 * recurrence)

    score = base_score * area_weight * recurrence_multiplier
    return round(score, 2)

def assign_severity_label(score):
    """
    Map numeric score to severity label:
    Critical / High / Medium / Low
    """
    if score >= 120:
        return 'Critical'
    elif score >= 90:
        return 'High'
    elif score >= 60:
        return 'Medium'
    else:
        return 'Low'

def score_dataframe(df):
    df['severity_score'] = df.apply(calculate_severity_score, axis=1)
    df['severity_label'] = df['severity_score'].apply(assign_severity_label)
    return df.sort_values('severity_score', ascending=False)

if __name__ == "__main__":
    df = pd.read_csv("../data/sample_audit_logs.csv")
    df['recurrence_count'] = 1  # placeholder
    result = score_dataframe(df)
    print(result[['control_id', 'business_area', 'finding_type',
                  'severity_score', 'severity_label']])
