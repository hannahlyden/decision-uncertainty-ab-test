# Executive Memo: Effects of Uncertainty Display on Decision-Making
**Hannah Lyden**
**February 2, 2026**

## 1. Objective

The purpose of this analysis is to evaluate how displaying uncertainty affects decision-making behavior in a simulated A/B test environment. Specifically, we examined:
- Whether uncertainty affects **choice selection**.
- Whether uncertainty improves **decision accuracy** (alignment with the true effect).
- Whether uncertainty changes the **decision-making process** (e.g., deliberation time).

These insights can guide design choices in decision-support systems, highlighting tradeoffs between cognitive effort and speed.

## 2. Methods

### Experimental Design

- **Groups**: Control (no uncertainty displayed) vs. Treatment (uncertainty displayed).
- **Participants**: Simulated decision-makers.
- **Tasks**: Each participant made multiple binary decisions under varying evidence strength (High, Moderate, Low).

### Hypotheses
| Hypothesis | Expected Direction |
|------------|--------------------|
| 1. Choice Selection | Treatment may alter choice probabilities depending on evidence strength |
| 2. Decision Accuracy | Treatment may increase alignment with true effect |
| 3. Decision Time | Treatment increases deliberation time, especially under low evidence |

### Analyses

1. **Logistic Regression**
- Model: `chosen_option ~ evidence_strength * treatment_group`
- Outcome: probability of selecting the positive-effect option

2. **Linear Regression**
- Model: `decision_time_sec ~ evidence_strength + treatment_group`
- Outcome: decision time in seconds

3. **Secondary Analyses**
- Within-person choice consistency
- Predicted probabilities by treatment and evidence strength
- Alignment with true effect

### Figures / Tables Reference:

Table 1: Logistic regression coefficients and significance  
Figure 1: Choice distribution by treatment & evidence strength (stacked bar)  
Table 2: Predicted probabilities by group and evidence strength  
Figure 2: Decision time by treatment group (boxplot)  
Table 3: Accuracy by treatment group (alignment with true effect)  
Figure 3: Heatmap of alignment with true effect  

## 3. Results

### 3.1 Choice Behavior
- Logistic regression indicates no statistically significant differences in choice selection between treatment groups or across evidence levels.
- Predicted probabilities (Table 2) show minor directional differences but are small: treatment group is slightly less likely to choose the positive-effect option under low evidence.

**Figure 1**: Choice distribution by treatment & evidence strength
- Stacked bars show proportions of choices for each evidence level in Control vs. Treatment.

**Table 1**: Logistic regression output
- Includes coefficients, standard errors, z-values, and p-values for evidence strength, treatment, and interaction terms.

### 3.2 Decision Accuracy

- Overall alignment with the true effect is high:
    - **Control**: 94% correct
    - **Treatment**: 92% correct

**Figure 3 / Table 3**: Heatmap and summary of alignment with true effect
- Shows accuracy across treatment and evidence levels, confirming minimal impact on outcome quality.
- Within-person consistency is slightly higher in the treatment group, suggesting **more stable decision patterns**, though differences are modest.

### 3.3 Decision Time

- Treatment significantly increased decision time by ~3 seconds.
- Low-evidence scenarios require more time to decide (+1.56 seconds relative to high evidence).
- This supports the hypothesis that uncertainty affects the decision process, not just the outcome.

**Figure 2**: Decision time by treatment group (boxplot)
- Clear separation of medians, with wider interquartile range in treatment group.

## 4. Interpretation

- **Process vs. Outcome**: Uncertainty display encourages slower, more deliberate decisions without substantially improving accuracy.
- **Ceiling Effect**: Accuracy is high in all conditions, so the lack of choice differences is consistent with near-optimal decision-making.
- **Tradeoffs**: Displaying uncertainty adds cognitive effort (slower decisions) but does not harm choice quality.
- **Behavioral Signal**: Small improvements in within-person consistency suggest that uncertainty may encourage more consistent decision strategies.

## 5. Recommendations

1. Use uncertainty cues when deliberation is desirable
    - For high-stakes or ambiguous decisions, displaying uncertainty can encourage careful thought.

2. Avoid for low-stakes, time-sensitive decisions
    - The 3-second delay per decision may reduce throughput or user satisfaction without improving outcomes.

3. Further Testing:
    - Evaluate with real users and more complex decision scenarios to validate these simulated findings.

## 6. Key Takeaways (Executive Summary)

- Uncertainty display **does not change choice outcomes** in high-accuracy scenarios.
- Uncertainty **increases deliberation time**, especially under low evidence.
- Minor improvements in decision consistency suggest process-level effects.
- Implication: uncertainty can be a **reflective feature** to encourage careful decision-making, with tradeoffs in speed.