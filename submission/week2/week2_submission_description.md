# Week 2 Deliverable Description: Spontaneous Data Analysis & Disproportionality Testing

**Internship Role**: Pharmaceutical Research Assistant  
**Topic**: Disproportionality Analysis of Semaglutide Psychiatric ADRs in FDA FAERS  
**Author**: Aryan Ayush  
**Word Count**: 284 words  

### Submission Overview

The Week 2 deliverable presents an end-to-end, reproducible computational pharmacovigilance analysis investigating post-marketing psychiatric adverse event reports in the FDA Adverse Event Reporting System (FAERS) from 2018 through 2025. Extracted via the OpenFDA API (`api.fda.gov/drug/event.json`) and cross-verified against public quarterly extracts, the dataset contrasts 100,912 semaglutide primary suspect reports against 47,266 active comparator SGLT2 inhibitor reports (Empagliflozin, Dapagliflozin, Canagliflozin). Utilizing an active antidiabetic comparator class inherently controls for baseline metabolic comorbidity, overcoming a major source of confounding present in traditional whole-database analyses.

Applying standardized pharmacovigilance signal detection criteria (lower bound of 95% CI of ROR > 1.0, PRR >= 2.0, Yates-corrected Chi-square >= 4.0, N >= 3 cases), our analytical pipeline evaluated seven MedDRA preferred terms under the Psychiatric disorders System Organ Class. Statistically robust safety signals were detected for three categories: Suicidal Ideation (ROR = 2.61, 95% CI: 2.18–3.12, PRR = 2.60, Chi2 = 116.35, p = 3.98e-27), Panic Attack (ROR = 4.40, 95% CI: 2.96–6.54, PRR = 4.39, Chi2 = 62.94), and Depressed Mood (ROR = 2.11, 95% CI: 1.72–2.58, PRR = 2.10, Chi2 = 54.23). In contrast, Suicide Attempt (ROR = 0.67) and Insomnia (ROR = 0.96) showed no disproportionality signal.

The submission package includes the formal Word report (`week2_data_analysis.docx`) embedding eight publication-quality 300 DPI figures, the processed research dataset in Excel and CSV formats (`pharmaceutical_dataset.xlsx`, `.csv`), and an interactive, fully executed Jupyter Notebook (`pharmaceutical_data_analysis.ipynb`) providing complete analytical code reproducibility. The findings demonstrate that while semaglutide exhibits disproportionate spontaneous reporting for affective symptoms, regulatory interpretation must account for intense media-stimulated reporting.
