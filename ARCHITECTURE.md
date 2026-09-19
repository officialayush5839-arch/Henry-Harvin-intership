# Project Architecture

## Overview

This project is a 4-week pharmaceutical research portfolio studying the post-marketing pharmacovigilance of Semaglutide (GLP-1 receptor agonist) using the FDA FAERS database. It follows an integrated research design where each week builds upon the findings and decisions of the preceding week.

## Research Flow Architecture

```
WEEK 1: Literature Review
│   ├── Systematic search of PubMed, Google Scholar
│   ├── 10-20 verified scholarly articles
│   ├── Literature matrix and synthesis
│   └── Research gap identification
│       └── GAP: Psychiatric ADR signals under-characterized
│           ├── Research Question formulated
│           └── Hypothesis (H₀/H₁) defined
│
├───────────────────────────────────────────┐
│                                           ▼
WEEK 2: Data Analysis (FDA FAERS)
│   ├── Public dataset: FDA FAERS (2018–2025)
│   ├── Drug filter: Semaglutide vs SGLT2 inhibitors
│   ├── ADR filter: Psychiatric MedDRA terms
│   ├── Disproportionality analysis
│   │   ├── Reporting Odds Ratio (ROR)
│   │   ├── Proportional Reporting Ratio (PRR)
│   │   └── Chi-square test
│   ├── Descriptive statistics
│   └── Scientific visualizations
│       └── FINDING: Signal strength quantified
│
├───────────────────────────────────────────┐
│                                           ▼
WEEK 3: Experimental Design Simulation
│   ├── Design: Prospective active surveillance cohort
│   ├── IV: Drug exposure (Semaglutide vs SGLT2i)
│   ├── DV: Psychiatric ADR incidence
│   ├── N = 2,000 (proposed)
│   ├── Protocol, safety, ethics
│   └── Would test the signal found in Week 2
│
├───────────────────────────────────────────┐
│                                           ▼
WEEK 4: Critical Evaluation
    ├── Paper: STEP 1 Trial (Wilding et al., NEJM 2021)
    ├── Methodology critique (13+ components)
    ├── RCT vs real-world evidence comparison
    └── Why rare ADRs may be missed in controlled trials
```

## Directory Architecture

```
pharmaceutical_research_portfolio/
├── README.md                          # Project overview and reproducibility
├── GOALS.md                           # Research goals and success criteria
├── ARCHITECTURE.md                    # This file
├── TODO.md                            # Task tracking
├── CHANGELOG.md                       # Version history
├── requirements.txt                   # Python dependencies
├── environment.yml                    # Conda environment
│
├── config/                            # Configuration files
│   ├── project_config.yaml            # Project metadata
│   ├── research_config.yaml           # Research parameters
│   └── analysis_config.yaml           # Statistical settings
│
├── docs/                              # Research documentation
│   ├── research/                      # Topic, RQ, hypothesis, gaps
│   ├── methodology/                   # Data collection, stats, design plans
│   └── submission/                    # Per-week submission checklists
│
├── week1_literature_review/           # Week 1 deliverables
│   ├── article_summaries/             # Individual article analyses
│   ├── synthesis/                     # Cross-cutting synthesis
│   ├── references/                    # BibTeX and CSV references
│   └── report/                        # Word document
│
├── week2_data_analysis/               # Week 2 deliverables
│   ├── data/{raw,processed,metadata}/ # Data pipeline
│   ├── scripts/                       # Python analysis scripts
│   ├── notebooks/                     # Jupyter analysis
│   ├── results/{tables,figures,statistical_results}/
│   ├── dataset/                       # Final datasets (CSV/XLSX)
│   └── report/                        # Word document
│
├── week3_experimental_design/         # Week 3 deliverables
│   ├── flowcharts/                    # Experimental workflow diagrams
│   ├── figures/                       # Design figures
│   └── report/                        # Word document
│
├── week4_critical_evaluation/         # Week 4 deliverables
│   ├── figures/                       # Evaluation figures
│   └── report/                        # Word document
│
├── references/                        # Master reference database
├── analysis/                          # Shared analysis utilities
├── assets/                            # Shared figures, diagrams, tables
├── reports/                           # Organized report copies
├── submission/                        # Submission-ready packages
├── qa/                                # Quality assurance
│   └── checkpoints/                   # Stage checkpoints
└── src/                               # Source code modules
```

## Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Language | Python 3.10+ | Analysis and automation |
| Data | pandas, numpy | Data manipulation |
| Statistics | scipy, statsmodels | Statistical testing |
| Visualization | matplotlib, seaborn | Scientific figures |
| Documents | python-docx, openpyxl | Word/Excel generation |
| Data Source | OpenFDA API / FAERS CSVs | Public drug safety data |
| Notebooks | Jupyter | Interactive analysis |
| Framework | AntiGravity Enterprise | Project scaffolding and QA |

## Data Flow

```
FDA FAERS (Public)
    │
    ▼
data_collection.py ──► data/raw/
    │
    ▼
data_cleaning.py ──► data/processed/
    │
    ├──► descriptive_statistics.py ──► results/tables/
    ├──► statistical_tests.py ──► results/statistical_results/
    └──► visualization.py ──► results/figures/
         │
         ▼
    Word Reports (python-docx)
```
