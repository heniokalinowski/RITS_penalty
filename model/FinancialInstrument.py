from typing import Optional, List

import Limit


class FinancialInstrument:
    def __init__(self, ticker: str, type: str, size: float, position: float, vwap: float, nlv: float,
                 last: float, bid: float, bid_size: float, ask: float, ask_size: float, volume: float,
                 unrealized: float, realized: float, currency: str, total_volume: float,
                 limits: List[Limit], interest_rate: float, is_tradeable: bool, is_shortable: bool,
                 start_period: int, stop_period: int, description: str, unit_multiplier: float,
                 display_unit: str, start_price: float, min_price: float, max_price: float,
                 quoted_decimals: int, trading_fee: float, limit_order_rebate: float, min_trade_size: int,
                 max_trade_size: int, required_tickers: Optional[List[str]], underlying_tickers: Optional[List[str]],
                 bond_coupon: float, interest_payments_per_period: int, base_security: str,
                 fixing_ticker: Optional[str], api_orders_per_second: int, execution_delay_ms: int,
                 interest_rate_ticker: Optional[str], otc_price_range: float):
        self.ticker = ticker
        self.type = type
        self.size = size
        self.position = position
        self.vwap = vwap
        self.nlv = nlv
        self.last = last
        self.bid = bid
        self.bid_size = bid_size
        self.ask = ask
        self.ask_size = ask_size
        self.volume = volume
        self.unrealized = unrealized
        self.realized = realized
        self.currency = currency
        self.total_volume = total_volume
        self.limits = limits
        self.interest_rate = interest_rate
        self.is_tradeable = is_tradeable
        self.is_shortable = is_shortable
        self.start_period = start_period
        self.stop_period = stop_period
        self.description = description
        self.unit_multiplier = unit_multiplier
        self.display_unit = display_unit
        self.start_price = start_price
        self.min_price = min_price
        self.max_price = max_price
        self.quoted_decimals = quoted_decimals
        self.trading_fee = trading_fee
        self.limit_order_rebate = limit_order_rebate
        self.min_trade_size = min_trade_size
        self.max_trade_size = max_trade_size
        self.required_tickers = required_tickers
        self.underlying_tickers = underlying_tickers
        self.bond_coupon = bond_coupon
        self.interest_payments_per_period = interest_payments_per_period
        self.base_security = base_security
        self.fixing_ticker = fixing_ticker
        self.api_orders_per_second = api_orders_per_second
        self.execution_delay_ms = execution_delay_ms
        self.interest_rate_ticker = interest_rate_ticker
        self.otc_price_range = otc_price_range


def from_dict(data: dict):
    limits = [Limit.from_dict(limit) for limit in data.get('limits', [])]

    return FinancialInstrument(
        ticker=data.get('ticker', ''),
        type=data.get('type', ''),
        size=data.get('size', 0.0),
        position=data.get('position', 0.0),
        vwap=data.get('vwap', 0.0),
        nlv=data.get('nlv', 0.0),
        last=data.get('last', 0.0),
        bid=data.get('bid', 0.0),
        bid_size=data.get('bid_size', 0.0),
        ask=data.get('ask', 0.0),
        ask_size=data.get('ask_size', 0.0),
        volume=data.get('volume', 0.0),
        unrealized=data.get('unrealized', 0.0),
        realized=data.get('realized', 0.0),
        currency=data.get('currency', ''),
        total_volume=data.get('total_volume', 0.0),
        limits=limits,
        interest_rate=data.get('interest_rate', 0.0),
        is_tradeable=data.get('is_tradeable', False),
        is_shortable=data.get('is_shortable', False),
        start_period=data.get('start_period', 0),
        stop_period=data.get('stop_period', 0),
        description=data.get('description', ''),
        unit_multiplier=data.get('unit_multiplier', 1),
        display_unit=data.get('display_unit', ''),
        start_price=data.get('start_price', 0.0),
        min_price=data.get('min_price', 0.0),
        max_price=data.get('max_price', 0.0),
        quoted_decimals=data.get('quoted_decimals', 2),
        trading_fee=data.get('trading_fee', 0.0),
        limit_order_rebate=data.get('limit_order_rebate', 0.0),
        min_trade_size=data.get('min_trade_size', 0),
        max_trade_size=data.get('max_trade_size', 0),
        required_tickers=data.get('required_tickers', None),
        underlying_tickers=data.get('underlying_tickers', None),
        bond_coupon=data.get('bond_coupon', 0.0),
        interest_payments_per_period=data.get('interest_payments_per_period', 0),
        base_security=data.get('base_security', ''),
        fixing_ticker=data.get('fixing_ticker', None),
        api_orders_per_second=data.get('api_orders_per_second', 10),
        execution_delay_ms=data.get('execution_delay_ms', 0),
        interest_rate_ticker=data.get('interest_rate_ticker', None),
        otc_price_range=data.get('otc_price_range', 0.0)
    )
