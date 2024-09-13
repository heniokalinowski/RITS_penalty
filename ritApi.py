# python support for http://rit.306w.ca/RIT-REST-API/#
# no support for "idiot resistance"
import requests

# get

def _url(path):
    return 'http://10.1.7.22:10009/v1' + path


def case_get(ses):
    return ses.get(_url('/case')).json()


def trader_get(ses):
    return ses.get(_url('/trader')).json()


def limits_get(ses):
    return ses.get(_url('/limits')).json()


def news_get(ses, since=None, limit=None):
    """
    since - Retrieve only news items after a particular news id. 
    limit - Result set limit, counting backwards from the most recent news item. Defaults to 20.
    """
    payload = {}
    if (since is not None) and (limit is not None):
        payload = {'since': since, 'limit': limit}
    elif since is not None:
        payload = {'since': since}
    elif limit is not None:
        payload = {'limit': limit}
    return ses.get(_url('/news'), params=payload).json()


def assets_get(ses, ticker=None):
    payload = {}
    if ticker is not None:
        payload = {'ticker': ticker}
    return ses.get(_url('/assets'), params=payload).json()


def securities_get(ses, ticker=None):
    if ticker is not None:
        payload = {'ticker': ticker}
        return ses.get(_url('/securities'), params=payload).json()[0]
    else:
        return ses.get(_url('/securities')).json()


def securities_book_get(ses, ticker, limit=1000):
    """
    limit - Maximum number of orders to return for each side of the order book. Defaults to 20.
    """
    if limit is not None:
        payload = {'ticker': ticker, 'limit': limit}
    else:
        payload = {'ticker': ticker}
    return ses.get(_url('/securities/book'), params=payload).json()


def securities_history_get(ses, ticker, period=None, limit=None):
    """
    period - Period to retrieve data from. Defaults to the current period.
    limit - Result set limit, counting backwards from the most recent tick. Defaults to retrieving the entire period.
    """
    if (period is not None) and (limit is not None):
        payload = {'ticker': ticker, 'period': period, 'limit': limit}
    elif period is not None:
        payload = {'ticker': ticker, 'period': period}
    elif limit is not None:
        payload = {'ticker': ticker, 'limit': limit}
    else:
        payload = {'ticker': ticker}
    return ses.get(_url('/securities/history'), params=payload).json()


def securities_tas_get(ses, ticker, period=None, limit=None):
    """
    period - Period to retrieve data from. Defaults to the current period.
    limit - Ticks to include, counting backwards from the most recent tick. Defaults to retrieving the entire period.
    """
    if (period is not None) and (limit is not None):
        payload = {'ticker': ticker, 'period': period, 'limit': limit}
    elif period is not None:
        payload = {'ticker': ticker, 'period': period}
    elif limit is not None:
        payload = {'ticker': ticker, 'limit': limit}
    else:
        payload = {'ticker': ticker}
    return ses.get(_url('/securities/tas'), params=payload).json()


def orders_get(ses, status):
    """
    STATUS: OPEN, TRANSACTED, CANCELLED
    """
    payload = {'status': status}
    return ses.get(_url('/orders'), params=payload).json()


def orders_id_get(ses, id):
    """
    id - the id of the order
    """
    url = _url('/orders/') + '{}'.format(id)
    return ses.get(url).json()


def tenders_get(ses):
    return ses.get(_url('/tenders')).json()


def leases_get(ses):
    return ses.get(_url('/leases')).json()


def leases_id_get(ses, id):
    """
    id - The id of the asset lease.
    """
    url = _url('/leases/') + '{}'.format(id)
    return ses.get(url).json()


# post
def orders_market_post(ses, ticker, action, quantity, dry_run=0):
    """
    action: BUY, SELL
    quantity - quantity
    dry_run - Simulates the order execution and returns the result as if the order was executed.
    """
    payload = {'ticker': ticker, 'type': 'MARKET',
               'quantity': quantity, 'action': action, "dry_run": dry_run}

    return ses.post(_url('/orders'), params=payload).json()


def orders_limit_post(ses, ticker, action, quantity, price):
    """
    action: BUY, SELL
    quantity - quantity
    price - price
    """
    payload = {'ticker': ticker, 'type': 'LIMIT',
               'quantity': quantity, 'action': action, "price": price}
    return ses.post(_url('/orders'), params=payload).json()


def tenders_id_post(ses, id, price=None):
    """
    id - The id of the tender.
    price - Required if the tender is not fixed-bid.
    """
    url = _url('/tenders/') + '{}'.format(id)
    payload = {"price": price}
    return ses.post(url, params=payload).json()


def commands_cancel_post(ses, ticker=None, ids=None, query=None, all_flag=0):
    """ 
    ticker - Cancel all open orders for a security.
    ids: Cancel a set of orders referenced via a comma-separated list of order ids. For example, 12,13,91,1.
    query example: 'Ticker='CL' AND Price>124.23 AND Volume<0'
    all_flag - Set to 1 to cancel all open orders.
    """
    payload = {'all': all_flag, 'ticker': ticker, "ids": ids, "query": query}
    return ses.post(_url("/commands/cancel"), params=payload).json()


def commands_cancel_all_open_orders_post(ses):
    commands_cancel_post(ses, '', '', '', all_flag=1)


def leases_post(ses, ticker, from1=None, quantity1=None,
                from2=None, quantity2=None, from3=None, quantity3=None):
    """
    ticker - Ticker of the asset to lease or use.
    from1- Required for assets that can be used without leasing first (such as REFINERY type assets). Specifies the source ticker.
    quantity1-Required for assets that can be used without leasing first (such as REFINERY type assets). Specifies the source quantity.
    from2 - Specifies the 2nd source ticker (if required).
    quantity2 - Specifies the 2nd source quantity (if required).
    from3 -Specifies the 3rd source ticker (if required).
    quantity3 -Specifies the 3rd source quantity (if required).
    """
    payload = {"ticker": ticker, "from1": from1, "quantity1": quantity1,
               "from2": from2, "quantity2": quantity2, "from3": from3, "quantity3": quantity3}
    return ses.post(_url("/leases"), params=payload).json()


def leases_id_post(ses, ticker, from1, quantity1, id,
                   from2=None, quantity2=None, from3=None, quantity3=None):
    """
    from1 - Specifies the 1st source ticker.
    quantity1 - Specifies the 1st source quantity.
    from2 - Specifies the 2nd source ticker (if required).
    quantity2 - Specifies the 2nd source quantity (if required).
    from3 - Specifies the 3rd source ticker (if required).
    quantity3 -Specifies the 3rd source quantity (if required).
    id - The id of the asset lease.
    """
    payload = {"ticker": ticker, "from1": from1, "quantity1": quantity1,
               "from2": from2, "quantity2": quantity2, "from3": from3, "quantity3": quantity3}
    url = _url("/leases") + '{}'.format(id)
    return ses.post(url, params=payload).json()


# delete
def orders_id_delete(ses, id):
    """
    id - the id of the order
    """
    return ses.delete(_url('/orders/{}'.format(id))).json()


def tenders_id_delete(ses, id):
    """
    id - The id of the tender.
    """
    return ses.delete(_url('/tenders/{}'.format(id))).json()


def leases_id_delete(ses, id):
    """
    The id of the asset lease.
    """
    return ses.delete(_url('/leases/{}'.format(id))).json()
