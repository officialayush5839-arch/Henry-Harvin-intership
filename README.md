# Post-Marketing Pharmacovigilance and Safety Profiling of Semaglutide

[![AntiGravity Enterprise Framework](https://img.shields.io/badge/Framework-AntiGravity%20v2.0-blue.svg)](https://github.com/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![QA Acceptance: 100%](https://img.shields.io/badge/QA%20Status-All%20Gates%20Passed-brightgreen.svg)](FINAL_STATUS.md)
[![Citation Style: APA 7th](https://img.shields.io/badge/Citation-APA%207th-orange.svg)](references/citation_style.md)

> **Pharmaceutical Research Assistant Internship — 4-Week Research Portfolio**  
> **Author**: Aryan Ayush  
> **Institution**: Pharmaceutical Research Assistant Internship  
> **Framework**: AntiGravity Enterprise Framework v2.0  
> **Completion Date**: September 2026  

---

## Executive Overview

This repository houses a comprehensive, fully reproducible pharmaceutical research portfolio examining the post-marketing neuropsychiatric safety profile of **Semaglutide** (Ozempic, Wegovy, Rybelsus). Spanning four structured internship weeks, the project traces the complete lifecycle of an evidence-based drug safety investigation:

1. **Week 1 — Literature Review & Synthesis**: Systematic evidence base of 17 peer-reviewed PubMed articles diagnosing the paradox between spontaneous reporting signals and real-world EHR cohorts.
2. **Week 2 — Data Analysis & Disproportionality Testing**: Computational data mining of 100,912 Semaglutide reports vs. 47,266 active SGLT2i comparator reports in FDA FAERS (2018–2025), identifying robust safety signals for Suicidal Ideation ($\text{ROR} = 2.61$) and Depressed Mood ($\text{ROR} = 2.11$) while proving the influence of notoriety bias.
3. **Week 3 — Experimental Design Simulation**: A 12-month prospective active-surveillance cohort protocol ($N = 2,000$) with active comparator SGLT2 inhibitors and validated psychometrics (PHQ-9, C-SSRS) engineered to overcome spontaneous reporting limitations.
4. **Week 4 — Critical Methodological Appraisal**: CONSORT-guided appraisal of the pivotal STEP 1 trial (Wilding et al., 2021, *NEJM*), identifying systematic exclusion of psychiatric comorbidity and passive safety capture as the root causes of pre-approval safety blindspots.
5. **Master Integration & QA**: A unified final portfolio Word report, clean modular submission packages with 200+ word descriptions, and 27 verified stage checkpoints.

---

## Key Scientific Findings & Empirical Metrics

### FAERS Disproportionality Results (Semaglutide vs. SGLT2 Inhibitors)

| MedDRA Preferred Term | Semaglutide Cases ($a$) | SGLT2i Cases ($c$) | Reporting Odds Ratio (95% CI) | Proportional Reporting Ratio (PRR) | $\chi^2$ Statistic (Yates) | $p$-value | Regulatory Signal Detected? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Suicidal Ideation** | 776 | 140 | **2.61 (2.18–3.12)** | **2.60** | **116.35** | $3.98 \times 10^{-27}$ | **YES (CONFIRMED SIGNAL)** |
| **Panic Attack** | 253 | 27 | **4.40 (2.96–6.54)** | **4.39** | **62.94** | $2.13 \times 10^{-15}$ | **YES (CONFIRMED SIGNAL)** |
| **Depressed Mood** | 520 | 116 | **2.11 (1.72–2.58)** | **2.10** | **54.23** | $1.78 \times 10^{-13}$ | **YES (CONFIRMED SIGNAL)** |
| **Depression** | 1,730 | 496 | 1.64 (1.49–1.82) | 1.63 | 95.75 | $1.30 \times 10^{-22}$ | NO ($\text{PRR} < 2.0$) |
| **Anxiety** | 1,878 | 630 | 1.40 (1.28–1.54) | 1.40 | 53.64 | $2.40 \times 10^{-13}$ | NO ($\text{PRR} < 2.0$) |
| **Insomnia** | 1,377 | 672 | 0.96 (0.87–1.05) | 0.96 | 0.73 | $3.93 \times 10^{-1}$ | NO (Null association) |
| **Suicide Attempt** | 106 | 74 | 0.67 (0.50–0.90) | 0.67 | 6.62 | $1.01 \times 10^{-2}$ | NO (Inverse trend) |

*Signal Thresholds: Lower bound of 95% CI of $\text{ROR} > 1.0$, $\text{PRR} \ge 2.0$, $\chi^2_{\text{Yates}} \ge 4.0$, case count $a \ge 3$.*

---

## Primary Deliverables Summary

### 1. Formal Microsoft Word Reports (`reports/` and `submission/`)
- **Week 1 Report**: `reports/week1/week1_literature_review.docx` (45.5 KB, 91 paras, 2 tables)
- **Week 2 Report**: `reports/week2/week2_data_analysis.docx` (1,100.5 KB, 104 paras, 8 embedded 300 DPI figures)
- **Week 3 Report**: `reports/week3/week3_experimental_design.docx` (433.1 KB, 82 paras, embedded study flowchart)
- **Week 4 Report**: `reports/week4/week4_critical_evaluation.docx` (42.9 KB, 58 paras, 13-component matrix)
- **Final Master Portfolio Report**: `reports/final/final_integrated_research_portfolio.docx` (980.5 KB, 112 paras, 3 tables, 5 embedded figures)

### 2. Tabular Datasets & Methodology Matrices
- `week1_literature_review/literature_matrix.xlsx` & `.csv` (17 verified PubMed studies)
- `week2_data_analysis/dataset/pharmaceutical_dataset.xlsx` & `.csv` (Multi-sheet FAERS extract & stats)
- `week4_critical_evaluation/methodology_matrix.xlsx` & `.csv` (13-component CONSORT appraisal)

### 3. Executable Code & Notebooks
- `week2_data_analysis/scripts/` (`data_collection.py`, `data_cleaning.py`, `descriptive_statistics.py`, `statistical_tests.py`, `visualization.py`)
- `week2_data_analysis/notebooks/pharmaceutical_data_analysis.ipynb` (Interactive analysis notebook)
- `src/qa_runner.py` (Automated 6-gate QA test runner)

### 4. High-Resolution Visual Assets (300 DPI)
- `week2_data_analysis/results/figures/fig1_total_reports.png`
- `week2_data_analysis/results/figures/fig2_sema_psych_dist.png`
- `week2_data_analysis/results/figures/fig3_forest_plot.png`
- `week2_data_analysis/results/figures/fig4_grouped_comparison.png`
- `week2_data_analysis/results/figures/fig5_pie_chart.png`
- `week2_data_analysis/results/figures/fig6_temporal_trend.png`
- `week2_data_analysis/results/figures/fig7_signal_heatmap.png`
- `week2_data_analysis/results/figures/fig8_outcome_severity.png`
- `assets/figures/week3_study_flowchart.png` (Experimental clinical workflow)

### 5. Quality Assurance & Audit Records (`qa/`)
- `qa/citation_validation.md` (Stage 19: 100% reference verifiability, 0 hallucinations)
- `qa/statistical_validation.md` (Stage 20: 100% mathematical precision verified)
- `qa/document_validation.md` (Stage 21: Typography, tables, 0 placeholder tokens)
- `qa/research_quality_checklist.md` (Stage 22: COPE ethics & simulation transparency)
- `qa/final_audit.md` (Stage 26: Complete stage-by-stage audit signoff)
- `qa/checkpoints/stage_00_checkpoint.md` through `stage_26_checkpoint.md` (All 27 checkpoints)

---

## Repository Architecture

```text
pharmaceutical_research_portfolio/
├── config/                                 # Project, research, and analysis configurations
│   ├── analysis_config.yaml
│   ├── project_config.yaml
│   └── research_config.yaml
├── docs/                                   # Architectural and methodology documentation
│   ├── integration_map.md                  # Master cross-week scientific lineage map
│   ├── framework_inventory.md
│   ├── project_initialization.md
│   ├── methodology/                        # Protocol and analysis plans
│   └── research/                           # Research questions, hypotheses, problem statement
├── week1_literature_review/                # Week 1: Systematic literature review
│   ├── literature_matrix.csv / .xlsx
│   ├── search_strategy.md
│   ├── inclusion_exclusion_criteria.md
│   ├── article_summaries/                  # 17 individual peer-reviewed study summaries
│   └── synthesis/                          # Trends, breakthroughs, challenges, gaps
├── week2_data_analysis/                    # Week 2: Quantitative FAERS pharmacovigilance
│   ├── dataset/                            # pharmaceutical_dataset.csv / .xlsx
│   ├── data/ (raw, processed, metadata)
│   ├── scripts/                            # Reproducible analytical pipeline
│   ├── results/ (figures, tables, stats)
│   └── notebooks/                          # pharmaceutical_data_analysis.ipynb
├── week3_experimental_design/              # Week 3: Simulated prospective active surveillance
│   ├── flowchart.png
│   ├── experimental_protocol.md
│   ├── safety_protocol.md
│   ├── ethical_considerations.md
│   └── troubleshooting.md
├── week4_critical_evaluation/              # Week 4: Methodological critique of STEP 1 trial
│   ├── methodology_matrix.csv / .xlsx
│   ├── selected_article.md
│   ├── strengths.md
│   └── limitations.md
├── reports/                                # Formal Microsoft Word reports (.docx)
│   ├── week1/week1_literature_review.docx
│   ├── week2/week2_data_analysis.docx
│   ├── week3/week3_experimental_design.docx
│   ├── week4/week4_critical_evaluation.docx
│   └── final/final_integrated_research_portfolio.docx
├── submission/                             # Submission-ready modular packages
│   ├── week1/ (docx, matrix, 268-word description)
│   ├── week2/ (docx, dataset, ipynb, 284-word description)
│   ├── week3/ (docx, flowchart, 272-word description)
│   ├── week4/ (docx, matrix, 265-word description)
│   └── final_portfolio/ (docx, 312-word description)
├── references/                             # Master bibliography (BibTeX, CSV, APA guide)
├── qa/                                     # Quality assurance audits and stage checkpoints
│   ├── checkpoints/                        # 27 verified stage checkpoints (00 to 26)
│   ├── citation_validation.md
│   ├── statistical_validation.md
│   ├── document_validation.md
│   ├── research_quality_checklist.md
│   └── final_audit.md
├── src/                                    # Automation scripts and QA test runners
│   ├── qa_runner.py
│   └── reporting/ (docx generators and packagers)
├── ARCHITECTURE.md
├── CHANGELOG.md
├── FINAL_STATUS.md
├── GOALS.md
├── TODO.md
├── requirements.txt
└── environment.yml
```

---

## Reproducibility & Execution Guide

### 1. Environment Setup
```powershell
# Clone or navigate to the repository
cd "c:\Users\ARYAN - AYUSH\OneDrive\Desktop\an intership\pharmaceutical_research_portfolio"

# Install dependencies via pip
pip install -r requirements.txt
```

### 2. Execute Data Pipeline & Statistical Analysis
```powershell
# Step 1: Query OpenFDA API or execute fallback extract
python week2_data_analysis/scripts/data_collection.py

# Step 2: Clean and validate raw data
python week2_data_analysis/scripts/data_cleaning.py

# Step 3: Compute descriptive statistics and event tables
python week2_data_analysis/scripts/descriptive_statistics.py

# Step 4: Execute disproportionality tests (ROR, PRR, Chi-square)
python week2_data_analysis/scripts/statistical_tests.py

# Step 5: Render 8 publication-quality figures at 300 DPI
python week2_data_analysis/scripts/visualization.py
```

### 3. Generate Word Reports & Re-Package Deliverables
```powershell
# Generate all Word deliverables
python src/reporting/generate_week1_report.py
python src/reporting/generate_week2_report.py
python src/reporting/generate_week3_report.py
python src/reporting/generate_week4_report.py
python src/reporting/generate_final_portfolio.py

# Package clean submission directories
python src/reporting/package_submissions.py
```

### 4. Run Automated QA Verification
```powershell
# Run custom 6-gate project QA runner
python src/qa_runner.py

# Run AntiGravity framework validation
& "..\..\ecc antigravity\AntiGravity-Enterprise-Framework\ag.bat" validate
```

---

## Quality Assurance Signoff

Every requirement across all 26 staged execution steps has been evaluated, verified against live file outputs, and signed off with **PASS** status. For full audit details, see [`FINAL_STATUS.md`](FINAL_STATUS.md) and [`qa/final_audit.md`](qa/final_audit.md).

**Project Status**: **COMPLETE AND READY FOR SUBMISSION**
