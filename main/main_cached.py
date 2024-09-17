from penalty import calculate_penalty_for_json


with open('/home/elentirald/PycharmProjects/RITS_penalty/securities.json', 'r', encoding='utf-8') as file:
    json: str = file.read()

penalty: float = calculate_penalty_for_json(json)

print(penalty)