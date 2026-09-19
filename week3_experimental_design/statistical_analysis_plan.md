# Statistical Analysis Plan (SAP)

**Disclaimer: This document outlines a SIMULATED/PROPOSED experimental design for educational and portfolio purposes. It is NOT an executed clinical trial.**

## Primary Endpoint Analysis
- **Model:** The primary analysis will utilize a Cox Proportional Hazards regression model to compare the time to the first onset of a new psychiatric disorder (defined by clinical thresholds on the PHQ-9 or GAD-7) between the Semaglutide and SGLT2 inhibitor groups.
- **Output:** Results will be reported as a Hazard Ratio (HR) with a 95% Confidence Interval (CI) and associated p-value.
- **Covariates:** The model will adjust for the stratification variables: biological sex, age group, and baseline PHQ-9 score category.

## Secondary Analysis
- **Survival Curves:** Kaplan-Meier survival curves will be plotted to visually assess the cumulative incidence of psychiatric events over the 12-month period.
- **Comparison:** A log-rank test will be used to compare the survival distributions between the two treatment arms.

## Subgroup Analyses
To identify specific vulnerable populations or differential effects, subgroup analyses will be conducted based on:
- Biological Sex (Male vs. Female)
- Age categories
- Baseline BMI (Obesity vs. Severe Obesity)
- Baseline PHQ-9 scores (Minimal vs. Mild)

## Sensitivity Analyses
- **Per-Protocol Analysis:** While the primary analysis is Intention-To-Treat (ITT), a per-protocol analysis will be conducted, including only patients who adhered strictly to the treatment regimen and completed all assessments.
- **Missing Data:** Multiple imputation techniques using chained equations (MICE) will be employed to handle missing data, assuming data is Missing at Random (MAR).

## Multiplicity Adjustment
- To control the Family-Wise Error Rate (FWER) across multiple secondary endpoints and subgroup analyses, a Hochberg step-up procedure will be implemented.

## Software
- All statistical analyses will be performed using **R** (specifically relying on the `survival` and `survminer` packages) or **Python** (utilizing the `lifelines` library), depending on the analytical team's workflow preferences. Code will be version-controlled via Git.
