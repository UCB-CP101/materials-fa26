import pandas as pd

def compute_stats(df: pd.DataFrame, col1: str= 'x', col2: str= 'y') -> pd.DataFrame:
    """
    Computes a DataFrame with mean, standard deviation, and correlation coefficient
    for the given two columns.

    Parameters:
    - df: pd.DataFrame, the input DataFrame
    - col1: str, name of the first column
    - col2: str, name of the second column

    Returns:
    - pd.DataFrame with mean, std, and correlation coefficient
    """
    summary = pd.DataFrame({
        "Mean": [df[col1].mean(), df[col2].mean()],
        "Std": [df[col1].std(), df[col2].std()],
        "Corr": [df[col1].corr(df[col2]), df[col1].corr(df[col2])]  # Corr is repeated for both rows
    }, index=[col1, col2])

    return summary.round(1)
