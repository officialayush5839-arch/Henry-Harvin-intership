# Changelog

All notable changes to the **Pharmaceutical Research Portfolio** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-09-17

### Added
- **Framework Discovery & Project Scaffolding (Stages 0–1)**:
  - Initialized enterprise project structure via AntiGravity CLI (`ag.bat init`).
  - Created 47+ specialized directories spanning `config/`, `docs/`, `week1_literature_review/`, `week2_data_analysis/`, `week3_experimental_design/`, `week4_critical_evaluation/`, `reports/`, `submission/`, `references/`, `qa/`, and `src/`.
  - Added project, research, and analysis YAML configurations.
- **Topic Selection & Research Foundation (Stages 2–3)**:
  - Evaluated 7 candidate pharmaceutical topics against 8 feasibility criteria; selected Semaglutide post-marketing pharmacovigilance.
  - Formulated PICO research questions, formal hypotheses ($H_0/H_1$), and conceptual frameworks.
- **Week 1 Literature Search & Synthesis (Stages 4–6)**:
  - Systematically identified and verified 17 peer-reviewed PubMed articles (PMIDs and DOIs confirmed against NLM).
  - Built `literature_matrix.csv` and `literature_matrix.xlsx`.
  - Synthesized emerging trends, breakthroughs, controversies (FAERS vs Nature Medicine), challenges, and research gaps.
  - Generated formal APA 7th formatted Word report: `reports/week1/week1_literature_review.docx`.
- **Week 2 Data Collection, Cleaning & Statistical Disproportionality (Stages 7–10)**:
  - Automated OpenFDA API data extraction pipeline (`data_collection.py`, `data_cleaning.py`).
  - Extracted 100,912 Semaglutide reports and 47,266 active comparator SGLT2 inhibitor reports.
  - Executed disproportionality tests (ROR, 95% CI, PRR, Yates-corrected Chi-square); detected statistically significant safety signals for Suicidal Ideation ($\text{ROR} = 2.61$), Depressed Mood ($\text{ROR} = 2.11$), and Panic Attack ($\text{ROR} = 4.40$).
  - Rendered 8 publication-quality 300 DPI figures (`fig1`–`fig8`).
  - Built interactive Jupyter Notebook (`pharmaceutical_data_analysis.ipynb`) and research datasets (`pharmaceutical_dataset.csv`, `.xlsx`).
  - Generated formal Word report: `reports/week2/week2_data_analysis.docx`.
- **Week 3 Experimental Design Simulation (Stages 11–14)**:
  - Formulated 12-month prospective active-surveillance cohort protocol ($N = 2,000$) with active SGLT2i comparator.
  - Specified psychometric instruments (PHQ-9, C-SSRS, GAD-7), automated crisis alerts, DSMB stopping rules, and survival SAP.
  - Rendered 300 DPI clinical workflow diagram (`assets/figures/week3_study_flowchart.png`).
  - Generated formal Word report: `reports/week3/week3_experimental_design.docx`.
- **Week 4 Critical Evaluation of STEP 1 Trial (Stages 15–17)**:
  - Appraised landmark trial (Wilding et al., 2021, NEJM) using 13-component CONSORT/ICH-GCP methodology matrix.
  - Diagnosed pre-approval safety blindspots: systematic exclusion of psychiatric comorbidity and passive adverse event capture.
  - Generated `methodology_matrix.csv`, `.xlsx`, and formal Word report: `reports/week4/week4_critical_evaluation.docx`.
- **Cross-Week Integration & Master Audits (Stages 18–22)**:
  - Authored `docs/integration_map.md` linking the 4 weeks into a single continuous scientific inquiry.
  - Verified 100% reference verifiability (0 hallucinations) in `qa/citation_validation.md`.
  - Re-calculated all statistics with 0 discrepancies in `qa/statistical_validation.md`.
  - Verified document formatting and 0 placeholders in `qa/document_validation.md`.
  - Confirmed research integrity and simulation transparency in `qa/research_quality_checklist.md`.
- **Final Portfolio & Submission Packages (Stages 23–26)**:
  - Generated master integrated Word report: `reports/final/final_integrated_research_portfolio.docx`.
  - Assembled clean submission packages in `submission/week1/` through `submission/final_portfolio/` with standalone 200+ word descriptions.
  - Executed framework validation (`ag.bat validate`) and automated project QA runner (`src/qa_runner.py`), passing all acceptance gates.
  - Verified all 27 stage checkpoints (`qa/checkpoints/stage_00_checkpoint.md` to `stage_26_checkpoint.md`).
  - Authored `qa/final_audit.md` and `FINAL_STATUS.md`.
