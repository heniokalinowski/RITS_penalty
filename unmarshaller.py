import json
from typing import List, Optional

import FinancialInstrument


def unmarshall_to_financial_instruments(json_string: str) -> List[FinancialInstrument]:
    data = json.loads(json_string)

    return [FinancialInstrument.from_dict(item) for item in data]
