# Quality Assurance Report: Data & Statistical Validation Audit (Stage 20)

**Project Title**: Post-Marketing Pharmacovigilance and Safety Profiling of Semaglutide  
**Audit Conducted**: September 2026  
**Auditor**: AntiGravity Enterprise Framework Statistical Verification Engine  
**Analytical Standard**: ICH E9 Statistical Principles for Clinical Trials & CIOMS Pharmacovigilance Guidelines  

---

## 1. Audit Scope & Traceability Pipeline

This audit independently verified the end-to-end analytical data pipeline from raw extraction to reported values:
$$\text{OpenFDA API / Aggregate Source} \longrightarrow \text{Raw CSV} \longrightarrow \text{Data Cleaning} \longrightarrow \text{Processed CSV} \longrightarrow \text{Statistical Code} \longrightarrow \text{Output Tables} \longrightarrow \text{300 DPI Figures} \longrightarrow \text{Word Reports}$$

Every cell frequency, point estimate, 95% confidence limit, test statistic, and p-value was re-computed in an isolated Python session and verified against reported values.

---

## 2. Independent Calculation Verification Table

| MedDRA Preferred Term | $a$ (Sema+) | $b$ (Sema-) | $c$ (SGLT2+) | $d$ (SGLT2-) | Reported ROR (95% CI) | Audit ROR (95% CI) | Reported PRR | Audit PRR | $\chi^2$ (Yates) | $p$-value | Discrepancy | Audit Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Depression** | 1,730 | 99,182 | 496 | 46,770 | 1.64 (1.49–1.82) | 1.64 (1.49–1.82) | 1.63 | 1.63 | 95.75 | 1.30e-22 | 0.000 | **PASS** |
| **Depressed Mood** | 520 | 100,392 | 116 | 47,150 | 2.11 (1.72–2.58) | 2.11 (1.72–2.58) | 2.10 | 2.10 | 54.23 | 1.78e-13 | 0.000 | **PASS** |
| **Suicidal Ideation** | 776 | 100,136 | 140 | 47,126 | 2.61 (2.18–3.12) | 2.61 (2.18–3.12) | 2.60 | 2.60 | 116.35 | 3.98e-27 | 0.000 | **PASS** |
| **Suicide Attempt** | 106 | 100,806 | 74 | 47,192 | 0.67 (0.50–0.90) | 0.67 (0.50–0.90) | 0.67 | 0.67 | 6.62 | 1.01e-02 | 0.000 | **PASS** |
| **Anxiety** | 1,878 | 99,034 | 630 | 46,636 | 1.40 (1.28–1.54) | 1.40 (1.28–1.54) | 1.40 | 1.40 | 53.64 | 2.40e-13 | 0.000 | **PASS** |
| **Insomnia** | 1,377 | 99,535 | 672 | 46,594 | 0.96 (0.87–1.05) | 0.96 (0.87–1.05) | 0.96 | 0.96 | 0.73 | 3.93e-01 | 0.000 | **PASS** |
| **Panic Attack** | 253 | 100,659 | 27 | 47,239 | 4.40 (2.96–6.54) | 4.40 (2.96–6.54) | 4.39 | 4.39 | 62.94 | 2.13e-15 | 0.000 | **PASS** |

---

## 3. Signal Classification Verification

Signal detection criteria:
1. Lower bound of 95% Confidence Interval for $\text{ROR} > 1.0$
2. $\text{PRR} \ge 2.0$
3. $\chi^2_{\text{Yates}} \ge 4.0$
4. Case count $a \ge 3$

| ADR Term | Lower CI $> 1.0$? | PRR $\ge 2.0$? | $\chi^2 \ge 4.0$? | $a \ge 3$? | Overall Signal Detected |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Suicidal Ideation** | YES (2.18) | YES (2.60) | YES (116.35) | YES (776) | **CONFIRMED SIGNAL** |
| **Panic Attack** | YES (2.96) | YES (4.39) | YES (62.94) | YES (253) | **CONFIRMED SIGNAL** |
| **Depressed Mood** | YES (1.72) | YES (2.10) | YES (54.23) | YES (520) | **CONFIRMED SIGNAL** |
| **Depression** | YES (1.49) | NO (1.63) | YES (95.75) | YES (1,730) | **NO SIGNAL (PRR < 2.0)** |
| **Anxiety** | YES (1.28) | NO (1.40) | YES (53.64) | YES (1,878) | **NO SIGNAL (PRR < 2.0)** |
| **Insomnia** | NO (0.87) | NO (0.96) | NO (0.73) | YES (1,377) | **NO SIGNAL** |
| **Suicide Attempt** | NO (0.50) | NO (0.67) | YES (6.62) | YES (106) | **NO SIGNAL (Inverse Trend)** |

---

## 4. Analytical Code Audit

1. **`week2_data_analysis/scripts/data_collection.py`**: Validated requests handling, OpenFDA API query syntax, fallback exception trapping, raw CSV serialization.
2. **`week2_data_analysis/scripts/data_cleaning.py`**: Validated zero missing records, non-negative integer casting, deduplication check, cleaning report output.
3. **`week2_data_analysis/scripts/descriptive_statistics.py`**: Verified proportionality aggregation, rates per 10,000 calculation, summary table formatting.
4. **`week2_data_analysis/scripts/statistical_tests.py`**: Confirmed math for ROR, PRR, standard error of ln(ROR), Yates continuity correction, and two-sided p-value estimation.
5. **`week2_data_analysis/scripts/visualization.py`**: Verified 8 high-resolution 300 DPI figures with proper titles, axes, legends, source annotations, and clean visual layouts.
6. **`week2_data_analysis/notebooks/pharmaceutical_data_analysis.ipynb`**: Verified complete, executable Jupyter notebook mirroring the script pipeline.

**Stage 20 Final Audit Determination**: **PASS (Zero Discrepancies, 100% Reproducibility)**
