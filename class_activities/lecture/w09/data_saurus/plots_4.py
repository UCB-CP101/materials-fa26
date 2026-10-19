import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_scatter_grid(dfs: list[pd.DataFrame], cols: tuple[str, str]=('x','y'), figsize: tuple = (10, 10)):
    """
    Plots a 2x2 grid of scatterplots using a list of four DataFrames.

    Parameters:
    - dfs: list of pd.DataFrame, must contain exactly 4 DataFrames
    - cols: tuple (str, str), column names to plot (x, y)
    - figsize: tuple, figure size

    Returns:
    - Displays a 2x2 scatterplot grid
    """
    if len(dfs) != 4:
        raise ValueError("The function requires exactly 4 DataFrames.")

    fig, axes = plt.subplots(2, 2, figsize=figsize)

    for ax, df, title in zip(axes.flat, dfs, [f"Plot {i + 1}" for i in range(4)]):
        if all(col in df for col in cols):
            # x = df.loc[:, cols[0]]
            # y = df.loc[:, cols[1]]
            sns.scatterplot(data=df, x=cols[0], y=cols[1], ax=ax, alpha=0.7, edgecolor=None)
            # sns.jointplot(x=x, y=y, ax=ax, alpha=0.7, kind="scatter", color="#4CB391")

        else:
            ax.set_xticks([])
            ax.set_yticks([])
            title += " (Columns not found)"
        ax.set_title(title)

    plt.tight_layout()
    plt.show()
