import unittest
# Import the functions and rules from your logic file
from triage_logic import calculate_triage_score, determine_risk_level, RULES 

class TestTriageScoring(unittest.TestCase):
    """
    Test suite for the Triage Score Calculator functions.
    """

    # --- Setup/Teardown (Optional but good practice) ---
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        # Define a standard profile for minor adjustments in tests
        self.standard_profile = {
            "age": 40,
            "duration_days": 3,
            "symptoms": {"fever": "moderate", "fatigue": "mild"}
        }
        # Define the thresholds for assertions
        self.LOW_RISK_THRESHOLD = RULES['triage_thresholds']['low_risk']  # 5.0
        self.MEDIUM_RISK_THRESHOLD = RULES['triage_thresholds']['medium_risk'] # 15.0

    # --- Test Cases for calculate_triage_score ---
    
    def test_01_base_score_calculation(self):
        """Tests standard scoring without age/duration factors."""
        # Expected calculation: (fever 3.0 * moderate 1.5) + (fatigue 2.0 * mild 1.0) = 4.5 + 2.0 = 6.5
        score, _ = calculate_triage_score(self.standard_profile)
        # assertAlmostEqual is used for float comparisons to avoid precision errors
        self.assertAlmostEqual(score, 6.5, places=2, msg="Base score calculation failed.")

    def test_02_critical_override_triggered(self):
        """Tests that the score immediately returns 100.0 for critical combinations."""
        critical_profile = {
            "age": 20,
            "duration_days": 1,
            "symptoms": {"chest_pain": "severe", "shortness_of_breath": "moderate", "fever": "severe"}
        }
        score, _ = calculate_triage_score(critical_profile)
        self.assertAlmostEqual(score, 100.0, msg="Critical override did not return 100.0.")

    def test_03_age_factor_applied(self):
        """Tests that the +3.0 age factor is correctly applied."""
        old_profile = self.standard_profile.copy()
        old_profile['age'] = 70 # Triggers +3.0 factor
        # Expected: 6.5 (base) + 3.0 (age) = 9.5
        score, _ = calculate_triage_score(old_profile)
        self.assertAlmostEqual(score, 9.5, places=2, msg="Age factor not applied correctly.")

    def test_04_duration_factor_applied(self):
        """Tests that the +2.0 duration factor is correctly applied."""
        long_duration_profile = self.standard_profile.copy()
        long_duration_profile['duration_days'] = 10 # Triggers +2.0 factor
        # Expected: 6.5 (base) + 2.0 (duration) = 8.5
        score, _ = calculate_triage_score(long_duration_profile)
        self.assertAlmostEqual(score, 8.5, places=2, msg="Duration factor not applied correctly.")
        
    def test_05_unknown_symptom_ignored(self):
        """Tests that a symptom not in the weights is ignored (weight=0.0)."""
        unknown_profile = self.standard_profile.copy()
        unknown_profile['symptoms']['unknown_rash'] = 'severe'
        # Expected: 6.5 (base), unknown symptom should not change the score
        score, _ = calculate_triage_score(unknown_profile)
        self.assertAlmostEqual(score, 6.5, places=2, msg="Unknown symptom affected the score.")

    # --- Test Cases for determine_risk_level ---

    def test_06_risk_level_low(self):
        """Tests scoring resulting in a LOW risk level."""
        # Score must be < 5.0 (low_risk threshold)
        self.assertEqual(determine_risk_level(4.99), "LOW")
        self.assertEqual(determine_risk_level(0.0), "LOW")

    def test_07_risk_level_medium(self):
        """Tests scoring resulting in a MEDIUM risk level."""
        # Score must be >= 5.0 and < 15.0
        self.assertEqual(determine_risk_level(self.LOW_RISK_THRESHOLD), "MEDIUM", msg="Boundary test at low_risk threshold failed.")
        self.assertEqual(determine_risk_level(14.99), "MEDIUM")

    def test_08_risk_level_high(self):
        """Tests scoring resulting in a HIGH risk level."""
        # Score must be >= 15.0 (medium_risk threshold)
        self.assertEqual(determine_risk_level(self.MEDIUM_RISK_THRESHOLD), "HIGH", msg="Boundary test at medium_risk threshold failed.")
        self.assertEqual(determine_risk_level(100.0), "HIGH")
        

if __name__ == '__main__':
    unittest.main()
