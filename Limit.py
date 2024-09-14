class Limit:
    def __init__(self, name: str, units: float):
        self.name = name
        self.units = units

def from_dict(data: dict):
    return Limit(
        name=data.get('name', ''),
        units=data.get('units', 0.0)
    )