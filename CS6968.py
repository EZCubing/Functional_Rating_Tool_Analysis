import pandas as pd
from scipy.stats import pearsonr
import numpy as np
 
def calculate_test_retest_reliability(data, col1, col2):
    """
    Calculate Test-Retest Reliability using Pearson correlation coefficient.

    Parameters:
        data (DataFrame): The dataset containing the scores.
        col1 (str): The column name for the first set of scores.
        col2 (str): The column name for the second set of scores.

    Returns:
        float: Pearson correlation coefficient between col1 and col2.
    """
    # Extract the columns
    scores_1 = data[col1]
    scores_2 = data[col2]

    # Calculate Pearson correlation
    correlation, _ = pearsonr(scores_1, scores_2)

    return correlation

def calculate_inter_rater_reliability(data, cols):
    """
    Calculate Inter-Rater Reliability using the average Pearson correlation coefficient.

    Parameters:
        data (DataFrame): The dataset containing the scores.
        cols (list): List of column names for the raters.

    Returns:
        float: Average Pearson correlation coefficient among all raters.
    """
    correlations = []
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            corr, _ = pearsonr(data[cols[i]], data[cols[j]])
            correlations.append(corr)
    return np.mean(correlations)

def calculate_internal_consistency(data, cols):
    """
    Calculate Internal Consistency using Cronbach's Alpha.

    Parameters:
        data (DataFrame): The dataset containing the scores.
        cols (list): List of column names for the raters.

    Returns:
        float: Cronbach's Alpha.
    """
    scores = data[cols].values
    item_variances = np.var(scores, axis=0, ddof=1)
    total_variance = np.var(np.sum(scores, axis=1), ddof=1)
    n_items = len(cols)
    alpha = n_items / (n_items - 1) * (1 - np.sum(item_variances) / total_variance)
    return alpha

def calculate_criterion_validity(data, observed_col, estimated_col):
    """
    Calculate Criterion Validity using Pearson correlation coefficient.

    Parameters:
        data (DataFrame): The dataset containing the scores.
        observed_col (str): The column name for observed scores.
        estimated_col (str): The column name for estimated scores.

    Returns:
        float: Pearson correlation coefficient between observed and estimated scores.
    """
    observed_scores = data[observed_col]
    estimated_scores = data[estimated_col]
    correlation, _ = pearsonr(observed_scores, estimated_scores)
    return correlation

# Example usage 
if __name__ == "__main__":
    # Load the dataset
    file_path = "Problem set 1 - Validity, Reliability.xlsx"  # Replace with the actual file path
    df = pd.read_excel(file_path)

    # Columns for test-retest reliability
    test_retest_pairs = [
        ("Estimated FRS Score (In-clinic, Week 0)", "Estimated FRS Score (Remote, Week 1)"),
        ("Estimated FRS Score (Remote, Week 1)", "Estimated FRS Score (Remote, Week 2)"),
        ("Estimated FRS Score (In-clinic, Week 0)", "Estimated FRS Score (Remote, Week 2)")
    ]

    # Calculate and print Test-Retest Reliability for all pairs
    for col1, col2 in test_retest_pairs:
        test_retest_corr = calculate_test_retest_reliability(df, col1, col2)
        print(f"Test-Retest Reliability between {col1} and {col2}: {test_retest_corr:.3f}")

    # Columns for inter-rater reliability
    rater_cols = [
        "Observed FRS Score (Doctor, Week 0)",
        "Observed FRS Score (Therapist, Week 0)",
        "Observed FRS Score (Caregiver, Week 0)"
    ]

    # Calculate Inter-Rater Reliability
    inter_rater_corr = calculate_inter_rater_reliability(df, rater_cols)
    print(f"Inter-Rater Reliability (Average Correlation): {inter_rater_corr:.3f}")

    # Calculate Internal Consistency (Cronbach's Alpha)
    cronbach_alpha = calculate_internal_consistency(df, rater_cols)
    print(f"Internal Consistency (Cronbach's Alpha): {cronbach_alpha:.3f}")

    # Columns for criterion validity
    criterion_pairs = [
        ("Observed FRS Score (Doctor, Week 0)", "Estimated FRS Score (In-clinic, Week 0)"),
        ("Observed FRS Score (Therapist, Week 0)", "Estimated FRS Score (In-clinic, Week 0)"),
        ("Observed FRS Score (Caregiver, Week 0)", "Estimated FRS Score (In-clinic, Week 0)")
    ]

    # Calculate and print Criterion Validity for all pairs
    for observed_col, estimated_col in criterion_pairs:
        criterion_corr = calculate_criterion_validity(df, observed_col, estimated_col)
        print(f"Criterion Validity between {observed_col} and {estimated_col}: {criterion_corr:.3f}")
