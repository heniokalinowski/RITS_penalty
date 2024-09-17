from typing import List

import pandas as pd

from model.FinancialInstrument import FinancialInstrument


def financial_instruments_to_dataframe(instruments: List[FinancialInstrument]) -> pd.DataFrame:
    data = []

    for instrument in instruments:
        instrument_data = {
            'ticker': instrument.ticker,
            'type': instrument.type,
            'size': instrument.size,
            'position': instrument.position,
            'vwap': instrument.vwap,
            'nlv': instrument.nlv,
            'last': instrument.last,
            'bid': instrument.bid,
            'bid_size': instrument.bid_size,
            'ask': instrument.ask,
            'ask_size': instrument.ask_size,
            'volume': instrument.volume,
            'unrealized': instrument.unrealized,
            'realized': instrument.realized,
            'currency': instrument.currency,
            'total_volume': instrument.total_volume,
            'interest_rate': instrument.interest_rate,
            'is_tradeable': instrument.is_tradeable,
            'is_shortable': instrument.is_shortable,
            'start_period': instrument.start_period,
            'stop_period': instrument.stop_period,
            'description': instrument.description,
            'unit_multiplier': instrument.unit_multiplier,
            'display_unit': instrument.display_unit,
            'start_price': instrument.start_price,
            'min_price': instrument.min_price,
            'max_price': instrument.max_price,
            'quoted_decimals': instrument.quoted_decimals,
            'trading_fee': instrument.trading_fee,
            'limit_order_rebate': instrument.limit_order_rebate,
            'min_trade_size': instrument.min_trade_size,
            'max_trade_size': instrument.max_trade_size,
            'required_tickers': instrument.required_tickers,
            'underlying_tickers': instrument.underlying_tickers,
            'bond_coupon': instrument.bond_coupon,
            'interest_payments_per_period': instrument.interest_payments_per_period,
            'base_security': instrument.base_security,
            'fixing_ticker': instrument.fixing_ticker,
            'api_orders_per_second': instrument.api_orders_per_second,
            'execution_delay_ms': instrument.execution_delay_ms,
            'interest_rate_ticker': instrument.interest_rate_ticker,
            'otc_price_range': instrument.otc_price_range
        }

        # Przetworzenie limitów do prostszej formy, np. jako listy nazw
        instrument_data['limits'] = ', '.join([limit.name for limit in instrument.limits])

        # Dodanie danych dla jednego instrumentu do listy
        data.append(instrument_data)

    # Konwersja listy słowników na pandasowy DataFrame
    df = pd.DataFrame(data)

    return df
