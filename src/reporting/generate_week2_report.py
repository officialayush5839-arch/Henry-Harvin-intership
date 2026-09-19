import os
import shutil
import pandas as pd
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_styles import (
    create_document, add_title_page, add_h1, add_h2, add_h3, 
    add_callout, apply_table_styles, NAVY, SLATE, CHARCOAL
)

def generate_week2_report():
    print("Generating Week 2 Data Analysis Word Report...")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    doc = create_document()

    # Title Page
    add_title_page(
        doc,
        title="Disproportionality Analysis of Psychiatric Adverse Events with Semaglutide in FDA FAERS",
        subtitle="A Comparative Pharmacovigilance Study Against SGLT2 Inhibitors (2018–2025)",
        author="Aryan Ayush",
        affiliation="Pharmaceutical Research Assistant Internship",
        date_str="September 2026",
        week_tag="Week 2 Portfolio Deliverable"
    )

    # Table of Contents Outline
    add_h1(doc, "Table of Contents")
    toc_items = [
        "1. Executive Summary",
        "2. Pharmacovigilance Framework & Research Rationale",
        "3. Data Collection & Preprocessing Methodology",
        "    3.1 Data Source: FDA Adverse Event Reporting System (FAERS)",
        "    3.2 Query Strategy and OpenFDA Extraction",
        "    3.3 Data Cleaning, Quality Assurance, and Data Dictionary",
        "4. Statistical Analysis Methodology",
        "    4.1 Descriptive Analysis and Event Rates",
        "    4.2 Disproportionality Metrics (ROR, PRR, Chi-Square)",
        "    4.3 Signal Detection Threshold Criteria",
        "5. Empirical Results",
        "    5.1 Total Reporting Volume and Baseline Comparisons",
        "    5.2 2x2 Contingency Tables and Metric Computation",
        "    5.3 Identified Pharmacovigilance Signals",
        "6. High-Resolution Visualizations and Figure Interpretations",
        "    6.1 Figure 1: Total Adverse Event Reports by Drug Class",
        "    6.2 Figure 2: Frequency Distribution of Psychiatric ADRs for Semaglutide",
        "    6.3 Figure 3: Reporting Odds Ratio Forest Plot with 95% Confidence Intervals",
        "    6.4 Figure 4: Comparative Reporting Rates per 10,000 Total Reports",
        "    6.5 Figure 5: Proportional Share of Psychiatric System Organ Classes",
        "    6.6 Figure 6: Longitudinal Reporting Trends (2018-2025)",
        "    6.7 Figure 7: Signal Strength Heatmap across MedDRA Terms",
        "    6.8 Figure 8: Serious Outcome Distribution in Psychiatric ADRs",
        "7. Methodological Discussion, Bias Evaluation, and Study Limitations",
        "8. Clinical and Regulatory Recommendations",
        "9. References (APA 7th Edition)"
    ]
    for item in toc_items:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(item)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10.5)
        if not item.startswith("    "):
            r.font.bold = True
            r.font.color.rgb = NAVY
    doc.add_page_break()

    # 1. Executive Summary
    add_h1(doc, "1. Executive Summary")
    doc.add_paragraph(
        "This Week 2 quantitative pharmacovigilance report investigates post-marketing spontaneous adverse event reports for semaglutide "
        "(Ozempic, Wegovy, Rybelsus) compared to an active comparator class of sodium-glucose cotransporter-2 (SGLT2) inhibitors "
        "(Empagliflozin, Dapagliflozin, Canagliflozin) within the FDA Adverse Event Reporting System (FAERS) database spanning 2018 to 2025."
    )
    doc.add_paragraph(
        "Analyzing 100,912 total adverse event reports for semaglutide and 47,266 reports for SGLT2 inhibitors, we conducted disproportionality "
        "analyses across seven MedDRA preferred terms: Depression, Depressed Mood, Suicidal Ideation, Suicide Attempt, Anxiety, Insomnia, and Panic Attack. "
        "Applying internationally harmonized signal detection criteria (lower 95% CI of ROR > 1.0, PRR >= 2.0, Chi-square >= 4.0, N >= 3), "
        "statistically significant disproportionality signals were detected for three neuropsychiatric categories:"
    )
    doc.add_paragraph(
        "1. Suicidal Ideation: ROR = 2.61 (95% CI: 2.18–3.12, PRR = 2.60, Chi-square = 116.35, p = 3.98e-27, Signal = YES)\n"
        "2. Panic Attack: ROR = 4.40 (95% CI: 2.96–6.54, PRR = 4.39, Chi-square = 62.94, p = 2.13e-15, Signal = YES)\n"
        "3. Depressed Mood: ROR = 2.11 (95% CI: 1.72–2.58, PRR = 2.10, Chi-square = 54.23, p = 1.78e-13, Signal = YES)"
    )
    doc.add_paragraph(
        "Conversely, Suicide Attempt (ROR = 0.67, 95% CI: 0.50–0.90) and Insomnia (ROR = 0.96, 95% CI: 0.87–1.05) exhibited no disproportional "
        "signal. General Anxiety (ROR = 1.40) and Depression (ROR = 1.64) demonstrated elevated reporting odds but failed the strict PRR >= 2.0 threshold. "
        "These findings establish genuine safety signals in spontaneous reporting but require careful contextualization regarding stimulated reporting "
        "and notoriety bias."
    )
    add_callout(
        doc,
        "Statistical Conclusion: Semaglutide exhibits statistically robust disproportionality for suicidal ideation, panic attacks, and "
        "depressed mood relative to active SGLT2i comparators in FAERS. While disproportionality does not establish causation, it triggers "
        "mandatory regulatory surveillance and warrants prospective active cohort validation.",
        alert_type="NOTE"
    )

    # 2. Pharmacovigilance Framework & Rationale
    add_h1(doc, "2. Pharmacovigilance Framework & Research Rationale")
    doc.add_paragraph(
        "Spontaneous adverse event reporting systems represent the principal mechanism for detecting post-marketing drug safety issues. "
        "However, analyzing spontaneous data without an active comparator invites severe indication bias. In diabetes and obesity management, "
        "patients frequently present with underlying neuropsychiatric comorbidities. By contrasting semaglutide with SGLT2 inhibitors—medications "
        "prescribed for the same primary indication (type 2 diabetes) and patient demographic—we effectively control for baseline metabolic comorbidity, "
        "enabling more specific assessment of drug-associated disproportionality."
    )

    # 3. Data Collection & Preprocessing
    add_h1(doc, "3. Data Collection & Preprocessing Methodology")
    add_h2(doc, "3.1 Data Source: FDA Adverse Event Reporting System (FAERS)")
    doc.add_paragraph(
        "Data were extracted via the OpenFDA API (https://api.fda.gov/drug/event.json) and cross-referenced against published aggregate "
        "FAERS data files covering January 1, 2018 through mid-2025. FAERS captures spontaneous reports submitted by healthcare professionals, "
        "consumers, and pharmaceutical manufacturers globally."
    )

    add_h2(doc, "3.2 Query Strategy and OpenFDA Extraction")
    doc.add_paragraph(
        "A multi-tiered query pipeline was executed using Python requests scripts (`data_collection.py`):\n"
        "• Target Drug Class: Search strings `patient.drug.medicinalproduct:('semaglutide' OR 'ozempic' OR 'wegovy' OR 'rybelsus')` with "
        "`patient.drug.drugcharacterization:1` (Primary Suspect).\n"
        "• Active Comparator Class: Search strings `patient.drug.medicinalproduct:('empagliflozin' OR 'dapagliflozin' OR 'canagliflozin' OR 'jardiance' OR 'farxiga' OR 'invokana')` with Primary Suspect designation.\n"
        "• Adverse Event Terms: Exact MedDRA preferred terms under System Organ Class (SOC) 'Psychiatric disorders'."
    )

    add_h2(doc, "3.3 Data Cleaning, Quality Assurance, and Data Dictionary")
    doc.add_paragraph(
        "Data cleaning adhered to ICH E2B standards (`data_cleaning.py`). The pipeline verified zero missing values across critical fields, "
        "enforced case deduplication on standardized Case IDs, validated integer counts, and computed non-target event frequencies (non_adr_count) "
        "for contingency table construction. The processed data file (`processed_faers_data.csv`) was locked and validated with automated unit checks."
    )

    # 4. Statistical Analysis Methodology
    add_h1(doc, "4. Statistical Analysis Methodology")
    doc.add_paragraph(
        "Disproportionality analysis tests whether a specific adverse event is reported more frequently in association with a drug of interest "
        "compared to a control group of drugs. For each psychiatric ADR term, a 2x2 contingency table was constructed:"
    )

    # 2x2 Table
    ct_table = doc.add_table(rows=3, cols=3)
    ct_table.rows[0].cells[0].text = "Reporting Stratum"
    ct_table.rows[0].cells[1].text = "Target Psychiatric ADR"
    ct_table.rows[0].cells[2].text = "All Other Reported ADRs"
    ct_table.rows[1].cells[0].text = "Semaglutide (Exposed)"
    ct_table.rows[1].cells[1].text = "a (Target Event with Sema)"
    ct_table.rows[1].cells[2].text = "b (Non-Target Events with Sema)"
    ct_table.rows[2].cells[0].text = "SGLT2 Inhibitors (Control)"
    ct_table.rows[2].cells[1].text = "c (Target Event with SGLT2i)"
    ct_table.rows[2].cells[2].text = "d (Non-Target Events with SGLT2i)"
    apply_table_styles(ct_table, [2.5, 2.0, 2.0])
    doc.add_paragraph()

    add_h2(doc, "4.2 Mathematical Formulas")
    doc.add_paragraph(
        "• Reporting Odds Ratio (ROR):"
    )
    doc.add_paragraph(
        "    ROR = (a / b) / (c / d) = (a * d) / (b * c)"
    )
    doc.add_paragraph(
        "    95% CI for ROR = exp[ ln(ROR) ± 1.96 * sqrt(1/a + 1/b + 1/c + 1/d) ]"
    )
    doc.add_paragraph(
        "• Proportional Reporting Ratio (PRR):"
    )
    doc.add_paragraph(
        "    PRR = [a / (a + b)] / [c / (c + d)]"
    )
    doc.add_paragraph(
        "• Chi-Square Statistic with Yates' Continuity Correction (chi2):"
    )
    doc.add_paragraph(
        "    chi2 = N * (|a*d - b*c| - N/2)^2 / [(a + b) * (c + d) * (a + c) * (b + d)], where N = a + b + c + d"
    )

    add_h2(doc, "4.3 Predefined Signal Detection Criteria")
    doc.add_paragraph(
        "In accordance with European Medicines Agency (EMA) and FDA pharmacovigilance guidelines, a valid safety signal is defined when all "
        "four of the following criteria are simultaneously satisfied:\n"
        "1. Lower bound of 95% Confidence Interval for ROR > 1.0\n"
        "2. Proportional Reporting Ratio (PRR) >= 2.0\n"
        "3. Chi-square statistic (Yates corrected) >= 4.0\n"
        "4. Number of exposed cases a >= 3"
    )

    # 5. Empirical Results
    add_h1(doc, "5. Empirical Results")
    doc.add_paragraph(
        "Across the 2018–2025 period, 100,912 semaglutide reports and 47,266 SGLT2 inhibitor reports were evaluated. Table 2 presents the "
        "complete empirical disproportionality metrics, contingency cell frequencies, test statistics, and signal classifications."
    )

    # Load results CSV
    stat_csv = os.path.join(BASE_DIR, 'week2_data_analysis', 'results', 'statistical_results', 'disproportionality_results.csv')
    df_stat = pd.read_csv(stat_csv)

    table_res = doc.add_table(rows=len(df_stat)+1, cols=8)
    table_res.rows[0].cells[0].text = "ADR Term"
    table_res.rows[0].cells[1].text = "a (Sema)"
    table_res.rows[0].cells[2].text = "c (SGLT2)"
    table_res.rows[0].cells[3].text = "ROR (95% CI)"
    table_res.rows[0].cells[4].text = "PRR"
    table_res.rows[0].cells[5].text = "Chi2"
    table_res.rows[0].cells[6].text = "p-value"
    table_res.rows[0].cells[7].text = "Signal?"

    for idx, row in df_stat.iterrows():
        r_cells = table_res.rows[idx+1].cells
        r_cells[0].text = str(row['ADR_Term'])
        r_cells[1].text = f"{int(row['a (Sema with ADR)']):,}"
        r_cells[2].text = f"{int(row['c (SGLT2i with ADR)']):,}"
        ror_str = f"{row['ROR']:.2f} ({row['ROR_95%_CI_Lower']:.2f}-{row['ROR_95%_CI_Upper']:.2f})"
        r_cells[3].text = ror_str
        r_cells[4].text = f"{row['PRR']:.2f}"
        r_cells[5].text = f"{row['Chi2_Stat']:.1f}"
        p_val = row['P_Value']
        p_str = f"{p_val:.2e}" if p_val < 0.001 else f"{p_val:.3f}"
        r_cells[6].text = p_str
        r_cells[7].text = "YES" if row['Signal_Detected'] else "NO"

    apply_table_styles(table_res, [1.3, 0.7, 0.7, 1.6, 0.6, 0.6, 0.8, 0.7])
    doc.add_paragraph()

    # 6. High-Resolution Visualizations
    add_h1(doc, "6. High-Resolution Visualizations and Figure Interpretations")
    doc.add_paragraph(
        "Eight publication-quality figures were programmatically generated at 300 DPI to communicate the statistical findings."
    )

    fig_dir = os.path.join(BASE_DIR, 'week2_data_analysis', 'results', 'figures')
    figures = [
        ("fig1_total_reports.png", "Figure 1. Total Adverse Event Reports by Drug Class in FAERS",
         "Demonstrates the substantial post-marketing reporting volume for semaglutide (100,912 reports) reflecting exponential market uptake relative to active comparator SGLT2 inhibitors (47,266 reports)."),
        ("fig2_sema_psych_dist.png", "Figure 2. Frequency Distribution of Psychiatric Adverse Events for Semaglutide",
         "Illustrates case volume breakdown across MedDRA preferred terms. Anxiety (1,878 reports) and Depression (1,730 reports) represent the most frequent absolute counts, followed by Insomnia (1,377) and Suicidal Ideation (776)."),
        ("fig3_forest_plot.png", "Figure 3. Reporting Odds Ratio (ROR) Forest Plot with 95% Confidence Intervals",
         "Key inferential figure depicting ROR point estimates and 95% confidence bounds. Panic attacks (ROR 4.40), Suicidal ideation (ROR 2.61), and Depressed mood (ROR 2.11) clearly separate from the null boundary (ROR = 1.0)."),
        ("fig4_grouped_comparison.png", "Figure 4. Comparative Reporting Rates per 10,000 Total Adverse Event Reports",
         "Standardized event rate comparison. Semaglutide exhibits 76.9 suicidal ideation reports per 10,000 reports compared to only 29.6 per 10,000 for SGLT2 inhibitors, representing a 2.6-fold reporting rate disparity."),
        ("fig5_pie_chart.png", "Figure 5. Proportion of Psychiatric vs Non-Psychiatric ADRs for Semaglutide",
         "Shows that psychiatric adverse events account for 6.58% (6,640 reports) of total semaglutide adverse reactions, while non-psychiatric organ systems (gastrointestinal, metabolic) comprise 93.42%."),
        ("fig6_temporal_trend.png", "Figure 6. Longitudinal Reporting Trends of Psychiatric ADRs (2018–2025)",
         "Highlights exponential escalation in semaglutide psychiatric reporting starting in late 2021 following Wegovy FDA approval and viral media coverage, in contrast to linear reporting for SGLT2 inhibitors."),
        ("fig7_signal_heatmap.png", "Figure 7. Signal Strength Heatmap across MedDRA Preferred Terms",
         "Color-coded matrix indexing ROR magnitude. Darker hues represent high signal intensity for Panic Attack (4.40), Suicidal Ideation (2.61), and Depressed Mood (2.11)."),
        ("fig8_outcome_severity.png", "Figure 8. Serious Outcome Distribution in Reported Psychiatric Events",
         "Depicts clinical severity proportions. Among reported psychiatric events, hospitalization occurred in 44.2% of semaglutide cases and 46.8% of SGLT2i cases; life-threatening episodes occurred in 8.5% and 6.2% respectively.")
    ]

    for fname, ftitle, fdesc in figures:
        fpath = os.path.join(fig_dir, fname)
        if os.path.exists(fpath):
            add_h2(doc, ftitle)
            doc.add_picture(fpath, width=Inches(6.0))
            p_cap = doc.add_paragraph()
            p_cap.paragraph_format.space_before = Pt(4)
            p_cap.paragraph_format.space_after = Pt(12)
            r_cap = p_cap.add_run(f"Figure Note: {fdesc}")
            r_cap.font.name = 'Times New Roman'
            r_cap.font.size = Pt(9.5)
            r_cap.font.italic = True
            r_cap.font.color.rgb = CHARCOAL

    # 7. Methodological Discussion
    add_h1(doc, "7. Methodological Discussion, Bias Evaluation, and Study Limitations")
    doc.add_paragraph(
        "The identification of statistically significant disproportionality for suicidal ideation (ROR 2.61), panic attacks (ROR 4.40), "
        "and depressed mood (ROR 2.11) requires rigorous critical appraisal. Disproportionality in spontaneous databases is a measure of "
        "relative reporting frequency, NOT biological incidence or causation."
    )
    doc.add_paragraph(
        "Crucial biases operative in this dataset include:\n"
        "1. Notoriety and Stimulated Reporting: Following international press coverage in mid-2023 regarding European regulatory investigations "
        "into GLP-1 suicidality, spontaneous submissions surged. This stimulated reporting inevitably elevates ROR metrics independently of true risk.\n"
        "2. Confounding by Indication: Semaglutide is prescribed extensively for severe obesity. Major depressive disorder and affective dysregulation "
        "have a markedly higher baseline prevalence in obesity cohorts compared to patients managed solely for mild diabetes.\n"
        "3. Absence of Denominator Exposure: FAERS does not capture total prescription volume. Because semaglutide usage expanded by over 400% "
        "between 2021 and 2024, higher absolute report counts are an expected consequence of massive patient exposure."
    )

    # 8. Recommendations
    add_h1(doc, "8. Clinical and Regulatory Recommendations")
    doc.add_paragraph(
        "Based on these empirical findings:\n"
        "• Healthcare providers should conduct routine baseline psychiatric assessments before initiating semaglutide, particularly in patients "
        "with personal or familial histories of depressive illness.\n"
        "• Regulatory agencies should continue active surveillance but avoid premature black-box warnings that might deter patients from "
        "cardiometabolically life-saving therapy without definitive prospective proof.\n"
        "• A prospective active-surveillance cohort study with active comparators is urgently indicated to overcome the intrinsic limitations of FAERS."
    )

    # 9. References
    add_h1(doc, "9. References (APA 7th Edition)")
    references = [
        "Food and Drug Administration. (2024). FDA Adverse Event Reporting System (FAERS) Public Dashboard and OpenFDA API Documentation. U.S. Department of Health and Human Services.",
        "Khouri, C., et al. (2024). The REporting of A Disproportionality Analysis for DrUg Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): Explanation and Elaboration. Drug Safety, 47(6), 541-558.",
        "McIntyre, R. S., et al. (2024). The association between glucagon-like peptide-1 receptor agonists and suicidality: reports to FAERS. Expert Opinion on Drug Safety, 23(3), 311-317.",
        "Schoretsanitis, G., et al. (2024). Disproportionality Analysis From World Health Organization Data on Semaglutide, Liraglutide, and Suicidality. JAMA Network Open, 7(8), e2423385.",
        "Wang, W., Volkow, N. D., et al. (2024). Association of semaglutide with risk of suicidal ideation in a real-world cohort. Nature Medicine, 30(1), 168-176.",
        "Wilding, J. P. H., et al. (2021). Once-Weekly Semaglutide in Adults with Overweight or Obesity (STEP 1 Trial). New England Journal of Medicine, 384(11), 989-1002."
    ]
    for ref in references:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.5)
        p.paragraph_format.first_line_indent = Inches(-0.5)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(ref)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    # Save to reports and copy to submission
    out_dir = os.path.join(BASE_DIR, 'reports', 'week2')
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'week2_data_analysis.docx')
    doc.save(out_file)
    print(f"Report saved successfully to {out_file}")

    sub_dir = os.path.join(BASE_DIR, 'submission', 'week2')
    os.makedirs(sub_dir, exist_ok=True)
    sub_file = os.path.join(sub_dir, 'week2_data_analysis.docx')
    shutil.copy(out_file, sub_file)
    print(f"Copied to submission directory: {sub_file}")

if __name__ == "__main__":
    generate_week2_report()
