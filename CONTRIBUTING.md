# Contributing to the Pharmaceutical Research Portfolio

Thank you for your interest in contributing to the **Pharmaceutical Research Portfolio** project. This project is dedicated to reproducible, high-integrity post-marketing pharmacovigilance and pharmacoepidemiological research, with a primary focus on evaluating adverse drug reaction (ADR) reporting associated with GLP-1 receptor agonists (specifically Semaglutide) and active comparator classes (SGLT2 inhibitors) using spontaneous reporting datasets such as FDA FAERS.

To preserve scientific rigor, computational reproducibility, and regulatory compliance, all contributors are required to adhere to the guidelines outlined below.

---

## 1. Principles of Scientific Integrity and Ethics

1. **Academic Rigor and Honesty**: All analytical scripts, statistical models, and documented findings must strictly reflect genuine data processing workflows. Falsification, fabrication, or selective reporting of data and statistics is unacceptable.
2. **Citation Standards**: When integrating external scientific literature, background evidence, or comparative data, all references must follow **APA 7th edition** formatting. DOIs, PMIDs, and complete bibliographic metadata must be provided where available. Never invent or hallucinate references.
3. **Data Privacy and De-identification**: FAERS data is public and anonymized; however, contributors must never attempt re-identification of patients, reporters, or healthcare institutions. Ensure that raw personal data, API tokens, credentials, or confidential environment variables are never committed.
4. **Transparency in Simulation vs. Observed Data**: When developing or testing computational pipelines using synthetic or simulated datasets, clearly designate files, variables, and documentation with the explicit `[SIMULATED]` or `[PROPOSED]` label.

---

## 2. Development and Research Environment Setup

### 2.1 Prerequisites
- Python >= 3.10
- Conda or virtualenv package manager
- Git version control

### 2.2 Environment Initialization
You may configure your workspace using either Conda or Pip:

```bash
# Option A: Conda
conda env create -f environment.yml
conda activate pharma_research

# Option B: Virtual Environment with pip
python -m venv .venv
# Activate on Windows:
.venv\Scripts\activate
# Activate on Unix/macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 3. Directory and Module Organization

Contributors must align additions to the established directory structure:

- `config/`: Configuration files in YAML format defining study parameters, statistical thresholds, and project metadata.
- `src/`: Modular, reusable Python source code (data ingestion, data cleaning, statistical signal detection algorithms, visualization utilities).
- `week1_literature_review/`: Systematic literature synthesis, background epidemiology, and reference bibliographies.
- `week2_data_analysis/`: FAERS data processing pipelines, disproportionality calculation scripts (ROR, PRR, Chi-square), and notebooks.
- `week3_experimental_design/`: Pharmacovigilance protocol design, cohort definition, bias mitigation frameworks, and sensitivity testing.
- `week4_critical_evaluation/`: Methodological validation, signal triage, regulatory implications, and final synthesis reports.
- `reports/`: Generated academic reports, formal summaries, and presentation assets.
- `tests/`: Unit and integration test suites validating analytical pipelines.

---

## 4. Code and Analysis Standards

### 4.1 Statistical Computing Standards
- **Standardized Calculations**: All disproportionality metrics (Reporting Odds Ratio [ROR], Proportional Reporting Ratio [PRR], Information Component [IC], Chi-square statistics) must implement two-by-two contingency formulations with continuity corrections where cell counts are small (e.g., $a < 5$).
- **Significance Thresholds**: Statistical thresholds must adhere to `config/analysis_config.yaml`:
  - 95% Confidence Interval lower bound $> 1.0$ for ROR.
  - $\text{PRR} \ge 2.0$ with $\chi^2 \ge 4.0$ and minimum case count $n \ge 3$.
- **Seed Control**: All stochastic simulations or bootstrap resamplings must specify an explicit random seed for exact reproducibility.

### 4.2 Python Style Guide
- Follow **PEP 8** conventions for Python code.
- Provide comprehensive docstrings conforming to the Google or NumPy docstring format, specifying input types, output structures, and exceptions.
- Include static type annotations (`typing`) where applicable.

---

## 5. Git Workflow and Pull Request Process

1. **Branching Strategy**:
   - `main`: Production-ready, validated code, analytical pipelines, and published reports.
   - Feature/Analysis Branches: Create dedicated branches using descriptive prefixes:
     - `feature/signal-detection-algorithm`
     - `analysis/psychiatric-adr-cohort`
     - `docs/lit-review-synthesis`

2. **Commit Conventions**:
   Commit messages should follow standard conventional commits:
   - `feat: implement ROR calculation module with 95% CI`
   - `fix: resolve zero-division edge case in PRR contingency table`
   - `docs: add APA 7th literature review on GLP-1 RA psychiatric signals`
   - `test: add unit tests for FAERS data ingestion parser`

3. **Submitting a Pull Request**:
   - Provide a clear PR description highlighting the objective, methodology, and results.
   - Verify that all unit tests pass locally before requesting review.
   - Ensure no large data files (raw FAERS dumps, `.csv.gz`, `.zip`) are committed.
   - Await peer review and address comments promptly.

---

## 6. Questions and Contact

For questions regarding study protocols, methodological design, or technical contributions, please open an issue in the project repository or contact the research team via the project communication channels.
