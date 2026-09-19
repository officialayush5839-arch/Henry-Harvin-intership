# Conceptual Framework: Semaglutide Pharmacovigilance

## 1. The Pathway of Signal Detection
The pharmacovigilance lifecycle for semaglutide begins with spontaneous reporting. Patients, healthcare providers, and manufacturers submit reports of adverse events to databases like FAERS. This uncurated influx of data serves as the foundational substrate for signal detection, acting as an early warning system for rare or unforeseen adverse drug reactions (ADRs).

## 2. Disproportionality Analysis (ROR/PRR Framework)
To extract meaningful signals from the noise of spontaneous reports, researchers employ disproportionality analysis. This statistical framework relies on metrics like the Reporting Odds Ratio (ROR) or Proportional Reporting Ratio (PRR). These metrics compare the frequency of a specific ADR reported for semaglutide against the background reporting rate of that same ADR for all other drugs in the database. A statistically significant ROR suggests a potential safety signal requiring further investigation.

## 3. Evaluating Signals: The Bradford Hill Criteria
A critical component of this conceptual model is the transition from statistical association (signal generation) to causal inference. Disproportionality alone cannot establish causality. To bridge this gap, generated signals must be evaluated using frameworks like the Bradford Hill criteria, assessing factors such as biological plausibility, temporality, consistency across studies, and dose-response relationships.

## 4. Visual Conceptual Diagram

```mermaid
graph TD
    A[Post-Market Drug Exposure (Semaglutide)] --> B(Spontaneous AE Reporting)
    B --> C{FAERS Database}
    C --> D[Data Mining & Extraction]
    D --> E(Disproportionality Analysis)
    E -->|Calculate ROR/PRR| F{Signal Generation}
    F -->|Significant Signal| G[Causal Evaluation]
    G -->|Bradford Hill Criteria| H{Validated Signal}
    H -->|Yes| I[Regulatory Action / Label Update]
    H -->|No / Confounded| J[Further Epidemiological Study]
    
    %% Connections to other findings
    G -.->|Conflicts with| K[RWE / Cohort Studies e.g., Wang et al.]
    E -.->|Methodological Control| L[READUS-PV Guidelines]
```

## 5. Integrating Project Findings
This conceptual framework contextualizes the Week 1 findings. The rapid growth of studies (Trend 1) represents an intensification at the 'Data Mining' node. The discovery of NAION or psychiatric signals (Breakthroughs) are instances of 'Signal Generation'. However, the critical contradiction provided by Wang et al. (Nature Medicine) demonstrates the vital loop where a FAERS-generated signal is challenged during 'Causal Evaluation' by robust Real-World Evidence (RWE), highlighting the 'Confounding by Indication' challenge. Furthermore, the implementation of READUS-PV acts as a necessary regulatory filter operating on the 'Disproportionality Analysis' node.

## 6. Connection to Future Weeks
This Week 1 synthesis establishes the baseline landscape of semaglutide PV. Week 2 will likely build upon this by delving into specific epidemiological validation studies (like Wang et al.) that test the FAERS signals. Week 3 and 4 will involve synthesizing these divergent data streams (SRS vs. RWE) to formulate comprehensive risk-benefit assessments and propose targeted future research methodologies, addressing the gaps identified in this initial framework.
