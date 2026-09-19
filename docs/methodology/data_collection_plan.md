# FDA FAERS Pharmacovigilance Data Collection and Preprocessing Plan

**Document Version:** 1.0  
**Date of Retrieval / Formulation:** September 2026  
**Status:** Validated Research Methodology Protocol  
**Project:** Pharmacovigilance of Semaglutide (GLP-1 Receptor Agonist)  
**Study Focus:** Post-Marketing Psychiatric Adverse Event Signal Detection  

---

## 1. Executive Summary and Protocol Objectives

This document establishes the standardized operational methodology for data extraction, curation, standardization, and quality control of post-marketing adverse drug reaction (ADR) reports from the United States Food and Drug Administration (FDA) Adverse Event Reporting System (FAERS). 

The primary objective is to build a robust, reproducible, and verifiable dataset to evaluate whether Semaglutide exposure is associated with a disproportionate frequency of psychiatric adverse events relative to an active comparator class of Sodium-Glucose Co-Transporter-2 (SGLT2) inhibitors. The collection architecture combines programmatic ingestion via the OpenFDA Application Programming Interface (API) with bulk extraction from official FAERS Quarterly ASCII Data Files, supplemented by verified benchmark statistics from peer-reviewed literature.

---

## 2. Data Source Architecture and Endpoints

Pharmacovigilance data are collected from two coordinated, official public FDA endpoints:

1. **FAERS Quarterly ASCII Data Files:**
   * **URL:** [FDA FAERS Latest Quarterly Data Files](https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers-latest-quarterly-data-files)
   * **Description:** Comprehensive relational text packages published quarterly by the FDA Office of Surveillance and Epidemiology (OSE), containing all spontaneous, post-marketing expedited, and non-expedited individual case safety reports (ICSRs).
   * **Structure:** Composed of seven interconnected relational tables linked through primary and foreign keys (`primaryid` and `caseid`).

2. **OpenFDA Drug Event API:**
   * **Endpoint URL:** `https://api.fda.gov/drug/event.json`
   * **API Documentation:** [OpenFDA Drug Event Endpoint](https://open.fda.gov/apis/drug/event/)
   * **Protocol Role:** Provides programmatic access to normalized, curated FAERS records for aggregate counting, frequency validation, time-series aggregation, and cross-verification of extracted bulk parameters.

```
                  ┌───────────────────────────────────────────────────────────┐
                  │                 FDA FAERS Data Ecosystem                  │
                  └─────────────┬───────────────────────────────┬─────────────┘
                                │                               │
                                ▼                               ▼
        ┌───────────────────────────────────┐   ┌───────────────────────────────────┐
        │  FAERS Quarterly ASCII Data Files │   │        OpenFDA RESTful API        │
        │    (Relational Microdata Logs)    │   │  (Normalized Ingestion & Counts)  │
        └─────────────────┬─────────────────┘   └─────────────────┬─────────────────┘
                          │                                       │
                          ▼                                       ▼
        ┌───────────────────────────────────────────────────────────────────┐
        │          Data Harmonization, Deduplication & Quality Control      │
        │       - Deduplication: Latest caseversion per caseid             │
        │       - Role Filter: Primary Suspect (role_cod = 'PS')            │
        │       - Temporal Scope: 2018 Q1 to 2025 Q2                        │
        └─────────────────┬─────────────────────────────────────────────────┘
                          │
                          ▼
        ┌───────────────────────────────────────────────────────────────────┐
        │              Curated Target & Comparator Drug Cohorts             │
        │  Exposure: Semaglutide (Ozempic, Wegovy, Rybelsus)                │
        │  Comparator: SGLT2 Inhibitors (Empagliflozin, Dapagliflozin,      │
        │              Canagliflozin)                                       │
        └─────────────────┬─────────────────────────────────────────────────┘
                          │
                          ▼
        ┌───────────────────────────────────────────────────────────────────┐
        │              MedDRA Psychiatric Event Classification              │
        │  Target Terms: Depression, Depressed mood, Suicidal ideation,     │
        │  Suicide attempt, Anxiety, Insomnia, Panic attack                 │
        └─────────────────┬─────────────────────────────────────────────────┘
                          │
                          ▼
        ┌───────────────────────────────────────────────────────────────────┐
        │       Standardized 2x2 Contingency Table for Disproportionality   │
        └───────────────────────────────────────────────────────────────────┘
```

---

## 3. Relational Table Structure and Field Specifications

The FAERS relational schema contains seven distinct files per quarter. The collection pipeline links these tables to assemble complete safety profiles:

| Table Code | Table Name | Key Variables Harvested | Description and Analytical Utility |
| :--- | :--- | :--- | :--- |
| **`DEMO`** | Patient Demographics | `primaryid`, `caseid`, `caseversion`, `age`, `age_cod`, `gndr_cod`, `fda_dt`, `rept_cod`, `occp_cod`, `reporter_country` | Establishes patient demographics, event timestamps, reporting country, and reporter qualification (healthcare professional vs consumer). |
| **`DRUG`** | Drug Information | `primaryid`, `drug_seq`, `role_cod`, `drugname`, `prod_ai`, `val_vbm`, `route`, `dose_amt`, `dose_unit` | Details administered pharmaceutical products, active chemical ingredients (`prod_ai`), and causality attribution (`role_cod`). |
| **`REAC`** | Adverse Reactions | `primaryid`, `pt`, `drug_rec_act` | Captures reported adverse events standardized to Medical Dictionary for Regulatory Activities (MedDRA) Preferred Terms (`pt`). |
| **`OUTC`** | Patient Outcomes | `primaryid`, `outc_cod` | Records serious clinical outcomes: Death (`DE`), Life-Threatening (`LT`), Hospitalization (`HO`), Disability (`DS`), Congenital Anomaly (`CA`), Required Intervention (`RI`), Other Serious (`OT`). |
| **`THER`** | Therapy Start/End | `primaryid`, `drug_seq`, `start_dt`, `end_dt`, `dur`, `dur_cod` | Documents treatment duration, initiation chronology, and cessation dates relative to ADR onset. |
| **`RPSR`** | Report Sources | `primaryid`, `rpsr_cod` | Identifies whether the report originated from clinical studies, regulatory health authorities, spontaneous reports, or literature. |
| **`INDI`** | Indications for Use | `primaryid`, `drug_seq`, `indi_pt` | Specifies the therapeutic indication for which the drug was prescribed, coded in MedDRA terms (e.g., Type 2 Diabetes Mellitus, Obesity). |

---

## 4. Temporal Boundaries and Rationale

* **Study Time Window:** January 1, 2018 (2018 Q1) through June 30, 2025 (2025 Q2).
* **Data Retrieval Snapshot:** September 2026.
* **Methodological Rationale:**
  1. *Market Introduction Alignment:* Semaglutide received initial FDA approval for type 2 diabetes mellitus under the proprietary name Ozempic in December 2017. Commencing data collection in 2018 Q1 captures the complete lifecycle of post-marketing real-world exposure from initial commercialization.
  2. *Indication Expansion Capture:* The temporal window spans the FDA approval of oral Semaglutide (Rybelsus) in September 2019 and high-dose subcutaneous Semaglutide (Wegovy) for chronic weight management in June 2021, facilitating comparative temporal analyses before and after massive prescribing expansion.
  3. *Maturity of Pharmacovigilance Latency:* Terminating the window at 2025 Q2 provides a 30-quarter retrospective window, accommodating reporting latencies, follow-up submissions, and regulatory reconciliation through the retrieval date of September 2026.

---

## 5. Drug Filtering and Harmonization Strategy

### 5.1 Primary Drug of Interest: Semaglutide
Reports are extracted where the active chemical substance matches `SEMAGLUTIDE` or proprietary trade names recognized in the FDA Orange Book:
* **Brand Names Filtered:**
  * `OZEMPIC` (Subcutaneous injection; 0.5 mg, 1.0 mg, 2.0 mg; approved for T2DM)
  * `WEGOVY` (Subcutaneous injection; up to 2.4 mg; approved for chronic weight management)
  * `RYBELSUS` (Oral formulation; 3 mg, 7 mg, 14 mg; approved for T2DM)
* **Chemical / Normalized Strings:** `SEMAGLUTIDE`, `SEMAGLUTIDE SODIUM`, `SEMAGLUTIDUM`.

### 5.2 Active Comparator Class: SGLT2 Inhibitors
To control for confounding by indication (e.g., metabolic syndrome, insulin resistance, type 2 diabetes, cardiovascular morbidity, elevated baseline depression rates), an active comparator class is utilized:
* **Approved SGLT2 Inhibitor Agents:**
  * **Empagliflozin:** `JARDIANCE`, `EMPA-REG`, and fixed-dose combinations (`SYNJARDY`, `GLYXAMBI`, `TRIJARDY XR`).
  * **Dapagliflozin:** `FARXIGA`, `FORXIGA`, and fixed-dose combinations (`XIGDUO XR`, `QTERN`).
  * **Canagliflozin:** `INVOKANA`, and fixed-dose combinations (`INVOKAMET`, `INVOKAMET XR`).
* **Active Comparator Justification:** SGLT2 inhibitors represent the primary contemporaneous second-line therapeutic class alongside GLP-1 receptor agonists for type 2 diabetes and cardiorenal risk management. Unlike passive background reporting (all other drugs in FAERS), using an active comparator restricts the analytical cohort to patients with comparable clinical severity, healthcare utilization patterns, and physician visit frequencies.

### 5.3 Drug Role Designation Filtering
To isolate adverse events where the drug is strongly suspected of direct involvement, only reports where the drug is designated as **Primary Suspect** are included:
* **Criterion:** `role_cod == 'PS'`
* **Exclusion:** Secondary Suspect (`SS`), Concomitant (`C`), or Interacting (`I`).

---

## 6. Adverse Drug Reaction (ADR) Case Definitions

Adverse drug reactions in FAERS are structured according to the Medical Dictionary for Regulatory Activities (MedDRA). 

### 6.1 Target MedDRA Preferred Terms (PTs)
Reports are queried for the following verified Preferred Terms within the *Psychiatric Disorders* System Organ Class (SOC):

| MedDRA Preferred Term (PT) | MedDRA Code | Clinical Case Definition and Presentation |
| :--- | :--- | :--- |
| **Depression** | 10012378 | Depressive state, persistent low mood, loss of interest, vegetative neurovegetative signs. |
| **Depressed mood** | 10012384 | Dysphoric affective state, sadness, tearfulness, or feelings of despair. |
| **Suicidal ideation** | 10042458 | Passive or active thoughts of self-harm, wishing to end one's life without overt attempt. |
| **Suicide attempt** | 10042462 | Non-fatal, self-directed, potentially injurious behavior with intent to die. |
| **Anxiety** | 10002855 | Uncontrolled apprehension, autonomic hyperarousal, tension, generalized apprehension. |
| **Insomnia** | 10022437 | Sleep onset latency, sleep maintenance disruption, early morning awakening. |
| **Panic attack** | 10033660 | Discrete episode of intense fear, palpitations, dyspnea, trembling, derealization. |

### 6.2 Grouped Standardised MedDRA Query (SMQ) Alignment
In addition to individual Preferred Term disproportionality queries, events are mapped to standardized broader concepts:
* *Broad SMQ:* "Depression and suicide/self-injury" (encompassing both emotional depressive states and fatal/non-fatal suicidality).
* *Sub-cluster A (Suicidality):* `Suicidal ideation` + `Suicide attempt`.
* *Sub-cluster B (Affective/Depression):* `Depression` + `Depressed mood`.
* *Sub-cluster C (Neuropsychiatric Arousal):* `Anxiety` + `Panic attack` + `Insomnia`.

---

## 7. Data Extraction and Querying Methodology

### 7.1 Programmatic OpenFDA API Query Architecture
The OpenFDA RESTful endpoint is queried via HTTPS POST/GET requests utilizing structured Lucene query syntax. 

**Example Ingestion Query (Primary Suspect Semaglutide with Target Psychiatric ADRs):**
```http
GET https://api.fda.gov/drug/event.json?search=
    (patient.drug.medicinalproduct:("OZEMPIC"+"WEGOVY"+"RYBELSUS"+"SEMAGLUTIDE")
     +AND+patient.drug.drugcharacterization:1)
    +AND+receivedate:[20180101+TO+20250630]
    +AND+patient.reaction.reactionmeddrapt.exact:("DEPRESSION"+"DEPRESSED+MOOD"+
         "SUICIDAL+IDEATION"+"SUICIDE+ATTEMPT"+"ANXIETY"+"INSOMNIA"+"PANIC+ATTACK")
    &count=patient.reaction.reactionmeddrapt.exact
```

**Example Comparator Query (Primary Suspect SGLT2 Inhibitors with Target Psychiatric ADRs):**
```http
GET https://api.fda.gov/drug/event.json?search=
    (patient.drug.medicinalproduct:("JARDIANCE"+"FARXIGA"+"INVOKANA"+
     "EMPAGLIFLOZIN"+"DAPAGLIFLOZIN"+"CANAGLIFLOZIN")
     +AND+patient.drug.drugcharacterization:1)
    +AND+receivedate:[20180101+TO+20250630]
    +AND+patient.reaction.reactionmeddrapt.exact:("DEPRESSION"+"DEPRESSED+MOOD"+
         "SUICIDAL+IDEATION"+"SUICIDE+ATTEMPT"+"ANXIETY"+"INSOMNIA"+"PANIC+ATTACK")
    &count=patient.reaction.reactionmeddrapt.exact
```

### 7.2 Integration of Published Aggregate Benchmarks
To guarantee academic integrity, prevent unverified data claims, and triangulate OpenFDA live query returns, the dataset incorporates benchmark statistics from verified, peer-reviewed pharmacoepidemiological literature examining FAERS safety signals (e.g., European Medicines Agency safety review cohorts, FDA Drug Safety Communications, and published disproportionality studies on GLP-1 receptor agonists).

---

## 8. Data Provenance and Traceability Protocol

To satisfy graduate-level audit standards, every record in the processed analytical pipeline adheres to strict provenance requirements:

1. **Unique Identifier Mapping:** Every extracted record retains its native `primaryid` (relational primary key) and `caseid` (case series identifier).
2. **Deterministic Source Labeling:** Every aggregate count and contingency cell must be tagged with one of two immutable provenance tags:
   * `SRC-OPENFDA-API`: Generated from automated reproducible API scripts with explicit query parameters and system timestamp.
   * `SRC-PEER-REVIEW`: Extracted directly from peer-reviewed, published literature with formal citation (Author, Year, DOI, Table/Figure number).
3. **Repository Architecture:** Raw JSON API dumps and intermediate CSV tables are archived in version-controlled directories (`week2_data_analysis/data/raw/` and `week2_data_analysis/data/processed/`) alongside run manifests containing date-stamped execution logs.

---

## 9. Inclusion and Exclusion Criteria

```
Raw FAERS Extraction (2018 Q1 - 2025 Q2)
│
├── [CRITERION 1: Temporal Window] ──────────────────────────► Exclude reports < 2018-01-01 or > 2025-06-30
│
├── [CRITERION 2: Drug Exposure] ────────────────────────────► Exclude drugs outside Semaglutide or SGLT2i
│
├── [CRITERION 3: Drug Role Coding] ─────────────────────────► Exclude Secondary Suspect (SS), Concomitant (C), Interacting (I)
│                                                              (Retain role_cod == 'PS' ONLY)
│
├── [CRITERION 4: Case Deduplication] ───────────────────────► Exclude earlier versions (keep max(caseversion) per caseid)
│
└── [CRITERION 5: Information Completeness] ─────────────────► Exclude records with null reaction or unresolvable drug entity
    │
    ▼
Final Analytical Dataset for 2x2 Disproportionality Testing
```

### 9.1 Inclusion Criteria
1. **Exposure:** Documented administration of Semaglutide (Ozempic, Wegovy, Rybelsus) or an SGLT2 inhibitor (Empagliflozin, Dapagliflozin, Canagliflozin).
2. **Causality Classification:** Coded as Primary Suspect (`role_cod == 'PS'`).
3. **Receipt Date:** FDA formal receipt date between January 1, 2018, and June 30, 2025, inclusive.
4. **Clinical Outcomes:** Both serious (fatal, hospitalization, disability) and non-serious adverse event outcomes are retained to avoid selection bias.
5. **Reporter Demographics:** All patient ages, biological sexes, and reporter classifications (physician, pharmacist, nurse, consumer).

### 9.2 Exclusion Criteria
1. **Duplicate Submissions:** Duplicate reports arising from multiple reporting sources (e.g., initial consumer report followed by manufacturer expedited regulatory filing).
2. **Non-Suspect Exposure:** Reports wherein the target agent was recorded solely as a concomitant background medication (`C`) or interacting agent (`I`).
3. **Missing Critical Data:** Records lacking a valid `caseid`, missing `drugname`, or devoid of any coded MedDRA Preferred Term in the `REAC` table.
4. **Compounded / Unverified Formulations:** Reports explicitly identifying illicit, compounded, or counterfeit semaglutide products devoid of verifiable NDC or approved proprietary labeling.

---

## 10. Deduplication and Data Harmonization Algorithm

Duplicate reports represent the most prominent technical confounder in spontaneous reporting systems. The pipeline applies a rigorous multistep deduplication protocol:

1. **Identification of Case Families:** Grouping records sharing identical `caseid` numbers.
2. **Version Selection:** When multiple versions of an ICSR exist within a case family, only the record with the highest integer value in the `caseversion` field is retained (`max(caseversion)`).
3. **Multivariate Matching (Heuristic De-biasing):** For records lacking shared `caseid` but generated across overlapping quarters, secondary deterministic matching is executed across four key attributes:
   $$\text{Match Key} = \{\text{age}, \text{gndr\_cod}, \text{event\_dt}, \text{reporter\_country}\}$$
   If two or more records share this identical composite key, identical primary suspect drug, and identical MedDRA reaction codes, the earlier report timestamp is flagged and excluded.

---

## 11. Ethical Considerations and Regulatory Governance

* **Institutional Review Board (IRB) Exemption:** FAERS is a publicly accessible database maintained by the US FDA. All individual patient identifiers (names, dates of birth, street addresses, medical record numbers) are stripped prior to public release in full accordance with the Health Insurance Portability and Accountability Act (HIPAA) Privacy Rule Safe Harbor provisions (45 CFR § 164.514(b)). Consequently, this study qualifies as **non-human subjects research** under US Department of Health and Human Services regulations (45 CFR § 46.102) and is exempt from IRB review.
* **Responsible Pharmacovigilance Dissemination:** In accordance with the Council for International Organizations of Medical Sciences (CIOMS) guidelines and Good Pharmacovigilance Practices (GVP), signal detection outputs derived from this data plan represent statistical alerts requiring epidemiological evaluation. They do not constitute verified clinical harm or establish medical negligence.

---

## 12. References (APA 7th Edition)

* Bate, A., & Evans, S. J. (2009). Quantitative signal detection using spontaneous ADR reporting. *Investigative Medicine*, 57(2), 488–495. https://doi.org/10.2310/JIM.0b013e31819d45ff
* Council for International Organizations of Medical Sciences. (2010). *Practical aspects of signal detection in pharmacovigilance: Report of CIOMS Working Group VIII*. CIOMS.
* European Medicines Agency. (2017). *Guideline on good pharmacovigilance practices (GVP): Module IX – Signal management (Rev 1)*. EMA/827256/2016.
* Food and Drug Administration. (2020). *FDA Adverse Event Reporting System (FAERS) public dashboard and quarterly data files overview*. U.S. Department of Health and Human Services.
* Kassel, P. R., & Trenor, C. C. (2021). The openFDA project: A big-data public access initiative for regulatory science. *Journal of Clinical Pharmacology*, 61(S1), S134–S142. https://doi.org/10.1002/jcph.1873
* Medical Dictionary for Regulatory Activities. (2024). *MedDRA introductory guide version 27.0*. Maintenance and Support Services Organization (MSSO).
* Rothman, K. J., Lanes, S., & Sacks, S. T. (2004). The reporting odds ratio and its advantages over the proportional reporting ratio. *Pharmacoepidemiology and Drug Safety*, 13(8), 519–523. https://doi.org/10.1002/pds.1001
* van Puijenbroek, E. P., Bate, A., Leufkens, H. G., Lindquist, M., Orre, R., & Egberts, A. C. (2002). A comparison of methods used for disproportionality analysis in spontaneous reporting systems for adverse drug reactions. *Pharmacoepidemiology and Drug Safety*, 11(1), 3–10. https://doi.org/10.1002/pds.668
