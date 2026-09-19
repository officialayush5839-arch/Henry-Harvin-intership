import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 1. Week 1 Literature Review MD
w1_md = """# Post-Marketing Pharmacovigilance and Safety Profiling of Semaglutide
## A Critical Systematic Literature Review, Evidence Synthesis, and Research Proposal Foundation

**Deliverable**: Week 1 Research Portfolio Deliverable  
**Author**: Aryan Ayush  
**Role**: Pharmaceutical Research Assistant  
**Institution / Internship**: Pharmaceutical Research Assistant Internship  
**Date**: September 2026  
**Framework**: AntiGravity Enterprise Framework v2.0  
**Citation Style**: American Psychological Association (APA) 7th Edition  

---

## 1. Executive Summary

Semaglutide, a long-acting glucagon-like peptide-1 receptor agonist (GLP-1 RA), has emerged as a cornerstone therapeutic agent for type 2 diabetes mellitus (T2DM) and chronic weight management. Following widespread global adoption, post-marketing spontaneous reporting systems—most notably the United States Food and Drug Administration Adverse Event Reporting System (FAERS)—have registered disproportionate safety signals pertaining to neuropsychiatric adverse drug reactions (ADRs), including depression, anxiety, panic attacks, and suicidal ideation.

This Week 1 comprehensive review evaluates the current state of scholarly evidence surrounding semaglutide safety. A systematic search across PubMed, Embase, and Crossref yielded 17 peer-reviewed, verified scholarly publications published between 2020 and 2026. Evidence synthesis demonstrates a critical scientific paradox: while spontaneous reporting databases (FAERS, WHO VigiBase) consistently reveal elevated Reporting Odds Ratios (ROR > 2.0) for depressive mood and suicidal ideation, large-scale Electronic Health Record (EHR) cohort analyses (e.g., Wang et al., 2024, *Nature Medicine*) demonstrate neutral to potentially protective associations. This divergence underscores profound methodological limitations inherent in spontaneous pharmacovigilance data, including notoriety bias, stimulated reporting following media publicity, confounding by indication, and the absence of accurate denominator exposure data.

> **Core Finding**: Spontaneous pharmacovigilance systems provide rapid hypothesis-generating safety signals, but active-comparator prospective surveillance is urgently required to delineate drug-induced etiology from underlying psychiatric comorbidities in obesity and type 2 diabetes.

---

## 2. Clinical Background & Pharmacological Context

GLP-1 receptor agonists mimic endogenous glucagon-like peptide-1, enhancing glucose-dependent insulin secretion, suppressing inappropriate glucagon release, delaying gastric emptying, and centrally mediating appetite regulation through hypothalamic GLP-1 receptors. Semaglutide is commercially formulated as once-weekly subcutaneous injections for diabetes (Ozempic, 0.5 mg to 2.0 mg) and obesity (Wegovy, 2.4 mg), as well as a once-daily oral tablet (Rybelsus, 3 mg to 14 mg) co-formulated with sodium N-[8-(2-hydroxybenzoyl) amino] caprylate (SNAC) to facilitate gastric absorption.

Pivotal Phase III clinical trials, including the SUSTAIN and STEP clinical programs (Wilding et al., 2021), established profound clinical efficacy, demonstrating mean body weight reductions of 14.9% alongside substantial glycated hemoglobin (HbA1c) decreases. However, randomized controlled trials (RCTs) typically enroll narrowly selected cohorts, excluding patients with active major psychiatric illness, severe hepatic or renal impairment, and polypharmacy. Consequently, real-world post-marketing exposure among millions of patients across diverse demographic and clinical backgrounds has revealed safety considerations that escaped pre-approval detection.

---

## 3. Systematic Literature Search Methodology

### 3.1 Search Strategy and Database Parameters
To establish a rigorous evidence base, a systematic search was conducted across international scholarly databases including PubMed/MEDLINE, Google Scholar, and Crossref, complemented by regulatory safety communications from the FDA, EMA, and MHRA. The search strategy incorporated controlled vocabulary (Medical Subject Headings [MeSH]) and targeted boolean syntax:

```text
("Semaglutide"[Mesh] OR "GLP-1 Receptor Agonists"[Mesh] OR "Ozempic" OR "Wegovy" OR "Rybelsus") AND
("Adverse Drug Reaction Reporting Systems"[Mesh] OR "Pharmacovigilance"[Mesh] OR "FAERS" OR "Disproportionality Analysis") AND
("Depression"[Mesh] OR "Suicidal Ideation"[Mesh] OR "Psychiatric Disorders" OR "Safety Profile")
```

### 3.2 Inclusion and Exclusion Criteria

| Criterion Category | Inclusion Criteria | Exclusion Criteria |
| :--- | :--- | :--- |
| **Publication Period** | Peer-reviewed studies published between 2020 and 2026 | Pre-2020 publications lacking post-marketing Wegovy exposure |
| **Study Design** | Spontaneous reporting pharmacovigilance (FAERS, VigiBase), RCT safety updates, prospective/retrospective cohorts | Opinion pieces, unstructured editorials, conference abstracts without full methodology |
| **Intervention / Drug** | Semaglutide (subcutaneous or oral), class-wide GLP-1 RAs with explicit semaglutide disaggregation | Studies examining non-incretin antidiabetic drugs without a GLP-1 comparator |
| **Outcome Measures** | Disproportionality metrics (ROR, PRR, IC, EBGM), clinical psychiatric endpoints, severe adverse events | Preclinical animal-only assays lacking translational safety evaluation |

---

## 4. Evidence Matrix: Summary of Verified Scholarly Literature

A total of 17 peer-reviewed studies meeting all quality and inclusion benchmarks were analyzed:
- **Core FAERS Semaglutide Studies**: PMID 38887555, PMID 39502525, PMID 38943656, PMID 39922760, PMID 39221363, PMID 40523410.
- **Methodology & Pivotal Trial**: PMID 38713347 (READUS-PV Guidelines), PMID 33567185 (STEP 1 Trial; Wilding et al., 2021).
- **Psychiatric Signal & Cohort Studies**: PMID 39163046 (WHO VigiBase), PMID 38087976 (FAERS Suicidality), PMID 38182782 (Nature Medicine EHR Cohort).
- **Organ-System Safety Profiling**: PMID 39767190 (GI Safety), PMID 39267168 (Digestive ADRs), PMID 39040467 (Metabolic ADRs), PMID 39578328 (Ophthalmic ADRs), PMID 38925559 (Alopecia Signal), PMID 40787040 (Alopecia Scoping Review).

Full details are documented in `week1_literature_review/literature_matrix.csv` and `literature_matrix.xlsx`.

---

## 5. Critical Thematic Synthesis

### 5.1 Emerging Trends in GLP-1 Receptor Agonist Surveillance
The pharmacological landscape of GLP-1 RA surveillance has transformed. Post-marketing safety evaluation has expanded from traditional gastrointestinal symptoms into multi-organ considerations, including psychiatric reactions, non-arteritic anterior ischemic optic neuropathy (NAION), and dermatological outcomes (alopecia). Furthermore, formulation-dependent differences have emerged, with subcutaneous administration exhibiting higher reporting volume for neuropsychiatric events.

### 5.2 Major Breakthroughs and Discrepant Findings
A primary breakthrough is the empirical detection of disproportionality signals for depression, anxiety, and suicidal ideation in spontaneous databases (FAERS, VigiBase). However, these signals stand in stark contradiction to real-world target-trial emulation studies (Wang et al., 2024, *Nature Medicine*), which observed a 49% to 73% lower risk of suicidal ideation among semaglutide users. This contradiction represents a pivotal methodological controversy in modern pharmacoepidemiology.

### 5.3 Methodological Challenges in Spontaneous Pharmacovigilance
Spontaneous reporting systems suffer from voluntary underreporting (capturing approximately 1%–10% of true events), notoriety bias, stimulated reporting following high-profile media coverage, and the absence of true denominator exposure data. In addition, confounding by indication poses an unavoidable challenge due to the high baseline prevalence of depression in obesity.

### 5.4 Identified Research Gaps
1. **Lack of Active Comparator Standardization**: Prior FAERS studies frequently compared semaglutide against the entire database rather than active antidiabetic comparators (e.g., SGLT2 inhibitors).
2. **Dose-Dependent Nuances**: Insufficient disaggregation between low-dose diabetic regimens (0.5–1.0 mg) and high-dose obesity regimens (2.4 mg).
3. **Temporal Dynamics**: Limited evaluation of how reporting odds ratios evolved longitudinally relative to media publicity.
4. **Lack of Prospective Validation**: Absence of prospective active-surveillance cohort studies with standardized psychometric rating scales.

---

## 6. Research Proposal Foundation

### 6.1 Research Problem Statement
Pre-approval clinical trials excluded psychiatric illness, while spontaneous reporting is confounded by notoriety bias. Clinicians lack definitive evidence regarding whether semaglutide confers a genuine drug-specific psychiatric risk relative to alternative contemporary antidiabetic therapies.

### 6.2 PICO Framework & Research Questions
- **Population (P)**: Adult patients (>= 18 years) with post-marketing adverse event reports in FDA FAERS (2018–2025).
- **Intervention (I)**: Semaglutide (Ozempic, Wegovy, Rybelsus) as primary suspect medication.
- **Comparator (C)**: Active comparator SGLT2 inhibitors (Empagliflozin, Dapagliflozin, Canagliflozin).
- **Outcome (O)**: Disproportionately higher reporting of MedDRA-coded psychiatric adverse events.

**Primary Research Question**: Is semaglutide exposure associated with a statistically significant disproportionate reporting rate of psychiatric adverse events compared to active comparator SGLT2 inhibitors in FDA FAERS (2018–2025)?

### 6.3 Formal Hypotheses
- **Null Hypothesis ($H_0$)**: $\text{ROR} \le 1.0$ (no disproportionate safety signal).
- **Alternative Hypothesis ($H_1$)**: $\text{ROR} > 1.0$, with lower 95% CI $> 1.0$, $\text{PRR} \ge 2.0$, and $\chi^2_{\text{Yates}} \ge 4.0$ (statistically robust signal).

---

## 7. References (APA 7th Edition)

1. Khouri, C., et al. (2024). The REporting of A Disproportionality Analysis for DrUg Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV). *Drug Safety*, 47(6), 541–558.
2. McIntyre, R. S., et al. (2024). The association between glucagon-like peptide-1 receptor agonists and suicidality: reports to FAERS. *Expert Opinion on Drug Safety*, 23(3), 311–317.
3. Schoretsanitis, G., et al. (2024). Disproportionality Analysis From World Health Organization Data on Semaglutide, Liraglutide, and Suicidality. *JAMA Network Open*, 7(8), e2423385.
4. Wang, W., Volkow, N. D., et al. (2024). Association of semaglutide with risk of suicidal ideation in a real-world cohort. *Nature Medicine*, 30(1), 168–176.
5. Wilding, J. P. H., et al. (2021). Once-Weekly Semaglutide in Adults with Overweight or Obesity (STEP 1 Trial). *New England Journal of Medicine*, 384(11), 989–1002.
"""

with open(os.path.join(BASE_DIR, "week1_literature_review", "literature_review.md"), "w", encoding="utf-8") as f:
    f.write(w1_md)

# 2. Week 2 Data Analysis MD
w2_md = """# Disproportionality Analysis of Psychiatric Adverse Events with Semaglutide in FDA FAERS
## A Comparative Pharmacovigilance Study Against SGLT2 Inhibitors (2018–2025)

**Deliverable**: Week 2 Research Portfolio Deliverable  
**Author**: Aryan Ayush  
**Role**: Pharmaceutical Research Assistant  
**Institution / Internship**: Pharmaceutical Research Assistant Internship  
**Date**: September 2026  
**Framework**: AntiGravity Enterprise Framework v2.0  

---

## 1. Executive Summary

This Week 2 quantitative report investigates post-marketing spontaneous adverse event reports for semaglutide (Ozempic, Wegovy, Rybelsus) compared to an active comparator class of SGLT2 inhibitors (Empagliflozin, Dapagliflozin, Canagliflozin) in FDA FAERS (2018–2025). Analyzing 100,912 semaglutide reports and 47,266 SGLT2 inhibitor reports across seven MedDRA psychiatric terms, statistically significant safety signals were confirmed for:
1. **Suicidal Ideation**: $\text{ROR} = 2.61$ (95% CI: 2.18–3.12, $\text{PRR} = 2.60$, $\chi^2 = 116.35$, $p = 3.98 \times 10^{-27}$, **Signal = YES**)
2. **Panic Attack**: $\text{ROR} = 4.40$ (95% CI: 2.96–6.54, $\text{PRR} = 4.39$, $\chi^2 = 62.94$, $p = 2.13 \times 10^{-15}$, **Signal = YES**)
3. **Depressed Mood**: $\text{ROR} = 2.11$ (95% CI: 1.72–2.58, $\text{PRR} = 2.10$, $\chi^2 = 54.23$, $p = 1.78 \times 10^{-13}$, **Signal = YES**)

Conversely, **Suicide Attempt** ($\text{ROR} = 0.67$) and **Insomnia** ($\text{ROR} = 0.96$) exhibited no disproportional signal, while general **Depression** ($\text{ROR} = 1.64$) and **Anxiety** ($\text{ROR} = 1.40$) did not cross the strict $\text{PRR} \ge 2.0$ threshold.

---

## 2. Statistical Findings & 2x2 Contingency Metrics

| MedDRA Preferred Term | Semaglutide Cases ($a$) | SGLT2i Cases ($c$) | ROR (95% CI) | PRR | $\chi^2$ (Yates) | $p$-value | Signal Detected? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Suicidal Ideation** | 776 | 140 | **2.61 (2.18–3.12)** | **2.60** | **116.35** | $3.98 \times 10^{-27}$ | **YES (SIGNAL)** |
| **Panic Attack** | 253 | 27 | **4.40 (2.96–6.54)** | **4.39** | **62.94** | $2.13 \times 10^{-15}$ | **YES (SIGNAL)** |
| **Depressed Mood** | 520 | 116 | **2.11 (1.72–2.58)** | **2.10** | **54.23** | $1.78 \times 10^{-13}$ | **YES (SIGNAL)** |
| **Depression** | 1,730 | 496 | 1.64 (1.49–1.82) | 1.63 | 95.75 | $1.30 \times 10^{-22}$ | NO ($\text{PRR} < 2.0$) |
| **Anxiety** | 1,878 | 630 | 1.40 (1.28–1.54) | 1.40 | 53.64 | $2.40 \times 10^{-13}$ | NO ($\text{PRR} < 2.0$) |
| **Insomnia** | 1,377 | 672 | 0.96 (0.87–1.05) | 0.96 | 0.73 | $3.93 \times 10^{-1}$ | NO |
| **Suicide Attempt** | 106 | 74 | 0.67 (0.50–0.90) | 0.67 | 6.62 | $1.01 \times 10^{-2}$ | NO |

---

## 3. High-Resolution Visualizations

The following 8 publication-quality figures were programmatically generated and embedded in the Word report (`week2_data_analysis.docx`):
- `fig1_total_reports.png`: Total adverse event report counts by drug class.
- `fig2_sema_psych_dist.png`: Breakdown of psychiatric ADR cases for Semaglutide.
- `fig3_forest_plot.png`: Reporting Odds Ratio Forest Plot with 95% Confidence Intervals.
- `fig4_grouped_comparison.png`: Reporting rates standardized per 10,000 reports.
- `fig5_pie_chart.png`: Proportion of psychiatric vs non-psychiatric ADRs.
- `fig6_temporal_trend.png`: Annual longitudinal reporting trajectories (2018–2025).
- `fig7_signal_heatmap.png`: Signal intensity heatmap across MedDRA categories.
- `fig8_outcome_severity.png`: Distribution of serious clinical outcomes (hospitalization, life-threatening).

---

## 4. Methodological Discussion

The detection of disproportionate reporting for suicidal ideation ($\text{ROR} = 2.61$) and depressed mood ($\text{ROR} = 2.11$) in FAERS represents a valid safety signal requiring regulatory attention. However, disproportionality in spontaneous databases is a measure of relative reporting frequency, NOT biological incidence or causation. Intense media publicity surrounding Ozempic and Wegovy, notoriety bias, stimulated reporting, and baseline depression comorbidity in obesity are primary confounding factors.
"""

with open(os.path.join(BASE_DIR, "week2_data_analysis", "data_analysis_report.md"), "w", encoding="utf-8") as f:
    f.write(w2_md)

# 3. Week 3 Experimental Design MD
w3_md = """# Prospective Active-Surveillance Cohort Study on the Neuropsychiatric Safety of Semaglutide
## A Simulated Experimental Design and Clinical Protocol with Active SGLT2 Inhibitor Comparator

**Deliverable**: Week 3 Research Portfolio Deliverable (Simulated Protocol)  
**Author**: Aryan Ayush  
**Role**: Pharmaceutical Research Assistant  
**Institution / Internship**: Pharmaceutical Research Assistant Internship  
**Date**: September 2026  
**Framework**: AntiGravity Enterprise Framework v2.0  

---

## 1. Executive Summary & Simulation Statement

> **ACADEMIC SIMULATION NOTICE**: This document delineates a simulated experimental design and clinical protocol developed to address the observational limitations of spontaneous pharmacovigilance (Weeks 1 and 2); no human clinical trial has been executed.

To overcome the lack of denominator exposure and voluntary underreporting in FAERS, this Week 3 deliverable develops a 12-month prospective active-surveillance cohort protocol enrolling 2,000 adult participants (1,000 initiating semaglutide SC 0.25–2.4 mg and 1,000 initiating active comparator SGLT2 inhibitors).

---

## 2. Study Design & Variable Taxonomy

- **Design**: Multi-center, prospective active-surveillance cohort study with active comparator control and blinded endpoint adjudication.
- **Independent Variable**: Drug exposure (Semaglutide vs. SGLT2 inhibitor Empagliflozin/Dapagliflozin).
- **Primary Dependent Variable**: Time to first incident moderate-to-severe depressive episode ($\text{PHQ-9} \ge 15$) or suicidal ideation/behavior ($\text{C-SSRS} \ge \text{Level 3}$).
- **Secondary Dependent Variables**: Generalized anxiety symptoms (GAD-7), sleep quality (PSQI), and all-cause treatment discontinuation.
- **Sample Size & Power**: $N = 2,000$ (1,000 per arm) provides 80% statistical power at $\alpha = 0.05$ to detect a Hazard Ratio $\ge 1.75$ with an anticipated 15% annual attrition.

---

## 3. Clinical Workflow Diagram

The complete operational study progression—from participant screening, baseline psychometrics, and dose escalation through longitudinal surveillance (M3, M6, M9, M12), crisis escalation, and survival modeling—is illustrated in `assets/figures/week3_study_flowchart.png`.

---

## 4. Safety Governance & DSMB Stopping Rules

- **Automated Electronic Crisis Alerts**: Endorsement of PHQ-9 Item 9 $\ge 2$ or C-SSRS $\ge \text{Level 3}$ triggers an immediate electronic notification to on-call trial psychiatrists and mandates clinical assessment within 2 hours.
- **Independent DSMB**: Conducts quarterly interim reviews with pre-specified stopping boundaries (interim $\text{HR} > 2.5, p < 0.001$).
"""

with open(os.path.join(BASE_DIR, "week3_experimental_design", "experimental_design_report.md"), "w", encoding="utf-8") as f:
    f.write(w3_md)

# 4. Week 4 Critical Evaluation MD
w4_md = """# Critical Methodological Evaluation of the Landmark STEP 1 Clinical Trial
## A Rigorous Appraisal of Randomized Trial Architecture, Safety Surveillance Blindspots, and Post-Marketing Divergence

**Deliverable**: Week 4 Research Portfolio Deliverable  
**Author**: Aryan Ayush  
**Role**: Pharmaceutical Research Assistant  
**Institution / Internship**: Pharmaceutical Research Assistant Internship  
**Date**: September 2026  
**Framework**: AntiGravity Enterprise Framework v2.0  

---

## 1. Executive Summary

This deliverable provides an exhaustive methodological appraisal of the landmark STEP 1 trial (Wilding et al., 2021, *New England Journal of Medicine*; PMID 33567185, DOI: 10.1056/NEJMoa2032183), the pivotal Phase 3 trial that demonstrated -14.9% mean weight reduction with semaglutide 2.4 mg versus -2.4% with placebo. Benchmarked against CONSORT 2010 and ICH-E6 GCP guidelines across a 13-component evaluation matrix, the analysis diagnoses why pre-approval trials failed to detect the neuropsychiatric safety signals identified in post-marketing spontaneous databases.

---

## 2. Key Methodological Strengths & Vulnerabilities

### Exemplary Strengths:
1. **Allocation & Blinding**: Central interactive web-response randomization (2:1 allocation) and visually identical pens preserved double-blind masking.
2. **Estimand Rigor**: Dual reporting of trial product estimand (efficacy under adherence) and treatment policy estimand (Intention-to-Treat).
3. **High Retention**: 92.6% of participants completed the 68-week trial duration across 129 multinational sites.

### Critical Safety Blindspots:
1. **Systematic Psychiatric Exclusion**: Participants with a PHQ-9 score $\ge 15$, major depressive disorder within 2 years, or prior suicide attempts were excluded, screening out vulnerable populations susceptible to psychiatric adverse reactions.
2. **Passive Adverse Event Capture**: Safety monitoring relied on spontaneous patient reporting and open-ended interviews rather than validated longitudinal psychometric scales (PHQ-9, C-SSRS).
3. **Placebo vs. Active Comparator**: Inert placebo control maximized efficacy effect size but precluded comparative safety evaluation against alternative metabolic therapies.

---

## 3. Cross-Week Synthesis

The four weeks form an integrated evidentiary chain: pre-approval trials (STEP 1) prioritize internal efficacy by excluding psychiatric comorbidity; post-marketing spontaneous reporting (FAERS) detects real-world safety signals; and prospective active surveillance with active comparators provides the definitive framework for causality assessment.
"""

with open(os.path.join(BASE_DIR, "week4_critical_evaluation", "critical_evaluation_report.md"), "w", encoding="utf-8") as f:
    f.write(w4_md)

# 5. Final Master Portfolio MD
wfinal_md = """# Comprehensive Post-Marketing Pharmacovigilance, Experimental Simulation, and Methodological Appraisal of Semaglutide
## An Integrated 4-Week Pharmaceutical Research Portfolio Investigating Neuropsychiatric Adverse Reactions

**Deliverable**: Final Master Research Portfolio Deliverable  
**Author**: Aryan Ayush  
**Role**: Pharmaceutical Research Assistant  
**Institution / Internship**: Pharmaceutical Research Assistant Internship  
**Date**: September 2026  
**Framework**: AntiGravity Enterprise Framework v2.0  

---

## Executive Summary & Abstract

This master portfolio synthesizes an intensive 4-week pharmaceutical research inquiry examining the neuropsychiatric safety profile of Semaglutide (Ozempic, Wegovy, Rybelsus):
1. **Week 1**: Systematic evidence review of 17 peer-reviewed PubMed articles diagnosing the paradox between spontaneous signals and EHR cohorts.
2. **Week 2**: Quantitative FAERS data mining (100,912 Semaglutide vs 47,266 SGLT2i reports), detecting significant disproportionality for Suicidal Ideation ($\text{ROR} = 2.61$) and Depressed Mood ($\text{ROR} = 2.11$) while accounting for notoriety bias.
3. **Week 3**: Prospective active-surveillance cohort simulation ($N = 2,000$) with active SGLT2i controls and validated psychometric scales (PHQ-9, C-SSRS).
4. **Week 4**: Methodological critique of the STEP 1 trial (Wilding et al., 2021, *NEJM*), identifying psychiatric exclusion and passive safety capture as the root causes of pre-approval safety blindspots.

All formal deliverables are available in Microsoft Word format (`.docx`) in `reports/` and `submission/`.
"""

with open(os.path.join(BASE_DIR, "reports", "final", "final_integrated_research_portfolio.md"), "w", encoding="utf-8") as f:
    f.write(wfinal_md)

print("Generated markdown versions of all 4 weekly reports and final portfolio successfully.")
