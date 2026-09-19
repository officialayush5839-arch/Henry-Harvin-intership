# Week 2: Data Analysis & Statistical Testing

## Overview
This week focuses on obtaining, cleaning, and statistically analyzing FDA FAERS data regarding psychiatric adverse drug reactions (ADRs) associated with Semaglutide compared to SGLT2 inhibitors.

## Objectives
- Retrieve ADR reports from OpenFDA API (or use validated fallback data if API is unavailable)
- Clean and preprocess the dataset
- Compute descriptive statistics for the cohorts
- Conduct disproportionality analysis (ROR, PRR, Chi-square)
- Visualize results with publication-quality charts

## Data Sources
- **FDA FAERS via OpenFDA API:** Event counts for Semaglutide and SGLT2i.
- **Reference Literature:** Published studies are used to approximate reporting patterns if the API fails.

## Outputs
- `data/raw/`: Raw JSON/CSV data from API/Fallback
- `data/processed/`: Cleaned dataset ready for analysis
- `data/metadata/`: Documentation of variables and data sources
- `results/tables/`: Descriptive statistics tables
- `results/statistical_results/`: Disproportionality analysis results
- `results/figures/`: High-resolution visual charts
