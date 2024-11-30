import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define file paths with descriptive variable names
DATA_DIR = "data"  # Assuming data files are in a folder named "data"
PAGU_FILE = "pagu-dana-desa.csv"
REALISASI_FILE = "realisasi-dana-desa.csv"


def load_data():
    """
    Reads and merges pagu and realisasi dataframes.

    Returns:
        pd.DataFrame: Merged dataframe containing pagu and realisasi data.
    """

    pagu_df = pd.read_csv(f"{DATA_DIR}/{PAGU_FILE}", delimiter="\t")
    realisasi_df = pd.read_csv(f"{DATA_DIR}/{REALISASI_FILE}", delimiter="\t")

    merged_df = pagu_df.merge(realisasi_df, on=["kdprov", "kdpemda"])
    merged_df = merged_df.rename(
        columns={"nilai_x": "pagu", "nilai_y": "realisasi"}
    )

    return merged_df


def clean_data(df):
    """
    Drops rows with missing values (NaN).

    Args:
        df (pd.DataFrame): Dataframe to clean.

    Returns:
        pd.DataFrame: Cleaned dataframe with missing values removed.
    """

    return df.dropna()


def calculate_utilization(df):
    """
    Calculates the utilization rate (realisasi / pagu).

    Args:
        df (pd.DataFrame): Dataframe containing pagu and realisasi columns.

    Returns:
        pd.DataFrame: Dataframe with a new 'utilisasi' column.
    """

    df["utilisasi"] = df["realisasi"] / df["pagu"]
    return df


def plot_scatter(df, x_col, y_col):
    """
    Creates a scatter plot of two columns from the dataframe.

    Args:
        df (pd.DataFrame): Dataframe containing the data.
        x_col (str): Name of the column for the x-axis.
        y_col (str): Name of the column for the y-axis.
    """

    sns.scatterplot(x=x_col, y=y_col, data=df, alpha=0.7)
    plt.xlabel(f"{x_col.title()}")
    plt.ylabel(f"{y_col.title()}")
    plt.title(f"Scatter Plot of {x_col.title()} vs. {y_col.title()}")
    plt.show()


def plot_normal_distribution(df, col):
    """
    Creates a histogram with a normal distribution curve for a specific column.

    Args:
        df (pd.DataFrame): Dataframe containing the data.
        col (str): Name of the column to analyze.
    """

    plt.figure(figsize=(8, 6))
    sns.histplot(df[col], kde=True, color="blue", bins=30, stat="density", linewidth=0)
    plt.title(f"Normal Distribution of {col.title()}", fontsize=16)
    plt.xlabel(f"{col.title()}", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    data = load_data()
    data = clean_data(data)
    data = calculate_utilization(data)

    plot_scatter(data, "pagu", "utilisasi")
    plot_normal_distribution(data, "utilisasi")