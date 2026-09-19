import os
import pandas as pd

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'processed_faers_data.csv')
TABLES_DIR = os.path.join(BASE_DIR, 'results', 'tables')
os.makedirs(TABLES_DIR, exist_ok=True)

def main():
    print("Computing descriptive statistics...")
    
    if not os.path.exists(PROCESSED_DATA_PATH):
        print(f"Error: Processed data not found at {PROCESSED_DATA_PATH}.")
        return

    df = pd.read_csv(PROCESSED_DATA_PATH)
    
    # Overall summary by drug class
    summary = df.groupby('drug_class').agg(
        Total_Reports=('total_reports', 'first'),
        Total_Psych_Events=('adr_count', 'sum')
    ).reset_index()
    
    summary['Psych_Event_Proportion (%)'] = (summary['Total_Psych_Events'] / summary['Total_Reports'] * 100).round(3)
    
    summary_path = os.path.join(TABLES_DIR, 'overall_summary.csv')
    summary.to_csv(summary_path, index=False)
    
    # Specific ADR breakdown
    pivot = df.pivot(index='adr_term', columns='drug_class', values='adr_count').reset_index()
    pivot = pivot.fillna(0)
    
    # Add proportions for each ADR
    for drug in ['Semaglutide', 'SGLT2i']:
        if drug in pivot.columns:
            total_drug = summary.loc[summary['drug_class'] == drug, 'Total_Reports'].values[0]
            pivot[f'{drug}_Prop (%)'] = (pivot[drug] / total_drug * 100).round(4)
            
    breakdown_path = os.path.join(TABLES_DIR, 'adr_breakdown.csv')
    pivot.to_csv(breakdown_path, index=False)
    
    print("Descriptive statistics generated:")
    print("\nOverall Summary:")
    try:
        from tabulate import tabulate
        print(tabulate(summary, headers='keys', tablefmt='psql', showindex=False))
        print("\nADR Breakdown:")
        print(tabulate(pivot, headers='keys', tablefmt='psql', showindex=False))
    except ImportError:
        print(summary)
        print("\nADR Breakdown:")
        print(pivot)
        
    print(f"\nTables saved to {TABLES_DIR}")

if __name__ == "__main__":
    main()
