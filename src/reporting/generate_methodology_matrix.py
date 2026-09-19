import os
import pandas as pd
from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter

def generate_matrix():
    data = [
        {
            "Methodological_Component": "Research Question",
            "Published_Study_Approach": "STEP 1 had clear PICO",
            "Best_Practice_Expectation": "Specific measurable question",
            "Assessment_Observation": "Meets standard but focus is efficacy over safety",
            "Potential_Improvement": "Explicit incorporation of psychiatric safety as primary/secondary objective"
        },
        {
            "Methodological_Component": "Study Design",
            "Published_Study_Approach": "RCT double-blind placebo-controlled",
            "Best_Practice_Expectation": "Appropriate for objective",
            "Assessment_Observation": "Meets gold standard but no active comparator",
            "Potential_Improvement": "Inclusion of active comparator (e.g., Liraglutide) to benchmark safety"
        },
        {
            "Methodological_Component": "Sample Size",
            "Published_Study_Approach": "N=1,961 (2:1)",
            "Best_Practice_Expectation": "Adequate power calculation",
            "Assessment_Observation": "Adequate for primary but limited for rare ADRs (Rule of Three)",
            "Potential_Improvement": "Larger pooled safety cohorts or post-market pharmacovigilance for rare AEs"
        },
        {
            "Methodological_Component": "Sample Selection",
            "Published_Study_Approach": "BMI>=30 or >=27 with comorbidity, no diabetes",
            "Best_Practice_Expectation": "Representative",
            "Assessment_Observation": "Excludes diabetes and psychiatric conditions",
            "Potential_Improvement": "More inclusive criteria to evaluate real-world psychiatric safety profile"
        },
        {
            "Methodological_Component": "Controls",
            "Published_Study_Approach": "Placebo + lifestyle intervention",
            "Best_Practice_Expectation": "Appropriate comparator",
            "Assessment_Observation": "No active comparator limits safety comparison",
            "Potential_Improvement": "Use active comparator like Bupropion/Naltrexone"
        },
        {
            "Methodological_Component": "Randomization",
            "Published_Study_Approach": "2:1 IWRS stratified",
            "Best_Practice_Expectation": "Adequate concealment",
            "Assessment_Observation": "Meets standard",
            "Potential_Improvement": "None required, methodology is robust"
        },
        {
            "Methodological_Component": "Blinding",
            "Published_Study_Approach": "Double-blind matching placebo",
            "Best_Practice_Expectation": "Adequate masking",
            "Assessment_Observation": "Risk of functional unblinding via GI side effects",
            "Potential_Improvement": "Active placebo to mimic side effect profile"
        },
        {
            "Methodological_Component": "Variables",
            "Published_Study_Approach": "Body weight %, >=5% threshold",
            "Best_Practice_Expectation": "Clearly operationalized",
            "Assessment_Observation": "Well-defined but psychiatric outcomes not primary",
            "Potential_Improvement": "Include validated psychiatric AE screening variables"
        },
        {
            "Methodological_Component": "Measurements",
            "Published_Study_Approach": "Body weight, waist circumference, biomarkers",
            "Best_Practice_Expectation": "Validated reliable instruments",
            "Assessment_Observation": "Objective measures but psychiatric assessment tools not used",
            "Potential_Improvement": "Incorporate standardized psychiatric screening tools for all participants"
        },
        {
            "Methodological_Component": "Data Collection",
            "Published_Study_Approach": "eCRF, 68 weeks, regular visits",
            "Best_Practice_Expectation": "Standardized protocol",
            "Assessment_Observation": "Comprehensive but short for chronic therapy",
            "Potential_Improvement": "Longer follow-up periods (e.g., 2-5 years) for chronic AEs"
        },
        {
            "Methodological_Component": "Statistical Analysis",
            "Published_Study_Approach": "MMRM, pattern-mixture MI, dual estimands",
            "Best_Practice_Expectation": "Pre-specified SAP",
            "Assessment_Observation": "Sophisticated, appropriate, CONSORT-compliant",
            "Potential_Improvement": "Time-to-event analysis for adverse events"
        },
        {
            "Methodological_Component": "Reproducibility",
            "Published_Study_Approach": "NCT03548935 registered, protocol available",
            "Best_Practice_Expectation": "Pre-registration + data sharing",
            "Assessment_Observation": "Protocol available but individual data not public",
            "Potential_Improvement": "Open data sharing of de-identified patient-level data"
        },
        {
            "Methodological_Component": "Ethical Considerations",
            "Published_Study_Approach": "IRB/IEC approval, informed consent, DSMB",
            "Best_Practice_Expectation": "Full ethical compliance",
            "Assessment_Observation": "Meets standard; industry sponsorship disclosed",
            "Potential_Improvement": "Independent academic steering committee for data analysis"
        },
        {
            "Methodological_Component": "Reporting Transparency",
            "Published_Study_Approach": "CONSORT, NEJM standards",
            "Best_Practice_Expectation": "Complete transparent reporting",
            "Assessment_Observation": "High quality reporting but psychiatric AE details limited",
            "Potential_Improvement": "Detailed granular reporting of all neuropsychiatric AEs"
        }
    ]

    df = pd.DataFrame(data)

    base_dir = r"c:\Users\ARYAN - AYUSH\OneDrive\Desktop\an intership\pharmaceutical_research_portfolio"
    out_dir = os.path.join(base_dir, "week4_critical_evaluation")
    os.makedirs(out_dir, exist_ok=True)

    csv_path = os.path.join(out_dir, "methodology_matrix.csv")
    xlsx_path = os.path.join(out_dir, "methodology_matrix.xlsx")

    df.to_csv(csv_path, index=False)

    # Excel formatting
    with pd.ExcelWriter(xlsx_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Methodology Matrix')
        workbook = writer.book
        worksheet = writer.sheets['Methodology Matrix']
        
        # Format headers
        for cell in worksheet[1]:
            cell.font = Font(bold=True)
            
        # Freeze pane
        worksheet.freeze_panes = 'A2'
        
        # Word wrap and column widths
        for col_idx, col in enumerate(worksheet.columns, 1):
            col_letter = get_column_letter(col_idx)
            worksheet.column_dimensions[col_letter].width = 35
            for cell in col:
                cell.alignment = Alignment(wrap_text=True, vertical='top')
                
    print(f"Successfully generated files in {out_dir}")

if __name__ == '__main__':
    generate_matrix()
