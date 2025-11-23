# Basic-Triage
Basic Symptom Checker/Triage Tool

## Project Overview

This project is a Command Line Interface (CLI) application designed as a preliminary health risk assessment tool. It functions as a rule-based expert system, taking user-reported symptoms and demographic data (age, duration) to calculate a weighted **Triage Score**. The score is then classified into an actionable risk category: **LOW**, **MEDIUM**, or **HIGH** risk. The primary goal is to provide immediate, high-performance ($\mathbf{< 1 \text{s}}$) guidance to the user.

## Features

  * **Modular Design:** Separated into three distinct functional modules: Input, Decision Engine, and Output.
  * **Rule-Based Classification:** Uses an external JSON configuration file to assign weights to symptoms and define risk thresholds.
  * **Performance Guaranteed:** The core calculation logic is optimized to execute in less than 1 second, fulfilling a key Non-Functional Requirement (NFR).
  * **Critical Override Logic:** Instantly flags high-risk symptom combinations (e.g., chest pain and shortness of breath) regardless of the overall score.
  * **Robust Input Validation:** Includes error handling for incorrect data types and ranges during user input.
  * **Maintainable Configuration:** All medical rules and recommendations are stored externally in `triage_rules.json`.

## Technologies/Tools Used

  * **Language:** Python 3.x
  * **Core Libraries:**
      * `json` (for reading configuration rules)
      * `time` (for measuring performance NFR compliance)
  * **Testing:** `unittest` (for verifying core logic)
  * **Version Control:** Git

## Steps to Install & Run the Project

### Prerequisites

You must have **Python 3.x** installed on your system.

### Installation

### Running the Application

1.  Ensure the configuration file, **`triage_rules.json`**, is present in the main directory.
2.  Execute the main script from your terminal:
    python main.py
3.  Follow the prompts to enter your age, symptom duration, and the severity of the available symptoms.

##  Instructions for Testing

Unit tests are used to verify the integrity and accuracy of the core Decision Engine logic.

1.  Ensure you are in the project's root directory (`symptom_checker/`).
2.  Run the Python `unittest` module:
      python -m unittest

##  Key Tests Verified:

  * **Threshold Testing:** Confirms inputs near the risk boundaries (LOW/MEDIUM, MEDIUM/HIGH) are classified correctly.
  * **Critical Overrides:** Verifies that inputs matching critical rules bypass normal scoring and result in an immediate **HIGH** risk classification.
  * **Performance Compliance:** Tests confirm the calculation time remains well within the **1 second** NFR limit.
