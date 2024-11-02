import pandas as pd
import matplotlib.pyplot as plt
import seaborn.objects as so


def load():
    url = "https://data.cdc.gov/api/views/8pt5-q6wp/rows.csv?accessType=DOWNLOAD"
    df = pd.read_csv(url)
    df_subset = df.loc[(df["Group"] == "By State") \
    &(df["Time Period Start Date"] == "05/07/2020"), \
    ["Indicator", "Group", "State", "Time Period Start Date", \
    "Time Period End Date", "Value", "High CI"]]
    pivoted = df_subset.pivot(index="State", columns="Indicator", values="Value")
    regions = pd.read_csv("https://github.com/cphalpert/census-regions/raw/refs/heads/master/us%20census%20bureau%20regions%20and%20divisions.csv")
    return pivoted, regions

def summarise(df):
    """Get summary statistics for indicator values"""
    summary = df.describe()
    return summary.loc['mean', :]

def scatter(df):
    f = plt.figure(figsize=(12,8))
    so.Plot(df, x="Symptoms of Anxiety Disorder", y="Symptoms of Depressive Disorder")\
        .add(so.Dots()).add(so.Text(fontsize=8), \
        text="State") \
    .label(
        x="% of Sample Reporting Anxiety Symptoms",
        y="% of Sample Reporting Depressive Symptoms",
        title="Anxiety & Depression Symptoms By State During Early COVID",
    ).on(f).show()
    return "Success"

def anx_boxplot(pivoted, regions):
    merged = pd.merge(pivoted, regions, on="State", how='outer', indicator=True)
    merged.boxplot(column="Symptoms of Anxiety Disorder", by="Division", \
        grid=False, figsize = (12,8))
    plt.xticks(rotation=45)
    plt.xlabel("Regional Division")
    plt.ylabel("Anxiety Symptoms % Distribution")
    plt.title("Anxiety Symptoms By Region During Early COVID")
    plt.show()
    return "Success"

def dep_boxplot(pivoted, regions):
    merged = pd.merge(pivoted, regions, on="State", how='outer', indicator=True)
    merged.boxplot(column="Symptoms of Depressive Disorder", by="Division", \
        grid=False, figsize = (12,8))
    plt.xticks(rotation=45)
    plt.xlabel("Regional Division")
    plt.ylabel("Depressive Symptoms % Distribution")
    plt.title("Depressive Symptoms By Region During Early COVID")
    plt.show()
    return "Success"