import pandas as pd


def compact(df: pd.DataFrame) -> pd.DataFrame:
    return df.loc[:, (df != df.iloc[0]).any()]