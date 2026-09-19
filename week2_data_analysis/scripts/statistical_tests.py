import os
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, fisher_exact

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'processed_faers_data.csv')
STAT_RESULTS_DIR = os.path.join(BASE_DIR, 'results', 'statistical_results')
os.makedirs(STAT_RESULTS_DIR, exist_ok=True)

def calculate_ror_prr(a, b, c, d):
    """
    Calculate ROR, PRR, and 95% CI for ROR.
    a: Exposed (Semaglutide) with event
    b: Exposed (Semaglutide) without event
    c: Unexposed (SGLT2i) with event
    d: Unexposed (SGLT2i) without event
    """
    # Prevent division by zero
    if a == 0 or b == 0 or c == 0 or d == 0:
        return np.nan, np.nan, np.nan, np.nan
        
    # ROR
    ror = (a * d) / (b * c)
    se_log_ror = np.sqrt(1/a + 1/b + 1/c + 1/d)
    lower_ci = np.exp(np.log(ror) - 1.96 * se_log_ror)
    upper_ci = np.exp(np.log(ror) + 1.96 * se_log_ror)
    
    # PRR
    prr = (a / (a + b)) / (c / (c + d))
    
    return ror, lower_ci, upper_ci, prr

def main():
    print("Running statistical tests...")
    
    if not os.path.exists(PROCESSED_DATA_PATH):
        print(f"Error: Processed data not found at {PROCESSED_DATA_PATH}.")
        return

    df = pd.read_csv(PROCESSED_DATA_PATH)
    
    # We need Semaglutide and SGLT2i data
    sema = df[df['drug_class'] == 'Semaglutide'].set_index('adr_term')
    sglt2 = df[df['drug_class'] == 'SGLT2i'].set_index('adr_term')
    
    results = []
    
    # Common terms
    terms = set(sema.index).intersection(set(sglt2.index))
    
    for term in terms:
        a = int(sema.loc[term, 'adr_count'])
        b = int(sema.loc[term, 'non_adr_count'])
        c = int(sglt2.loc[term, 'adr_count'])
        d = int(sglt2.loc[term, 'non_adr_count'])
        
        table = [[a, b], [c, d]]
        
        # ROR and PRR
        ror, ci_low, ci_high, prr = calculate_ror_prr(a, b, c, d)
        
        # Statistical tests
        # Use Fisher's exact if expected freq < 5, else Chi-square with Yates
        row_sums = [a+b, c+d]
        col_sums = [a+c, b+d]
        total = sum(row_sums)
        expected = [[r*c/total for c in col_sums] for r in row_sums]
        
        if any(e < 5 for row in expected for e in row):
            test_used = "Fisher Exact"
            _, p_value = fisher_exact(table)
            chi2_stat = np.nan
        else:
            test_used = "Chi-square (Yates)"
            chi2_stat, p_value, _, _ = chi2_contingency(table, correction=True)
            
        # Signal detection criteria: lower CI > 1.0 AND PRR >= 2.0 AND chi2 >= 4.0
        # (Assuming alpha=0.05, chi2 >= 3.84 is often used, but prompt specifies >= 4.0)
        signal = False
        if pd.notna(ci_low) and ci_low > 1.0 and pd.notna(prr) and prr >= 2.0:
            if test_used == "Chi-square (Yates)" and chi2_stat >= 4.0:
                signal = True
            elif test_used == "Fisher Exact" and p_value < 0.05: # proxy for chi2 threshold
                signal = True
                
        results.append({
            'ADR_Term': term,
            'a (Sema with ADR)': a,
            'b (Sema without ADR)': b,
            'c (SGLT2i with ADR)': c,
            'd (SGLT2i without ADR)': d,
            'ROR': ror,
            'ROR_95%_CI_Lower': ci_low,
            'ROR_95%_CI_Upper': ci_high,
            'PRR': prr,
            'Test_Used': test_used,
            'Chi2_Stat': chi2_stat,
            'P_Value': p_value,
            'Signal_Detected': signal
        })
        
    res_df = pd.DataFrame(results)
    output_path = os.path.join(STAT_RESULTS_DIR, 'disproportionality_results.csv')
    res_df.to_csv(output_path, index=False)
    
    print("\n--- Disproportionality Analysis Results ---")
    for _, row in res_df.iterrows():
        print(f"\nADR: {row['ADR_Term']}")
        print(f"  ROR: {row['ROR']:.2f} (95% CI: {row['ROR_95%_CI_Lower']:.2f} - {row['ROR_95%_CI_Upper']:.2f})")
        print(f"  PRR: {row['PRR']:.2f}")
        stat = f"Chi2 = {row['Chi2_Stat']:.2f}, " if pd.notna(row['Chi2_Stat']) else ""
        print(f"  Test: {row['Test_Used']} ({stat}p = {row['P_Value']:.4e})")
        print(f"  Signal Detected: {'YES' if row['Signal_Detected'] else 'NO'}")
        
    print(f"\nDetailed results saved to {output_path}")

if __name__ == "__main__":
    main()
