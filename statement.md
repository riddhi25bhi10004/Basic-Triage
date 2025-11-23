That's the final piece of documentation! The `statement.md` file serves as a brief, high-level summary for the project manager or stakeholder.

Here are the contents for your **Basic Symptom Checker/Triage Tool** project, formatted for the `statement.md` file.

---

# 📜 Project Statement: Basic Symptom Checker/Triage Tool

## 1. Problem Statement

Patients frequently rely on generalized internet searches for self-diagnosis, often resulting in unnecessary visits to clinics or, more dangerously, delayed attention to critical symptoms. There is a need for an immediate, standardized, and safe preliminary **risk assessment tool** to guide users toward the appropriate level of care, preventing misuse of emergency services and promoting timely self-care decisions.

## 2. Scope of the Project

The scope is limited to developing a **Command Line Interface (CLI)** application built in Python.

* **In Scope:**
    * Implementing a **rule-based Decision Engine** using static weights and thresholds defined in a local JSON file.
    * Achieving the Non-Functional Requirement (NFR) of **sub-one-second performance** for the triage calculation.
    * Providing a simple, **three-category risk classification** (LOW, MEDIUM, HIGH) with actionable recommendations.
    * Implementing robust data validation and error handling for user inputs.
* **Out of Scope:**
    * Developing a full web-based Graphical User Interface (GUI).
    * Integrating with live clinical data systems or APIs.
    * Providing actual medical advice; the tool is for **preliminary triage only**.

## 3. Target Users

The primary target users are individuals seeking immediate, non-emergency health guidance.

* **End User (Primary):** **General Public** seeking quick risk classification based on current symptoms.
* **Maintainer (Secondary):** **System Administrators or Clinical Staff** who need to update the symptom weights and risk thresholds via the external configuration file.

## 4. High-Level Features

The Triage Tool offers three major high-level features corresponding to the functional modules:

1.  **Guided Symptom Input:** A structured CLI interface to accurately capture and validate user demographics (age, duration) and symptom severity.
2.  **Instant Risk Classification:** A high-performance Decision Engine that calculates a weighted Triage Score and classifies the risk level based on configured thresholds.
3.  **Actionable Recommendation Output:** Provides clear, non-technical advice guiding the user to the correct course of action (Self-care, Routine visit, or Immediate care).