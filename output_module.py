def print_recommendation(risk_level, score, rules):
    """Prints the final recommendation to the user."""
    
    print("\n" + "="*50)
    print(f"*** Triage Assessment Result ***")
    print(f"Risk Level: **{risk_level}**")
    print(f"Calculated Score: {score:.2f}")
    print("-" * 50)
    
    # Use the predefined text from the rules for clear, consistent output
    recommendation = rules['recommendations'].get(risk_level, "Assessment inconclusive. Contact a professional.")
    
    print(f"Recommendation:\n{recommendation}")
    print("="*50)
