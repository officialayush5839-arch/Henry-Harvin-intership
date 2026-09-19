import os
import shutil
import pandas as pd
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_styles import (
    create_document, add_title_page, add_h1, add_h2, add_h3, 
    add_callout, apply_table_styles, NAVY, SLATE, CHARCOAL
)

def generate_week4_report():
    print("Generating Week 4 Critical Evaluation Word Report...")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    doc = create_document()

    # Title Page
    add_title_page(
        doc,
        title="Critical Methodological Evaluation of the Landmark STEP 1 Clinical Trial",
        subtitle="A Rigorous Appraisal of Randomized Trial Architecture, Safety Surveillance Blindspots, and Post-Marketing Divergence",
        author="Aryan Ayush",
        affiliation="Pharmaceutical Research Assistant Internship",
        date_str="September 2026",
        week_tag="Week 4 Portfolio Deliverable"
    )

    # Table of Contents Outline
    add_h1(doc, "Table of Contents")
    toc_items = [
        "1. Executive Summary",
        "2. Selected Article Metadata and Clinical Significance",
        "3. Methodological Appraisal Framework (CONSORT & ICH-GCP)",
        "4. 13-Component Comprehensive Methodology Matrix",
        "5. Critical Analysis of Methodological Strengths",
        "    5.1 Rigorous Randomization and Double-Blind Integrity",
        "    5.2 Trial Product vs. Treatment Policy Estimand Strategy",
        "    5.3 Exceptional Longitudinal Participant Retention (92.6%)",
        "    5.4 Multi-Center International Diversity",
        "6. In-Depth Methodological Vulnerabilities and Blindspots",
        "    6.1 Systematic Psychiatric Exclusion and External Validity Loss",
        "    6.2 Passive Safety Capture vs. Active Neuropsychiatric Surveillance",
        "    6.3 Placebo Control vs. Active Comparator Limitations",
        "    6.4 Post-Cessation Metabolic and Psychological Rebound",
        "    6.5 Industry Sponsorship and Reporting Architecture",
        "7. Actionable Methodological Recommendations for Future Trials",
        "8. Cross-Week Synthesis: Why Pre-Approval RCTs Miss Post-Marketing Signals",
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
        "This Week 4 critical appraisal presents an exhaustive methodological evaluation of the landmark STEP 1 trial (Wilding et al., 2021, "
        "New England Journal of Medicine), the pivotal Phase 3 randomized controlled trial that secured FDA and EMA approval for semaglutide 2.4 mg "
        "(Wegovy) for chronic weight management. The study demonstrated remarkable therapeutic efficacy, achieving a mean body-weight reduction "
        "of -14.9% with semaglutide versus -2.4% with placebo over 68 weeks."
    )
    doc.add_paragraph(
        "Utilizing a 13-component appraisal matrix grounded in CONSORT 2010 and ICH-E6 GCP guidelines, we critically scrutinized the trial's "
        "architecture. While STEP 1 demonstrated exemplary randomized trial rigor—including central interactive response system allocation, "
        "double-blind masking, 92.6% participant completion, and dual estimand frameworks—it exhibits critical structural vulnerabilities "
        "regarding safety surveillance. Most significantly, the protocol systematically excluded individuals with major psychiatric illness or "
        "recent suicidal history and relied on passive, spontaneous reporting for adverse events rather than validated prospective psychometric rating scales."
    )
    add_callout(
        doc,
        "Appraisal Conclusion: The STEP 1 trial is an exemplary efficacy study that established semaglutide's weight-loss superiority. However, "
        "its restrictive eligibility and passive safety monitoring created a systemic blindspot for neuropsychiatric adverse reactions, "
        "explaining why disproportionality signals for suicidal ideation and depression emerged only after millions of diverse patients "
        "were exposed in real-world post-marketing environments (Weeks 1 and 2).",
        alert_type="NOTE"
    )

    # 2. Selected Article Metadata
    add_h1(doc, "2. Selected Article Metadata and Clinical Significance")
    doc.add_paragraph(
        "The appraised publication is documented below with verified scholarly metadata:"
    )
    
    meta_table = doc.add_table(rows=8, cols=2)
    meta_rows = [
        ("Article Title", "Once-Weekly Semaglutide in Adults with Overweight or Obesity (STEP 1 Trial)"),
        ("Lead Authors", "John P.H. Wilding, D.M., Rachel L. Batterham, M.B., B.S., Ph.D., Salvatore Calanna, Ph.D., et al."),
        ("Journal & Date", "New England Journal of Medicine (NEJM), March 18, 2021; Vol. 384, No. 11, pp. 989–1002"),
        ("Identifiers", "DOI: 10.1056/NEJMoa2032183 | PMID: 33567185 | ClinicalTrials.gov: NCT03548935"),
        ("Study Design", "Phase 3a, randomized, double-blind, placebo-controlled, multinational trial (129 sites, 16 countries)"),
        ("Population Size", "N = 1,961 adults without type 2 diabetes (BMI >= 30, or >= 27 with >= 1 weight-related condition)"),
        ("Intervention Arms", "Semaglutide SC 2.4 mg once weekly (N = 1,306) vs. Matched Placebo (N = 655) for 68 weeks + lifestyle intervention"),
        ("Primary Endpoints", "Percentage change in body weight and achievement of >= 5% weight reduction at week 68")
    ]
    for idx, (label, val) in enumerate(meta_rows):
        meta_table.rows[idx].cells[0].text = label
        meta_table.rows[idx].cells[1].text = val
    apply_table_styles(meta_table, [2.0, 4.5])
    doc.add_paragraph()

    # 3. Methodological Appraisal Framework
    add_h1(doc, "3. Methodological Appraisal Framework (CONSORT & ICH-GCP)")
    doc.add_paragraph(
        "The evaluation benchmarked the published trial against the Consolidated Standards of Reporting Trials (CONSORT 2010) statement, "
        "ICH-E6 (R2) Good Clinical Practice guidelines, and the FDA Guidance on Safety Assessment in Clinical Trials. Rather than assigning "
        "arbitrary subjective numerical scores, we executed an objective component-by-component comparative assessment comparing the published "
        "approach against gold-standard best practices."
    )

    # 4. 13-Component Comprehensive Methodology Matrix
    add_h1(doc, "4. 13-Component Comprehensive Methodology Matrix")
    doc.add_paragraph(
        "Table 3 provides the detailed comparative analysis across the 13 fundamental methodological dimensions:"
    )

    # Load matrix CSV
    mat_csv = os.path.join(BASE_DIR, 'week4_critical_evaluation', 'methodology_matrix.csv')
    df_mat = pd.read_csv(mat_csv)

    table_mat = doc.add_table(rows=len(df_mat)+1, cols=4)
    table_mat.rows[0].cells[0].text = "Component"
    table_mat.rows[0].cells[1].text = "Published Study Approach"
    table_mat.rows[0].cells[2].text = "Best-Practice Expectation"
    table_mat.rows[0].cells[3].text = "Assessment & Identified Gap"

    for idx, row in df_mat.iterrows():
        r_cells = table_mat.rows[idx+1].cells
        r_cells[0].text = str(row['Methodological_Component'])
        r_cells[1].text = str(row['Published_Study_Approach'])
        r_cells[2].text = str(row['Best_Practice_Expectation'])
        r_cells[3].text = str(row['Assessment_Observation'])

    apply_table_styles(table_mat, [1.3, 1.8, 1.7, 1.7])
    doc.add_paragraph()

    # 5. Methodological Strengths
    add_h1(doc, "5. Critical Analysis of Methodological Strengths")
    doc.add_paragraph(
        "The STEP 1 trial exhibited exceptional execution across multiple core clinical trial domains:\n"
        "1. Randomization and Masking: Centralized interactive Web-response systems ensured 2:1 allocation concealing sequence from investigators. "
        "Semaglutide and placebo pens were visually identical, preserving double-blind integrity.\n"
        "2. Estimand Precision: In accordance with ICH E9 (R1) guidelines, the authors pre-specified two distinct estimands: the 'trial product "
        "estimand' (evaluating on-treatment efficacy under full adherence) and the 'treatment policy estimand' (evaluating Intention-to-Treat "
        "irrespective of adherence or rescue therapy), providing complete statistical transparency.\n"
        "3. Participant Retention: Over a 68-week trial duration, 92.6% of participants completed the trial and 81.1% adhered to the target "
        "medication regimen, an extraordinarily high retention rate for chronic anti-obesity trials.\n"
        "4. Multinational Scope: Conducted across 129 academic and clinical centers in 16 nations across North America, Europe, South America, and Asia."
    )

    # 6. Methodological Vulnerabilities and Blindspots
    add_h1(doc, "6. In-Depth Methodological Vulnerabilities and Blindspots")
    doc.add_paragraph(
        "Despite its clinical excellence, critical methodological blindspots compromised the trial's ability to detect neuropsychiatric safety signals:"
    )

    blindspots = [
        ("Systematic Psychiatric Exclusion: ", "Participants with a PHQ-9 score >= 15, a history of major depressive disorder within 2 years, or any prior suicide attempt were strictly excluded. In the real world, 20% to 35% of individuals seeking obesity management carry co-occurring affective or depressive disorders. By screening out vulnerable individuals, the trial created an artificially resilient study population, masking vulnerability to GLP-1 receptor-mediated mood changes."),
        ("Passive Adverse Event Collection: ", "Safety surveillance relied on spontaneous patient reporting and open-ended investigator questioning ('Have you felt unwell since the last visit?') rather than structured, validated psychiatric rating instruments (e.g., C-SSRS or weekly PHQ-9). Mild-to-moderate emotional blunting, anhedonia, and emergent suicidal thoughts are notoriously underreported in unstructured clinical interviews."),
        ("Placebo vs. Active Comparator: ", "Employing an inert placebo control maximized the observed effect size of weight loss but prevented comparative safety evaluation against alternative metabolic interventions (e.g., SGLT2 inhibitors or intensive behavioral therapy alone)."),
        ("Post-Cessation Rebound: ", "The trial terminated follow-up at week 68 with only a 7-week safety extension. Subsequent extension studies (STEP 1 Trial Extension, Wilding et al., 2022) revealed that participants regained two-thirds of lost weight within 12 months of cessation. The psychological trauma and affective distress associated with rapid weight regain were uncaptured in the primary manuscript.")
    ]
    for b_title, b_desc in blindspots:
        p = doc.add_paragraph()
        r1 = p.add_run(f"• {b_title}")
        r1.font.bold = True
        r1.font.color.rgb = NAVY
        r2 = p.add_run(b_desc)
        r2.font.color.rgb = CHARCOAL

    # 7. Recommendations
    add_h1(doc, "7. Actionable Methodological Recommendations for Future Trials")
    doc.add_paragraph(
        "To elevate clinical trial methodology in cardiometabolic pharmacotherapy, we recommend three structural protocol modifications:\n"
        "1. Active Psychometric Screening: Incorporate mandatory baseline, mid-trial, and end-of-treatment electronic C-SSRS and PHQ-9 administration "
        "for all CNS-active or systemic incretin therapies.\n"
        "2. Pragmatic Eligibility Criteria: Liberalize psychiatric exclusion criteria to allow patients with stable, treated depression or mild anxiety, "
        "establishing safety in populations mirroring true clinical practice.\n"
        "3. Active-Comparator Trial Designs: Compare emerging incretins directly against active metabolic controls (e.g., dual GIP/GLP-1 agonists or SGLT2i) "
        "to establish comparative risk-benefit profiles."
    )

    # 8. Cross-Week Synthesis
    add_h1(doc, "8. Cross-Week Synthesis: Why Pre-Approval RCTs Miss Post-Marketing Signals")
    doc.add_paragraph(
        "The findings of Week 4 seamlessly unite the four-week research portfolio:\n"
        "• In Week 1, we identified an empirical paradox: FAERS and VigiBase documented elevated suicidal ideation signals, whereas real-world "
        "EHR cohorts (Wang et al., 2024) indicated neutral or protective effects.\n"
        "• In Week 2, our empirical disproportionality analysis confirmed robust statistical signals for suicidal ideation (ROR 2.61) and "
        "panic attacks (ROR 4.40) in FAERS relative to SGLT2 inhibitors.\n"
        "• In Week 3, we designed a prospective active-surveillance cohort simulation (N = 2,000) explicitly engineered to capture validated "
        "psychometric endpoints and bridge observational gaps.\n"
        "• In Week 4, our critical evaluation of the STEP 1 trial provides the definitive methodological explanation: pre-approval RCTs are "
        "optimized for efficacy and systematically exclude psychiatric vulnerability, leaving post-marketing pharmacovigilance as the primary "
        "detector of real-world neuropsychiatric safety signals."
    )

    # 9. References
    add_h1(doc, "9. References (APA 7th Edition)")
    references = [
        "Consortium for Reporting Trials. (2010). CONSORT 2010 Explanation and Elaboration: updated guidelines for reporting parallel group randomised trials. BMJ, 340, c869.",
        "International Council for Harmonisation. (2016). Integrated Addendum to ICH E6(R1): Guideline for Good Clinical Practice E6(R2). Current Step 4 Version.",
        "Khouri, C., et al. (2024). The REporting of A Disproportionality Analysis for DrUg Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV). Drug Safety, 47(6), 541-558.",
        "Wang, W., Volkow, N. D., et al. (2024). Association of semaglutide with risk of suicidal ideation in a real-world cohort. Nature Medicine, 30(1), 168-176.",
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

    # Save to reports and copy to submission
    out_dir = os.path.join(BASE_DIR, 'reports', 'week4')
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'week4_critical_evaluation.docx')
    doc.save(out_file)
    print(f"Report saved successfully to {out_file}")

    sub_dir = os.path.join(BASE_DIR, 'submission', 'week4')
    os.makedirs(sub_dir, exist_ok=True)
    sub_file = os.path.join(sub_dir, 'week4_critical_evaluation.docx')
    shutil.copy(out_file, sub_file)
    print(f"Copied to submission directory: {sub_file}")

if __name__ == "__main__":
    generate_week4_report()
