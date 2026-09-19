import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_flowchart():
    print("Generating Week 3 Experimental Workflow Diagram...")
    fig, ax = plt.subplots(figsize=(10, 14), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis('off')

    stages = [
        ("1. Research Question", "Does Semaglutide elevate new-onset psychiatric incidence vs SGLT2i?", "#1F497D"),
        ("2. Scientific Hypotheses", "Null (H0: HR=1.0) vs. Alternative (H1: HR>1.0 in active cohort)", "#2E5B88"),
        ("3. Study Design Framework", "Prospective Active-Surveillance Cohort Study (12-Month Multi-Center)", "#366092"),
        ("4. Target Population & Sample", "Adults (N=2,000; 1,000 per arm) initiating GLP-1 RA or SGLT2i", "#41729F"),
        ("5. Arm Allocation & Matching", "Semaglutide 0.25-2.4mg vs SGLT2i (Empa/Dapa) with Propensity Matching", "#588BAE"),
        ("6. Active Clinical Intervention", "Standardized Dose Escalation + Lifestyle Counseling Protocol", "#6C9BC2"),
        ("7. Multi-Dimensional Measurement", "Baseline, M3, M6, M9, M12: PHQ-9, C-SSRS, GAD-7 & Biomarkers", "#4682B4"),
        ("8. Rigorous Data Collection", "Centralized Electronic Data Capture (EDC) & Masked Reviewers", "#3A75C4"),
        ("9. Quality Control & Safety Gates", "Independent DSMB, Pre-specified Stopping Rules & Crisis Referral", "#206095"),
        ("10. Statistical Analysis Plan", "Kaplan-Meier Survival, Cox Proportional Hazards & Sensitivity Tests", "#1A4D75"),
        ("11. Clinical & Regulatory Interpretation", "Translational Evidence Synthesis for Patient Safety & Guidelines", "#0F324D")
    ]

    box_width = 7.4
    box_height = 0.8
    x_start = 1.3

    for i, (title, desc, color) in enumerate(stages):
        y = 13.0 - (i * 1.18)
        
        # Draw box
        rect = patches.FancyBboxPatch(
            (x_start, y - box_height/2), box_width, box_height,
            boxstyle="round,pad=0.15,rounding_size=0.2",
            ec=color, fc=color, alpha=0.95
        )
        ax.add_patch(rect)
        
        # Add text
        ax.text(x_start + 0.3, y + 0.12, title, fontsize=11, fontweight='bold', color='white', va='center')
        ax.text(x_start + 0.3, y - 0.18, desc, fontsize=9, fontstyle='italic', color='#EAECEE', va='center')

        # Draw connecting arrow to next box
        if i < len(stages) - 1:
            next_y = 13.0 - ((i + 1) * 1.18)
            ax.annotate(
                '', xy=(5.0, next_y + box_height/2), xytext=(5.0, y - box_height/2),
                arrowprops=dict(arrowstyle="-|>", color='#1F497D', lw=2.0, mutation_scale=15)
            )

    plt.title("Figure 1. Experimental Protocol Workflow Diagram\nSimulated Prospective Cohort Active Surveillance Study (N=2,000)", 
              fontsize=13, fontweight='bold', color='#1F497D', pad=15)

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    out_paths = [
        os.path.join(BASE_DIR, 'assets', 'figures', 'week3_study_flowchart.png'),
        os.path.join(BASE_DIR, 'week3_experimental_design', 'flowchart.png')
    ]
    for p in out_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        plt.savefig(p, bbox_inches='tight', dpi=300)
        print(f"Flowchart saved to: {p}")
    plt.close()

if __name__ == "__main__":
    draw_flowchart()
