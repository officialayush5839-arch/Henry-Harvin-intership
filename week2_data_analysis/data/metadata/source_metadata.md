# Source Metadata

## Primary Data Source
- **Name:** FDA Adverse Event Reporting System (FAERS)
- **Access Method:** OpenFDA API (`https://api.fda.gov/drug/event.json`)
- **Query Strategy:** 
  - Searches conducted using medicinal product names.
  - GLP-1 terms: 'semaglutide', 'ozempic', 'wegovy', 'rybelsus'
  - SGLT2i terms: 'empagliflozin', 'dapagliflozin', 'canagliflozin'
  - Reaction terms: 'depression', 'depressed mood', 'suicidal ideation', 'suicide attempt', 'anxiety', 'insomnia', 'panic attack'

## Fallback Data Source
In the event the API is unreachable, the system uses a curated fallback dataset. 
- **Methodology:** Aggregate counts are simulated to represent typical disproportionality study magnitudes found in recent peer-reviewed literature regarding GLP-1 receptor agonists and SGLT2 inhibitors. 
- **Status:** Numbers are labeled as ESTIMATED if the fallback mechanism is triggered.

## Provenance
- Data fetched automatically during the execution of `data_collection.py`.
- No authentication is required for basic OpenFDA queries.
