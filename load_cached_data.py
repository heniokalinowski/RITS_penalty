import unmarshaller

with open('/home/elentirald/PycharmProjects/RITS_penalty/securities.json', 'r', encoding='utf-8') as file:
    json = file.read()

financial_instruments = unmarshaller.unmarshall_to_financial_instruments(json)

print(financial_instruments)
