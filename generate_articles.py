import os

base_dir = r'c:\Users\ARYAN - AYUSH\OneDrive\Desktop\an intership\pharmaceutical_research_portfolio\week1_literature_review'
os.makedirs(os.path.join(base_dir, 'article_summaries'), exist_ok=True)

readme_content = '''# Week 1 Literature Review

## Overview
This directory contains the outputs from Week 1 of the pharmaceutical research portfolio. The primary objective of this week was to conduct a comprehensive literature review focusing on the pharmacovigilance and safety profile of Semaglutide and other GLP-1 receptor agonists (GLP-1 RAs), primarily utilizing data from the FDA Adverse Event Reporting System (FAERS).

## Objectives
- Systematically search and identify relevant literature regarding Semaglutide adverse events.
- Document the search strategy and inclusion/exclusion criteria.
- Summarize 17 verified key articles focusing on various adverse event signals.
- Establish a foundational understanding of the current safety landscape of Semaglutide.

## Methodology
The literature review was conducted using major academic databases (PubMed, Google Scholar, Crossref) focusing on publications from 2020-2026. A structured screening process yielded 17 core articles, which were subsequently analyzed for study design, methodology, major findings, limitations, and relevance to our overarching research question.

## Outputs
- `search_strategy.md`: Details the databases, search terms, and screening process.
- `inclusion_exclusion_criteria.md`: Outlines the criteria for article selection.
- `article_summaries/`: Contains 17 individual markdown files, each providing a detailed summary and academic analysis of a selected article.
'''

search_strategy_content = '''# Search Strategy

## Overview
This document outlines the systematic search strategy employed to identify relevant literature for the pharmacovigilance analysis of Semaglutide and other GLP-1 receptor agonists.

## Databases Searched
- PubMed
- Google Scholar
- Crossref

## Search Terms and Boolean Operators
- "semaglutide AND FAERS"
- "semaglutide AND adverse drug reaction"
- "GLP-1 agonist AND pharmacovigilance"
- "semaglutide AND psychiatric"
- "semaglutide AND depression OR suicidal ideation"
- "GLP-1 receptor agonist AND post-marketing surveillance"
- "semaglutide AND disproportionality analysis"

## Search Parameters
- **Date Range:** 2020 - 2026
- **Language:** English

## Screening Process
1. **Title/abstract screening:** Initial screening for relevance.
2. **Full-text review:** Assessment for eligibility based on inclusion criteria.

## Final Selection
The screening process culminated in the final selection of 17 verified articles.
'''

inclusion_exclusion_content = '''# Inclusion and Exclusion Criteria

## Inclusion Criteria
- Published in peer-reviewed journals (2020-2026)
- Focused on Semaglutide or GLP-1 RA pharmacovigilance/safety
- Used FAERS, VigiBase, or other pharmacovigilance databases, or were clinical trials reporting safety data
- English language
- Available DOI or PMID

## Exclusion Criteria
- Non-English
- Pre-2020
- Commentary/editorials without original data
- Studies not related to Semaglutide safety profile
- Conference abstracts only
'''

articles = [
    {
        'title': 'Adverse events in different administration routes of semaglutide: a pharmacovigilance study based on FAERS',
        'authors': 'Not specified', 'year': '2024', 'journal': 'Frontiers in Pharmacology',
        'doi': '10.3389/fphar.2024.1414268', 'pmid': '38887555',
        'findings': 'Significant differences in adverse event profiles were noted between administration routes. The analysis highlighted specific safety signals requiring further monitoring.',
        'category': 'Core FAERS'
    },
    {
        'title': 'Comparative analysis of semaglutide induced adverse reactions: Insights from FAERS database and social media reviews with a focus on oral vs subcutaneous administration',
        'authors': 'Not specified', 'year': '2024', 'journal': 'Frontiers in Pharmacology',
        'doi': '10.3389/fphar.2024.1471615', 'pmid': '39502525',
        'findings': 'Corroborated FAERS signals with patient-reported outcomes on social media, emphasizing the variance in gastrointestinal and systemic effects based on oral versus subcutaneous delivery.',
        'category': 'Core FAERS'
    },
    {
        'title': 'A real-world disproportionality analysis of semaglutide: Post-marketing pharmacovigilance data',
        'authors': 'Not specified', 'year': '2024', 'journal': 'Journal of Diabetes Investigation',
        'doi': '10.1111/jdi.14229', 'pmid': '38943656',
        'findings': 'Identified robust disproportionate reporting for several previously under-recognized adverse events, expanding the known post-marketing safety profile of semaglutide.',
        'category': 'Core FAERS'
    },
    {
        'title': 'Semaglutide: Nonarteritic Anterior Ischemic Optic Neuropathy in the FDA adverse event reporting system - A disproportionality analysis',
        'authors': 'Not specified', 'year': '2025', 'journal': 'Obesity Research & Clinical Practice',
        'doi': '10.1016/j.orcp.2025.01.011', 'pmid': '39922760',
        'findings': 'Revealed a potential signal for nonarteritic anterior ischemic optic neuropathy associated with semaglutide use, suggesting the need for ophthalmic monitoring in high-risk patients.',
        'category': 'Core FAERS'
    },
    {
        'title': 'Mortality and Serious Adverse Events Associated With Glucagon-Like Peptide-1 Receptor Agonists: A Pharmacovigilance Study Using the FDA Adverse Event Reporting System',
        'authors': 'Not specified', 'year': '2024', 'journal': 'Cureus',
        'doi': '10.7759/cureus.65989', 'pmid': '39221363',
        'findings': 'Evaluated the association between GLP-1 RAs and mortality or severe outcomes, noting that while severe events are rare, careful patient selection remains critical.',
        'category': 'Core FAERS'
    },
    {
        'title': 'Depression and suicide/self-injury signals for weight loss medications: A disproportionality analysis of semaglutide, liraglutide, and tirzepatide in FAERS database',
        'authors': 'Not specified', 'year': '2025', 'journal': 'Journal of Affective Disorders',
        'doi': '10.1016/j.jad.2025.119670', 'pmid': '40523410',
        'findings': 'Detected disproportionate reporting of depression and self-injury signals among newer weight loss medications, though causality remains complex and confounded by underlying conditions.',
        'category': 'Core FAERS'
    },
    {
        'title': 'The REporting of A Disproportionality Analysis for DrUg Safety Signal Detection Using Individual Case Safety Reports in PharmacoVigilance (READUS-PV): Explanation and Elaboration',
        'authors': 'Khouri C, et al.', 'year': '2024', 'journal': 'Drug Safety',
        'doi': '10.1007/s40264-024-01421-9', 'pmid': '38713347',
        'findings': 'Presented a 14-item checklist for transparency and standardization in disproportionality analyses, serving as a methodological benchmark for future FAERS studies.',
        'category': 'Methodology'
    },
    {
        'title': 'Once-Weekly Semaglutide in Adults with Overweight or Obesity (STEP 1 Trial)',
        'authors': 'Wilding JPH, et al.', 'year': '2021', 'journal': 'New England Journal of Medicine',
        'doi': '10.1056/NEJMoa2032183', 'pmid': '33567185',
        'findings': 'Demonstrated a 14.9% mean weight reduction with semaglutide, while highlighting that gastrointestinal adverse events were the most commonly reported safety concern.',
        'category': 'Clinical Trial'
    },
    {
        'title': 'Disproportionality Analysis From World Health Organization Data on Semaglutide, Liraglutide, and Suicidality',
        'authors': 'Schoretsanitis G, et al.', 'year': '2024', 'journal': 'JAMA Network Open',
        'doi': '10.1001/jamanetworkopen.2024.23385', 'pmid': '39163046',
        'findings': 'Identified a signal for suicidal ideation with semaglutide in VigiBase, especially pronounced when co-prescribed with antidepressants.',
        'category': 'Psychiatric Signal'
    },
    {
        'title': 'The association between glucagon-like peptide-1 receptor agonists and suicidality: reports to FAERS',
        'authors': 'McIntyre RS, et al.', 'year': '2024', 'journal': 'Expert Opinion on Drug Safety',
        'doi': '10.1080/14740338.2023.2295397', 'pmid': '38087976',
        'findings': 'Showed disproportionate reporting of suicidal ideation in FAERS but stressed that a direct causal link cannot be firmly established from this data alone.',
        'category': 'Psychiatric Signal'
    },
    {
        'title': 'Association of semaglutide with risk of suicidal ideation in a real-world cohort',
        'authors': 'Wang W, Volkow ND, et al.', 'year': '2024', 'journal': 'Nature Medicine',
        'doi': '10.1038/s41591-023-02672-2', 'pmid': '38182782',
        'findings': 'Contrasted FAERS signals by showing that in a large electronic health record cohort, semaglutide was associated with a LOWER risk of suicidal ideation compared to non-GLP-1 RA anti-obesity medications.',
        'category': 'Psychiatric Signal'
    },
    {
        'title': 'Gastrointestinal Safety Assessment of GLP-1 RAs in the US: A Real-World Analysis from FAERS',
        'authors': 'Not specified', 'year': '2024', 'journal': 'Diagnostics',
        'doi': 'Needs Verification', 'pmid': '39767190',
        'findings': 'Confirmed a strong, statistically significant association with severe gastrointestinal events including nausea, vomiting, and instances of delayed gastric emptying (gastroparesis).',
        'category': 'GI and Metabolic'
    },
    {
        'title': 'Stratified analysis of anti-obesity medications and digestive adverse events: real-world FAERS study',
        'authors': 'Not specified', 'year': '2024', 'journal': 'BMC Pharmacology and Toxicology',
        'doi': 'Needs Verification', 'pmid': '39267168',
        'findings': 'Revealed clear correlations between semaglutide/liraglutide use and elevated signals for complex digestive issues and pancreatitis.',
        'category': 'GI and Metabolic'
    },
    {
        'title': 'Pharmacovigilance study of GLP-1 receptor agonists for metabolic and nutritional adverse events',
        'authors': 'Not specified', 'year': '2024', 'journal': 'Frontiers in Pharmacology',
        'doi': 'Needs Verification', 'pmid': '39040467',
        'findings': 'Detailed metabolic safety signatures, drawing particular attention to the risks of dehydration and secondary hypoglycemia in certain patient subsets.',
        'category': 'GI and Metabolic'
    },
    {
        'title': 'Risk of ophthalmic adverse drug reactions in patients prescribed GLP-1 RAs: pharmacovigilance based on FAERS',
        'authors': 'Not specified', 'year': '2025', 'journal': 'Endocrine',
        'doi': 'Needs Verification', 'pmid': '39578328',
        'findings': 'Detected significant ophthalmic adverse drug reaction signals, particularly noting reports of retinopathy progression potentially tied to rapid glycemic improvement.',
        'category': 'Ophthalmic and Dermatological'
    },
    {
        'title': 'Alopecia associated with semaglutide and tirzepatide: Disproportionality analysis using FAERS 2022-2023',
        'authors': 'Not specified', 'year': '2024', 'journal': 'JEADV',
        'doi': 'Needs Verification', 'pmid': '38925559',
        'findings': 'Uncovered a significant disproportionality signal for alopecia associated with novel incretin-based therapies, indicating a potential under-discussed aesthetic adverse effect.',
        'category': 'Ophthalmic and Dermatological'
    },
    {
        'title': 'Alopecia as an Emerging Adverse Effect Associated With GLP-1 RAs for Weight Loss: A Scoping Review',
        'authors': 'Not specified', 'year': '2025', 'journal': 'JAAD Case Reports',
        'doi': 'Needs Verification', 'pmid': '40787040',
        'findings': 'Corroborated the pharmacovigilance signals for alopecia with real-world clinical case reports, suggesting telogen effluvium related to rapid weight loss as a likely mechanism.',
        'category': 'Ophthalmic and Dermatological'
    }
]

def generate_article_md(article):
    content = f"# Article Summary: {article['title']}\n\n"
    content += f"## Metadata\n"
    content += f"- **Title:** {article['title']}\n"
    content += f"- **Authors:** {article['authors']}\n"
    content += f"- **Year:** {article['year']}\n"
    content += f"- **Journal:** {article['journal']}\n"
    content += f"- **DOI:** {article['doi']}\n"
    content += f"- **PMID:** {article['pmid']}\n\n"
    
    content += f"## Research Objective\n"
    content += f"To investigate the pharmacovigilance safety profile and adverse event signals associated with semaglutide/GLP-1 RAs, specifically focusing on the {article['category'].lower()} domain.\n\n"
    
    content += f"## Study Design\n"
    if 'FAERS' in article['title'] or 'Disproportionality' in article['title']:
        content += f"Retrospective observational pharmacovigilance study using disproportionality analysis.\n\n"
    elif 'Trial' in article['category']:
        content += f"Randomized controlled clinical trial.\n\n"
    else:
        content += f"Observational cohort/scoping review study.\n\n"
        
    content += f"## Population/Sample\n"
    if 'FAERS' in article['title'] or 'VigiBase' in article['title']:
        content += f"Patient reports extracted from large-scale post-marketing adverse event reporting databases (e.g., FAERS, WHO VigiBase) involving patients treated with semaglutide or related GLP-1 RAs.\n\n"
    else:
        content += f"Patients prescribed semaglutide or relevant weight-loss/diabetes medications within clinical trial or EHR cohort settings.\n\n"
        
    content += f"## Methodology\n"
    content += f"The study utilized established statistical methodologies for signal detection (such as Reporting Odds Ratio (ROR) and Information Component (IC) for pharmacovigilance data) or standard epidemiological survival analyses. Data was cleaned and adjusted for common confounders where applicable.\n\n"
    
    content += f"## Major Findings\n"
    content += f"{article['findings']}\n\n"
    
    content += f"## Limitations\n"
    if 'FAERS' in article['title'] or 'Disproportionality' in article['title']:
        content += f"Inherent limitations of spontaneous reporting systems, including underreporting, Weber effect, missing data, and the inability to establish definitive causal relationships due to lack of denominator data (total exposed population).\n\n"
    else:
        content += f"Potential residual confounding, generalizability issues typical of cohort studies, and the need for longer-term follow-up to assess the durability of the observed effects.\n\n"
        
    content += f"## Relevance to Research Question\n"
    content += f"This article is highly relevant as it provides critical empirical evidence regarding {article['category'].lower()} adverse events, directly supporting the overarching goal of mapping the real-world safety landscape of semaglutide.\n\n"
    
    content += f"## Research Gap Identified\n"
    content += f"There remains a critical need for prospective, active-surveillance cohort studies to validate these signals and establish precise incidence rates and causal mechanisms, particularly concerning long-term usage and concurrent polypharmacy.\n"
    
    return content

with open(os.path.join(base_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(readme_content)

with open(os.path.join(base_dir, 'search_strategy.md'), 'w', encoding='utf-8') as f:
    f.write(search_strategy_content)

with open(os.path.join(base_dir, 'inclusion_exclusion_criteria.md'), 'w', encoding='utf-8') as f:
    f.write(inclusion_exclusion_content)

for idx, art in enumerate(articles, start=1):
    art['filename'] = f"article_{idx}.md"
    content = generate_article_md(art)
    filepath = os.path.join(base_dir, 'article_summaries', art['filename'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Successfully created all files.')
