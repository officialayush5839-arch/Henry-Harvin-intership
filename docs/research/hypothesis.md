# Hypotheses and Statistical Framework

This document outlines the formal statistical hypotheses and the analytical framework used to evaluate the potential association between Semaglutide and psychiatric adverse drug reactions (ADRs).

## Formal Hypotheses

The primary research question is addressed through the following null and alternative hypotheses:

*   **Null Hypothesis ($H_0$):** There is no disproportionate signal for psychiatric ADRs associated with Semaglutide compared to the background reporting rate (represented by the active comparator). Mathematically, the Reporting Odds Ratio (ROR) for psychiatric ADRs with Semaglutide is less than or equal to 1.0 ($ROR \le 1.0$).
*   **Alternative Hypothesis ($H_1$):** A disproportionate signal exists for psychiatric ADRs associated with Semaglutide. Mathematically, the Reporting Odds Ratio (ROR) for psychiatric ADRs with Semaglutide is greater than 1.0 ($ROR > 1.0$).

## Statistical Framework: Disproportionality Analysis

The study will utilize disproportionality analysis, the standard pharmacoepidemiological method for signal detection in spontaneous reporting databases like FAERS. This involves comparing the frequency of a specific ADR reported for a drug of interest against the frequency of that ADR reported for all other drugs (or a specific comparator group).

The analysis relies on a 2×2 contingency table:

| | Target ADR (Psychiatric Events) | All Other ADRs | Total |
| :--- | :---: | :---: | :---: |
| **Drug of Interest (Semaglutide)** | a | b | a + b |
| **Comparator (SGLT2 inhibitors)** | c | d | c + d |
| **Total** | a + c | b + d | N |

*   **a:** Number of reports involving Semaglutide and a psychiatric event.
*   **b:** Number of reports involving Semaglutide and any other event.
*   **c:** Number of reports involving the comparator and a psychiatric event.
*   **d:** Number of reports involving the comparator and any other event.

### Reporting Odds Ratio (ROR)

The primary measure of disproportionality will be the Reporting Odds Ratio (ROR). In the context of pharmacovigilance, the ROR estimates the odds of a specific adverse event being reported for a particular drug compared to the odds of the same event being reported for other drugs.

$ROR = \frac{a / c}{b / d} = \frac{a \times d}{b \times c}$

A higher ROR suggests a stronger association (signal) between the drug and the adverse event.

### Signal Detection Threshold and Significance Level

To identify a statistically significant safety signal and reject the null hypothesis, the following criteria must be met:

*   **Significance Level:** The alpha level ($\alpha$) is set at 0.05.
*   **Detection Threshold:** A signal is considered detected if the **lower bound of the 95% Confidence Interval (CI) of the ROR is greater than 1.0**. Furthermore, to reduce false positives from small sample sizes, a minimum threshold of reported cases (e.g., $a \ge 3$) is typically required.
