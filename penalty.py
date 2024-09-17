from typing import List

import numpy as np
import pandas as pd

import unmarshaller
from delta.vollib import calculate_deltas
from financial_instruments_to_data_frame import financial_instruments_to_dataframe
from model.FinancialInstrument import FinancialInstrument


def calculate_penalty(df: pd.DataFrame, delta_limit: float = 1_000, delta_penalty_in_percentage: float = 0.5) -> float:
    portfolio_delta = df['delta'] * df['position']
    delta_sum = abs(portfolio_delta.sum())

    return 0 if delta_sum <= delta_limit else (delta_sum - delta_limit) * 0.01 * delta_penalty_in_percentage

def calculate_penalty_for_json(json: str) -> float:
    financial_instruments: List[FinancialInstrument] = unmarshaller.unmarshall_to_financial_instruments(json)
    dataframe: pd.DataFrame = financial_instruments_to_dataframe(financial_instruments)

    dataframe['position'] = np.random.randint(-10_000, 10_000, size=len(dataframe))

    # compacted_dataframe: pd.DataFrame = compact(dataframe)
    deltas: pd.DataFrame = calculate_deltas(dataframe)
    penalty: float = calculate_penalty(deltas)

    return penalty