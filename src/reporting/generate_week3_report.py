import os
import shutil
import pandas as pd
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx_styles import (
    create_document, add_title_page, add_h1, add_h2, add_h3, 
    add_callout, apply_table_styles, NAVY, SLATE, CHARCOAL
)

def generate_week3_report():
    print("Generating Week 3 Experimental Design Word Report...")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    doc = create_document()

    # Title Page
    add_title_page(
        doc,
        title="Prospective Active-Surveillance Cohort Study on the Neuropsychiatric Safety of Semaglutide",
        subtitle="A Simulated Experimental Design and Clinical Protocol with Active SGLT2 Inhibitor Comparator",
        author="Aryan Ayush",
        affiliation="Pharmaceutical Research Assistant Internship",
        date_str="September 2026",
        week_tag="Week 3 Portfolio Deliverable (Simulated Study Design)"
    )

    # Table of Contents Outline
    add_h1(doc, "Table of Contents")
    toc_items = [
        "1. Executive Summary & Simulation Statement",
        "2. Clinical Rationale and Translational Context",
        "3. Research Objectives and PICO Framework",
        "    3.1 Primary and Secondary Research Questions",
        "    3.2 Statistical Hypotheses",
        "4. Variable Taxonomy and Operational Definitions",
        "    4.1 Independent Exposure Variables",
        "    4.2 Primary and Secondary Dependent Endpoints",
        "    4.3 Control Variables and Confounder Management",
        "5. Control Strategy and Active Comparator Rationale",
        "6. Sample Size, Power Calculation, and Eligibility Criteria",
        "    6.1 Power Determination (N = 2,000 Cohort)",
        "    6.2 Inclusion and Exclusion Criteria",
        "7. Experimental and Clinical Protocol",
        "    7.1 Patient Recruitment and Baseline Assessment",
        "    7.2 Dose Titration and Regimen Management",
        "    7.3 Longitudinal Surveillance Schedule (M3, M6, M9, M12)",
        "8. Clinical Workflow Diagram",
        "9. Data Collection and Measurement Instruments",
        "    9.1 Validated Rating Scales (PHQ-9, C-SSRS, GAD-7)",
        "    9.2 Centralized Electronic Data Capture (EDC)",
        "10. Safety Monitoring, Crisis Escalation, and DSMB Oversight",
        "11. Ethical Considerations and Regulatory Compliance",
        "12. Troubleshooting and Risk Mitigation Protocol",
        "13. Statistical Analysis Plan (SAP)",
        "    13.1 Primary Survival Analysis (Cox Proportional Hazards)",
        "    13.2 Propensity Score Matching and Sensitivity Analyses",
        "14. References (APA 7th Edition)"
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
    add_h1(doc, "1. Executive Summary & Simulation Statement")
    add_callout(
        doc,
        "ACADEMIC SIMULATION NOTICE: This document delineates a fully realized, scientifically rigorous experimental design "
        "and clinical protocol. As stipulated by the internship curriculum, this is an advanced methodological simulation developed to "
        "address the epidemiological limitations of spontaneous pharmacovigilance (Weeks 1 and 2); no actual human laboratory or clinical trial "
        "has been executed.",
        alert_type="CAUTION"
    )
    doc.add_paragraph(
        "Spontaneous pharmacovigilance findings from Week 2 identified significant disproportionality signals for suicidal ideation "
        "(ROR = 2.61, 95% CI: 2.18–3.12) and depressed mood (ROR = 2.11, 95% CI: 1.72–2.58) among semaglutide reports in FAERS. "
        "However, spontaneous reporting cannot establish biological causation due to reporting bias, media stimulation, and lack of denominator "
        "exposure data. To overcome these constraints, this Week 3 deliverable develops a comprehensive, 12-month prospective active-surveillance "
        "cohort study protocol comparing adult patients newly initiating semaglutide (N = 1,000) versus active comparator SGLT2 inhibitors "
        "(N = 1,000)."
    )
    doc.add_paragraph(
        "Employing validated psychometric screening tools administered longitudinally (PHQ-9, C-SSRS, GAD-7) alongside blinded clinical "
        "endpoint adjudication, this protocol specifies sample size power calculations (80% power to detect Hazard Ratio >= 1.75 at alpha = 0.05), "
        "propensity score matching, pre-specified stopping boundaries, independent Data Safety Monitoring Board (DSMB) oversight, and an immediate "
        "psychiatric crisis escalation protocol. This design provides a blueprint for prospective regulatory validation."
    )

    # 2. Clinical Rationale
    add_h1(doc, "2. Clinical Rationale and Translational Context")
    doc.add_paragraph(
        "The unresolved debate between spontaneous safety signals (FAERS, VigiBase) and observational electronic health record cohorts "
        "(Nature Medicine, 2024) stems from confounding by indication and voluntary reporting anomalies. Patients with severe obesity or diabetes "
        "possess substantially elevated baseline lifetime risks for major depressive episodes. By designing a prospective study with an active "
        "comparator (SGLT2 inhibitors) prescribed for overlapping cardiometabolic indications, baseline comorbidity, lifestyle factors, and "
        "healthcare contact frequency are inherently balanced, isolating the pharmacodynamic impact of GLP-1 receptor modulation on central "
        "neurobehavioral pathways."
    )

    # 3. Research Objectives and PICO
    add_h1(doc, "3. Research Objectives and PICO Framework")
    doc.add_paragraph(
        "The prospective trial design is structured via the PICO paradigm:"
    )
    pico = [
        ("Population: ", "Adult patients (aged 18–75 years) diagnosed with type 2 diabetes mellitus or obesity (BMI >= 30 kg/m2, or >= 27 kg/m2 with cardiometabolic comorbidity) initiating a new line of pharmacotherapy."),
        ("Intervention: ", "Semaglutide subcutaneous injection (once weekly, titrated from 0.25 mg to target maintenance dose of 1.0 mg or 2.4 mg) plus standard lifestyle counseling."),
        ("Comparator: ", "Active comparator SGLT2 inhibitor (Empagliflozin 10–25 mg daily or Dapagliflozin 10 mg daily) plus standard lifestyle counseling."),
        ("Outcome: ", "Time to first onset of adjudicated moderate-to-severe depressive episode (PHQ-9 score >= 15) or any suicidal ideation/behavior (C-SSRS >= Level 3) over 12 months.")
    ]
    for p_title, p_desc in pico:
        p = doc.add_paragraph()
        r1 = p.add_run(f"• {p_title}")
        r1.font.bold = True
        r1.font.color.rgb = NAVY
        r2 = p.add_run(p_desc)
        r2.font.color.rgb = CHARCOAL

    add_h2(doc, "3.1 Formal Hypotheses")
    doc.add_paragraph(
        "Null Hypothesis (H0): The hazard rate of incident moderate-to-severe psychiatric adverse events in patients treated with semaglutide "
        "is equal to that in patients treated with SGLT2 inhibitors over 12 months (Hazard Ratio [HR] = 1.0)."
    )
    doc.add_paragraph(
        "Alternative Hypothesis (H1): The hazard rate of incident moderate-to-severe psychiatric adverse events in patients treated with "
        "semaglutide is significantly higher than in patients treated with SGLT2 inhibitors (Hazard Ratio [HR] > 1.0, alpha = 0.05)."
    )

    # 4. Variable Taxonomy
    add_h1(doc, "4. Variable Taxonomy and Operational Definitions")
    doc.add_paragraph(
        "Methodological rigor necessitates precise classification of experimental variables to prevent misclassification and residual confounding:"
    )

    var_table = doc.add_table(rows=5, cols=3)
    var_table.rows[0].cells[0].text = "Variable Class"
    var_table.rows[0].cells[1].text = "Operational Parameter"
    var_table.rows[0].cells[2].text = "Measurement Instrument / Method"
    
    var_data = [
        ("Independent Variable", "Antidiabetic / Anti-obesity Drug Regimen", "Semaglutide (SC 0.25–2.4 mg/wk) vs SGLT2i (Empagliflozin/Dapagliflozin daily), tracked via pharmacy fill logs"),
        ("Primary Dependent Variable", "Time to incident major depressive episode or suicidal ideation", "PHQ-9 total score >= 15 or C-SSRS >= Level 3 confirmed by masked psychiatrist adjudication"),
        ("Secondary Dependent Variables", "Generalized anxiety symptoms, sleep quality, all-cause discontinuation", "GAD-7 total score >= 10, Pittsburgh Sleep Quality Index (PSQI), time to drug cessation"),
        ("Confounders & Covariates", "Baseline BMI, % weight loss, prior psychiatric history, concomitant medications", "Monthly weight logs, medical chart abstraction, concomitant psychotropic pill counts")
    ]
    for idx, (vc, op, mi) in enumerate(var_data, start=1):
        var_table.rows[idx].cells[0].text = vc
        var_table.rows[idx].cells[1].text = op
        var_table.rows[idx].cells[2].text = mi
    apply_table_styles(var_table, [1.5, 2.5, 2.5])
    doc.add_paragraph()

    # 5. Control Strategy
    add_h1(doc, "5. Control Strategy and Active Comparator Rationale")
    doc.add_paragraph(
        "Utilizing a placebo control in patients with established type 2 diabetes or severe obesity is ethically problematic and fails to "
        "account for the psychological impact of clinical treatment engagement. SGLT2 inhibitors represent the optimal active comparator because:\n"
        "1. They share overlapping clinical indications (glycemic management, cardiovascular risk reduction, moderate weight loss of 2–4 kg).\n"
        "2. They possess a distinct mechanism of action (renal glucose excretion) with minimal central nervous system penetrance.\n"
        "3. Spontaneous reporting profiles in FAERS demonstrated neutral baseline reporting for affective disorders (ROR = 0.96 for insomnia, ROR = 0.67 for suicide attempts), providing a stable epidemiological reference."
    )

    # 6. Sample Size & Eligibility
    add_h1(doc, "6. Sample Size, Power Calculation, and Eligibility Criteria")
    doc.add_paragraph(
        "Assuming a baseline 12-month incidence of moderate depressive symptoms of 5.0% in the active comparator SGLT2i cohort, a two-sided log-rank "
        "test at alpha = 0.05 with 80% power (beta = 0.20) to detect a Hazard Ratio (HR) of 1.75 requires 142 primary event endpoints. "
        "Anticipating a 15% cumulative loss to follow-up over 12 months, the study recruits a total sample of N = 2,000 patients (1,000 per arm)."
    )

    add_h2(doc, "6.2 Inclusion and Exclusion Criteria")
    doc.add_paragraph(
        "Inclusion Criteria:\n"
        "• Adults aged 18 to 75 years.\n"
        "• Confirmed diagnosis of type 2 diabetes (HbA1c 7.0%–10.0%) or obesity (BMI >= 30 kg/m2, or >= 27 kg/m2 with hypertension/dyslipidemia).\n"
        "• Newly prescribed either semaglutide or SGLT2i (treatment-naive or switching after >= 3 months washout).\n"
        "• Capable of completing electronic psychometric questionnaires in English or Spanish."
    )
    doc.add_paragraph(
        "Exclusion Criteria:\n"
        "• Active major psychiatric disorder (bipolar disorder, schizophrenia, active psychosis) within the preceding 12 months.\n"
        "• History of suicide attempt within the past 3 years, or baseline C-SSRS score >= Level 4.\n"
        "• Personal or family history of medullary thyroid carcinoma or Multiple Endocrine Neoplasia syndrome type 2 (MEN 2).\n"
        "• Severe chronic kidney disease (eGFR < 30 mL/min/1.73m2) or end-stage liver disease."
    )

    # 7. Protocol
    add_h1(doc, "7. Experimental and Clinical Protocol")
    doc.add_paragraph(
        "Patients undergo standardized baseline evaluations, including structured clinical interviews (MINI), baseline psychometric testing, "
        "vital signs, HbA1c, and fasting metabolic profiles. Dose escalation for semaglutide adheres strictly to clinical package inserts: "
        "0.25 mg weekly for 4 weeks, titrating to 0.5 mg, 1.0 mg, and if indicated for weight management, 2.4 mg at Month 4. "
        "Comparator patients receive Empagliflozin 10 mg daily (titrated to 25 mg if needed) or Dapagliflozin 10 mg daily."
    )

    # 8. Workflow Diagram
    add_h1(doc, "8. Clinical Workflow Diagram")
    doc.add_paragraph(
        "The overall study execution pathway—from participant screening through longitudinal follow-up and final endpoint analysis—is "
        "illustrated in Figure 1."
    )
    flowchart_path = os.path.join(BASE_DIR, 'assets', 'figures', 'week3_study_flowchart.png')
    if os.path.exists(flowchart_path):
        doc.add_picture(flowchart_path, width=Inches(5.5))
        p_cap = doc.add_paragraph()
        p_cap.paragraph_format.space_before = Pt(4)
        p_cap.paragraph_format.space_after = Pt(12)
        r_cap = p_cap.add_run("Figure 1. Operational workflow and milestone progression of the prospective active-surveillance cohort simulation.")
        r_cap.font.name = 'Times New Roman'
        r_cap.font.size = Pt(9.5)
        r_cap.font.italic = True
        r_cap.font.color.rgb = CHARCOAL

    # 9. Measurement Instruments
    add_h1(doc, "9. Data Collection and Measurement Instruments")
    doc.add_paragraph(
        "Psychometric evaluations occur at Baseline, Month 3, Month 6, Month 9, and Month 12 via a centralized, 21 CFR Part 11-compliant "
        "Electronic Data Capture (EDC) platform:\n"
        "• Patient Health Questionnaire-9 (PHQ-9): Assesses depression severity. A validated score >= 15 represents moderate-to-severe depression.\n"
        "• Columbia-Suicide Severity Rating Scale (C-SSRS): Gold-standard instrument tracking suicidal ideation and behavior. Any endorsement "
        "of active ideation with intent (Level 4–5) or preparatory behaviors triggers emergency stopping and clinical intervention.\n"
        "• Generalized Anxiety Disorder 7-item (GAD-7): Tracks secondary affective symptoms.\n"
        "• Adjudication Committee: All primary endpoint triggers are independently reviewed by a blinded panel of two board-certified psychiatrists."
    )

    # 10. Safety and Ethics
    add_h1(doc, "10. Safety Monitoring, Crisis Escalation, and DSMB Oversight")
    doc.add_paragraph(
        "Participant safety is prioritized above all study objectives. The protocol enforces automated electronic alerts: if a participant "
        "scores >= 2 on PHQ-9 Item 9 (thoughts of death or self-harm) or endorses C-SSRS Level 3 or higher, the system instantly notifies the "
        "on-call trial psychiatrist, locks electronic survey administration, and initiates a mandatory clinical evaluation within 2 hours. "
        "An independent Data Safety Monitoring Board (DSMB) reviews unblinded safety data every 3 months. Pre-specified stopping rules dictate "
        "trial termination if the semaglutide arm demonstrates an interim Hazard Ratio > 2.5 with p < 0.001 for suicide-related endpoints."
    )

    # 11. Statistical Analysis Plan
    add_h1(doc, "11. Statistical Analysis Plan (SAP)")
    doc.add_paragraph(
        "The primary analysis follows the Intention-to-Treat (ITT) principle, complemented by an on-treatment per-protocol sensitivity analysis. "
        "Time-to-event outcomes are modeled using Kaplan-Meier survival curves with two-sided log-rank tests. Multivariable Cox proportional "
        "hazards regression will estimate the Hazard Ratio (HR) and 95% confidence intervals, adjusting for baseline PHQ-9, age, sex, BMI, and "
        "baseline antidepressant use. To minimize residual selection bias, 1:1 propensity score matching (caliper 0.2 SD of logit) will be performed "
        "as a secondary robustness verification."
    )

    # 12. References
    add_h1(doc, "12. References (APA 7th Edition)")
    references = [
        "American Diabetes Association. (2024). Standards of Care in Diabetes—2024. Diabetes Care, 47(Suppl. 1), S1-S343.",
        "Food and Drug Administration. (2020). Enhancing the Diversity of Clinical Trial Populations — Eligibility Criteria, Enrollment Practices, and Trial Designs Guidance for Industry. U.S. FDA.",
        "Khouri, C., et al. (2024). The REporting of A Disproportionality Analysis for DrUg Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV). Drug Safety, 47(6), 541-558.",
        "Kroenke, K., Spitzer, R. L., & Williams, J. B. (2001). The PHQ-9: validity of a brief depression severity measure. Journal of General Internal Medicine, 16(9), 606-613.",
        "Posner, K., et al. (2011). The Columbia-Suicide Severity Rating Scale: initial validity and internal consistency findings from three multisite studies with adolescents and adults. American Journal of Psychiatry, 168(12), 1266-1277.",
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
    out_dir = os.path.join(BASE_DIR, 'reports', 'week3')
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'week3_experimental_design.docx')
    doc.save(out_file)
    print(f"Report saved successfully to {out_file}")

    sub_dir = os.path.join(BASE_DIR, 'submission', 'week3')
    os.makedirs(sub_dir, exist_ok=True)
    sub_file = os.path.join(sub_dir, 'week3_experimental_design.docx')
    shutil.copy(out_file, sub_file)
    print(f"Copied to submission directory: {sub_file}")

if __name__ == "__main__":
    generate_week3_report()
