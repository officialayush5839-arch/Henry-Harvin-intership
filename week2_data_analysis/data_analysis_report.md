# Disproportionality Analysis of Psychiatric Adverse Events with Semaglutide in FDA FAERS
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
1. **Suicidal Ideation**: $	ext{ROR} = 2.61$ (95% CI: 2.18–3.12, $	ext{PRR} = 2.60$, $\chi^2 = 116.35$, $p = 3.98 	imes 10^{-27}$, **Signal = YES**)
2. **Panic Attack**: $	ext{ROR} = 4.40$ (95% CI: 2.96–6.54, $	ext{PRR} = 4.39$, $\chi^2 = 62.94$, $p = 2.13 	imes 10^{-15}$, **Signal = YES**)
3. **Depressed Mood**: $	ext{ROR} = 2.11$ (95% CI: 1.72–2.58, $	ext{PRR} = 2.10$, $\chi^2 = 54.23$, $p = 1.78 	imes 10^{-13}$, **Signal = YES**)

Conversely, **Suicide Attempt** ($	ext{ROR} = 0.67$) and **Insomnia** ($	ext{ROR} = 0.96$) exhibited no disproportional signal, while general **Depression** ($	ext{ROR} = 1.64$) and **Anxiety** ($	ext{ROR} = 1.40$) did not cross the strict $	ext{PRR} \ge 2.0$ threshold.

---

## 2. Statistical Findings & 2x2 Contingency Metrics

| MedDRA Preferred Term | Semaglutide Cases ($a$) | SGLT2i Cases ($c$) | ROR (95% CI) | PRR | $\chi^2$ (Yates) | $p$-value | Signal Detected? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Suicidal Ideation** | 776 | 140 | **2.61 (2.18–3.12)** | **2.60** | **116.35** | $3.98 	imes 10^{-27}$ | **YES (SIGNAL)** |
| **Panic Attack** | 253 | 27 | **4.40 (2.96–6.54)** | **4.39** | **62.94** | $2.13 	imes 10^{-15}$ | **YES (SIGNAL)** |
| **Depressed Mood** | 520 | 116 | **2.11 (1.72–2.58)** | **2.10** | **54.23** | $1.78 	imes 10^{-13}$ | **YES (SIGNAL)** |
| **Depression** | 1,730 | 496 | 1.64 (1.49–1.82) | 1.63 | 95.75 | $1.30 	imes 10^{-22}$ | NO ($	ext{PRR} < 2.0$) |
| **Anxiety** | 1,878 | 630 | 1.40 (1.28–1.54) | 1.40 | 53.64 | $2.40 	imes 10^{-13}$ | NO ($	ext{PRR} < 2.0$) |
| **Insomnia** | 1,377 | 672 | 0.96 (0.87–1.05) | 0.96 | 0.73 | $3.93 	imes 10^{-1}$ | NO |
| **Suicide Attempt** | 106 | 74 | 0.67 (0.50–0.90) | 0.67 | 6.62 | $1.01 	imes 10^{-2}$ | NO |

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

The detection of disproportionate reporting for suicidal ideation ($	ext{ROR} = 2.61$) and depressed mood ($	ext{ROR} = 2.11$) in FAERS represents a valid safety signal requiring regulatory attention. However, disproportionality in spontaneous databases is a measure of relative reporting frequency, NOT biological incidence or causation. Intense media publicity surrounding Ozempic and Wegovy, notoriety bias, stimulated reporting, and baseline depression comorbidity in obesity are primary confounding factors.
