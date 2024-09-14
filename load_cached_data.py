import unmarshaller
from financial_instruments_to_data_frame import financial_instruments_to_dataframe

with open('/home/elentirald/PycharmProjects/RITS_penalty/securities.json', 'r', encoding='utf-8') as file:
    json = file.read()

financial_instruments = unmarshaller.unmarshall_to_financial_instruments(json)

dataframe = financial_instruments_to_dataframe(financial_instruments)

print(dataframe)
