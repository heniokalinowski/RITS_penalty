from typing import List

import numpy as np
import pandas as pd

import unmarshaller
from delta.vollib import calculate_deltas
from financial_instruments_to_data_frame import financial_instruments_to_dataframe
from model.FinancialInstrument import FinancialInstrument
from penalty import calculate_penalty
from utilities.dataframe_compact import compact


with open('/home/elentirald/PycharmProjects/RITS_penalty/securities.json', 'r', encoding='utf-8') as file:
    json = file.read()

financial_instruments: List[FinancialInstrument] = unmarshaller.unmarshall_to_financial_instruments(json)
dataframe: pd.DataFrame = financial_instruments_to_dataframe(financial_instruments)

dataframe['position'] = np.random.randint(-10_000, 10_000, size=len(dataframe))

# compacted_dataframe: pd.DataFrame = compact(dataframe)
deltas: pd.DataFrame = calculate_deltas(dataframe)
penalty: float = calculate_penalty(deltas)

print(deltas)
