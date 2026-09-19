# Prospective Active Surveillance Cohort Study Protocol: Investigating Psychiatric Outcomes with Semaglutide vs. SGLT2 Inhibitors

**Document Version:** 1.0  
**Effective Date:** September 2026  
**Study Classification:** Methodological Simulation / Proposed Study Protocol  
**Project Phase:** Week 3 Experimental Design Simulation  
**Regulatory Alignment:** ICH-GCP E6(R2), ENCePP Guide on Methodological Standards in Pharmacoepidemiology  

---

> [!IMPORTANT]
> ### NOTICE OF SIMULATED PROTOCOL STATUS
> **THIS DOCUMENT REPRESENTS A PROPOSED STUDY DESIGN AND METHODOLOGICAL SIMULATION.**  
> It outlines an advanced prospective pharmacoepidemiological research protocol developed to address the epistemological limitations of spontaneous reporting pharmacovigilance (e.g., FDA FAERS). **No human participants have been recruited, randomized, or treated under this simulated protocol.** All sample size calculations, operational visit schedules, outcome assessment schedules, and analytical frameworks are designed for theoretical simulation and academic demonstration within the pharmaceutical research portfolio.

---

## 1. Scientific Background and Study Rationale

### 1.1 The Epistemological Gap in Spontaneous Pharmacovigilance
In Week 2 of this research portfolio, retrospective disproportionality analyses of the FDA FAERS database were conducted to assess post-marketing psychiatric adverse event signals associated with Semaglutide. While disproportionality metrics (such as the Reporting Odds Ratio and Proportional Reporting Ratio) provide vital early warning signals, spontaneous adverse event reporting systems suffer from intrinsic structural limitations:
1. **The Denominator Problem:** FAERS captures reported events (numerators) but possesses no record of total patient-years of drug exposure (denominators), precluding the calculation of true population incidence rates or absolute risk differences.
2. **Susceptibility to Reporting Biases:** Disproportionality signals are highly sensitive to the Weber effect, notoriety bias (stimulated reporting following media publicity or regulatory warnings), and severe underreporting of non-acute psychiatric morbidity.
3. **Absence of Baseline Psychiatric Stratification:** Spontaneous reports lack pre-treatment psychometric evaluations, making it impossible to differentiate treatment-emergent psychiatric events from preexisting, fluctuating affective disorders.

### 1.2 Rationale for a Prospective Active Surveillance Cohort
To overcome these limitations, a **prospective active surveillance cohort study with an active comparator** is the gold-standard observational design. By actively screening patients at scheduled intervals using standardized, psychometrically validated psychiatric instruments, this protocol:
* Establishes a true epidemiological denominator across time ($N = 2,000$ patient-years).
* Eliminates voluntary reporting bias through protocolized, active longitudinal monitoring.
* Controls for baseline psychiatric vulnerability and metabolic confounding through rigorous eligibility screening and multivariable propensity score adjustment.

---

## 2. Study Design and Architectural Framework

* **Study Architecture:** Prospective, multicenter, non-interventional active surveillance cohort study with active comparator design.
* **Observation Framework:** Real-world observational registry where pharmacological treatment decisions are made at the sole discretion of treating clinicians in routine clinical practice prior to and independent of study enrollment.
* **Duration of Follow-Up:** 12 months (52 weeks) of continuous longitudinal surveillance per participant.
* **Primary Study Arms:**
  1. **Exposure Arm:** Semaglutide (Subcutaneous or Oral formulation).
  2. **Active Comparator Arm:** Sodium-Glucose Co-Transporter-2 (SGLT2) Inhibitors (Empagliflozin, Dapagliflozin, or Canagliflozin).

```
                      STUDY WORKFLOW AND PARTICIPANT PROGRESSION
                      
               ┌─────────────────────────────────────────────────────────┐
               │    Target Population: Adults initiating pharmacotherapy │
               │          for Glycemic Control or Weight Management      │
               └────────────────────────────┬────────────────────────────┘
                                            │ Screening & Baseline Assessment
                                            ▼ (PHQ-9, C-SSRS, GAD-7, ISI)
               ┌─────────────────────────────────────────────────────────┐
               │            Eligibility Confirmation & Consent           │
               │    Excluding active psychosis / imminent suicide risk   │
               └──────────────┬───────────────────────────┬──────────────┘
                              │                           │
                              ▼                           ▼
        ┌───────────────────────────┐       ┌───────────────────────────┐
        │   EXPOSURE COHORT (N=1,000)│       │  COMPARATOR COHORT(N=1,000)│
        │   Semaglutide Initiation  │       │  SGLT2 Inhibitor Initiation│
        │  (Ozempic, Wegovy, Ryb.)  │       │  (Empa-, Dapa-, Cana-)    │
        └─────────────┬─────────────┘       └─────────────┬─────────────┘
                      │                                   │
                      └─────────────────┬─────────────────┘
                                        │
                                        ▼
               ┌─────────────────────────────────────────────────────────┐
               │       Active Surveillance Schedule: 12-Month Follow-Up  │
               │       Timepoints: Baseline, M1, M3, M6, M9, M12         │
               │       Assessments: ePRO (PHQ-9, C-SSRS, GAD-7, ISI)     │
               └────────────────────────┬────────────────────────────────┘
                                        │
                                        ▼
               ┌─────────────────────────────────────────────────────────┐
               │              Primary & Secondary Endpoints              │
               │  - New-onset Clinically Significant Depression (PHQ-9)  │
               │  - Treatment-Emergent Suicidal Ideation/Behavior(C-SSRS)│
               │  - Generalized Anxiety (GAD-7) & Insomnia (ISI)         │
               └────────────────────────┬────────────────────────────────┘
                                        │
                                        ▼
               ┌─────────────────────────────────────────────────────────┐
               │    Propensity Score Matched Survival & Cox Regression   │
               └─────────────────────────────────────────────────────────┘
```

---

## 3. Study Population and Eligibility Criteria

### 3.1 Target Population
Adult outpatients presenting in endocrinology, internal medicine, cardiology, or obesity medicine clinics with clinical indications for glycemic optimization (Type 2 Diabetes Mellitus) or chronic weight management (BMI $\ge 30 \text{ kg/m}^2$, or $\ge 27 \text{ kg/m}^2$ with weight-related comorbidities).

### 3.2 Inclusion Criteria
1. **Age Requirement:** Age $\ge 18$ years at the time of written informed consent.
2. **Treatment Initiation:** Physician decision to initiate either Semaglutide (any approved brand/route) or an SGLT2 inhibitor within 14 days prior to baseline evaluation.
3. **Treatment-Naïve Washout:** No exposure to GLP-1 receptor agonists or SGLT2 inhibitors within the preceding 12 months (new-user cohort design).
4. **Digital Literacy & Device Access:** Willingness and cognitive ability to complete electronic patient-reported outcome (ePRO) surveys via smartphone or computer.
5. **Informed Consent:** Voluntary written informed consent provided prior to protocol-specific procedures.

### 3.3 Exclusion Criteria
1. **Acute Psychiatric Instability:** Active psychotic disorder, bipolar disorder type I with acute mania, or active suicidal intent/behavior within the past 6 months (documented via baseline Columbia-Suicide Severity Rating Scale [C-SSRS] score $> 3$).
2. **Concurrent Dual Therapy:** Concomitant prescription of both a GLP-1 RA and an SGLT2 inhibitor at baseline.
3. **Substance Use Disorder:** Active moderate-to-severe substance use disorder (excluding tobacco/nicotine) within the past 12 months (DSM-5 criteria).
4. **Contraindicated Medical Conditions:** Personal or family history of medullary thyroid carcinoma (MTC), Multiple Endocrine Neoplasia syndrome type 2 (MEN 2), end-stage renal disease (eGFR $< 20 \text{ mL/min/1.73m}^2$), or active pregnancy/lactation.
5. **Life Expectancy:** Severely compromised medical condition with anticipated life expectancy $< 12$ months.

---

## 4. Exposure and Comparator Specifications

### 4.1 Primary Exposure Arm: Semaglutide Cohort
* **Agent:** Semaglutide (human glucagon-like peptide-1 receptor agonist).
* **Formulations Included:**
  * Subcutaneous once-weekly injection (Ozempic: 0.5 mg, 1.0 mg, 2.0 mg; Wegovy: 0.25 mg titrated up to 2.4 mg).
  * Oral daily tablet (Rybelsus: 3 mg, 7 mg, 14 mg).
* **Dosing:** Clinically titrated according to approved product labeling by the prescribing physician.

### 4.2 Active Comparator Arm: SGLT2 Inhibitor Cohort
* **Agent:** Approved oral Sodium-Glucose Co-Transporter-2 inhibitors:
  * Empagliflozin (Jardiance: 10 mg or 25 mg daily).
  * Dapagliflozin (Farxiga: 5 mg or 10 mg daily).
  * Canagliflozin (Invokana: 100 mg or 300 mg daily).
* **Active Comparator Rationale:**
  * Patients initiating SGLT2 inhibitors share baseline metabolic characteristics, disease duration, cardiovascular risk factors, and socioeconomic attributes with those initiating Semaglutide.
  * SGLT2 inhibitors exert glucose-lowering and weight-modulating effects through an insulin-independent renal glucosuria mechanism, having no established direct pharmacological interaction with central nervous system appetite/satiety circuitry or neuroendocrine monoaminergic pathways.
  * This active comparator design substantially mitigates confounding by indication relative to non-user or general population controls.

---

## 5. Outcome Measures and Psychometric Instruments

All primary and secondary psychiatric endpoints are measured using standardized, internationally validated psychometric instruments administered via an automated, secure ePRO platform.

```
                           PSYCHOMETRIC ASSESSMENT BATTERY
┌────────────────────────┬─────────────────────────┬──────────────────────────────────────────┐
│ Instrument Name        │ Construct Measured      │ Clinical Cutoff / Endpoint Definition    │
├────────────────────────┼─────────────────────────┼──────────────────────────────────────────┤
│ PHQ-9                  │ Major Depressive        │ Score >= 10 (Moderate to Severe) OR     │
│ (Patient Health        │ Symptom Severity        │ categorical increase >= 5 points from    │
│ Questionnaire-9)       │                         │ baseline.                                │
│                        │                         │                                          │
│ C-SSRS                 │ Suicidal Ideation       │ Any "Yes" on Ideation items 1-5 OR any   │
│ (Columbia-Suicide      │ and Suicidal Behavior   │ suicidal behavior during follow-up.      │
│ Severity Rating Scale) │                         │ Item 4-5 triggers urgent alert.          │
│                        │                         │                                          │
│ GAD-7                  │ Generalized Anxiety     │ Score >= 10 (Moderate to Severe Anxiety) │
│ (Generalized Anxiety   │ Severity                │                                          │
│ Disorder 7-item)       │                         │                                          │
│                        │                         │                                          │
│ ISI                    │ Sleep Maintenance and   │ Score >= 15 (Moderate to Severe Clinical │
│ (Insomnia Severity     │ Onset Latency           │ Insomnia)                                │
│ Index)                 │                         │                                          │
└────────────────────────┴─────────────────────────┴──────────────────────────────────────────┘
```

### 5.1 Primary Endpoint: Cumulative 12-Month Psychiatric Incidence
The primary composite safety endpoint is the **time to first occurrence of a treatment-emergent clinically significant depressive or suicidal event within 12 months of therapy initiation**, defined as either:
1. New-onset clinically significant depression: Patient Health Questionnaire-9 (PHQ-9) score $\ge 10$ (moderate-to-severe depression) in a patient with a baseline score $< 10$, OR an increase of $\ge 5$ points from baseline in a patient with mild baseline symptoms.
2. Treatment-emergent suicidal ideation or behavior: Columbia-Suicide Severity Rating Scale (C-SSRS) positive response on suicidal ideation items (Item 1: Wish to be dead; Item 2: Non-specific active suicidal thoughts; Item 3: Active suicidal ideation with any methods; Item 4: Active suicidal ideation with some intent; Item 5: Active suicidal ideation with specific plan and intent) or any suicidal behavior (preparatory acts, aborted attempts, interrupted attempts, actual attempts).

### 5.2 Secondary Endpoints
1. **Generalized Anxiety Emergence:** Time to first occurrence of a Generalized Anxiety Disorder 7-item (GAD-7) score $\ge 10$ in patients with baseline score $< 10$.
2. **Clinical Insomnia Emergence:** Time to first occurrence of an Insomnia Severity Index (ISI) score $\ge 15$ in patients with baseline score $< 15$.
3. **Severe Neuropsychiatric Events:** Rate of psychiatric-related emergency department presentations, psychiatric inpatient hospitalizations, or initiated psychiatric pharmacotherapy (antidepressants, anxiolytics, antipsychotics).
4. **Treatment Discontinuation:** All-cause and adverse-event-driven treatment discontinuation rates across the 12-month period.

---

## 6. Surveillance Schedule and Follow-up Timeline

Participants undergo longitudinal active monitoring over a 52-week period via a hybrid clinical-digital framework:

| Protocol Milestone | Visit Window | Delivery Modality | Clinical and Psychometric Data Collected |
| :--- | :--- | :--- | :--- |
| **Screening / Baseline** | Day -14 to Day 0 | In-Clinic | Informed consent; medical/psychiatric history; baseline BMI, HbA1c; PHQ-9, C-SSRS, GAD-7, ISI; medication reconciliation. |
| **Month 1 (Week 4)** | $\pm 3$ days | ePRO Digital | PHQ-9, C-SSRS, GAD-7, ISI; dose escalation tracking; tolerability check. |
| **Month 3 (Week 12)** | $\pm 7$ days | In-Clinic / Hybrid | Full psychometric battery (PHQ-9, C-SSRS, GAD-7, ISI); weight; blood pressure; adverse events; concomitant medication audit. |
| **Month 6 (Week 26)** | $\pm 7$ days | In-Clinic | Full psychometric battery; metabolic labs (HbA1c, fasting lipids); BMI; medication adherence check. |
| **Month 9 (Week 39)** | $\pm 7$ days | ePRO Digital | Full psychometric battery (PHQ-9, C-SSRS, GAD-7, ISI); dose verification; AE survey. |
| **Month 12 (Week 52)** | $\pm 10$ days | In-Clinic (Exit) | Final psychometric battery; complete metabolic panel; HbA1c; exit interview; adjudication of all reported adverse events. |

---

## 7. Sample Size Determination and Statistical Power

### 7.1 Statistical Parameter Assumptions
* **Significance Level ($\alpha$):** Two-sided $\alpha = 0.05$.
* **Statistical Power ($1 - \beta$):** $80\%$ ($0.80$).
* **Baseline Event Rate in Comparator Arm ($P_{\text{SGLT2i}}$):** In patients with type 2 diabetes or metabolic syndrome, the annual incidence of new-onset depressive symptoms or significant psychometric elevation in clinical trials is approximately $5.0\%$ ($0.050$).
* **Anticipated Event Rate in Semaglutide Arm ($P_{\text{Sema}}$):** To detect an absolute increase of $3.5\%$ (hypothesized incidence of $8.5\%$; Relative Risk / Hazard Ratio $\approx 1.70$), which represents a clinically meaningful safety signal:
  $$\Delta = P_{\text{Sema}} - P_{\text{SGLT2i}} = 0.085 - 0.050 = 0.035$$

### 7.2 Sample Size Formula for Two Independent Proportions
$$n = \frac{\left( Z_{\alpha/2} \sqrt{2 \bar{P} (1 - \bar{P})} + Z_{\beta} \sqrt{P_1(1 - P_1) + P_2(1 - P_2)} \right)^2}{(P_1 - P_2)^2}$$

Where:
* $Z_{\alpha/2} = 1.960$
* $Z_{\beta} = 0.842$
* $P_1 = 0.085, \quad P_2 = 0.050$
* $\bar{P} = \frac{0.085 + 0.050}{2} = 0.0675$

Applying the formulation yields an unadjusted sample size of approximately $816$ participants per arm ($1,632$ total).

### 7.3 Loss-to-Follow-Up and Final Target Cohort Size
Accounting for an anticipated $18.4\%$ attrition rate over 12 months due to loss to follow-up, transfer of care, or voluntary withdrawal:
$$N_{\text{Arm}} = \frac{816}{1 - 0.184} \approx 1,000 \text{ participants per arm}$$
$$\mathbf{Total \; Target \; Study \; Population \; (N) = 2,000 \; participants} \quad (1,000 \text{ Semaglutide}, \; 1,000 \text{ SGLT2i})$$

---

## 8. Confounding Control and Statistical Analysis Plan

### 8.1 Propensity Score Methodology
To balance observed baseline covariates between the non-randomized Semaglutide and SGLT2i cohorts, a **Propensity Score (PS)** will be estimated using multivariable logistic regression modeling the probability of initiating Semaglutide:
$$e(X) = P(\text{Exposure} = \text{Semaglutide} \mid X)$$

**Covariates Included in the Propensity Model ($X$):**
* Demographics: Age, sex, race/ethnicity, body mass index (BMI).
* Clinical Indication: Type 2 diabetes mellitus duration, baseline HbA1c, primary weight management indication without diabetes.
* Baseline Psychiatric Profile: Baseline PHQ-9, GAD-7, and ISI continuous scores, lifetime history of depression in clinical remission.
* Comorbidities: Hypertension, dyslipidemia, cardiovascular disease, chronic kidney disease (eGFR), sleep apnea.
* Concomitant Pharmacotherapy: Baseline antidepressant, anxiolytic, antihypertensive, and lipid-lowering therapies.

**Balancing Technique:** Inverse Probability of Treatment Weighting (IPTW) with stabilized weights, trimmed at the 1st and 99th percentiles to avoid extreme weights. Covariate balance will be verified using Standardized Mean Differences (SMD), with $SMD < 0.10$ indicating excellent balance.

### 8.2 Primary Time-to-Event Analysis
* **Survival Function Estimation:** Weighted Kaplan-Meier cumulative incidence curves will be constructed for both cohorts.
* **Proportional Hazards Regression:** Multivariable Cox proportional hazards models will estimate the adjusted Hazard Ratio (aHR) and corresponding 95% Confidence Intervals for the primary endpoint:
  $$h(t \mid \text{Exposure}, X) = h_0(t) \exp\left( \beta_1 \cdot \text{Semaglutide} + \sum \beta_j X_j \right)$$
* **Proportional Hazards Assumption:** Evaluated through inspection of Schoenfeld residuals against transformed time.

---

## 9. Ethical Safeguards and Patient Safety Monitoring

### 9.1 Automated Real-Time Psychiatric Alerts
Patient safety is paramount. The ePRO surveillance platform incorporates an automated electronic safety trigger:
1. **Trigger Condition:** Any participant endorsing:
   * A positive score on C-SSRS Item 4 (active suicidal ideation with intent) or Item 5 (active suicidal ideation with specific plan and intent).
   * Any suicidal behavior within the preceding interval.
   * Score $\ge 2$ on PHQ-9 Item 9 ("Thoughts that you would be better off dead, or of hurting yourself in some way").
2. **Automated Response Protocol:**
   * Immediate on-screen provision of national crisis resources (e.g., 988 Suicide & Crisis Lifeline).
   * Automated high-priority SMS and email alerts dispatched to the site Principal Investigator and designated on-call study psychiatrist within 15 minutes.
   * Mandatory telephone contact and clinical triage conducted within 2 hours of alert trigger.

### 9.2 Data Safety Monitoring Board (DSMB)
An independent DSMB consisting of two board-certified psychiatrists, an endocrinologist, and an independent biostatistician will conduct scheduled interim safety reviews at 25%, 50%, and 75% patient enrollment. Formal Haybittle-Peto stopping boundaries will be utilized; if the Semaglutide arm exhibits a statistically significant excess in validated suicidal ideation or behavior ($p < 0.001$), the DSMB is mandated to recommend immediate trial suspension.

---

## 10. References (APA 7th Edition)

* Austin, P. C. (2011). An introduction to propensity score methods for reducing the effects of confounding in observational studies. *Multivariate Behavioral Research*, 46(3), 399–424. https://doi.org/10.1080/00273171.2011.568786
* Bastien, C. H., Vallières, A., & Morin, C. M. (2001). Validation of the Insomnia Severity Index as an outcome measure for insomnia research. *Sleep Medicine*, 2(4), 297–307. https://doi.org/10.1016/S1389-9457(00)00065-4
* European Network of Centres for Pharmacoepidemiology and Pharmacovigilance. (2024). *The ENCePP guide on methodological standards in pharmacoepidemiology (Rev 10)*. European Medicines Agency.
* International Council for Harmonisation. (2016). *Integrated addendum to ICH E6(R1): Guideline for good clinical practice E6(R2)*. ICH Harmonised Guideline.
* Kroenke, K., Spitzer, R. L., & Williams, J. B. (2001). The PHQ-9: Validity of a brief depression severity measure. *Journal of General Internal Medicine*, 16(9), 606–613. https://doi.org/10.1046/j.1525-1497.2001.016009606.x
* Posner, K., Brown, G. K., Stanley, B., Brent, D. A., Yershova, K. V., Oquendo, M. A., Currier, G. W., Melvin, G. A., Greenhill, L., Shen, S., & Mann, J. J. (2011). The Columbia-Suicide Severity Rating Scale: Initial validity and internal consistency findings from three multisite studies with adolescents and adults. *American Journal of Psychiatry*, 168(12), 1266–1277. https://doi.org/10.1176/appi.ajp.2011.10111704
* Spitzer, R. L., Kroenke, K., Williams, J. B., & Löwe, B. (2006). A brief measure for assessing generalized anxiety disorder: The GAD-7. *Archives of Internal Medicine*, 166(10), 1092–1097. https://doi.org/10.1001/archinte.166.10.1092
* Vandenbroucke, J. P., von Elm, E., Altman, D. G., Gøtzsche, P. C., Mulrow, C. D., Pocock, S. J., Poole, C., Schlesselman, J. J., & Egger, M. (2007). Strengthening the Reporting of Observational Studies in Epidemiology (STROBE): Explanation and elaboration. *PLOS Medicine*, 4(10), e297. https://doi.org/10.1371/journal.pmed.0040297
