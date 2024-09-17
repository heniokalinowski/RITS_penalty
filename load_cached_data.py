import pandas as pd

import unmarshaller
from delta.quantlib import calculate_deltas_quantlib
from delta.vollib import calculate_implied_volatilities
from financial_instruments_to_data_frame import financial_instruments_to_dataframe
from utilities.dataframe_compact import compact


with open('/home/elentirald/PycharmProjects/RITS_penalty/securities.json', 'r', encoding='utf-8') as file:
    json = file.read()

financial_instruments = unmarshaller.unmarshall_to_financial_instruments(json)

dataframe = financial_instruments_to_dataframe(financial_instruments)

compacted_dataframe = compact(dataframe)
deltas = calculate_implied_volatilities(dataframe)
quantlib_result = calculate_deltas_quantlib(dataframe)
print(quantlib_result)

