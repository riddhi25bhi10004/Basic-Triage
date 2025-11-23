import time

def calculate_triage_score(profile, rules):
    """Calculates the Triage Score based on weighted rules."""
    
    start_time = time.time()
    score = 0.0

    # 1. Apply Critical Rules (Overrides)
    # The fix ensures 'critical_rules' is present in the rules dictionary.
    for rule in rules.get('critical_rules', []): 
        # Check if the rule is a tuple of two symptoms
        if isinstance(rule, tuple) and len(rule) == 2:
            symptom1, symptom2 = rule
            # Use .get to safely check for symptom presence in the profile
            if profile['symptoms'].get(symptom1) and profile['symptoms'].get(symptom2):
                # If critical combination found, set max score and immediately return
                return 100.0, time.time() - start_time
    
    # 2. Score Individual Symptoms
    for symptom, severity in profile['symptoms'].items():
        # Get weight and multiplier safely, defaulting to 0.0 and 1.0 respectively
        weight = rules['symptom_weights'].get(symptom, 0.0)
        multiplier = rules['severity_multipliers'].get(severity, 1.0)
        
        score += weight * multiplier
        
    # 3. Apply Age and Duration Factors (Simplified)
    # Risk increases slightly with age > 65
    if profile['age'] > 65:
        score += 3.0
    
    # Risk increases slightly with long duration > 7 days
    if profile['duration_days'] > 7:
        score += 2.0
        
    end_time = time.time()
    
    # The performance metric: calculation time
    calculation_time = end_time - start_time
    
    return score, calculation_time

def determine_risk_level(score, rules):
    """Determines the risk level based on the calculated score."""
    
    thresholds = rules['triage_thresholds']
    
    # HIGH is defined by a score >= the 'medium_risk' threshold (15.0)
    # This is a common pattern where the high end of 'medium' is the start of 'high'.
    # I'll adjust the logic to use 'medium_risk' as the lower bound for HIGH.
    if score >= thresholds['medium_risk']:
        return "HIGH"
    # MEDIUM is defined by a score >= 'low_risk' threshold (5.0)
    elif score >= thresholds['low_risk']:
        return "MEDIUM"
    else:
        return "LOW"

if __name__ == '__main__':
    # --- Rules Definition ---
    rules = {
        "symptom_weights": {"fever": 3.0, "fatigue": 2.0, "sore_throat": 1.0, "chest_pain": 50.0},
        "severity_multipliers": {"mild": 1.0, "moderate": 1.5, "severe": 2.0},
        "triage_thresholds": {"low_risk": 5.0, "medium_risk": 15.0},
        # FIX: Added 'critical_rules' to prevent KeyError.
        # Example critical rule: Chest pain + shortness of breath is max risk
        "critical_rules": [("chest_pain", "shortness_of_breath")] 
    }

    # --- Test Case 1: Standard Calculation ---
    print("--- Test Case 1: Standard Calculation ---")
    mock_profile_1 = {
        "age": 45,
        "duration_days": 3,
        "symptoms": {
            "fever": "moderate",  # 3.0 * 1.5 = 4.5
            "fatigue": "severe",  # 2.0 * 2.0 = 4.0
            "sore_throat": "mild" # 1.0 * 1.0 = 1.0
        } # Total Score: 4.5 + 4.0 + 1.0 = 9.5
    }
    score_1, t_1 = calculate_triage_score(mock_profile_1, rules)
    print(f"Calculated Score: {score_1:.2f} (Expected: 9.50)")
    print(f"Risk Level: {determine_risk_level(score_1, rules)} (Expected: MEDIUM)")
    print(f"Calculation Time: {t_1:.6f} seconds (Target: < 1.0s)")

    # --- Test Case 2: Critical Override Triggered ---
    print("\n--- Test Case 2: Critical Override ---")
    mock_profile_2 = {
        "age": 70, # Age > 65 is irrelevant here due to override
        "duration_days": 10, # Duration > 7 days is irrelevant here due to override
        "symptoms": {
            "fever": "mild",
            "chest_pain": "severe", # Critical symptom 1
            "shortness_of_breath": "severe" # Critical symptom 2
        } # Critical combination should trigger max score (100.0)
    }
    score_2, t_2 = calculate_triage_score(mock_profile_2, rules)
    print(f"Calculated Score: {score_2:.2f} (Expected: 100.00)")
    print(f"Risk Level: {determine_risk_level(score_2, rules)} (Expected: HIGH)")
    print(f"Calculation Time: {t_2:.6f} seconds (Target: < 1.0s)")
