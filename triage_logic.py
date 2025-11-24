import time

# --- Rules Definition (Keep this consistent with your generator script) ---
RULES = {
    "symptom_weights": {
        "fever": 3.0, "fatigue": 2.0, "sore_throat": 1.0, 
        "chest_pain": 50.0, "shortness_of_breath": 50.0,
    },
    "severity_multipliers": {"mild": 1.0, "moderate": 1.5, "severe": 2.0},
    "triage_thresholds": {"low_risk": 5.0, "medium_risk": 15.0},
    "critical_rules": [("chest_pain", "shortness_of_breath")] 
}

def calculate_triage_score(profile, rules=RULES):
    """Calculates the Triage Score based on weighted rules."""
    
    start_time = time.time()
    score = 0.0

    # 1. Apply Critical Rules (Overrides)
    for rule in rules.get('critical_rules', []): 
        if isinstance(rule, tuple) and len(rule) == 2:
            symptom1, symptom2 = rule
            if profile['symptoms'].get(symptom1) and profile['symptoms'].get(symptom2):
                # Critical Override
                return 100.0, time.time() - start_time
    
    # 2. Score Individual Symptoms
    for symptom, severity in profile['symptoms'].items():
        weight = rules['symptom_weights'].get(symptom, 0.0)
        multiplier = rules['severity_multipliers'].get(severity, 1.0)
        score += weight * multiplier
        
    # 3. Apply Age and Duration Factors
    if profile['age'] > 65:
        score += 3.0
    
    if profile['duration_days'] > 7:
        score += 2.0
        
    return score, time.time() - start_time

def determine_risk_level(score, rules=RULES):
    """Determines the risk level based on the calculated score."""
    
    thresholds = rules['triage_thresholds']
    
    if score >= thresholds['medium_risk']:
        return "HIGH"
    elif score >= thresholds['low_risk']:
        return "MEDIUM"
    else:
        return "LOW"
