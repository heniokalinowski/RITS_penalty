import pandas as pd


def calculate_penalty(df: pd.DataFrame, delta_limit: float = 1_000, delta_penalty_in_percentage: float = 0.5) -> float:
    portfolio_delta = df['delta'] * df['position']
    delta_sum = abs(portfolio_delta.sum())

    return 0 if delta_sum <= delta_limit else (delta_sum - delta_limit) * 0.01 * delta_penalty_in_percentage