import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_scatter(data, col1, col2, title):
    """
    Generate a scatter plot for two columns.

    Parameters:
        data (DataFrame): The dataset containing the scores.
        col1 (str): The column name for the first set of scores.
        col2 (str): The column name for the second set of scores.
        title (str): Title for the scatter plot.
    """
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data[col1], y=data[col2], alpha=0.7)
    plt.title(title)
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.grid(True)
    plt.show()

def plot_bland_altman(data1, data2, title):
    """
    Generate a Bland-Altman plot for two sets of scores.

    Parameters:
        data1 (Series): The first set of scores.
        data2 (Series): The second set of scores.
        title (str): Title for the Bland-Altman plot.
    """
    mean = (data1 + data2) / 2
    diff = data1 - data2  # Difference between measurements
    mean_diff = diff.mean()
    std_diff = diff.std()

    plt.figure(figsize=(8, 6))
    plt.scatter(mean, diff, alpha=0.7)
    plt.axhline(mean_diff, color='red', linestyle='--', label='Mean Difference')
    plt.axhline(mean_diff + 1.96 * std_diff, color='blue', linestyle='--', label='+1.96 SD')
    plt.axhline(mean_diff - 1.96 * std_diff, color='blue', linestyle='--', label='-1.96 SD')
    plt.title(title)
    plt.xlabel('Mean of Two Measures')
    plt.ylabel('Difference Between Measures')
    plt.legend()
    plt.grid(True)
    plt.show()  

# Example usage
if __name__ == "__main__":
    # Load the dataset 
    file_path = "/Users/ezcubing/CS_6968/Problem set 1 - Validity, Reliability.xlsx" 
    df = pd.read_excel(file_path)

    # Generate scatter plots for Test-Retest Reliability
    scatter_pairs = [
        ("Estimated FRS Score (In-clinic, Week 0)", "Estimated FRS Score (Remote, Week 1)", "Test-Retest: In-Clinic vs Remote Week 1"),
        ("Estimated FRS Score (Remote, Week 1)", "Estimated FRS Score (Remote, Week 2)", "Test-Retest: Remote Week 1 vs Remote Week 2"),
        ("Estimated FRS Score (In-clinic, Week 0)", "Estimated FRS Score (Remote, Week 2)", "Test-Retest: In-Clinic vs Remote Week 2")
    ]

    for col1, col2, title in scatter_pairs:
        plot_scatter(df, col1, col2, title)

    # Generate Bland-Altman plots for Test-Retest Reliability
    bland_altman_pairs = [
        (df["Estimated FRS Score (In-clinic, Week 0)"], df["Estimated FRS Score (Remote, Week 1)"], "Bland-Altman: In-Clinic vs Remote Week 1"),
        (df["Estimated FRS Score (Remote, Week 1)"], df["Estimated FRS Score (Remote, Week 2)"], "Bland-Altman: Remote Week 1 vs Remote Week 2"),
        (df["Estimated FRS Score (In-clinic, Week 0)"], df["Estimated FRS Score (Remote, Week 2)"], "Bland-Altman: In-Clinic vs Remote Week 2")
    ]

    for data1, data2, title in bland_altman_pairs:
        plot_bland_altman(data1, data2, title)

    # Generate scatter plots for Criterion Validity
    criterion_pairs = [
        ("Observed FRS Score (Doctor, Week 0)", "Estimated FRS Score (In-clinic, Week 0)", "Criterion Validity: Doctor vs In-Clinic"),
        ("Observed FRS Score (Therapist, Week 0)", "Estimated FRS Score (In-clinic, Week 0)", "Criterion Validity: Therapist vs In-Clinic"),
        ("Observed FRS Score (Caregiver, Week 0)", "Estimated FRS Score (In-clinic, Week 0)", "Criterion Validity: Caregiver vs In-Clinic")
    ]

    for col1, col2, title in criterion_pairs:
        plot_scatter(df, col1, col2, title)
 
