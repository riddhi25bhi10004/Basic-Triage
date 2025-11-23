import json

def load_rules():
    """Loads rules and weights from the JSON file."""
    try:
        with open('triage_rules.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: triage_rules.json not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to parse triage_rules.json.")
        return None

def get_user_input(rules):
    """Collects symptom data from the user."""
    
    # 1. Collect Demographic Data
    try:
        age = int(input("Enter your age: "))
        if not 1 <= age <= 120:
            raise ValueError
        
        duration = int(input("How many days have you had symptoms? "))
        if duration < 0:
            raise ValueError
    except ValueError:
        # Error Handling: graceful failure on bad input
        print("\n**Error Handling:** Invalid age or duration input. Please try again.")
        return None

    patient_profile = {
        "age": age,
        "duration_days": duration,
        "symptoms": {}
    }

    # 2. Collect Symptoms and Severity
    available_symptoms = rules['symptom_weights'].keys()
    print("\nPlease enter the severity (Mild, Moderate, Severe) for the following symptoms (or press Enter if absent):")
    
    for symptom in available_symptoms:
        severity = input(f"  {symptom} (Mild/Moderate/Severe): ").strip().lower()
        if severity in rules['severity_multipliers']:
            patient_profile['symptoms'][symptom] = severity
        elif severity:
            # Error Handling: Warn on bad severity input but continue
            print(f"Warning: '{severity}' is not a valid severity. Skipping {symptom}.")
            
    return patient_profile

if __name__ == '__main__':
    rules = load_rules()
    if rules:
        print("Rules loaded successfully.")
        
