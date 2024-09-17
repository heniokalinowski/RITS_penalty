import pandas as pd
from py_vollib.black_scholes.implied_volatility import implied_volatility


def parse_ticker(ticker: str) -> (int, str, int):
    months_to_expiry = int(ticker[3])
    option_type = ticker[4].lower()
    strike_price = int(ticker[5:])

    return strike_price, option_type, months_to_expiry

def calculate_implied_volatility(underlying_price: float, row: pd.Series) -> float:
    return implied_volatility(
        row['last'],
        underlying_price,
        row['strike'],
        row['months_to_expiry'] / 12.0,
        row['interest_rate'],
        row['option_type']
    )

def calculate_implied_volatilities(df: pd.DataFrame) -> pd.DataFrame:
    stock = df.iloc[0, :]
    options = df.iloc[1:, :]

    options['strike'], options['option_type'], options['months_to_expiry'] = zip(*options['ticker'].apply(parse_ticker))

    underlying_price: float = stock['last']

    options['implied_volatility'] = options.apply(lambda it: calculate_implied_volatility(underlying_price, it), axis='columns')

    return options
