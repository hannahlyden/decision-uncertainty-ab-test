# simulate_data.py
import numpy as np
import pandas as pd

# ------------------------------
# 1. Global Settings
# ------------------------------
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

N_PEOPLE = 50
N_SCENARIOS = 25
DECISIONS_PER_PERSON = 10
PROP_TREATED = 0.5

# True effect distribution
TRUE_EFFECT_MEAN = 0
TRUE_EFFECT_SD = 5

# Standard error distribution
SE_LOGMEAN = 0
SE_LOGSD = 0.5

# Risk tolerance per decision maker
RISK_TOL_MEAN = 0
RISK_TOL_SD = 0.5

# Decision noise
DECISION_NOISE_SD = 0.1

# Uncertainty penalties (for treatment group)
UNCERTAINTY_PENALTY = {"High": 1.0, "Moderate": 0.5, "Low": 0.2}

# Decision time parameters
BASE_DECISION_TIME = 20  # seconds
UNCERTAINTY_TIME_COST = 2
EXTRA_UNCERTAINTY_COST = 3
TIME_NOISE_SD = 1.0

# ------------------------------
# 2. Create Decision-Makers
# ------------------------------
decision_makers = pd.DataFrame({
    "decision_maker_id": range(1, N_PEOPLE + 1),
    "risk_tolerance": np.random.normal(RISK_TOL_MEAN, RISK_TOL_SD, N_PEOPLE)
})

# ------------------------------
# 3. Create Decision Scenarios
# ------------------------------
scenarios = pd.DataFrame({
    "scenario_id": range(1, N_SCENARIOS + 1),
    "true_effect": np.random.normal(TRUE_EFFECT_MEAN, TRUE_EFFECT_SD, N_SCENARIOS),
    "standard_error": np.random.lognormal(SE_LOGMEAN, SE_LOGSD, N_SCENARIOS)
})

# ------------------------------
# 4. Generate Decisions
# ------------------------------
all_decisions = []

decision_id = 1
for _, person in decision_makers.iterrows():
    chosen_scenarios = np.random.choice(scenarios["scenario_id"], DECISIONS_PER_PERSON, replace=False)
    
    for scenario_id in chosen_scenarios:
        scenario = scenarios.loc[scenarios["scenario_id"] == scenario_id].iloc[0]
        
        # Assign treatment
        treatment_group = np.random.binomial(1, PROP_TREATED)
        
        # Generate observed estimate
        estimated_effect = scenario["true_effect"] + np.random.normal(0, scenario["standard_error"])
        
        # Compute CI width and derive evidence strength
        ci_width = 2 * 1.96 * scenario["standard_error"]
        if ci_width <= np.percentile(2 * 1.96 * scenarios["standard_error"], 33):
            evidence_strength = "High"
        elif ci_width <= np.percentile(2 * 1.96 * scenarios["standard_error"], 66):
            evidence_strength = "Moderate"
        else:
            evidence_strength = "Low"
        
        # ------------------------------
        # Decision score
        # ------------------------------
        if treatment_group == 0:
            # Control: ignores uncertainty
            decision_score = estimated_effect + person["risk_tolerance"] + np.random.normal(0, DECISION_NOISE_SD)
        else:
            # Treatment: accounts for uncertainty
            penalty = UNCERTAINTY_PENALTY[evidence_strength]
            decision_score = estimated_effect - penalty + person["risk_tolerance"] + np.random.normal(0, DECISION_NOISE_SD)
        
        # Generate choice
        chosen_option = 1 if decision_score > 0 else 0
        
        # Decision quality
        correct_direction = 1 if (chosen_option == 1 and scenario["true_effect"] > 0) or \
                                  (chosen_option == 0 and scenario["true_effect"] <= 0) else 0
        
        # Decision time
        decision_time = BASE_DECISION_TIME
        if treatment_group == 1:
            decision_time += UNCERTAINTY_TIME_COST
            if evidence_strength == "Low":
                decision_time += EXTRA_UNCERTAINTY_COST
        decision_time += np.random.normal(0, TIME_NOISE_SD)
        
        # Save row
        all_decisions.append({
            "decision_id": decision_id,
            "decision_maker_id": person["decision_maker_id"],
            "scenario_id": scenario_id,
            "treatment_group": treatment_group,
            "estimated_effect": estimated_effect,
            "standard_error": scenario["standard_error"],
            "ci_width": ci_width,
            "evidence_strength": evidence_strength,
            "true_effect": scenario["true_effect"],
            "chosen_option": chosen_option,
            "decision_time_sec": decision_time,
            "correct_direction": correct_direction
        })
        
        decision_id += 1

# ------------------------------
# 5. Combine and Save
# ------------------------------
df = pd.DataFrame(all_decisions)
df.to_csv("decisions_analysis_ready.csv", index=False)
print("Simulation complete! Saved to 'decisions_analysis_ready.csv'.")
