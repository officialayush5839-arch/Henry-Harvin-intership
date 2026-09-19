# Data Dictionary

This document describes the variables present in the `processed_faers_data.csv` dataset.

| Variable Name | Data Type | Description |
|---|---|---|
| `drug_class` | String | The class of the drug (e.g., 'Semaglutide', 'SGLT2i'). |
| `total_reports` | Integer | The total number of adverse event reports for the drug class in the analyzed timeframe/database. |
| `adr_term` | String | The MedDRA preferred term (PT) for the psychiatric adverse drug reaction (e.g., 'Depression', 'Anxiety'). |
| `adr_count` | Integer | The number of reports specifically mentioning this `adr_term` for this `drug_class`. |
| `non_adr_count` | Integer | The number of reports for this `drug_class` that do NOT mention this `adr_term` (`total_reports` - `adr_count`). Used for 2x2 contingency tables. |
