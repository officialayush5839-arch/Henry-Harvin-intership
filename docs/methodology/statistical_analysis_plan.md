# Statistical Analysis Plan: Pharmacovigilance Disproportionality and Signal Detection

**Document Version:** 1.0  
**Effective Date:** September 2026  
**Status:** Approved Analytical Protocol  
**Project:** Pharmacovigilance of Semaglutide (GLP-1 Receptor Agonist)  
**Methodology:** Quantitative Disproportionality Analysis and Spontaneous Reporting Epidemiology  

---

## 1. Introduction and Analytical Objectives

This Statistical Analysis Plan (SAP) outlines the comprehensive quantitative framework for evaluating post-marketing adverse drug reaction (ADR) signals from the FDA Adverse Event Reporting System (FAERS). 

The primary investigative question is:
> *Is Semaglutide exposure associated with a statistically significant disproportional reporting signal for psychiatric adverse drug reactions compared to active comparator Sodium-Glucose Co-Transporter-2 (SGLT2) inhibitors?*

### 1.1 Formal Statistical Hypotheses
The primary research hypothesis is evaluated using the Reporting Odds Ratio (ROR) framework:

* **Null Hypothesis ($H_0$):**  
  The reporting odds of psychiatric adverse events for Semaglutide do not exceed the reporting odds for the comparator class (SGLT2 inhibitors).
  $$H_0: ROR \le 1.0$$

* **Alternative Hypothesis ($H_1$):**  
  The reporting odds of psychiatric adverse events for Semaglutide significantly exceed the reporting odds for the comparator class.
  $$H_1: ROR > 1.0$$

---

## 2. Descriptive Statistical Analysis Plan

Descriptive statistics will be computed to characterize the distribution of reports, quantify event frequencies, describe patient and reporter demographics, and evaluate longitudinal reporting trajectories.

### 2.1 ADR Frequency and Categorical Distribution
* **Categorical Metrics:** For each target MedDRA Preferred Term (Depression, Depressed mood, Suicidal ideation, Suicide attempt, Anxiety, Insomnia, Panic attack) and grouped psychiatric clusters, frequency counts ($n$) and relative proportions (%) will be tabulated:
  $$P_{\text{ADR}} = \left( \frac{n_{\text{ADR}}}{\sum N_{\text{Cohort}}} \right) \times 100\%$$
* **Severity Profiling:** Serious outcome distributions will be tabulated across both cohorts, broken down by FDA outcome codes:
  * Death (`DE`)
  * Life-Threatening (`LT`)
  * Hospitalization — Initial or Prolonged (`HO`)
  * Disability or Permanent Impairment (`DS`)
  * Congenital Anomaly (`CA`)
  * Required Intervention to Prevent Permanent Harm (`RI`)
  * Other Serious Medical Event (`OT`)

### 2.2 Demographic and Reporter Characterization
Demographic attributes extracted from the `DEMO` table will be summarized to identify potential cohort imbalances:
* **Age Distribution:** Continuous age data will be summarized using mean, standard deviation (SD), median, and interquartile range (IQR). Age will also be stratified into categorical cohorts:
  * Pediatric: $< 18$ years
  * Young Adults: $18 - 44$ years
  * Middle-Aged Adults: $45 - 64$ years
  * Older Adults: $\ge 65$ years
  * Unspecified / Missing
* **Biological Sex:** Absolute frequencies and percentages for Male, Female, and Unknown/Not Specified.
* **Reporter Qualification:** Stratification by reporter occupational category (`occp_cod`):
  * Physician (`MD`)
  * Pharmacist (`PH`)
  * Other Healthcare Professional (Nurse, Physician Assistant) (`HP`)
  * Consumer / Non-Healthcare Professional (`CN`)
  * Legal Representative (`LW`)
* **Geographic Origin:** Top reporting countries based on ISO country codes.

### 2.3 Temporal Trend Analysis
* **Longitudinal Reporting Density:** Quarterly reporting volumes from 2018 Q1 through 2025 Q2 will be tracked for both Semaglutide and SGLT2 inhibitors.
* **Milestone Mapping:** Time-series trends will be evaluated against critical clinical and regulatory milestones:
  * June 2021: FDA approval of Wegovy (Semaglutide 2.4 mg) for chronic weight management.
  * July 2023: European Medicines Agency (EMA) Pharmacovigilance Risk Assessment Committee (PRAC) initiation of safety review regarding GLP-1 RAs and suicidal ideation.
  * January 2024: FDA preliminary update on GLP-1 RAs and suicidal thoughts or actions.
* **Trend Metric:** Relative quarterly reporting proportion:
  $$RQP_t = \frac{n_{\text{Psychiatric}, t}}{N_{\text{All ADRs}, t}}$$

---

## 3. Disproportionality Analysis Framework

Disproportionality analysis evaluates whether a specific adverse event is reported more frequently in conjunction with a specific drug than would be expected based on the background reporting frequency across the database or an active comparator.

### 3.1 The 2×2 Contingency Matrix
The foundation of disproportionality metrics is the standard $2 \times 2$ contingency table:

| Drug Exposure Group | Target Psychiatric ADR | All Other Adverse Events | Total Drug Reports |
| :--- | :---: | :---: | :---: |
| **Semaglutide (Primary Exposure)** | $a$ | $b$ | $a + b$ |
| **SGLT2 Inhibitors (Active Comparator)** | $c$ | $d$ | $c + d$ |
| **Total Event Reports** | $a + c$ | $b + d$ | $N$ |

Where:
* **$a$**: Number of reports documenting Semaglutide and the target psychiatric ADR.
* **$b$**: Number of reports documenting Semaglutide and any other non-target adverse event.
* **$c$**: Number of reports documenting an SGLT2 inhibitor and the target psychiatric ADR.
* **$d$**: Number of reports documenting an SGLT2 inhibitor and any other non-target adverse event.
* **$N$**: Total cumulative reports across both cohorts ($N = a + b + c + d$).

---

### 3.2 Reporting Odds Ratio (ROR)
The Reporting Odds Ratio represents the odds of a specific event being reported for the drug of interest divided by the odds of that same event being reported for the comparator group.

#### Point Estimate:
$$ROR = \frac{a / b}{c / d} = \frac{a \times d}{b \times c}$$

#### Standard Error of the Natural Logarithm:
Under the asymptotic normal approximation of the log-transformed odds ratio:
$$SE(\ln(ROR)) = \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}}$$

#### 95% Confidence Interval:
$$\ln(ROR)_{95\%\text{ CI}} = \ln(ROR) \pm 1.96 \times SE(\ln(ROR))$$
$$95\% \text{ CI} = \left[ \exp\left( \ln(ROR) - 1.96 \times SE(\ln(ROR)) \right), \; \exp\left( \ln(ROR) + 1.96 \times SE(\ln(ROR)) \right) \right]$$

---

### 3.3 Proportional Reporting Ratio (PRR)
The Proportional Reporting Ratio evaluates the proportion of target ADR reports among all reports for the drug of interest relative to the corresponding proportion in the comparator group.

#### Point Estimate:
$$PRR = \frac{a / (a + b)}{c / (c + d)}$$

#### Standard Error of the Natural Logarithm:
$$SE(\ln(PRR)) = \sqrt{\frac{1}{a} - \frac{1}{a + b} + \frac{1}{c} - \frac{1}{c + d}}$$

#### 95% Confidence Interval:
$$95\% \text{ CI} = \left[ \exp\left( \ln(PRR) - 1.96 \times SE(\ln(PRR)) \right), \; \exp\left( \ln(PRR) + 1.96 \times SE(\ln(PRR)) \right) \right]$$

---

### 3.4 Pearson's Chi-Square Test ($\chi^2$)
To test the null hypothesis of independence between drug exposure and adverse event occurrence, Pearson's Chi-Square statistic is calculated:

$$\chi^2 = \frac{N (a \cdot d - b \cdot c)^2}{(a + b)(c + d)(a + c)(b + d)}$$

With degrees of freedom $df = (2 - 1) \times (2 - 1) = 1$.  
The critical threshold for statistical significance at $\alpha = 0.05$ is $\chi^2 \ge 3.841$ (or $\chi^2 \ge 4.0$ under standard regulatory signal detection heuristics).

#### Yates' Continuity Correction:
When cell counts are moderately small, Yates' corrected chi-square is computed to prevent inflation of Type I error:
$$\chi^2_{\text{Yates}} = \frac{N \left( |a \cdot d - b \cdot c| - \frac{N}{2} \right)^2}{(a + b)(c + d)(a + c)(b + d)}$$

---

## 4. Signal Detection Decision Criteria

To establish an authoritative, reproducible pharmacovigilance safety signal, a composite threshold model combining the criteria established by Evans et al. (2001) and European Medicines Agency (EMA) guidelines is applied.

A positive safety signal for a given MedDRA Preferred Term or cluster requires satisfying **ALL FOUR** of the following quantitative conditions simultaneously:

```
                                  SIGNAL DETECTION THRESHOLD MATRIX
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. Reporting Odds Ratio (ROR):                                                             │
│    Lower bound of the two-sided 95% Confidence Interval > 1.0                               │
│    (i.e., ROR_lower > 1.00)                                                                 │
│                                                                                             │
│ 2. Proportional Reporting Ratio (PRR):                                                      │
│    PRR >= 2.00                                                                              │
│                                                                                             │
│ 3. Statistical Test of Independence:                                                        │
│    Chi-Square (chi^2) >= 4.00 (p < 0.0455, df = 1)                                          │
│                                                                                             │
│ 4. Minimum Case Burden Threshold:                                                           │
│    Number of exposed cases documenting the event a >= 3                                     │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

If $a \ge 3$, $PRR \ge 2.0$, $\chi^2 \ge 4.0$, and $ROR_{\text{lower}} > 1.0$, the event is classified as an **Emergent Disproportionality Signal**. If any condition fails, the finding is classified as **No Statistically Disproportionate Signal**.

---

## 5. Statistical Assumptions, Justifications, and Fallback Procedures

| Assumption / Requirement | Theoretical Rationale | Potential Violation Scenario | Fallback Procedure / Diagnostic |
| :--- | :--- | :--- | :--- |
| **Cell Count Expectation ($\chi^2$)** | The asymptotic approximation for $\chi^2$ requires that expected cell frequencies be $\ge 5$ in all cells (or $\ge 80\%$ of cells with none $< 1$). | Ultra-rare adverse event terms (e.g., specific completed suicide codes with $a < 5$ or $c < 5$). | **Fisher's Exact Test:** If any expected frequency $E_{ij} = \frac{R_i C_j}{N} < 5$, two-tailed Fisher's exact test is executed to compute exact hypergeometric probability: <br> $p = \frac{(a+b)!(c+d)!(a+c)!(b+d)!}{a!b!c!d!N!}$ |
| **Independence of Observations** | Disproportionality equations assume that each record in the $2 \times 2$ table represents an independent biological event and patient. | Unidentified duplicate submissions, multiple reports for the same patient across consecutive quarters. | **Stringent Deduplication:** Algorithmic filtering retaining only `max(caseversion)` per `caseid` and multivariate duplicate screening prior to contingency table construction. |
| **Discrete Count Distribution** | FAERS data are discrete frequency counts characterized by severe right-skewness and overdispersion. | Applying continuous Gaussian parametric methods (e.g., standard linear regression) would introduce severe model misspecification. | **Non-Parametric & Odds Ratio Methods:** Disproportionality metrics (ROR, PRR) and exact non-parametric tests are inherently appropriate for discrete contingency data without requiring normality assumptions. |
| **Homogeneity Across Strata** | The crude association between Semaglutide and psychiatric ADRs may be confounded by patient age or sex. | Baseline demographic divergence between Semaglutide users (e.g., younger, higher female proportion for obesity) and SGLT2i users. | **Stratified Mantel-Haenszel Odds Ratio ($ROR_{MH}$):** Stratification by sex (Male vs Female) and age category ($< 65$ vs $\ge 65$) to compute adjusted summary odds ratios and evaluate confounding: <br> $ROR_{MH} = \frac{\sum (a_k d_k / N_k)}{\sum (b_k c_k / N_k)}$ |

---

## 6. Epistemological Scope: What the Analysis Can and Cannot Conclude

To maintain graduate-level academic integrity, the analytical outputs must be interpreted within the recognized epistemological boundaries of spontaneous reporting pharmacovigilance.

```
┌───────────────────────────────────────────────┐   ┌───────────────────────────────────────────────┐
│          WHAT THIS ANALYSIS CAN CONCLUDE      │   │       WHAT THIS ANALYSIS CANNOT CONCLUDE      │
├───────────────────────────────────────────────┤   ├───────────────────────────────────────────────┤
│ 1. Identification of Disproportionate Signals │   │ 1. Proof of Biological or Clinical Causation  │
│    Detects whether psychiatric ADRs are       │   │    Spontaneous reports cannot confirm that    │
│    reported with higher relative frequency    │   │    the drug directly induced the event.       │
│    for Semaglutide than an active comparator. │   │                                               │
│                                               │   │ 2. True Population Incidence or Absolute Risk │
│ 2. Generation of Empirical Hypotheses         │   │    Lacks a defined denominator (total number  │
│    Flags specific neurobehavioral patterns    │   │    of treated patients is entirely unknown).  │
│    warranting prospective clinical trials.    │   │                                               │
│                                               │   │ 3. Relative Risk Equivalence                  │
│ 3. Quantification of Reporting Disparity      │   │    ROR and PRR are reporting ratios, not      │
│    Measures the magnitude and precision of    │   │    true epidemiological Relative Risks (RR).  │
│    disproportional reporting (ROR, PRR, CI).  │   │                                               │
│                                               │   │ 4. Ruling Out Unmeasured Confounders          │
│ 4. Characterization of Reporting Trends       │   │    Underlying depression, obesity distress,   │
│    Tracks longitudinal dynamics before and    │   │    or life stressors cannot be controlled.    │
│    after regulatory alerts or approvals.      │   │                                               │
└───────────────────────────────────────────────┘   └───────────────────────────────────────────────┘
```

### 6.1 Key Systematic Biases in Spontaneous Pharmacovigilance
1. **Underreporting and Selective Reporting:** The vast majority of real-world adverse events are never reported to the FDA. Reports in FAERS reflect voluntary, non-random sampling, which may over-represent severe, unexpected, or highly publicized events.
2. **The Weber Effect:** A documented phenomenon wherein adverse event reporting rates for newly approved pharmaceutical products peak within the first 1 to 2 years following market entry and subsequently decline, regardless of true incidence.
3. **Notoriety Bias (Stimulated Reporting):** High-profile regulatory inquiries (such as the 2023 EMA probe) and intense mass media coverage regarding GLP-1 receptor agonists and mental health trigger stimulated reporting among both consumers and clinicians. This artificially inflates the numerator ($a$), potentially producing a spurious statistical signal.
4. **Channeling Bias and Confounding by Indication:** Patients prescribed Semaglutide for severe obesity or difficult-to-control diabetes may have elevated baseline prevalences of mood disorders and psychosocial distress compared to the general population. While the SGLT2 inhibitor comparator mitigates metabolic confounding, residual channeling cannot be fully eliminated.

---

## 7. Computational Pipeline and Tooling Specifications

* **Environment:** Python 3.10+ within isolated virtual environment.
* **Core Libraries:**
  * `pandas` (v2.0+) — Relational tabular joining, data cleaning, and aggregation.
  * `numpy` (v1.24+) — Vectorized mathematical computations and matrix transformations.
  * `scipy.stats` (v1.10+) — Chi-square tests of independence, Yates' correction, and Fisher's exact tests.
  * `statsmodels` (v0.14+) — Contingency tables and confidence interval estimation.
* **Precision and Rounding:** All intermediate calculations maintain 64-bit floating-point precision. Final test statistics ($\chi^2$), ratios ($ROR, PRR$), and confidence limits are reported rounded to four decimal places. P-values are reported to four decimal places, with values below $0.0001$ denoted as $p < 0.0001$.

---

## 8. References (APA 7th Edition)

* Agresti, A. (2018). *An introduction to categorical data analysis* (3rd ed.). John Wiley & Sons.
* Bate, A., & Evans, S. J. (2009). Quantitative signal detection using spontaneous ADR reporting. *Investigative Medicine*, 57(2), 488–495. https://doi.org/10.2310/JIM.0b013e31819d45ff
* European Medicines Agency. (2017). *Guideline on good pharmacovigilance practices (GVP): Module IX – Signal management (Rev 1)*. EMA/827256/2016.
* Evans, S. J., Waller, P. C., & Davis, S. (2001). Use of proportional reporting ratios (PRRs) for signal generation from spontaneous adverse drug reaction reports. *Pharmacoepidemiology and Drug Safety*, 10(6), 483–486. https://doi.org/10.1002/pds.677
* Montastruc, J. L., Sommet, A., Bagheri, H., & Lapeyre-Mestre, M. (2011). Benefits and strengths of the disproportionality analysis for identification of adverse drug reactions in a pharmacovigilance database. *British Journal of Clinical Pharmacology*, 72(6), 905–908. https://doi.org/10.1111/j.1365-2125.2011.04037.x
* Rothman, K. J., Lanes, S., & Sacks, S. T. (2004). The reporting odds ratio and its advantages over the proportional reporting ratio. *Pharmacoepidemiology and Drug Safety*, 13(8), 519–523. https://doi.org/10.1002/pds.1001
* van Puijenbroek, E. P., Bate, A., Leufkens, H. G., Lindquist, M., Orre, R., & Egberts, A. C. (2002). A comparison of methods used for disproportionality analysis in spontaneous reporting systems for adverse drug reactions. *Pharmacoepidemiology and Drug Safety*, 11(1), 3–10. https://doi.org/10.1002/pds.668
