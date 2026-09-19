import os
import pandas as pd

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'raw_faers_data.csv')
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'data', 'processed')
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

def main():
    print("Starting data cleaning...")
    
    if not os.path.exists(RAW_DATA_PATH):
        print(f"Error: Raw data not found at {RAW_DATA_PATH}. Please run data_collection.py first.")
        return

    df = pd.read_csv(RAW_DATA_PATH)
    
    # 1. Check for duplicates
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        df = df.drop_duplicates()
        print(f"Removed {dup_count} duplicated rows.")
        
    # 2. Handle missing values
    missing = df.isnull().sum().sum()
    if missing > 0:
        df = df.fillna(0)
        print(f"Filled {missing} missing values with 0.")
        
    # 3. Validate data types
    df['total_reports'] = df['total_reports'].astype(int)
    df['adr_count'] = df['adr_count'].astype(int)
    
    # 4. Feature engineering: Calculate non-ADR count for each row (useful for 2x2 table)
    df['non_adr_count'] = df['total_reports'] - df['adr_count']
    
    # 5. Format text
    df['adr_term'] = df['adr_term'].str.title()
    
    # Save processed data
    output_path = os.path.join(PROCESSED_DATA_DIR, 'processed_faers_data.csv')
    df.to_csv(output_path, index=False)
    
    # Generate cleaning report
    report_path = os.path.join(PROCESSED_DATA_DIR, 'cleaning_report.txt')
    with open(report_path, 'w') as f:
        f.write("Data Cleaning Report\n")
        f.write("====================\n")
        f.write(f"Original rows: {len(df) + dup_count}\n")
        f.write(f"Duplicates removed: {dup_count}\n")
        f.write(f"Missing values filled: {missing}\n")
        f.write(f"Final rows: {len(df)}\n")
        f.write("\nData Types:\n")
        f.write(str(df.dtypes))
        
    print(f"Processed data saved to {output_path}")
    print(f"Cleaning report saved to {report_path}")

if __name__ == "__main__":
    main()
