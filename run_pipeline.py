#!/usr/bin/env python3
"""
==========================================================
  Pharmaceutical Research Portfolio — Master Pipeline Runner
==========================================================
  Executes the full reproducible research pipeline:
    Stage 1: Data Collection  (OpenFDA API → raw CSV)
    Stage 2: Data Cleaning    (raw → processed CSV)
    Stage 3: Descriptive Statistics
    Stage 4: Statistical Tests (ROR, PRR, Chi-square)
    Stage 5: Visualization    (8 publication-quality 300 DPI figures)
    Stage 6: Literature Matrix generation
    Stage 7: Methodology Matrix generation
    Stage 8: Flowchart generation
    Stage 9: Jupyter Notebook generation
    Stage 10: Week 1 Word Report
    Stage 11: Week 2 Word Report
    Stage 12: Week 3 Word Report
    Stage 13: Week 4 Word Report
    Stage 14: Final Integrated Portfolio Report
    Stage 15: Markdown companion reports
    Stage 16: Submission packaging
    Stage 17: Checklist updates
    Stage 18: Stage checkpoint generation
    Stage 19: QA Runner (validation suite)
==========================================================
"""

import os
import sys
import time
import traceback

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "src"))
sys.path.insert(0, os.path.join(BASE_DIR, "src", "reporting"))

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# -- Utility ----------------------------------------------
class Colors:
    GREEN  = ""
    RED    = ""
    YELLOW = ""
    CYAN   = ""
    BOLD   = ""
    RESET  = ""

def header(text):
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")

def stage_header(num, title):
    print(f"\n-- Stage {num}: {title} --")

def success(msg):
    print(f"  [OK] {msg}")

def fail(msg):
    print(f"  [FAIL] {msg}")

def info(msg):
    print(f"  -> {msg}")

results = []

def run_stage(num, title, func):
    stage_header(num, title)
    start = time.time()
    try:
        func()
        elapsed = time.time() - start
        success(f"Completed in {elapsed:.1f}s")
        results.append((num, title, "PASS", f"{elapsed:.1f}s"))
    except Exception as e:
        elapsed = time.time() - start
        fail(f"Failed after {elapsed:.1f}s: {e}")
        traceback.print_exc()
        results.append((num, title, "FAIL", str(e)[:60]))

# ── Stage Implementations ────────────────────────────────

def stage_data_collection():
    """Collect FAERS data via OpenFDA API."""
    script = os.path.join(BASE_DIR, "week2_data_analysis", "scripts", "data_collection.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    raw_csv = os.path.join(BASE_DIR, "week2_data_analysis", "data", "raw", "raw_faers_data.csv")
    assert os.path.exists(raw_csv), "raw_faers_data.csv not found"
    import pandas as pd
    df = pd.read_csv(raw_csv)
    info(f"Raw dataset: {len(df)} rows, {len(df.columns)} columns")

def stage_data_cleaning():
    """Clean and process the raw FAERS data."""
    script = os.path.join(BASE_DIR, "week2_data_analysis", "scripts", "data_cleaning.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    processed = os.path.join(BASE_DIR, "week2_data_analysis", "data", "processed", "processed_faers_data.csv")
    assert os.path.exists(processed), "processed_faers_data.csv not found"
    import pandas as pd
    df = pd.read_csv(processed)
    info(f"Processed dataset: {len(df)} rows")

def stage_descriptive_stats():
    """Compute descriptive statistics."""
    script = os.path.join(BASE_DIR, "week2_data_analysis", "scripts", "descriptive_statistics.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    summary_csv = os.path.join(BASE_DIR, "week2_data_analysis", "results", "tables", "overall_summary.csv")
    assert os.path.exists(summary_csv), "overall_summary.csv not found"
    info("Descriptive statistics tables generated")

def stage_statistical_tests():
    """Run disproportionality analysis: ROR, PRR, Chi-square."""
    script = os.path.join(BASE_DIR, "week2_data_analysis", "scripts", "statistical_tests.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    results_csv = os.path.join(BASE_DIR, "week2_data_analysis", "results", "statistical_results", "disproportionality_results.csv")
    assert os.path.exists(results_csv), "disproportionality_results.csv not found"
    import pandas as pd
    df = pd.read_csv(results_csv)
    info(f"Disproportionality results: {len(df)} ADR categories analyzed")
    signals = df[df.get('signal_detected', df.columns[-1]) == True] if 'signal_detected' in df.columns else df
    info(f"Signal detection complete")

def stage_visualization():
    """Generate 8 publication-quality 300 DPI figures."""
    script = os.path.join(BASE_DIR, "week2_data_analysis", "scripts", "visualization.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    fig_dir = os.path.join(BASE_DIR, "week2_data_analysis", "results", "figures")
    figs = [f for f in os.listdir(fig_dir) if f.endswith('.png')]
    assert len(figs) >= 8, f"Expected >= 8 figures, found {len(figs)}"
    info(f"Generated {len(figs)} figures at 300 DPI")

def stage_literature_matrix():
    """Generate literature matrix (CSV + XLSX)."""
    script = os.path.join(BASE_DIR, "src", "reporting", "generate_literature_matrix.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    csv_f = os.path.join(BASE_DIR, "week1_literature_review", "literature_matrix.csv")
    xlsx_f = os.path.join(BASE_DIR, "week1_literature_review", "literature_matrix.xlsx")
    assert os.path.exists(csv_f) and os.path.exists(xlsx_f), "Literature matrix files missing"
    info("Literature matrix (CSV + XLSX) generated")

def stage_methodology_matrix():
    """Generate methodology comparison matrix (CSV + XLSX)."""
    script = os.path.join(BASE_DIR, "src", "reporting", "generate_methodology_matrix.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    csv_f = os.path.join(BASE_DIR, "week4_critical_evaluation", "methodology_matrix.csv")
    xlsx_f = os.path.join(BASE_DIR, "week4_critical_evaluation", "methodology_matrix.xlsx")
    assert os.path.exists(csv_f) and os.path.exists(xlsx_f), "Methodology matrix files missing"
    info("Methodology matrix (CSV + XLSX) generated")

def stage_flowchart():
    """Generate study protocol flowchart (300 DPI PNG)."""
    script = os.path.join(BASE_DIR, "src", "reporting", "generate_flowchart.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    fc = os.path.join(BASE_DIR, "assets", "figures", "week3_study_flowchart.png")
    assert os.path.exists(fc), "Flowchart not found"
    info("Study flowchart generated at 300 DPI")

def stage_notebook():
    """Generate Jupyter Notebook."""
    script = os.path.join(BASE_DIR, "src", "reporting", "generate_notebook.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    nb = os.path.join(BASE_DIR, "week2_data_analysis", "notebooks", "pharmaceutical_data_analysis.ipynb")
    assert os.path.exists(nb), "Notebook not found"
    info("Jupyter Notebook generated")

def stage_week1_report():
    """Generate Week 1 Literature Review Word report."""
    script = os.path.join(BASE_DIR, "src", "reporting", "generate_week1_report.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    docx_f = os.path.join(BASE_DIR, "reports", "week1", "week1_literature_review.docx")
    assert os.path.exists(docx_f), "Week 1 report not found"
    info(f"Week 1 report: {os.path.getsize(docx_f) / 1024:.1f} KB")

def stage_week2_report():
    """Generate Week 2 Data Analysis Word report."""
    script = os.path.join(BASE_DIR, "src", "reporting", "generate_week2_report.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    docx_f = os.path.join(BASE_DIR, "reports", "week2", "week2_data_analysis.docx")
    assert os.path.exists(docx_f), "Week 2 report not found"
    info(f"Week 2 report: {os.path.getsize(docx_f) / 1024:.1f} KB")

def stage_week3_report():
    """Generate Week 3 Experimental Design Word report."""
    script = os.path.join(BASE_DIR, "src", "reporting", "generate_week3_report.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    docx_f = os.path.join(BASE_DIR, "reports", "week3", "week3_experimental_design.docx")
    assert os.path.exists(docx_f), "Week 3 report not found"
    info(f"Week 3 report: {os.path.getsize(docx_f) / 1024:.1f} KB")

def stage_week4_report():
    """Generate Week 4 Critical Evaluation Word report."""
    script = os.path.join(BASE_DIR, "src", "reporting", "generate_week4_report.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    docx_f = os.path.join(BASE_DIR, "reports", "week4", "week4_critical_evaluation.docx")
    assert os.path.exists(docx_f), "Week 4 report not found"
    info(f"Week 4 report: {os.path.getsize(docx_f) / 1024:.1f} KB")

def stage_final_portfolio():
    """Generate Final Integrated Research Portfolio."""
    script = os.path.join(BASE_DIR, "src", "reporting", "generate_final_portfolio.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    docx_f = os.path.join(BASE_DIR, "reports", "final", "final_integrated_research_portfolio.docx")
    assert os.path.exists(docx_f), "Final portfolio report not found"
    info(f"Final portfolio: {os.path.getsize(docx_f) / 1024:.1f} KB")

def stage_markdown_reports():
    """Generate Markdown companion reports."""
    script = os.path.join(BASE_DIR, "src", "reporting", "generate_markdown_reports.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    info("Markdown companion reports generated")

def stage_submission_packaging():
    """Package submission directories."""
    script = os.path.join(BASE_DIR, "src", "reporting", "package_submissions.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    for week in ["week1", "week2", "week3", "week4", "final_portfolio"]:
        sub_dir = os.path.join(BASE_DIR, "submission", week)
        assert os.path.exists(sub_dir), f"submission/{week} missing"
    info("All 5 submission packages assembled")

def stage_checklists():
    """Update submission checklists."""
    script = os.path.join(BASE_DIR, "src", "reporting", "update_checklists.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    info("All 5 submission checklists updated")

def stage_checkpoints():
    """Generate stage checkpoint documents."""
    script = os.path.join(BASE_DIR, "src", "reporting", "generate_checkpoints.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})
    cp_dir = os.path.join(BASE_DIR, "qa", "checkpoints")
    cps = [f for f in os.listdir(cp_dir) if f.startswith("stage_") and f.endswith("_checkpoint.md")]
    info(f"Generated {len(cps)} stage checkpoints")

def stage_qa_runner():
    """Run the full QA validation suite."""
    script = os.path.join(BASE_DIR, "src", "qa_runner.py")
    info(f"Running {os.path.basename(script)} ...")
    exec(open(script, encoding="utf-8").read(), {"__name__": "__run__", "__file__": script})

# ── Main Pipeline ────────────────────────────────────────

def main():
    header("Pharmaceutical Research Portfolio — Full Pipeline Execution")
    
    print(f"  Project: Post-Marketing Pharmacovigilance of Semaglutide")
    print(f"  Author:  Aryan Ayush")
    print(f"  Base:    {BASE_DIR}")
    print()
    
    pipeline_start = time.time()
    
    # ─── Data Pipeline ───
    run_stage(1,  "Data Collection (OpenFDA API)",        stage_data_collection)
    run_stage(2,  "Data Cleaning & Processing",           stage_data_cleaning)
    run_stage(3,  "Descriptive Statistics",                stage_descriptive_stats)
    run_stage(4,  "Statistical Tests (ROR/PRR/Chi²)",     stage_statistical_tests)
    run_stage(5,  "Visualization (8 × 300 DPI figures)",  stage_visualization)
    
    # ─── Matrix & Asset Generation ───
    run_stage(6,  "Literature Matrix (CSV + XLSX)",       stage_literature_matrix)
    run_stage(7,  "Methodology Matrix (CSV + XLSX)",      stage_methodology_matrix)
    run_stage(8,  "Study Protocol Flowchart",             stage_flowchart)
    run_stage(9,  "Jupyter Notebook",                     stage_notebook)
    
    # ─── Word Report Generation ───
    run_stage(10, "Week 1 Report (.docx)",                stage_week1_report)
    run_stage(11, "Week 2 Report (.docx)",                stage_week2_report)
    run_stage(12, "Week 3 Report (.docx)",                stage_week3_report)
    run_stage(13, "Week 4 Report (.docx)",                stage_week4_report)
    run_stage(14, "Final Portfolio Report (.docx)",        stage_final_portfolio)
    
    # ─── Documentation & Packaging ───
    run_stage(15, "Markdown Companion Reports",           stage_markdown_reports)
    run_stage(16, "Submission Packaging",                  stage_submission_packaging)
    run_stage(17, "Submission Checklists",                 stage_checklists)
    run_stage(18, "Stage Checkpoints",                     stage_checkpoints)
    
    # ─── Quality Assurance ───
    run_stage(19, "QA Validation Suite",                   stage_qa_runner)
    
    pipeline_elapsed = time.time() - pipeline_start
    
    # --- Summary ---
    header("Pipeline Execution Summary")
    
    passed = sum(1 for r in results if r[2] == "PASS")
    failed = sum(1 for r in results if r[2] == "FAIL")
    total = len(results)
    
    print(f"  {'Stage':<6} {'Task':<45} {'Status':<8} {'Time/Error'}")
    print(f"  {'-'*6} {'-'*45} {'-'*8} {'-'*30}")
    for num, title, status, detail in results:
        print(f"  {num:<6} {title:<45} {status:<8} {detail}")
    
    print(f"\n  Total: {passed}/{total} PASSED, {failed}/{total} FAILED")
    print(f"  Pipeline completed in {pipeline_elapsed:.1f}s")
    
    if failed == 0:
        print(f"\n  ==========================================")
        print(f"  [OK] ALL PIPELINE STAGES PASSED SUCCESSFULLY")
        print(f"  ==========================================\n")
    else:
        print(f"\n  ==========================================")
        print(f"  [FAIL] {failed} STAGE(S) FAILED - SEE ABOVE")
        print(f"  ==========================================\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
