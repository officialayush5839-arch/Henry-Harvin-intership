# Stage 08 Checkpoint — Week 2 Data Collection and Cleaning

**Stage Identifier**: STAGE 8: DATA COLLECTION AND CLEANING  
**Verification Date**: September 2026  
**Auditor**: Lead Pharmaceutical Research Intern / AntiGravity Enterprise Framework  
**Stage Status**: **COMPLETE**  

---

### Objective
Collect public adverse event data, preserve raw extracts, execute data cleaning, and produce processed datasets.

### Actions Completed
1. Queried OpenFDA API and collected adverse event counts for Semaglutide and SGLT2 inhibitors across 7 MedDRA terms.
2. Preserved raw extract in `data/raw/raw_faers_data.csv`.
3. Cleaned data, removed duplicates, validated data types, and computed non-target event totals.
4. Outputted processed dataset and generated cleaning audit report.
5. Created final dataset files: `pharmaceutical_dataset.csv` and `pharmaceutical_dataset.xlsx`.

### Outputs Verified
- `week2_data_analysis/data/raw/raw_faers_data.csv`
- `week2_data_analysis/data/processed/processed_faers_data.csv`
- `week2_data_analysis/data/processed/cleaning_report.txt`
- `week2_data_analysis/dataset/pharmaceutical_dataset.csv`
- `week2_data_analysis/dataset/pharmaceutical_dataset.xlsx`

### Acceptance Status
- Acceptance criteria met: Raw data preserved, cleaning logged, datasets created in CSV and XLSX. Status: **COMPLETE**.
