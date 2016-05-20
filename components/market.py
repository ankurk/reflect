from yahoo_finance import Share, Currency
from flask import current_app


def get_stock_list():
    stock_list = current_app.config.get('STOCKS').split(',')
    return stock_list


def get_currs():
    currs = current_app.config.get('CURRS').split(',')
    return currs


def get_stock_prices(stocks):

    data = []
    for s in stocks:
        stock_data = {}
        share = Share(s)
        percent_change = round(float(share.get_change()) / float(share.get_prev_close()) * 100, 2)
        stock_data['symbol'] = s
        stock_data['price'] = round(float(share.get_price()), 2)
        stock_data['change_percent'] = percent_change
        data.append(stock_data)
    return data


def get_curr_prices(currs):

    data = []
    for c in currs:
        curr_data = {}
        curr = Currency(c)
        curr_data['symbol'] = c
        curr_data['price'] = round(float(curr.get_rate()), 2)
        data.append(curr_data)
    return data


def get_market_prices():

    stocks = get_stock_list()
    currs = get_currs()
    prices = {}

    prices['stocks'] = get_stock_prices(stocks)
    prices['currencies'] = get_curr_prices(currs)

    return prices


