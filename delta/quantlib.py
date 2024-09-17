import QuantLib as ql
import pandas as pd
from typing import List


def calculate_deltas_quantlib(df: pd.DataFrame) -> List[float]:
    deltas = []

    # Zakładamy, że DataFrame zawiera kolumny, które zawierają te wartości
    for _, row in df.iterrows():
        if row['type'] == 'OPTION':
            # Pobieranie wartości z DataFrame
            spot_price = row['last']
            strike_price = row['start_price']
            volatility = row['trading_fee'] / 100  # Możemy użyć 'trading_fee' jako przybliżenia zmienności
            risk_free_rate = row['interest_rate'] / 100  # Korzystamy z pola 'interest_rate'
            start_date = ql.Date(13, 9, 2024)  # Przykładowa data startowa
            expiration_days = (row['stop_period'] - row['start_period']) * 30  # Przekształcamy okres na dni
            expiration_date = ql.Date(start_date.serialNumber() + expiration_days)  # Data wygaśnięcia

            # Parametry opcji
            option_type = ql.Option.Call if row['description'].lower().find('call') != -1 else ql.Option.Put
            payoff = ql.PlainVanillaPayoff(option_type, strike_price)
            exercise = ql.EuropeanExercise(expiration_date)
            option = ql.VanillaOption(payoff, exercise)

            # Zmienna procesowa
            spot_handle = ql.QuoteHandle(ql.SimpleQuote(spot_price))
            rate_handle = ql.YieldTermStructureHandle(ql.FlatForward(start_date, risk_free_rate, ql.Actual365Fixed()))
            volatility_handle = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(start_date, ql.NullCalendar(), volatility, ql.Actual365Fixed()))

            process = ql.BlackScholesProcess(spot_handle, rate_handle, volatility_handle)

            # Ustawienie silnika wyceny
            option.setPricingEngine(ql.AnalyticEuropeanEngine(process))

            # Wycena opcji i obliczenie delty
            option.NPV()  # Obliczamy wartość opcji
            delta = option.delta()  # Pobieramy deltę

            deltas.append(delta)

    return deltas