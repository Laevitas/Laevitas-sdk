from enum import Enum


def prepare_query(**kwargs):
    queryurl = "?"
    for key, value in kwargs.items():
        if value == "":
            continue
        else:
            x = key + "=" + value + "&"
            queryurl += x
    queryurl = queryurl[:-1]
    return queryurl


class MARKET_CONSTS(Enum):
    BIT = -1
    DERIBIT = 0
    BITCOM = 1
    OKEX = 2
    POWERTRADE = 3
    BINANCE = 4
    DELTA_EXCHANGE = 5
    ZETA_EXCHANGE = 6
    BITMEX = 7
    BYBIT = 8
    DYDX = 9
    BITFINEX = 10
    HUOBI = 11
    KRAKEN = 12
    OKX = 13
    KWENTA = 14
    GMX = 15
    VERTEX = 16
    PERP_PROTOCOL = 17
    BITGET = 18
    AEVO = 19
    LYRA = 20
    LYRA_ARBITRUM = 21



class MARKET_CONSTS_DERIVS(Enum):
    BITMEX = -1
    BINANCE = 0
    FTX = 1
    BYBIT = 2
    DYDX = 3
    BITFINEX = 4
    DERIBIT = 5
    HUOBI = 6
    KRAKEN = 7
    OKEX = 8
