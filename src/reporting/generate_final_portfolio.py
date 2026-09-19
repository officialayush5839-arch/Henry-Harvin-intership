import os
import shutil
import pandas as pd
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_styles import (
    create_document, add_title_page, add_h1, add_h2, add_h3, 
    add_callout, apply_table_styles, NAVY, SLATE, CHARCOAL
)

def generate_final_portfolio():
    print("Generating Final Integrated Research Portfolio Word Document...")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    doc = create_document()

    # Title Page
    add_title_page(
        doc,
        title="Comprehensive Post-Marketing Pharmacovigilance, Experimental Simulation, and Methodological Appraisal of Semaglutide",
        subtitle="An Integrated 4-Week Pharmaceutical Research Portfolio Investigating Neuropsychiatric Adverse Reactions",
        author="Aryan Ayush",
        affiliation="Pharmaceutical Research Assistant Internship",
        date_str="September 2026",
        week_tag="Final Integrated Portfolio Deliverable"
    )

    # Table of Contents
    add_h1(doc, "Table of Contents")
    toc = [
        "1. Abstract",
        "2. Introduction & Pharmacological Context",
        "3. Research Problem Statement & Public Health Significance",
        "4. Systematic Literature Review & Evidence Synthesis",
        "    4.1 Search Strategy and Eligibility Framework",
        "    4.2 Evidence Matrix of 17 Verified Scholarly Studies",
        "    4.3 Synthesis of Conflicting Evidence: Spontaneous Signals vs. EHR Cohorts",
        "5. Identification of Core Research Gaps",
        "6. Research Questions and Formal Hypotheses",
        "    6.1 PICO Structure and Primary Inquiry",
        "    6.2 Null and Alternative Hypotheses",
        "7. Investigation Objectives (Primary & Secondary)",
        "8. Public Data Collection & Preprocessing Methodology",
        "    8.1 FDA Adverse Event Reporting System (FAERS) Architecture",
        "    8.2 OpenFDA API Extraction and Data Cleaning",
        "9. Statistical Analysis Methodology",
        "    9.1 2x2 Contingency Table Modeling",
        "    9.2 Mathematical Formulation of Disproportionality (ROR, PRR, Chi-Square)",
        "    9.3 Signal Detection Threshold Benchmarks",
        "10. Empirical Findings & Pharmacovigilance Signals",
        "    10.1 Comparative Reporting Volumes and Event Rates",
        "    10.2 Comprehensive Disproportionality Analysis Table",
        "    10.3 High-Resolution Analytical Visualizations (Figures 1-6)",
        "11. Simulated Prospective Experimental Design",
        "    11.1 Active-Surveillance Cohort Rationale (N = 2,000)",
        "    11.2 Active SGLT2 Inhibitor Comparator Strategy",
        "    11.3 Psychometric Rating Scales and Clinical Endpoints",
        "    11.4 Clinical Workflow Diagram (Figure 7)",
        "    11.5 Safety Protocols, Stopping Rules, and DSMB Oversight",
        "12. Critical Methodological Appraisal of the STEP 1 Clinical Trial",
        "    12.1 Overview of Landmark Publication (Wilding et al., 2021, NEJM)",
        "    12.2 13-Component CONSORT/ICH Appraisal Matrix",
        "    12.3 Root Cause Analysis of Pre-Approval Safety Blindspots",
        "13. Integrated Cross-Week Discussion",
        "14. Methodological Strengths & Study Limitations",
        "15. Future Research Directions & Translational Policy Recommendations",
        "16. Concluding Remarks",
        "17. Master References (APA 7th Edition)",
        "18. Appendices (Data Dictionary & Regulatory Verification Index)"
    ]
    for item in toc:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(item)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        if not item.startswith("    "):
            r.font.bold = True
            r.font.color.rgb = NAVY
    doc.add_page_break()

    # 1. Abstract
    add_h1(doc, "1. Abstract")
    doc.add_paragraph(
        "Background: Semaglutide, an incretin-mimetic glucagon-like peptide-1 receptor agonist (GLP-1 RA), has achieved unprecedented "
        "global adoption for type 2 diabetes and obesity management. However, post-marketing safety alerts concerning potential neuropsychiatric "
        "adverse reactions have prompted international regulatory scrutiny, while observational electronic health record (EHR) studies have reported "
        "conflicting, protective associations."
    )
    doc.add_paragraph(
        "Methods: This four-week research portfolio executes a unified, multi-methodological investigation: (1) systematic evidence synthesis "
        "across 17 peer-reviewed publications; (2) empirical disproportionality analysis of 100,912 semaglutide reports versus 47,266 active comparator "
        "SGLT2 inhibitor reports in the FDA Adverse Event Reporting System (FAERS) (2018–2025) across seven MedDRA psychiatric preferred terms; "
        "(3) development of a 12-month simulated prospective active-surveillance cohort protocol (N = 2,000) incorporating validated psychometric "
        "rating scales (PHQ-9, C-SSRS); and (4) critical CONSORT-guided methodological appraisal of the pivotal Phase 3 STEP 1 trial (Wilding et al., 2021, NEJM)."
    )
    doc.add_paragraph(
        "Results: In FAERS disproportionality modeling, semaglutide exhibited statistically significant safety signals for suicidal ideation "
        "(ROR = 2.61, 95% CI: 2.18–3.12, PRR = 2.60, Chi2 = 116.35, p = 3.98e-27), panic attack (ROR = 4.40, 95% CI: 2.96–6.54, PRR = 4.39, Chi2 = 62.94), "
        "and depressed mood (ROR = 2.11, 95% CI: 1.72–2.58, PRR = 2.10, Chi2 = 54.23). In contrast, suicide attempt (ROR = 0.67) and insomnia (ROR = 0.96) "
        "did not meet signal criteria. Methodological evaluation of STEP 1 identified systematic exclusion of psychiatric comorbidity and reliance on "
        "passive adverse event capture as the primary structural reasons pre-approval RCTs failed to detect these real-world signals."
    )
    doc.add_paragraph(
        "Conclusions: Spontaneous pharmacovigilance confirms disproportionate post-marketing reporting of affective and suicidal symptoms with "
        "semaglutide. However, because spontaneous reporting is susceptible to notoriety bias and lacks denominator exposure, prospective active-surveillance "
        "with active comparators is essential to establish true clinical incidence and protect vulnerable patient populations."
    )
    add_callout(
        doc,
        "Portfolio Thesis: Pre-approval clinical trials prioritize efficacy in highly selected, psychiatrically resilient cohorts, creating "
        "systemic safety blindspots. Spontaneous reporting systems detect these emergent signals post-marketing, providing the empirical "
        "foundation for rigorously powered prospective active-surveillance investigations.",
        alert_type="NOTE"
    )

    # 2. Introduction
    add_h1(doc, "2. Introduction & Pharmacological Context")
    doc.add_paragraph(
        "Glucagon-like peptide-1 receptor agonists (GLP-1 RAs) represent one of the most transformative drug classes of the 21st century. "
        "By binding to native GLP-1 receptors in pancreatic beta cells and the central nervous system, semaglutide stimulates glucose-dependent "
        "insulin release, inhibits glucagon secretion, retards gastric emptying, and centrally modulates satiety pathways within the arcuate "
        "nucleus and area postrema of the brain. Available in once-weekly subcutaneous injections for diabetes (Ozempic) and obesity (Wegovy), "
        "as well as an oral formulation (Rybelsus), semaglutide exposure has expanded to tens of millions of patients worldwide."
    )
    doc.add_paragraph(
        "Despite extraordinary clinical benefits—including substantial glycemic improvement, 15% mean body weight reductions, and documented "
        "cardiovascular risk mitigation—the rapid expansion of therapy into diverse, non-trial populations has been accompanied by emergent "
        "safety concerns. Most prominent among these are reports of depressive episodes, anxiety, emotional blunting, and suicidal ideation, "
        "triggering urgent safety evaluations by the FDA and the European Medicines Agency (EMA)."
    )

    # 3. Research Problem
    add_h1(doc, "3. Research Problem Statement & Public Health Significance")
    doc.add_paragraph(
        "The fundamental clinical and regulatory dilemma is whether semaglutide directly induces neuropsychiatric adverse reactions through "
        "central nervous system receptor interactions, or whether observed safety reports reflect confounding by indication (obesity and diabetes "
        "carrying high baseline depression rates), notoriety bias (surge in reporting stimulated by intense international media publicity), "
        "or rapid lifestyle and neurochemical adjustments following dramatic weight reduction. Differentiating true pharmacological risk from "
        "observational artifacts is an urgent public health imperative to prevent unnecessary medication discontinuations while ensuring robust "
        "patient safeguards."
    )

    # 4. Literature Review & Evidence Synthesis
    add_h1(doc, "4. Systematic Literature Review & Evidence Synthesis")
    doc.add_paragraph(
        "A rigorous systematic review of scholarly literature published between 2020 and 2026 was conducted across PubMed, MEDLINE, and "
        "regulatory registers. Seventeen peer-reviewed studies met strict inclusion criteria, comprising spontaneous pharmacovigilance studies, "
        "randomized clinical trial safety updates, real-world target-trial emulation cohorts, and reporting guideline frameworks (READUS-PV; Khouri et al., 2024)."
    )

    # Evidence Matrix Table
    lit_csv = os.path.join(BASE_DIR, 'week1_literature_review', 'literature_matrix.csv')
    df_lit = pd.read_csv(lit_csv)
    
    table_lit = doc.add_table(rows=len(df_lit)+1, cols=4)
    table_lit.rows[0].cells[0].text = "PMID"
    table_lit.rows[0].cells[1].text = "Author / Year"
    table_lit.rows[0].cells[2].text = "Journal"
    table_lit.rows[0].cells[3].text = "Key Findings & Contribution"

    for idx, row in df_lit.iterrows():
        r_cells = table_lit.rows[idx+1].cells
        r_cells[0].text = str(row.get('PMID', 'N/A'))
        r_cells[1].text = f"{str(row.get('Authors', 'Author'))} ({str(row.get('Year', '2024'))})"
        r_cells[2].text = str(row.get('Journal', 'Journal'))
        r_cells[3].text = str(row.get('Major_Findings', 'Summary'))
    apply_table_styles(table_lit, [1.0, 1.4, 1.8, 2.3])
    doc.add_paragraph()

    add_h2(doc, "4.3 Synthesis of Conflicting Evidence")
    doc.add_paragraph(
        "Critical synthesis reveals an extraordinary scientific paradox in modern pharmacoepidemiology:\n"
        "• Spontaneous Reporting Databases: Analyses of FAERS and WHO VigiBase (Schoretsanitis et al., 2024; McIntyre et al., 2024) identify "
        "consistent disproportionality signals for suicidal ideation, particularly in patients co-prescribed antidepressants.\n"
        "• Target-Trial Emulation Cohorts: A landmark study by Wang et al. (2024, Nature Medicine) evaluating electronic health records of "
        "over 1.8 million patients found that semaglutide was associated with a 49% to 73% lower risk of suicidal ideation relative to non-GLP-1 "
        "comparators. This sharp divergence underscores how voluntary reporting, notoriety bias, and unmeasured confounding distort spontaneous "
        "pharmacovigilance data."
    )

    # 5. Research Gaps
    add_h1(doc, "5. Identification of Core Research Gaps")
    doc.add_paragraph(
        "Synthesizing published literature established four major unresolved gaps:\n"
        "1. Active Comparator Deficit: Prior FAERS analyses predominantly compared semaglutide against the entire database background, "
        "conflating drug risk with metabolic indication comorbidity.\n"
        "2. Granular Term Specificity: Failure to disaggregate subtle affective symptoms (depressed mood, panic attacks) from major clinical endpoints (suicide attempts).\n"
        "3. Lack of Prospective Psychometric Tracking: Absence of prospective active-surveillance studies utilizing standardized scales (PHQ-9, C-SSRS).\n"
        "4. Pre-Approval RCT Safety Gaps: Insufficient examination of how trial eligibility criteria obscure psychiatric adverse reactions."
    )

    # 6. Research Questions and Hypotheses
    add_h1(doc, "6. Research Questions and Formal Hypotheses")
    doc.add_paragraph(
        "Primary Research Question (PICO): In adult patients with post-marketing adverse event reports in FDA FAERS (2018–2025), is semaglutide "
        "exposure associated with a statistically significant disproportionate reporting rate of psychiatric adverse events compared to active "
        "comparator SGLT2 inhibitors?"
    )
    doc.add_paragraph(
        "Null Hypothesis (H0): The Reporting Odds Ratio for psychiatric adverse events in semaglutide-exposed reports is ROR <= 1.0 relative "
        "to SGLT2 inhibitor reports, indicating no disproportionate safety signal.\n"
        "Alternative Hypothesis (H1): The Reporting Odds Ratio is ROR > 1.0, with the lower bound of the 95% confidence interval exceeding 1.0, "
        "PRR >= 2.0, and Chi-square >= 4.0, confirming a validated pharmacovigilance signal."
    )

    # 7. Objectives
    add_h1(doc, "7. Investigation Objectives (Primary & Secondary)")
    doc.add_paragraph(
        "Primary Objective: Quantitatively measure disproportionality metrics (ROR, PRR, Chi2) across seven psychiatric MedDRA preferred terms "
        "in FAERS comparing semaglutide to SGLT2 inhibitors.\n"
        "Secondary Objectives:\n"
        "1. Quantify the relative risk profile across individual psychiatric sub-domains.\n"
        "2. Formulate an executable prospective active-surveillance cohort protocol (N = 2,000) with validated psychometric instruments.\n"
        "3. Systematically evaluate the STEP 1 trial to diagnose why pre-approval trials failed to identify post-marketing neuropsychiatric signals."
    )

    # 8. Data Collection Methodology
    add_h1(doc, "8. Public Data Collection & Preprocessing Methodology")
    doc.add_paragraph(
        "Post-marketing reports were extracted from the FDA FAERS database via the OpenFDA API (`api.fda.gov/drug/event.json`) and validated "
        "against quarterly public extracts (January 2018 to June 2025). The target cohort comprised primary suspect reports for semaglutide "
        "(Ozempic, Wegovy, Rybelsus; N = 100,912). The active comparator cohort comprised primary suspect reports for SGLT2 inhibitors "
        "(Empagliflozin, Dapagliflozin, Canagliflozin; N = 47,266). Data cleaning enforced deduplication on unique Case IDs and verified zero missing "
        "values across essential variables (`data_cleaning.py`)."
    )

    # 9. Statistical Methodology
    add_h1(doc, "9. Statistical Analysis Methodology")
    doc.add_paragraph(
        "For each psychiatric MedDRA term, a 2x2 contingency table was constructed comparing exposed cases (a), exposed non-cases (b), "
        "comparator cases (c), and comparator non-cases (d). Metrics included:\n"
        "• Reporting Odds Ratio: ROR = (a * d) / (b * c) with 95% log-normal confidence bounds.\n"
        "• Proportional Reporting Ratio: PRR = [a / (a + b)] / [c / (c + d)].\n"
        "• Chi-Square with Yates' Continuity Correction: chi2 = N*(|a*d - b*c| - N/2)^2 / [(a+b)*(c+d)*(a+c)*(b+d)].\n"
        "Signal Threshold: Lower 95% CI of ROR > 1.0 AND PRR >= 2.0 AND chi2 >= 4.0 with a >= 3 cases."
    )

    # 10. Empirical Findings
    add_h1(doc, "10. Empirical Findings & Pharmacovigilance Signals")
    doc.add_paragraph(
        "Table 2 displays the complete empirical statistical findings across all seven evaluated MedDRA terms:"
    )

    stat_csv = os.path.join(BASE_DIR, 'week2_data_analysis', 'results', 'statistical_results', 'disproportionality_results.csv')
    df_stat = pd.read_csv(stat_csv)

    table_stat = doc.add_table(rows=len(df_stat)+1, cols=7)
    table_stat.rows[0].cells[0].text = "MedDRA Term"
    table_stat.rows[0].cells[1].text = "Sema Cases (a)"
    table_stat.rows[0].cells[2].text = "SGLT2 Cases (c)"
    table_stat.rows[0].cells[3].text = "ROR (95% CI)"
    table_stat.rows[0].cells[4].text = "PRR"
    table_stat.rows[0].cells[5].text = "Chi2 (Yates)"
    table_stat.rows[0].cells[6].text = "Signal Detected?"

    for idx, row in df_stat.iterrows():
        r_cells = table_stat.rows[idx+1].cells
        r_cells[0].text = str(row['ADR_Term'])
        r_cells[1].text = f"{int(row['a (Sema with ADR)']):,}"
        r_cells[2].text = f"{int(row['c (SGLT2i with ADR)']):,}"
        r_cells[3].text = f"{row['ROR']:.2f} ({row['ROR_95%_CI_Lower']:.2f}–{row['ROR_95%_CI_Upper']:.2f})"
        r_cells[4].text = f"{row['PRR']:.2f}"
        r_cells[5].text = f"{row['Chi2_Stat']:.1f}"
        r_cells[6].text = "YES (SIGNAL)" if row['Signal_Detected'] else "NO"
    apply_table_styles(table_stat, [1.4, 0.9, 0.9, 1.6, 0.6, 0.8, 1.0])
    doc.add_paragraph()

    # Visualizations embedded in Portfolio
    add_h2(doc, "10.3 Analytical Visualizations")
    fig_dir = os.path.join(BASE_DIR, 'week2_data_analysis', 'results', 'figures')
    portfolio_figs = [
        ("fig3_forest_plot.png", "Figure 1. Reporting Odds Ratio Forest Plot with 95% Confidence Intervals",
         "Depicts point estimates and 95% error margins for all psychiatric terms. Suicidal Ideation (2.61), Depressed Mood (2.11), and Panic Attack (4.40) exhibit clear disproportionality signals separating from the null boundary."),
        ("fig4_grouped_comparison.png", "Figure 2. Comparative Reporting Rates per 10,000 Total Adverse Event Reports",
         "Highlights standardized reporting disparities between Semaglutide and SGLT2 inhibitors."),
        ("fig6_temporal_trend.png", "Figure 3. Longitudinal Psychiatric Adverse Event Reporting Trends (2018–2025)",
         "Illustrates exponential reporting growth for semaglutide following 2021 Wegovy approval and media publicity."),
        ("fig7_signal_heatmap.png", "Figure 4. Signal Intensity Heatmap across MedDRA Categories",
         "Color-coded matrix confirming signal hotspots for panic attacks and suicidal ideation.")
    ]
    for fname, ftitle, fdesc in portfolio_figs:
        fpath = os.path.join(fig_dir, fname)
        if os.path.exists(fpath):
            add_h3(doc, ftitle)
            doc.add_picture(fpath, width=Inches(5.8))
            p_cap = doc.add_paragraph()
            p_cap.paragraph_format.space_before = Pt(3)
            p_cap.paragraph_format.space_after = Pt(10)
            r_cap = p_cap.add_run(f"Figure Description: {fdesc}")
            r_cap.font.name = 'Times New Roman'
            r_cap.font.size = Pt(9)
            r_cap.font.italic = True

    # 11. Simulated Prospective Experimental Design
    add_h1(doc, "11. Simulated Prospective Experimental Design")
    add_callout(
        doc,
        "SIMULATION CLARIFICATION: The prospective protocol below is an advanced methodological simulation designed to overcome "
        "the epidemiological blindspots of spontaneous pharmacovigilance; it has not been executed in human clinical subjects.",
        alert_type="CAUTION"
    )
    doc.add_paragraph(
        "To rigorously test whether semaglutide causes incident depressive or suicidal states, Week 3 developed a prospective "
        "active-surveillance cohort protocol. Adult participants (N = 2,000; 1,000 initiating semaglutide, 1,000 initiating SGLT2i) are followed "
        "longitudinally for 12 months across multi-center outpatient clinics. The study protocol incorporates:\n"
        "• Power Calculation: 80% power at alpha = 0.05 to detect a Hazard Ratio >= 1.75 assuming a 5% baseline 12-month event rate and 15% attrition.\n"
        "• Validated Psychometrics: Mandatory electronic administration of the PHQ-9 (depression severity) and C-SSRS (suicidal ideation/behavior) "
        "at baseline, Month 3, Month 6, Month 9, and Month 12.\n"
        "• Active Comparator Control: SGLT2 inhibitors control for diabetes/obesity comorbidity, frequent clinic visits, and the psychological impact of medical treatment.\n"
        "• Independent Adjudication & Safety: Blinded psychiatrist panel reviews all endpoint triggers (PHQ-9 >= 15 or C-SSRS >= Level 3), "
        "backed by an automated 2-hour clinical escalation protocol and DSMB stopping rules (interim HR > 2.5, p < 0.001)."
    )

    # Embed Week 3 Flowchart
    flowchart_path = os.path.join(BASE_DIR, 'assets', 'figures', 'week3_study_flowchart.png')
    if os.path.exists(flowchart_path):
        add_h2(doc, "11.4 Clinical Workflow Diagram")
        doc.add_picture(flowchart_path, width=Inches(5.5))
        p_cap = doc.add_paragraph()
        p_cap.paragraph_format.space_before = Pt(4)
        p_cap.paragraph_format.space_after = Pt(12)
        r_cap = p_cap.add_run("Figure 5. Master workflow diagram for the prospective active-surveillance cohort study simulation.")
        r_cap.font.name = 'Times New Roman'
        r_cap.font.size = Pt(9.5)
        r_cap.font.italic = True

    # 12. Critical Evaluation
    add_h1(doc, "12. Critical Methodological Appraisal of the STEP 1 Clinical Trial")
    doc.add_paragraph(
        "In Week 4, we critically appraised the seminal STEP 1 trial (Wilding et al., 2021, NEJM; PMID 33567185), the pivotal Phase 3 trial "
        "(N = 1,961) demonstrating -14.9% weight loss with once-weekly semaglutide 2.4 mg versus -2.4% with placebo. While the study met the highest "
        "standards of randomized efficacy research (CONSORT 2010 compliance, central randomization, 92.6% trial completion, dual estimand reporting), "
        "it suffered from fundamental safety surveillance blindspots:\n"
        "1. Psychiatric Exclusion: Participants with a PHQ-9 score >= 15, major depressive disorder within 2 years, or prior suicidal behavior were "
        "systematically excluded. This screened out the exact vulnerable sub-populations who experience adverse psychiatric events in real-world clinical practice.\n"
        "2. Passive Adverse Event Capture: The trial relied on open-ended spontaneous reporting rather than validated longitudinal psychometric scales, "
        "causing mild-to-moderate affective symptoms and suicidal thoughts to remain unmeasured.\n"
        "3. Inert Placebo Control: The absence of an active metabolic comparator inflated observable efficacy while obscuring comparative risk-benefit profiles."
    )

    # 13. Integrated Discussion
    add_h1(doc, "13. Integrated Cross-Week Discussion")
    doc.add_paragraph(
        "Synthesizing the four weekly investigations resolves the central pharmacoepidemiological paradox of GLP-1 receptor agonist safety:\n"
        "1. Pre-approval clinical trials (STEP 1) are engineered as high-internal-validity efficacy experiments that intentionally exclude psychiatric comorbidity. "
        "Consequently, neuropsychiatric adverse events are suppressed and evade pre-marketing detection.\n"
        "2. Upon broad commercial distribution, post-marketing spontaneous reporting systems (FAERS) capture real-world patient exposure. Spontaneous "
        "disproportionality analysis (Week 2) successfully detected robust safety signals for suicidal ideation (ROR 2.61) and panic attacks (ROR 4.40), "
        "generating urgent regulatory hypotheses.\n"
        "3. However, because FAERS lacks denominator exposure and is heavily confounded by notoriety bias and media coverage, spontaneous signals "
        "cannot establish causality.\n"
        "4. Definitive scientific resolution requires prospective active-surveillance cohort studies with active comparators (Week 3 simulation) "
        "to distinguish genuine neurobiological drug risk from underlying disease comorbidity."
    )

    # 14. Limitations
    add_h1(doc, "14. Methodological Strengths & Study Limitations")
    doc.add_paragraph(
        "Strengths: Methodological diversity integrating literature synthesis, raw public data mining, rigorous disproportionality math, "
        "experimental protocol planning, and formal clinical trial appraisal; 100% reproducible analytical code; complete reference verifiability.\n"
        "Limitations: Spontaneous reporting data is subject to underreporting, the Weber effect, and reporting stimulation; lack of prescription "
        "denominator data prevents incidence calculation; the experimental protocol is an academic simulation."
    )

    # 15. Future Directions & Policy
    add_h1(doc, "15. Future Research Directions & Translational Policy Recommendations")
    doc.add_paragraph(
        "1. Mandate Prospective Psychometric Monitoring: Regulatory agencies (FDA, EMA) should mandate structured psychometric screening (PHQ-9, C-SSRS) "
        "in all Phase 3/4 trials of CNS-penetrant incretin mimetics.\n"
        "2. Pragmatic Real-World Trial Inclusion: Future metabolic trials must broaden inclusion criteria to include patients with stable, treated affective illness.\n"
        "3. Clinical Vigilance without Panic: Clinicians should screen patients for personal or familial depressive history before prescribing semaglutide "
        "but avoid indiscriminate drug withholding, given the profound cardiometabolic benefits of therapy."
    )

    # 16. Conclusion
    add_h1(doc, "16. Concluding Remarks")
    doc.add_paragraph(
        "This research portfolio provides a complete, methodologically rigorous, and reproducible examination of semaglutide pharmacovigilance. "
        "By connecting literature review to raw spontaneous data analysis, prospective study design, and clinical trial critique, the portfolio "
        "illustrates how advanced pharmaceutical research bridges the gap between pre-approval efficacy and real-world patient safety."
    )

    # 17. References
    add_h1(doc, "17. Master References (APA 7th Edition)")
    references = [
        "American Diabetes Association. (2024). Standards of Care in Diabetes—2024. Diabetes Care, 47(Suppl. 1), S1-S343.",
        "Consortium for Reporting Trials. (2010). CONSORT 2010 Explanation and Elaboration: updated guidelines for reporting parallel group randomised trials. BMJ, 340, c869.",
        "Food and Drug Administration. (2024). FDA Adverse Event Reporting System (FAERS) Public Dashboard and OpenFDA API Documentation. U.S. Department of Health and Human Services.",
        "International Council for Harmonisation. (2016). Integrated Addendum to ICH E6(R1): Guideline for Good Clinical Practice E6(R2). Current Step 4 Version.",
        "Khouri, C., et al. (2024). The REporting of A Disproportionality Analysis for DrUg Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): Explanation and Elaboration. Drug Safety, 47(6), 541-558. https://doi.org/10.1007/s40264-024-01421-9",
        "Kroenke, K., Spitzer, R. L., & Williams, J. B. (2001). The PHQ-9: validity of a brief depression severity measure. Journal of General Internal Medicine, 16(9), 606-613.",
        "McIntyre, R. S., et al. (2024). The association between glucagon-like peptide-1 receptor agonists and suicidality: reports to FAERS. Expert Opinion on Drug Safety, 23(3), 311-317. https://doi.org/10.1080/14740338.2023.2295397",
        "Posner, K., et al. (2011). The Columbia-Suicide Severity Rating Scale: initial validity and internal consistency findings from three multisite studies. American Journal of Psychiatry, 168(12), 1266-1277.",
        "Schoretsanitis, G., et al. (2024). Disproportionality Analysis From World Health Organization Data on Semaglutide, Liraglutide, and Suicidality. JAMA Network Open, 7(8), e2423385. https://doi.org/10.1001/jamanetworkopen.2024.23385",
        "Wang, W., Volkow, N. D., et al. (2024). Association of semaglutide with risk of suicidal ideation in a real-world cohort. Nature Medicine, 30(1), 168-176. https://doi.org/10.1038/s41591-023-02672-2",
        "Wilding, J. P. H., Batterham, R. L., Calanna, S., et al. (2021). Once-Weekly Semaglutide in Adults with Overweight or Obesity (STEP 1 Trial). New England Journal of Medicine, 384(11), 989-1002. https://doi.org/10.1056/NEJMoa2032183",
        "Wilding, J. P. H., et al. (2022). Weight regain and cardiometabolic effects after withdrawal of semaglutide: The STEP 1 trial extension. Diabetes, Obesity and Metabolism, 24(8), 1553-1564."
    ]
    for ref in references:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.5)
        p.paragraph_format.first_line_indent = Inches(-0.5)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(ref)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    # 18. Appendices
    add_h1(doc, "18. Appendices")
    add_h2(doc, "Appendix A: Analytical Scripts & Artifact Repository Index")
    doc.add_paragraph(
        "All analytical code, data tables, and reproducible assets are organized in the AntiGravity project workspace:\n"
        "• Data Collection: `week2_data_analysis/scripts/data_collection.py` (OpenFDA API extraction)\n"
        "• Data Cleaning & Processing: `week2_data_analysis/scripts/data_cleaning.py`\n"
        "• Descriptive Statistics: `week2_data_analysis/scripts/descriptive_statistics.py`\n"
        "• Disproportionality Testing: `week2_data_analysis/scripts/statistical_tests.py`\n"
        "• Visualization Generator: `week2_data_analysis/scripts/visualization.py`\n"
        "• Interactive Analysis Notebook: `week2_data_analysis/notebooks/pharmaceutical_data_analysis.ipynb`\n"
        "• Literature Matrix: `week1_literature_review/literature_matrix.xlsx` and `.csv`\n"
        "• Methodology Appraisal Matrix: `week4_critical_evaluation/methodology_matrix.xlsx` and `.csv`\n"
        "• Quality Assurance Audits: `qa/citation_validation.md`, `qa/statistical_validation.md`, `qa/document_validation.md`, `qa/research_quality_checklist.md`"
    )

    # Save to reports and copy to submission
    out_dir = os.path.join(BASE_DIR, 'reports', 'final')
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'final_integrated_research_portfolio.docx')
    doc.save(out_file)
    print(f"Final integrated report saved successfully to {out_file}")

    sub_dir = os.path.join(BASE_DIR, 'submission', 'final_portfolio')
    os.makedirs(sub_dir, exist_ok=True)
    sub_file = os.path.join(sub_dir, 'final_integrated_research_portfolio.docx')
    shutil.copy(out_file, sub_file)
    print(f"Copied to submission directory: {sub_file}")

if __name__ == "__main__":
    generate_final_portfolio()
