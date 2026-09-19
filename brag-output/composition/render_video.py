import os
import sys
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTPUT_DIR = os.path.join(BASE_DIR, "brag-output")
ASSETS_DIR = os.path.join(OUTPUT_DIR, "assets")

WIDTH = 1920
HEIGHT = 1080
FPS = 30
DURATION_SEC = 20
TOTAL_FRAMES = FPS * DURATION_SEC  # 600 frames

# Load Fonts
def get_fonts():
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 64)
        subtitle_font = ImageFont.truetype("arial.ttf", 34)
        stat_font = ImageFont.truetype("arialbd.ttf", 46)
        tag_font = ImageFont.truetype("arialbd.ttf", 26)
        small_font = ImageFont.truetype("arial.ttf", 22)
    except Exception:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        stat_font = ImageFont.load_default()
        tag_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    return title_font, subtitle_font, stat_font, tag_font, small_font

title_font, subtitle_font, stat_font, tag_font, small_font = get_fonts()

# Load Images
img_lab = Image.open(os.path.join(ASSETS_DIR, "semaglutide_molecular_lab.jpg")).convert("RGB").resize((WIDTH, HEIGHT))
img_data = Image.open(os.path.join(ASSETS_DIR, "pharmacovigilance_data_center.jpg")).convert("RGB").resize((WIDTH, HEIGHT))
img_trial = Image.open(os.path.join(ASSETS_DIR, "clinical_trial_simulation.jpg")).convert("RGB").resize((WIDTH, HEIGHT))

forest_path = os.path.join(BASE_DIR, "week2_data_analysis", "results", "figures", "fig3_forest_plot.png")
img_forest = Image.open(forest_path).convert("RGB") if os.path.exists(forest_path) else None

heatmap_path = os.path.join(BASE_DIR, "week2_data_analysis", "results", "figures", "fig7_signal_heatmap.png")
img_heatmap = Image.open(heatmap_path).convert("RGB") if os.path.exists(heatmap_path) else None

flowchart_path = os.path.join(BASE_DIR, "assets", "figures", "week3_study_flowchart.png")
img_flowchart = Image.open(flowchart_path).convert("RGB") if os.path.exists(flowchart_path) else None

def draw_pill(draw, x, y, w, h, text, bg_color=(0, 229, 255, 200), text_color=(11, 17, 32)):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=h//2, fill=bg_color)
    bbox = tag_font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((x + (w - tw)//2, y + (h - th)//2 - 2), text, font=tag_font, fill=text_color)

def draw_glass_card(draw, x, y, w, h, bg_color=(11, 17, 32, 210), border_color=(0, 229, 255, 120)):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=16, fill=bg_color, outline=border_color, width=2)

def make_scene_1(frame_idx, n_frames):
    """Scene 1: The Hook (0.0s - 3.5s) - Molecular Lab, The Paradox"""
    progress = frame_idx / n_frames
    zoom = 1.0 + 0.08 * progress
    w_z = int(WIDTH * zoom)
    h_z = int(HEIGHT * zoom)
    frame = img_lab.resize((w_z, h_z), Image.Resampling.BILINEAR)
    # Center crop back to 1920x1080
    left = (w_z - WIDTH) // 2
    top = (h_z - HEIGHT) // 2
    frame = frame.crop((left, top, left + WIDTH, top + HEIGHT))

    # Dark gradient overlay
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    odraw.rectangle([0, 0, WIDTH, HEIGHT], fill=(11, 17, 32, int(110 + 60 * np.sin(progress * np.pi))))

    # Glass header banner
    draw_glass_card(odraw, 80, 80, 520, 50, (0, 229, 255, 40), (0, 229, 255, 180))
    odraw.text((105, 92), "PHARMACEUTICAL RESEARCH PORTFOLIO", font=tag_font, fill=(0, 229, 255))

    # Center dramatic card
    draw_glass_card(odraw, 80, 680, 1200, 310, (11, 17, 32, 225), (0, 229, 255, 150))
    odraw.text((120, 710), "DOES SEMAGLUTIDE CAUSE DEPRESSION?", font=title_font, fill=(255, 255, 255))
    odraw.text((120, 800), "A $100B GLP-1 RA drug class. An emerging post-marketing safety paradox.", font=subtitle_font, fill=(0, 229, 255))
    odraw.text((120, 860), "Investigating psychiatric adverse events in FDA FAERS big data (2018-2025).", font=subtitle_font, fill=(203, 213, 225))
    
    # Bottom tech indicator
    draw_pill(odraw, 120, 925, 280, 42, "FDA FAERS COHORT", (0, 229, 255, 220), (11, 17, 32))
    draw_pill(odraw, 420, 925, 300, 42, "DISPROPORTIONALITY", (255, 0, 85, 220), (255, 255, 255))

    frame = Image.alpha_composite(frame.convert("RGBA"), overlay)
    return frame.convert("RGB")

def make_scene_2(frame_idx, n_frames):
    """Scene 2: Big Data Mining (3.5s - 7.5s) - 148,178 Records Mined"""
    progress = frame_idx / n_frames
    zoom = 1.0 + 0.06 * progress
    w_z = int(WIDTH * zoom)
    h_z = int(HEIGHT * zoom)
    frame = img_data.resize((w_z, h_z), Image.Resampling.BILINEAR)
    left = (w_z - WIDTH) // 2
    top = (h_z - HEIGHT) // 2
    frame = frame.crop((left, top, left + WIDTH, top + HEIGHT))

    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    odraw.rectangle([0, 0, WIDTH, HEIGHT], fill=(11, 17, 32, 130))

    # Top banner
    draw_glass_card(odraw, 80, 80, 780, 54, (0, 229, 255, 40), (0, 229, 255, 180))
    odraw.text((105, 93), "STAGE 2: OPENFDA BIG DATA MINING PIPELINE", font=tag_font, fill=(0, 229, 255))

    # Stat Card 1: Semaglutide
    draw_glass_card(odraw, 80, 240, 540, 220, (11, 17, 32, 230), (0, 229, 255, 160))
    odraw.text((110, 265), "SEMAGLUTIDE (GLP-1 RA)", font=tag_font, fill=(0, 229, 255))
    count_sema = int(100912 * min(1.0, progress * 1.5))
    odraw.text((110, 310), f"{count_sema:,}", font=title_font, fill=(255, 255, 255))
    odraw.text((110, 395), "Primary Suspect Adverse Event Reports", font=small_font, fill=(148, 163, 184))

    # Stat Card 2: SGLT2i
    draw_glass_card(odraw, 660, 240, 540, 220, (11, 17, 32, 230), (16, 185, 129, 160))
    odraw.text((690, 265), "ACTIVE SGLT2i COMPARATORS", font=tag_font, fill=(16, 185, 129))
    count_sglt = int(47266 * min(1.0, progress * 1.5))
    odraw.text((690, 310), f"{count_sglt:,}", font=title_font, fill=(255, 255, 255))
    odraw.text((690, 395), "Empagliflozin, Dapagliflozin, Canagliflozin", font=small_font, fill=(148, 163, 184))

    # Bottom summary card
    draw_glass_card(odraw, 80, 720, 1120, 260, (11, 17, 32, 235), (0, 229, 255, 180))
    odraw.text((110, 745), "TOTAL ADVERSE EVENT REPORTS: 148,178", font=stat_font, fill=(255, 255, 255))
    odraw.text((110, 820), "Active comparator control eliminates diabetes/obesity baseline confounding.", font=subtitle_font, fill=(0, 229, 255))
    odraw.text((110, 875), "Mined via automated OpenFDA API & processed through Python data cleaning.", font=subtitle_font, fill=(203, 213, 225))

    frame = Image.alpha_composite(frame.convert("RGBA"), overlay)
    return frame.convert("RGB")

def make_scene_3(frame_idx, n_frames):
    """Scene 3: Empirical Signal Detection (7.5s - 11.5s) - Forest Plot & Heatmap"""
    progress = frame_idx / n_frames
    
    bg = Image.new("RGB", (WIDTH, HEIGHT), (11, 17, 32))
    bdraw = ImageDraw.Draw(bg)

    # Place Forest Plot on left
    if img_forest:
        fp_w = 900
        fp_h = int(img_forest.height * (fp_w / img_forest.width))
        fp_resized = img_forest.resize((fp_w, min(fp_h, 850)), Image.Resampling.BILINEAR)
        bg.paste(fp_resized, (70, 150))

    # Place Heatmap on right
    if img_heatmap:
        hm_w = 840
        hm_h = int(img_heatmap.height * (hm_w / img_heatmap.width))
        hm_resized = img_heatmap.resize((hm_w, min(hm_h, 480)), Image.Resampling.BILINEAR)
        bg.paste(hm_resized, (1010, 150))

    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    # Top Header
    draw_glass_card(odraw, 70, 50, 920, 54, (255, 0, 85, 50), (255, 0, 85, 200))
    odraw.text((95, 63), "STAGE 4: DISPROPORTIONALITY SIGNAL DETECTION (ROR / PRR / CHI-SQUARE)", font=tag_font, fill=(255, 80, 130))

    # Right Bottom Signal Highlight Card
    draw_glass_card(odraw, 1010, 660, 840, 340, (11, 17, 32, 240), (0, 229, 255, 200))
    odraw.text((1040, 685), "KEY SAFETY SIGNALS IDENTIFIED", font=stat_font, fill=(255, 255, 255))
    odraw.text((1040, 755), "* Suicidal Ideation: ROR = 2.61 (95% CI: 2.18-3.12, p = 3.98e-27)", font=subtitle_font, fill=(255, 80, 120))
    odraw.text((1040, 805), "* Panic Attack: ROR = 4.40 (95% CI: 2.96-6.54, p = 2.13e-15)", font=subtitle_font, fill=(255, 80, 120))
    odraw.text((1040, 855), "* Depressed Mood: ROR = 2.11 (95% CI: 1.72-2.58, p = 1.78e-13)", font=subtitle_font, fill=(0, 229, 255))
    odraw.text((1040, 920), "Twist: Suicide Attempt is INVERSE (ROR = 0.67) - Notoriety bias exposed!", font=tag_font, fill=(16, 185, 129))

    bg = Image.alpha_composite(bg.convert("RGBA"), overlay)
    return bg.convert("RGB")

def make_scene_4(frame_idx, n_frames):
    """Scene 4: Trial Autopsy & Active Surveillance Simulation (11.5s - 15.5s)"""
    progress = frame_idx / n_frames
    zoom = 1.0 + 0.05 * progress
    w_z = int(WIDTH * zoom)
    h_z = int(HEIGHT * zoom)
    frame = img_trial.resize((w_z, h_z), Image.Resampling.BILINEAR)
    left = (w_z - WIDTH) // 2
    top = (h_z - HEIGHT) // 2
    frame = frame.crop((left, top, left + WIDTH, top + HEIGHT))

    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    odraw.rectangle([0, 0, WIDTH, HEIGHT], fill=(11, 17, 32, 140))

    # Top Header
    draw_glass_card(odraw, 80, 60, 960, 54, (0, 229, 255, 40), (0, 229, 255, 180))
    odraw.text((105, 73), "STAGE 11-16: STEP 1 TRIAL CRITIQUE & CLINICAL SIMULATION", font=tag_font, fill=(0, 229, 255))

    # Left: Trial Critique Card
    draw_glass_card(odraw, 80, 160, 840, 480, (11, 17, 32, 230), (255, 0, 85, 160))
    odraw.text((110, 190), "WHY DID CLINICAL TRIALS MISS IT?", font=stat_font, fill=(255, 255, 255))
    odraw.text((110, 260), "Critical appraisal of landmark STEP 1 trial (NEJM 2021):", font=subtitle_font, fill=(0, 229, 255))
    odraw.text((110, 320), "1. Restrictive Eligibility Criteria", font=tag_font, fill=(255, 80, 120))
    odraw.text((140, 360), "Excluded patients with PHQ-9 >= 15 or suicidal history.", font=small_font, fill=(203, 213, 225))
    odraw.text((110, 410), "2. Passive Adverse Event Reporting", font=tag_font, fill=(255, 80, 120))
    odraw.text((140, 450), "No mandatory psychometric scales during 68-week trial.", font=small_font, fill=(203, 213, 225))
    odraw.text((110, 500), "3. Statistical Power Limits", font=tag_font, fill=(255, 80, 120))
    odraw.text((140, 540), "Rule of 3: Underpowered for adverse events < 0.2% frequency.", font=small_font, fill=(203, 213, 225))

    # Right: Active Surveillance Solution Card
    draw_glass_card(odraw, 960, 160, 880, 480, (11, 17, 32, 230), (16, 185, 129, 160))
    odraw.text((990, 190), "PROSPECTIVE SURVEILLANCE BLUEPRINT", font=stat_font, fill=(255, 255, 255))
    odraw.text((990, 260), "12-Month Active Surveillance Cohort Simulation (N=2,000):", font=subtitle_font, fill=(16, 185, 129))
    odraw.text((990, 320), "* 1,000 Semaglutide vs 1,000 Active SGLT2i Controls", font=tag_font, fill=(255, 255, 255))
    odraw.text((990, 370), "* Validated Psychometrics: PHQ-9, C-SSRS, GAD-7 at 3, 6, 12M", font=tag_font, fill=(255, 255, 255))
    odraw.text((990, 420), "* Independent DSMB Safety Charter with stopping rule (HR > 2.5)", font=tag_font, fill=(255, 255, 255))
    odraw.text((990, 470), "* Automated 2-Hour Electronic Crisis Alert Escalation Pathway", font=tag_font, fill=(0, 229, 255))
    odraw.text((990, 540), "Flowchart rendered at 300 DPI in week3_study_flowchart.png", font=small_font, fill=(148, 163, 184))

    # Bottom Banner
    draw_glass_card(odraw, 80, 680, 1760, 320, (11, 17, 32, 235), (0, 229, 255, 160))
    if img_flowchart:
        fc_thumb = img_flowchart.resize((500, int(img_flowchart.height * (500 / img_flowchart.width))), Image.Resampling.BILINEAR)
        frame.paste(fc_thumb, (1280, 700))
    odraw.text((110, 710), "STUDY FLOWCHART: COMPLETE ACTIVE SURVEILLANCE LIFECYCLE", font=stat_font, fill=(255, 255, 255))
    odraw.text((110, 775), "Simulated protocol bridges spontaneous FAERS disproportionality to prospective clinical trials.", font=subtitle_font, fill=(0, 229, 255))
    odraw.text((110, 830), "Complete with Belmont Report ethical standards and DSMB stopping charter.", font=subtitle_font, fill=(203, 213, 225))
    draw_pill(odraw, 110, 905, 340, 44, "N=2,000 ACTIVE COHORT", (16, 185, 129, 220), (11, 17, 32))
    draw_pill(odraw, 480, 905, 360, 44, "ICH-E6 GCP COMPLIANT", (0, 229, 255, 220), (11, 17, 32))

    frame = Image.alpha_composite(frame.convert("RGBA"), overlay)
    return frame.convert("RGB")

def make_scene_5(frame_idx, n_frames):
    """Scene 5: Master Portfolio & Outro (15.5s - 20.0s)"""
    progress = frame_idx / n_frames
    
    bg = Image.new("RGB", (WIDTH, HEIGHT), (11, 17, 32))
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    # Background ambient glow circles
    odraw.ellipse([-200, -200, 600, 600], fill=(0, 229, 255, 25))
    odraw.ellipse([1400, 500, 2200, 1300], fill=(255, 0, 85, 25))

    # Main Headline Card
    draw_glass_card(odraw, 120, 100, 1680, 220, (15, 23, 42, 230), (0, 229, 255, 200))
    odraw.text((160, 130), "PHARMACEUTICAL RESEARCH ASSISTANT PORTFOLIO", font=title_font, fill=(255, 255, 255))
    odraw.text((160, 225), "Post-Marketing Pharmacovigilance, Experimental Simulation & Methodological Appraisal", font=subtitle_font, fill=(0, 229, 255))

    # Deliverables Grid
    cards = [
        ("WEEK 1", "Literature Review", "17 Verified Studies (APA 7th)", (0, 229, 255)),
        ("WEEK 2", "FAERS Big Data", "148K Records • 8 Figures", (255, 0, 85)),
        ("WEEK 3", "Trial Simulation", "N=2,000 Cohort Flowchart", (16, 185, 129)),
        ("WEEK 4", "STEP 1 Critique", "13-Item CONSORT Matrix", (234, 179, 8)),
        ("FINAL", "Master Synthesis", "5 DOCX • 100% QA Passed", (168, 85, 247)),
    ]
    card_w = 310
    start_x = 120
    for idx, (w_tag, title, desc, col) in enumerate(cards):
        cx = start_x + idx * (card_w + 32)
        draw_glass_card(odraw, cx, 360, card_w, 240, (15, 23, 42, 230), (*col, 160))
        draw_pill(odraw, cx + 20, 385, 120, 36, w_tag, (*col, 220), (11, 17, 32))
        odraw.text((cx + 20, 440), title, font=tag_font, fill=(255, 255, 255))
        odraw.text((cx + 20, 490), desc, font=small_font, fill=(203, 213, 225))

    # Bottom Call to Action Card
    draw_glass_card(odraw, 120, 650, 1680, 350, (15, 23, 42, 240), (0, 229, 255, 220))
    odraw.text((160, 680), "100% REPRODUCIBLE • OPEN SOURCE RESEARCH", font=stat_font, fill=(255, 255, 255))
    odraw.text((160, 755), "github.com/officialayush5839-arch/Henry-Harvin-intership", font=title_font, fill=(0, 229, 255))
    odraw.text((160, 850), "Built with AntiGravity Enterprise Framework v2.0 • Author: Aryan Ayush", font=subtitle_font, fill=(148, 163, 184))
    draw_pill(odraw, 160, 920, 380, 44, "19 PIPELINE STAGES PASSED", (16, 185, 129, 220), (11, 17, 32))
    draw_pill(odraw, 580, 920, 340, 44, "ZERO FABRICATED CITATIONS", (0, 229, 255, 220), (11, 17, 32))

    bg = Image.alpha_composite(bg.convert("RGBA"), overlay)
    return bg.convert("RGB")

def render():
    print(f"Rendering {TOTAL_FRAMES} frames ({DURATION_SEC}s at {FPS}fps) to brag.mp4...")
    
    mp4_path = os.path.join(OUTPUT_DIR, "brag.mp4")
    jpg_path = os.path.join(OUTPUT_DIR, "brag.jpg")

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(mp4_path, fourcc, FPS, (WIDTH, HEIGHT))

    # Time boundaries
    s1_end = int(3.5 * FPS)
    s2_end = int(7.5 * FPS)
    s3_end = int(11.5 * FPS)
    s4_end = int(15.5 * FPS)
    s5_end = TOTAL_FRAMES

    poster_saved = False

    for f in range(TOTAL_FRAMES):
        if f < s1_end:
            frame_pil = make_scene_1(f, s1_end)
        elif f < s2_end:
            frame_pil = make_scene_2(f - s1_end, s2_end - s1_end)
        elif f < s3_end:
            frame_pil = make_scene_3(f - s2_end, s3_end - s2_end)
        elif f < s4_end:
            frame_pil = make_scene_4(f - s3_end, s4_end - s3_end)
        else:
            frame_pil = make_scene_5(f - s4_end, s5_end - s4_end)

        # Cross-fade transitions (last 10 frames of each scene)
        # Convert PIL to CV2 (BGR)
        frame_cv = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

        # Poster frame is picked around frame 40 (Scene 1 hero frame)
        if f == 40 and not poster_saved:
            frame_pil.save(jpg_path, quality=95)
            poster_saved = True
            print(f"  Saved poster frame to: {jpg_path}")

        out.write(frame_cv)
        if f % 60 == 0:
            print(f"  Rendered {f}/{TOTAL_FRAMES} frames ({f/FPS:.1f}s)...")

    out.release()
    print(f"Video render complete: {mp4_path} ({os.path.getsize(mp4_path) / (1024*1024):.2f} MB)")

if __name__ == "__main__":
    render()
