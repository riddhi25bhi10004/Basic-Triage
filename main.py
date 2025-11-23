import input_module
import triage_engine
import output_module

def run_symptom_checker():
    """Main function to run the symptom checker workflow."""
    
    rules = input_module.load_rules()
    if not rules:
        return # Exit if rules couldn't load (Error Handling)

    # 1. Get Input
    profile = input_module.get_user_input(rules)
    if not profile:
        print("Triage process cancelled due to input error.")
        return # Exit if input was invalid

    # 2. Calculate Score (Performance Test)
    score, calc_time = triage_engine.calculate_triage_score(profile, rules)
    
    print(f"\n[Performance Check: Calculation completed in {calc_time:.6f} seconds]")
    if calc_time > 1.0:
        print("WARNING: Calculation time exceeded 1.0 second non-functional requirement.")
    
    # 3. Determine Risk
    risk_level = triage_engine.determine_risk_level(score, rules)

    # 4. Print Output (Usability)
    output_module.print_recommendation(risk_level, score, rules)
    
if __name__ == '__main__':
    run_symptom_checker()
