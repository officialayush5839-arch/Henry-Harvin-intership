# Conceptual Framework

## Post-Marketing Pharmacovigilance Signal Detection for Semaglutide

### Framework Overview

This research portfolio operates within the established pharmacovigilance framework for post-marketing drug safety surveillance. The conceptual model connects spontaneous adverse event reporting to signal detection, hypothesis generation, and prospective validation.

### Theoretical Foundation

The pharmacovigilance lifecycle follows a well-established pathway:

```
PRE-MARKETING PHASE                    POST-MARKETING PHASE
─────────────────                      ────────────────────
Phase I–III Clinical Trials     →      Real-World Drug Use
(Controlled, limited population)       (Diverse, large population)
        │                                       │
        ▼                                       ▼
Known Safety Profile              Spontaneous Adverse Event Reporting
(Common ADRs identified)          (Rare/delayed ADRs emerge)
        │                                       │
        ▼                                       ▼
FDA Approval + Labeling           Signal Detection (FAERS Analysis)
                                         │
                                         ▼
                                  Signal Evaluation
                                  (Disproportionality Analysis)
                                         │
                                         ▼
                                  Hypothesis Generation
                                         │
                                         ▼
                                  Prospective Validation Studies
                                         │
                                         ▼
                                  Regulatory Action (if warranted)
```

### Application to This Research

**Phase 1 — Signal Identification (Week 1: Literature Review)**

The literature review identifies emerging signals from published pharmacovigilance analyses of Semaglutide. By synthesizing findings across multiple FAERS-based studies, this phase characterizes the current state of knowledge regarding psychiatric adverse events associated with GLP-1 receptor agonists.

**Phase 2 — Signal Quantification (Week 2: Data Analysis)**

Using the FDA FAERS database, this phase quantifies the disproportionality of psychiatric ADR reporting for Semaglutide compared to SGLT2 inhibitors. The primary metrics — Reporting Odds Ratio (ROR) and Proportional Reporting Ratio (PRR) — are established tools in pharmacovigilance signal detection (van Puijenbroek et al., 2002; Evans et al., 2001).

The 2×2 contingency table framework:

|                    | Target ADR (Psychiatric) | All Other ADRs |
|--------------------|-------------------------|----------------|
| Semaglutide        | a                       | b              |
| Comparator (SGLT2i)| c                       | d              |

- **ROR** = (a × d) / (b × c) — measures the odds of reporting the target ADR with Semaglutide vs the comparator
- **PRR** = [a/(a+b)] / [c/(c+d)] — measures the proportion of the target ADR among all ADRs for each drug

**Phase 3 — Hypothesis Testing Design (Week 3: Experimental Design)**

Based on the signal detected in Phase 2, this phase designs a prospective active surveillance cohort study that would test the hypothesis under controlled conditions with proper denominators, active monitoring, and validated psychiatric assessment instruments.

**Phase 4 — Methodological Evaluation (Week 4: Critical Evaluation)**

The critical evaluation of the STEP 1 Trial provides insight into why pre-marketing RCTs may not detect the signals identified in post-marketing surveillance. This phase connects the RCT-to-real-world evidence gap.

### Key Concepts

| Concept | Definition | Relevance |
|---------|-----------|-----------|
| Spontaneous reporting | Voluntary ADR reports submitted to regulatory authorities | Primary data source (FAERS) |
| Disproportionality analysis | Statistical method comparing observed vs expected ADR reporting rates | Primary analytical method |
| Reporting Odds Ratio (ROR) | Odds of a specific ADR being reported for one drug vs another | Primary signal metric |
| Signal | A reported causal relationship that warrants further investigation | What Week 2 seeks to quantify |
| Weber effect | Increased reporting in the first 2 years after drug launch | Key confounding factor |
| Notoriety bias | Media coverage increasing ADR reporting rates | Relevant to GLP-1 agonists |
| Stimulated reporting | Regulatory actions prompting increased reporting | FDA Semaglutide investigation |

### Assumptions and Limitations of the Framework

1. **FAERS does not establish causation** — Disproportionality signals indicate a reporting pattern, not a causal relationship
2. **No denominator data** — FAERS captures reports, not incidence rates; the number of patients exposed to each drug is unknown
3. **Reporting bias** — Voluntary reporting is subject to under-reporting, Weber effect, and stimulated reporting
4. **Confounding** — Patients on Semaglutide may differ systematically from those on SGLT2 inhibitors (indication bias, obesity-depression comorbidity)
5. **Signal, not proof** — This research generates hypotheses that require prospective confirmation (Week 3 design)

### References

- Evans, S. J. W., Waller, P. C., & Davis, S. (2001). Use of proportional reporting ratios (PRRs) for signal generation from spontaneous adverse drug reaction reports. *Pharmacoepidemiology and Drug Safety*, 10(6), 483–486.
- van Puijenbroek, E. P., Bate, A., Leufkens, H. G. M., Lindquist, M., Orre, R., & Egberts, A. C. G. (2002). A comparison of measures of disproportionality for signal detection in spontaneous reporting systems for adverse drug reactions. *Pharmacoepidemiology and Drug Safety*, 11(1), 3–10.
