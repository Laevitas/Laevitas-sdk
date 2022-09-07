import requests
from Laevitas.dataclasses import *
# from dataclasses import dataclass, field, make_dataclass
from enum import Enum
# from typing import List


def query(**kwargs):
    queryurl="?"
    for key, value in kwargs.items():
        if value == "":
            continue
        else:
            x = key+"="+value+"&"
            queryurl +=x
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
    FTX = 7


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


class CURRENCY(Enum):
    BTC = 1
    ETH = 0
    BCH = 2


class api():
    header = {"apiKey": 'none'}

    def __init__(self, key="none"):
        self.header["apiKey"] = key
        self.r = self.realtime()

    @classmethod
    def configure(self, header):
        self.header["apiKey"] = header

    class realtime:
        def __init__(self):
            self.option = self.options()

        class options:
            url = "https://api.laevitas.ch/analytics/options/"
            pass

            @classmethod
            def instruments(self,market="",currency="",maturity="",strike="",optiontype=""):

                """
                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities ( maturities function)
                :type maturity:
                :param strike: e.g., 25000
                :type strike:
                :param optiontype: C,P
                :type optiontype:
                :return: json data of dovs
                :rtype:
                """
                makequery = query(market=market, currency=currency, maturity=maturity, strike=strike,optiontype=optiontype)
                api_url = self.url + "Instruments" + makequery
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def get_atm(self, market: str, currency: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :return: returns At the money Implied Volatility Term Structure as an object with attributes alldata, Today, Yesterday, Two_days_ago, One_week_ago, Two_weeks_ago,
                Three_weeks_ago, One_month_ago
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                     api_url = self.url + "atm_iv_ts/" + market + "/" + currency
                     responsedata = requests.get(api_url, headers=api.header).json()
                     return responsedata

            @classmethod
            def gex_date(self, market: str, currency: str, maturity: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities ( maturities function)
                :type maturity:
                :return: Gamma Exposure by Expiration as a data class
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                maturity = maturity.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    maturity = maturity.upper()
                    api_url = self.url + "gex_date/" + market + "/" + currency + "/" + maturity
                    responsedata = requests.get(api_url, headers=api.header).json()
                    Response = Igex_date(responsedata,responsedata['date'])
                    for i in range(len(responsedata['data'])):
                        Response.data.append(gex_date_data(responsedata['data'][i]['strike'],
                                                           responsedata['data'][i]['optionType'],
                                                           responsedata['data'][i]['gex']
                                                           ))
                    return Response

            @classmethod
            def gex_date_all(self, market: str, currency: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :return: Gamma Exposure All Expirations
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "gex_date_all/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    Response = Igex_date_all(responsedata,responsedata['date'])
                    for i in range(len(responsedata['data'])):
                        Response.data.append(gex_date_all_data(responsedata['data'][i]['strike'],
                                                                               responsedata['data'][i]['optionType'],
                                                                             responsedata['data'][i]['gex']
                                                                               ))
                    return Response

            @classmethod
            def maturities(self, market: str, currency: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :return: json data of active expirations
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "maturities/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def oi_expiry(self, market: str, currency: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :return: Open interest by expiration
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "oi_expiry/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    Response = Iexpiry(responsedata, responsedata['date'])
                    for i in range(len(responsedata['data'])):
                        Response.data.append(expiry_data(responsedata['data'][i]['maturity'],
                                                            responsedata['data'][i]['c'],
                                                            responsedata['data'][i]['p'],
                                                            responsedata['data'][i]['notional_c'],
                                                            responsedata['data'][i]['notional_p']))
                    return Response

            @classmethod
            def oi_strike_all(self, market: str, currency: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :return: Open Interest by strike all expirations
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "oi_strike_all/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    Response = Ioi_strike_all(responsedata, responsedata['date'])
                    for i in range(len(responsedata['data'])):
                        Response.data.append(oi_strike_all_data(responsedata['data'][i]['strike'],
                                                            responsedata['data'][i]['c'],
                                                            responsedata['data'][i]['p'],
                                                            responsedata['data'][i]['notional_c'],
                                                            responsedata['data'][i]['notional_p']))
                    return Response

            @classmethod
            def oi_type(self, market: str, currency: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :return: json data of Open interest by type
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "oi_type/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def top_traded_option(self, market: str, currency: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :return: data of Top Traded Instrument
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "top_traded_option/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    Response = Itop_traded_option(responsedata, responsedata['date'])
                    for i in range(len(responsedata['data'])):
                        Response.data.append(top_traded_option_data(responsedata['data'][i]['volume'],
                                                                responsedata['data'][i]['instrument'],
                                                                responsedata['data'][i]['volume_usd']))
                    return Response

            @classmethod
            def v_expiry(self, market: str, currency: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :return: Volume by expiration
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "v_expiry/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    Response = Iexpiry(responsedata, responsedata['date'])
                    for i in range(len(responsedata['data'])):
                        Response.data.append(expiry_data(responsedata['data'][i]['maturity'],
                                                            responsedata['data'][i]['c'],
                                                            responsedata['data'][i]['p'],
                                                            responsedata['data'][i]['notional_c'],
                                                            responsedata['data'][i]['notional_p']))
                    return Response

            @classmethod
            def v_strike_all(self, market: str, currency: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :return: Volume by strike all expirations
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "v_strike_all/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    Response = v_strike_alli(responsedata, responsedata['date'])
                    for i in range(len(responsedata['data'])):
                        Response.data.append(v_strike_all_data(responsedata['data'][i]['strike'],
                                                            responsedata['data'][i]['C'],
                                                            responsedata['data'][i]['P'],
                                                            responsedata['data'][i]['USDVC'],
                                                            responsedata['data'][i]['USDVP']))
                    return Response

            @classmethod
            def volume_buy_sell_all(self, market: str, currency: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :return: json data of all volume buy/sell last 24h all expirations
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "volume_buy_sell_all/" + market.lower() + "/" + currency.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def iv_strike(self, market: str, currency: str, strike: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :param strike: e.g., 25000
                :type strike:
                :return: json data of implied volatility term structure by strike
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "iv_strike/" + market.lower() + "/" + currency.lower() + "/" + strike
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def oi_strike(self, market: str, currency: str, maturity: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities (maturities function)
                :type maturity:
                :return: json data of open interest by strike
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                maturity = maturity.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "oi_strike/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def oi_net_change_all(self, market: str, currency: str, hours: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :param hours: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720
                :type hours:
                :return: json data of Open interest change, all expirations
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "oi_net_change_all/" + market.lower() + "/" + currency.lower() + "/" + hours
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def top_instrument_oi_change(self, market: str, currency: str, hours: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :param hours: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720
                :type hours:
                :return: json data of top instrument open interest change
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "top_instrument_oi_change/" + market.lower() + "/" + currency.lower() + "/" + hours
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def volume_buy_sell(self, market: str, currency: str, maturity: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities (maturities function)
                :type maturity:
                :return: json data of volume buy sell last 24h
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                maturity = maturity.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "volume_buy_sell/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def v_strike(self, market: str, currency: str, maturity: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities (maturities function)
                :type maturity:
                :return: json data of volume by strike
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                maturity = maturity.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "v_strike/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def summary_trades(self, market: str, currency: str, hours: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :param hours: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720
                :type hours:
                :return: json data of top summary trades
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "summary_trades/" + market.lower() + "/" + currency.lower() + "/" + hours
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def greeks(self, market: str, currency: str, maturity: str, optiontype: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities (maturities function)
                :type maturity:
                :param optiontype: C,P
                :type optiontype:
                :return: greeks
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                maturity = maturity.upper()
                optiontype = optiontype.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif optiontype not in ["P", "C"]:
                    raise TypeError("type is either C or P")
                else:
                    maturity = maturity.upper()
                    api_url = self.url + "greeks/" + market + "/" + currency + "/" + maturity + "/" + optiontype
                    responsedata = requests.get(api_url, headers=api.header).json()
                    Response = Igreeks(responsedata,responsedata['date'])
                    for i in range(len(responsedata['data'])):
                        Response.data.append(greeks_data(responsedata['data'][i]['strike'],
                                                           responsedata['data'][i]['underlying_price'],
                                                           responsedata['data'][i]['delta'],
                                                           responsedata['data'][i]['gamma'],
                                                           responsedata['data'][i]['theta'],
                                                           responsedata['data'][i]['vega']
                                                           ))
                    return Response

            @classmethod
            def iv_all(self, market: str, currency: str, maturity: str, type: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities (maturities function)
                :type maturity:
                :param type: C , P
                :type type:
                :return: json data of implied volatility skew
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "iv_all/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper() + "/" + type.upper()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def iv_table(self, market: str, currency: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :return: json data of implied volatility
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "iv_table/" + market.lower() + "/" + currency.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def oi_net_change(self, market: str, currency: str, maturity: str, hour: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities (maturities function)
                :type maturity:
                :param hour: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720,
                :type hour:
                :return: json data of Open interest change by expiration
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "oi_net_change/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper() + "/" + hour
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def snapshot(self, market: str, currency: str):
                """

                :param market: BIT (BTC,ETH,BCH) | DERIBIT (BTC,ETH,SOL) | BYBIT (BTC) | OKEX (BTC,ETH,SOL) | POWERTRADE (ETH,BTC | DELTA_EXCHANGE (BTC,ETH,BCH,SOL, XRP,BNB) | ZETA_EXCHANGE (SOL)
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB
                :type currency:
                :return: json data of snapshot
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "snapshot/" + market.lower() + "/" + currency.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

        class futures:
            url = "https://api.laevitas.ch/analytics/futures/"
            pass

            @classmethod
            def instruments(self):
                """
                :return: json data of available futures instruments
                :rtype:
                """
                api_url = self.url + "instruments"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def alt_currency(self):
                """
                :return: json data of available futures currency
                :rtype:
                """
                api_url = self.url + "alt_currency"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def perpetual_funding(self,currency: str):
                """

                :param currency: BTC,ETH,BCH try the future alt_currency function for more available currency
                :type currency:
                :return: json data of perpetual funding
                :rtype:
                """
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                else:
                    api_url = self.url + "perpetual_funding/" +  currency.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def futures_yield(self,currency: str):
                """

                :param currency: BTC,ETH,BCH try the future alt_currency function for more available currency
                :type currency:
                :return: json data of futures yield
                :rtype:
                """
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                else:
                    api_url = self.url + "futures_yield/" + currency.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def futures_basis(self,currency: str):
                """

                :param currency: BTC,ETH,BCH try the future alt_currency function for more available currency
                :type currency:
                :return: json data of futures basis
                :rtype:
                """
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                else:
                    api_url = self.url + "futures_basis/" + currency.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def volume_breakdown(self,currency: str):
                """

                :param currency: BTC,ETH,BCH try the future alt_currency function for more available currency
                :type currency:
                :return: json data of volume breakdown
                :rtype:
                """
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                else:
                    api_url = self.url + "volume_breakdown/" + currency.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def oi_breakdown(self, currency: str):
                """

                :param currency: BTC,ETH,BCH try the future alt_currency function for more available currency
                :type currency:
                :return: json data of open interest breakdown
                :rtype:
                """
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                else:
                    api_url = self.url + "oi_breakdown/" + currency.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def futures_curve(self, currency: str, market = "" ):
                """

                :param currency: BTC,ETH,BCH try the future alt_currency function for more available currency
                :type currency:
                :param market: optional: Binance, Bitfinex, Bitmex, Bybit, Deribit, DyDx, FTX, Huobi, Kraken, OKEx
                :type market:
                :return: json data of futures term structure
                :rtype:
                """
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                else:
                    api_url = self.url + "oi_breakdown/" + currency.lower() + "/" + market
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def markets_oi_gainers_and_losers(self, currency: str, option: str , hour: str):
                """

                :param currency: BTC,ETH,BCH try the future alt_currency function for more available currency
                :type currency:
                :param option: perpetual, future , all
                :type option:
                :param hour: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720,
                :type hour:
                :return: json data of markets oi gainers and losers
                :rtype:
                """
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                else:
                    api_url = self.url + "markets_oi_gainers_and_losers/" + currency.lower() + "/" + option + "/" + hour
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def snapshot(self, market: str):
                """

                :param market: Binance, Bitfinex, Bitmex, Bybit, Deribit, DyDx, FTX, Huobi, Kraken, OKEx
                :type market:
                :return: json data of snapshot
                :rtype:
                """
                market = market.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "snapshot/" + market.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

        class move:
            url = "https://api.laevitas.ch//analytics/move/"
            pass

            @classmethod
            def oi_group(self):
                """
                :return: json data of open interest group
                :rtype:
                """
                api_url = self.url + "oi_group"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def oi_expiry(self):
                """
                :return: json data of open interest expiry
                :rtype:
                """
                api_url = self.url + "oi_expiry"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_expiry(self):
                """
                :return: json data of volume expiry
                :rtype:
                """
                api_url = self.url + "volume_expiry"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_group(self):
                """
                :return: json data of volume group
                :rtype:
                """
                api_url = self.url + "volume_group"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_expiry_buy_sell(self):
                """
                :return: json data of volume expiry buy sell
                :rtype:
                """
                api_url = self.url + "volume_expiry_buy_sell"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_contract_buy_sell(self):
                """
                :return: json data of volume contract buy sell
                :rtype:
                """
                api_url = self.url + "volume_contract_buy_sell"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_top_contract(self):
                """
                :return: json data of volume top contract
                :rtype:
                """
                api_url = self.url + "volume_top_contract"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_type_buy_sell(self):
                """
                :return: json data of volume type buy/sell
                :rtype:
                """
                api_url = self.url + "volume_type_buy_sell"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def oi_top_contract(self):
                """
                :return: json data of oi top contract
                :rtype:
                """
                api_url = self.url + "oi_top_contract"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def big_trades(self):
                """
                :return: json data of big trades
                :rtype:
                """
                api_url = self.url + "big_trades"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def contract_name(self):
                """
                :return: json data of contract names
                :rtype:
                """
                api_url = self.url + "contract_name"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def expirations(self):
                """
                :return: json data of expirations
                :rtype:
                """
                api_url = self.url + "expirations"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def ftx_vs_deribit(self):
                """
                :return: json data of ftx vs deribit
                :rtype:
                """
                api_url = self.url + "ftx_vs_deribit"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def live(self):
                """
                :return: json data of live
                :rtype:
                """
                api_url = self.url + "live"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

        class defi:
            url = "https://api.laevitas.ch/analytics/defi/"
            pass

            @classmethod
            def dovs(self):
                """
                :return: json data of dovs
                :rtype:
                """
                api_url = self.url + "dovs"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def ribbon(self):
                """
                :return: json data of ribbon
                :rtype:
                """
                api_url = self.url + "ribbon"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def friktion(self):
                """
                :return: json data of friktion
                :rtype:
                """
                api_url = self.url + "friktion"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def squeeth(self):
                """
                :return: json data of squeeth
                :rtype:
                """
                api_url = self.url + "squeeth"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def thetanuts(self):
                """
                :return: json data of thetanuts
                :rtype:
                """
                api_url = self.url + "thetanuts"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

        class derivs:
            url = "https://api.laevitas.ch/analytics/derivs/"
            pass


            @classmethod
            def futures(self, market: str, currency: str, maturity: str):
                """

                :param market: Full list of supported exchanges on instruments endpoint (futures.instrument function),exp: BITMEX | BINANCE | FTX | BYBIT | DYDX | BITFINEX | DERIBIT | HUOBI | KRAKEN | OKEX
                :type market:
                :param currency: BTC | ETH | ALTS (Full list of supported assets on instruments endpoint)
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23, Active expirations endpoint in options provide available maturities
                :type maturity:
                :return: json data of futures live data
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                maturity = maturity.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "futures/" + market + "/" + currency + "/" + maturity
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def perpetuals(self, market: str, currency: str):
                """

                :param market: Full list of supported exchanges on instruments endpoint (futures.instrument function),exp: BITMEX | BINANCE | FTX | BYBIT | DYDX | BITFINEX | DERIBIT | HUOBI | KRAKEN | OKEX
                :type market:
                :param currency: BTC | ETH | ALTS (Full list of supported assets on instruments endpoint)
                :type currency:
                :return: json live data of perpetual swaps
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "perpetuals/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def summary(self,currency=""):
                """

                :param currency: BTC | ETH | ALTS (Full list of supported assets on instruments endpoint)
                :type currency:
                :return: json data of summary
                :rtype:
                """
                currency = currency.upper()
                api_url = self.url + "summary/" + currency
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def oi_gainers(self, market: str, oitype: str, period: str):
                """

                :param market: Full list of supported exchanges on instruments endpoint (futures.instrument function),exp: BITMEX | BINANCE | FTX | BYBIT | DYDX | BITFINEX | DERIBIT | HUOBI | KRAKEN | OKEX
                :type market:
                :param oitype: future, perpetual
                :type oitype:
                :param period: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720, ytd
                :type period:
                :return: Open interest gainers
                :rtype:
                """
                market = market.upper()
                oitype = oitype.upper()
                if oitype not in ["FUTURE", "PERPETUAL"]:
                    raise TypeError("Type not available")
                elif market not in MARKET_CONSTS_DERIVS.__members__:
                    raise TypeError("Market not available")
                elif period not in ["1", "2", "4", "8", "12", "18", "24", "48", "168", "336", "504", "720", "ytd"]:
                    raise TypeError("period not available")
                else:
                    api_url = self.url + "oi_gainers/" + market + "/" + oitype.lower() + "/" + period
                    response = requests.get(api_url, headers=api.header).json()
                    Response = Ioi_gainers(response,response['date'])
                    for i in range(len(response['data'])):
                        Response.data.append(oi_gainers_data(response['data'][i]['symbol'],
                                                             response['data'][i]['open_interest_change'],
                                                             response['data'][i]['open_interest_change_notional']
                                                         ))
                    return Response

            @classmethod
            def price_gainers(self, market: str, oitype: str, period: str):
                """

                :param market: Full list of supported exchanges on instruments endpoint (futures.instrument function),exp: BITMEX | BINANCE | FTX | BYBIT | DYDX | BITFINEX | DERIBIT | HUOBI | KRAKEN | OKEX
                :type market:
                :param oitype: future, perpetual
                :type oitype:
                :param period: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720, ytd
                :type period:
                :return: json data of price gainers
                :rtype:
                """
                market = market.upper()
                oitype = oitype.upper()
                if oitype not in ["FUTURE", "PERPETUAL"]:
                    raise TypeError("Type not available")
                elif market not in MARKET_CONSTS_DERIVS.__members__:
                    raise TypeError("Market not available")
                elif period not in ["1", "2", "4", "8", "12", "18", "24", "48", "168", "336", "504", "720", "ytd"]:
                    raise TypeError("period not available")
                else:
                    api_url = self.url + "price_gainers/" + market + "/" + oitype.lower() + "/" + period
                    response = requests.get(api_url, headers=api.header).json()
                    return response

            @classmethod
            def top_funding(self, market: str):
                """

                :param market: Full list of supported exchanges on instruments endpoint (futures.instrument function),exp: BITMEX | BINANCE | FTX | BYBIT | DYDX | BITFINEX | DERIBIT | HUOBI | KRAKEN | OKEX
                :type market:
                :return: json data of top funding
                :rtype:
                """
                market = market.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "top_funding/" + market
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def top_gainers_losers(self, change: str ,type:str):
                """

                :param change: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720
                :type change:
                :param type: gainers , losers
                :type type:
                :return: json data of top gainers and losers
                :rtype:
                """

                api_url = self.url + "top_gainers_losers/" + change + "/" + type
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

    class historical:
        def __init__(self):
            self.option = self.options()

        class options:
            url = "https://api.laevitas.ch/historical/options/"
            pass

            @classmethod
            def option(self,market: str,instrument: str,start="",end="",limit="",page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param instrument: Currency-Maturity-Strike-C/P e.g., BTC-30JUN23-80000-C try (instruments function)
                :type instrument:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: option
                :rtype:
                """
                market=market.upper()
                instrument=instrument.upper()
                x=instrument.split("-")
                makequery = query(start=start,end=end,limit=limit,page=page)
                if len(x) != 4:
                    raise TypeError("wrong instrument")
                elif x[0] not in CURRENCY.__members__:
                    raise TypeError("Currency in insrument not available")
                elif x[3] not in ["P","C"]:
                    raise TypeError("type in instument is either C or P")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url+ market + "/" + instrument + makequery
                    response = requests.get(api_url,headers=api.header).json()
                else:
                    api_url = self.url+ market + "/" + instrument
                    response = requests.get(api_url,headers=api.header).json()
                return response

            @classmethod
            def iv(self,market: str,instrument: str,start="",end="",limit="",page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param instrument: Currency-Maturity-Strike-C/P e.g., BTC-30JUN23-80000-C try (instruments function)
                :type instrument:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: Instrument historical implied volatility
                :rtype:
                """
                market=market.upper()
                instrument=instrument.upper()
                x=instrument.split("-")
                makequery = query(start=start,end=end,limit=limit,page=page)
                if len(x) != 4:
                    raise TypeError("wrong instrument")
                elif x[0] not in CURRENCY.__members__:
                    raise TypeError("Currency in insrument not available")
                elif x[3] not in ["P","C"]:
                    raise TypeError("type in instument is either C or P")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url+ "iv/" + market + "/" + instrument + makequery
                    response = requests.get(api_url,headers=api.header).json()
                return response

            @classmethod
            def price(self,market: str,instrument: str,start="",end="",limit="",page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param instrument: Currency-Maturity-Strike-C/P e.g., BTC-30JUN23-80000-C try (instruments function)
                :type instrument:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of instrument historical price
                :rtype:
                """
                market=market.upper()
                instrument=instrument.upper()
                x=instrument.split("-")
                makequery = query(start=start,end=end,limit=limit,page=page)
                if len(x) != 4:
                    raise TypeError("wrong instrument")
                elif x[0] not in CURRENCY.__members__:
                    raise TypeError("Currency in insrument not available")
                elif x[3] not in ["P","C"]:
                    raise TypeError("type in instument is either C or P")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "price/" + market + "/" + instrument + makequery
                    response = requests.get(api_url,headers=api.header).json()
                else:
                    api_url = self.url+ "price/" + market + "/" + instrument
                    response = requests.get(api_url,headers=api.header).json()
                return response

            @classmethod
            def oi_volume(self,market: str,instrument: str,start="",end="",limit="",page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param instrument: Currency-Maturity-Strike-C/P e.g., BTC-30JUN23-80000-C try (instruments function)
                :type instrument:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of instrument historical open interest volume
                :rtype:
                """
                market=market.upper()
                instrument=instrument.upper()
                x=instrument.split("-")
                makequery = query(start=start,end=end,limit=limit,page=page)
                if len(x) != 4:
                    raise TypeError("wrong instrument")
                elif x[0] not in CURRENCY.__members__:
                    raise TypeError("Currency in insrument not available")
                elif x[3] not in ["P","C"]:
                    raise TypeError("type in instument is either C or P")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "oi_volume/" + market + "/" + instrument + makequery
                    response = requests.get(api_url,headers=api.header).json()
                else:
                    api_url = self.url + "oi_volume/" + market + "/" + instrument
                    response = requests.get(api_url,headers=api.header).json()
                return response

            @classmethod
            def underlying_price(self,market: str,instrument: str,start="",end="",limit="",page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param instrument: Currency-Maturity-Strike-C/P e.g., BTC-30JUN23-80000-C try (instruments function)
                :type instrument:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of instrument historical underlying price
                :rtype:
                """
                market=market.upper()
                instrument=instrument.upper()
                x=instrument.split("-")
                makequery = query(start=start,end=end,limit=limit,page=page)
                if len(x) != 4:
                    raise TypeError("wrong instrument")
                elif x[0] not in CURRENCY.__members__:
                    raise TypeError("Currency in insrument not available")
                elif x[3] not in ["P","C"]:
                    raise TypeError("type in instument is either C or P")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "underlying_price/" + market + "/" + instrument + makequery
                    response = requests.get(api_url,headers=api.header).json()
                else:
                    api_url = self.url + "underlying_price/" + market + "/" + instrument
                    response = requests.get(api_url,headers=api.header).json()
                return response

            @classmethod
            def oi_strike(self,market: str,currency: str, maturity: str,date: str):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities
                :type maturity:
                :param date: YYYY-MM-DDTHH e.g., 2022-07-24T01
                :type date :
                :return: json data of historical open interest by strike
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "oi_strike/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper() + "?date=" + date
                    responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_strike(self,market: str,currency: str, maturity: str,date: str):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities
                :type maturity:
                :param date: YYYY-MM-DDTHH e.g., 2022-07-24T01
                :type date :
                :return: json data of historical volume by strike
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if currency not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "volume_strike/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper() + "?date=" + date
                    responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_pc_ratio(self, market: str, currency: str,start="", end="", limit="10", page="1"):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of volume put call ratio
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "volume_pc_ratio/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "volume_pc_ratio/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def gex_index(self, market: str, currency: str,start="", end="", limit="10", page="1"):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of gamma exposure index
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "gex_index/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "gex_index/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def max_pain(self, market: str, currency: str,start="", end="", limit="10", page="1"):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of max pain monthly expiration
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "max_pain/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "max_pain/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def atm_iv(self, market: str, currency: str,start="", end="", limit="10", page="1"):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of at the money implied volatility (rolling maturity)
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "atm_iv/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "atm_iv/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def volume_total(self, market: str, currency: str,start="", end="", limit="10", page="1"):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of total volume
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "volume_total/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "volume_total/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def oi_pc_ratio(self, market: str, currency: str,start="", end="", limit="10", page="1"):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of open interests put call ratio
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "oi_pc_ratio/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "oi_pc_ratio/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def oi_total(self, market: str, currency: str,start="", end="", limit="10", page="1"):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of total open interest
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "oi_total/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "oi_total/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def vix(self, market: str, currency: str,start="", end="", limit="10", page="1"):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of vol index
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "vix/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "vix/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def dvol(self, market: str, currency: str,start="", end="", limit="10", page="1"):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,SOL
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of deribit volatility index
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "dvol/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "dvol/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def atm_iv_model(self, market: str, currency: str, type:str, start="", end="", limit="", page=""):
                """

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 25p , 10p , 25c, 10c
                :type type:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of at the money implied volatility model
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "type/atm_iv_model//" + market.lower() + "/" + currency.lower() + "/" + type + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "type/atm_iv_model/" + market.lower() + "/" + currency.lower() + "/" + type
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def butterfly(self, market: str, currency: str, type:str, start="", end="", limit="", page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param type: 25d , 10d  (d: delta)
                :type type:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of butterfly
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "type/butterfly/" + market.lower() + "/" + currency.lower() + "/" + type + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "type/butterfly/" + market.lower() + "/" + currency.lower() + "/" + type
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def butterfly_model(self, market: str, currency: str, type:str, start="", end="", limit="", page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param type: 25d , 10d (d: delta)
                :type type:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of butterfly model
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "type/butterfly_model/" + market.lower() + "/" + currency.lower() + "/" + type + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "type/butterfly_model/" + market.lower() + "/" + currency.lower() + "/" + type
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def skew(self, market: str, currency: str, type:str, start="", end="", limit="", page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 25d , 10d (d: delta)
                :type type:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of skew
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "type/skew/" + market.lower() + "/" + currency.lower() + "/" + type + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "type/skew/" + market.lower() + "/" + currency.lower() + "/" + type
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def skew_model(self, market: str, currency: str, type:str, start="", end="", limit="", page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 25d , 10d (d: delta)
                :type type:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of skew model
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "type/skew_model/" + market.lower() + "/" + currency.lower() + "/" + type + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "type/skew_model/" + market.lower() + "/" + currency.lower() + "/" + type
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def risk_reversal(self, market: str, currency: str, type:str, start="", end="", limit="", page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 25d , 10d (d: delta)
                :type type:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of risk reversal
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "type/risk_reversal/" + market.lower() + "/" + currency.lower() + "/" + type + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "type/risk_reversal/" + market.lower() + "/" + currency.lower() + "/" + type
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def risk_reversal_model(self, market: str, currency: str, type:str, start="", end="", limit="", page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 25d , 10d (d: delta)
                :type type:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of risk reversal model
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "type/risk_reversal_model/" + market.lower() + "/" + currency.lower() + "/" + type + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "type/risk_reversal_model/" + market.lower() + "/" + currency.lower() + "/" + type
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def gamma_bands(self, market: str, currency: str, type="1d", start="", end="", limit="", page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 1d default , 7d, 30d (atm volatility)
                :type type:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of gamma bands
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "type/gamma_bands/" + market.lower() + "/" + currency.lower() + "/" + type + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "type/gamma_bands/" + market.lower() + "/" + currency.lower() + "/" + type
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def iv_bid_ask(self, market: str, currency: str, type:str, start="", end="", limit="", page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: p_25, p_10, c_25, c_10
                :type type:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: implied volatility bid ask, all data in json format or specific period in dataclass format
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "type/iv_bid_ask/" + market.lower() + "/" + currency.lower() + "/" + type + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "type/iv_bid_ask/" + market.lower() + "/" + currency.lower() + "/" + type
                    response = requests.get(api_url, headers=api.header).json()

                Response = IpaginationIv_bid_ask(response,
                                             Ipaginationmeta(response['meta']['total'], response['meta']['page'],
                                                             response['meta']['items']))

                for i in range(len(response["items"])):
                    Response.date.append(response["items"][i]['date'])
                    Response.week.append(iv_bid_ask_data(response['items'][i]['7']['ask'],
                                                         response['items'][i]['7']['bid'],
                                                         response['items'][i]['7']['mark']))
                    Response.two_weeks.append(iv_bid_ask_data(response['items'][i]['14']['ask'],
                                                         response['items'][i]['14']['bid'],
                                                         response['items'][i]['14']['mark']))
                    Response.one_month.append(iv_bid_ask_data(response['items'][i]['30']['ask'],
                                                         response['items'][i]['30']['bid'],
                                                         response['items'][i]['30']['mark']))
                    Response.two_months.append(iv_bid_ask_data(response['items'][i]['60']['ask'],
                                                         response['items'][i]['60']['bid'],
                                                         response['items'][i]['60']['mark']))
                    Response.half_a_year.append(iv_bid_ask_data(response['items'][i]['180']['ask'],
                                                         response['items'][i]['180']['bid'],
                                                         response['items'][i]['180']['mark']))
                    Response.year.append(iv_bid_ask_data(response['items'][i]['365']['ask'],
                                                         response['items'][i]['365']['bid'],
                                                         response['items'][i]['365']['mark']))

                return Response

            @classmethod
            def total_oi(self, market: str, currency: str, maturity: str, start="", end="", limit="", page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: all | Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities
                :type maturity:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of total open interests
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "maturity/total_oi/" + market.lower() + "/" + currency.lower() + "/" + maturity + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "maturity/total_oi/" + market.lower() + "/" + currency.lower() + "/" + maturity
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def total_volume(self, market: str, currency: str, maturity: str, start="", end="", limit="", page=""):
                """

                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: all | Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities
                :type maturity:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of total volume
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "maturity/total_volume/" + market.lower() + "/" + currency.lower() + "/" + maturity + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "maturity/total_volume/" + market.lower() + "/" + currency.lower() + "/" + maturity
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def volumeOiByExchange(self,currency: str, maturity: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH,SOL
                :type currency:
                :param maturity: all | Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities
                :type maturity:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of open interest and volume by exchange
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "maturity/VolumeOiByExchange/" + currency.lower() + "/" + maturity + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "maturity/VolumeOiByExchange/" + currency.lower() + "/" + maturity
                    response = requests.get(api_url, headers=api.header).json()
                return response

        class futures:
            url = "https://api.laevitas.ch/historical/futures/"
            pass

            @classmethod
            def oi_weighted_funding (self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of open interest weighted funding
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "oi_weighted_funding/" + currency.lower()  + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "oi_weighted_funding/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def oi_weighted_volume_funding(self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of oi weighted volume funding
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "oi_weighted_volume_funding/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "oi_weighted_volume_funding/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def oi_weighted_basis(self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of oi annualised basis
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "oi_weighted_basis/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "oi_weighted_basis/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def total_oi(self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of total open interest
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "total_oi/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "total_oi/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def total_oi_by_margin(self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of total open interest by margin
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "total_oi_by_margin/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "total_oi_by_margin/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def total_volume(self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of total volume
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "total_volume/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "total_volume/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def total_volume_by_margin(self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of total volume by margin
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "total_volume_by_margin/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "total_volume_by_margin/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def realized_volatility(self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of realized volatility
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "realized_volatility/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "realized_volatility/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def alt_summary(self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of alt summary
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "alt_summary/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "alt_summary/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def alt_markets(self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of alt markets
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "alt_markets/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "alt_markets/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def market_index(self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of market index
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "market_index/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "market_index/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def indices_price(self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of indices price
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "indices_price/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "indices_price/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def futures_annualized_basis(self, currency: str,period:str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param period: 7 | 30 | 60 | 90 | 180 | 270 | 365
                :type period:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of futures annualized basis
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "futures_annualized_basis/" + currency.lower() +"/"+ period + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "futures_annualized_basis/" + currency.lower()+ "/" + period
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def perpetual_funding_exchange(self, currency: str, option: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param option: C,D (C: centralize, D: decentralize)
                :type option:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of perpetual funding exchange
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "perpetual_funding_exchange/" + currency.lower() + "/" + option + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "perpetual_funding_exchange/" + currency.lower() + "/" + option
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def total_oi_by_exchange(self, currency: str, option: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param option: C,D (C: centralize, D: decentralize)
                :type option:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of total oi by exchange
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "total_oi_by_exchange/" + currency.lower() + "/" + option + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "total_oi_by_exchange/" + currency.lower() + "/" + option
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def total_volume_by_exchange(self, currency: str, option: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param option: C,D (C: centralize, D: decentralize)
                :type option:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of total volume by exchange
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "total_volume_by_exchange/" + currency.lower() + "/" + option + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "total_volume_by_exchange/" + currency.lower() + "/" + option
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def perpetual_yield(self,market:str, currency: str, start="", end="", limit="", page=""):
                """

                :param market: BINANCE | BYBIT | BITMEX | FTX | HUOBI  BITFINEX | DERIBIT | KRAKEN | OKEX
                :type market:
                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of perpetual yield
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "perpetual_yield/" + currency.lower() + "/" + market.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "perpetual_yield/" + currency.lower() + "/" + market.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def perpetual_funding(self, market: str, currency: str, start="", end="", limit="", page=""):
                """

                :param market: BINANCE | BYBIT | BITMEX | FTX | HUOBI  BITFINEX | DERIBIT | KRAKEN | OKEX
                :type market:
                :param currency: BTC,ETH,BCH try the analytics future alt_currency function for more available currency
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of perpetual funding
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "perpetual_funding/" + currency.lower() + "/" + market.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "perpetual_funding/" + currency.lower() + "/" + market.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

        class move:
            url = "https://api.laevitas.ch/historical/move/"
            pass

            @classmethod
            def total_oi(self,market="ftx" ,currency="btc",start="",end="",limit="",page=""):
                """
                :param market: FTX
                :type market:
                :param currency: BTC
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: total oi data
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url+ "total_oi/" + market.lower()+ "/" +currency.lower() + makequery
                    response = requests.get(api_url,headers=api.header).json()
                    Response = Ipagination(response,
                        Ipaginationmeta(response['meta']['total'], response['meta']['page'], response['meta']['items'])

                    )
                    for i in range(len(response['items'])):
                        Response.items.append(IDateV(response['items'][i]['v'], response['items'][i]['date']))
                    return Response
                else:
                    api_url = self.url+ "total_oi/" + market.lower()+ "/" +currency.lower()
                    response = requests.get(api_url,headers=api.header).json()
                    Response = Ipagination(response,
                        Ipaginationmeta(response['meta']['total'],response['meta']['page'],response['meta']['items'])

                    )
                    for i in range(len(response['items'])):
                        Response.items.append(IDateV(response['items'][i]['v'], response['items'][i]['date']))
                    return Response

            @classmethod
            def volume_buy_sell(self,market="ftx" ,currency="btc", start="", end="", limit="", page=""):
                """

                :param market: FTX
                :type market:
                :param currency: BTC
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of volume buy sell
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "volume_buy_sell/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "volume_buy_sell/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def iv_type(self, market:str, currency:str,type:str, start="", end="", limit="", page=""):
                """

                :param market: FTX
                :type market:
                :param currency: BTC
                :type currency:
                :param type: daily, weekly, quarterly
                :type type:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of implied volatility type
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "iv_type/" + market.lower() + "/" + currency.lower()+ "/"+ type + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "iv_type/" + market.lower() + "/" + currency.lower()+ "/" + type
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def iv_historical_open_future(self, market: str, currency: str, is_open: str, start="", end="", limit="", page=""):
                """

                :param market: FTX
                :type market:
                :param currency: BTC
                :type currency:
                :param is_open : true or false
                :type is_open :
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of iv historical open future
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "iv_historical_open_future/" + market.lower() + "/" + currency.lower() + "/" + is_open.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "iv_historical_open_future/" + market.lower() + "/" + currency.lower() + "/" + is_open.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def total_volume(self, market="ftx", currency="btc", start="", end="", limit="", page=""):
                """

                :param market: FTX
                :type market:
                :param currency: BTC
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of total volume
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                if currency.upper() not in CURRENCY.__members__:
                    raise TypeError("Currency not available")
                elif makequery != "":
                    api_url = self.url + "total_volume/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "total_volume/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def historical_iv(self, contract_name: str, market="ftx", start="", end="", limit="", page=""):
                """

                :param market: FTX
                :type market:
                :param contract_name: try realtime.move.contract_name function for contract names. EXP : BTC-MOVE-2022Q4
                :type contract_name:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of historical implied volatility
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "historical_iv/" + market.lower() + "/" + contract_name.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "historical_iv/" + market.lower() + "/" + contract_name.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def historical_oi(self, contract_name: str, market="ftx", start="", end="", limit="", page=""):
                """

                :param market: FTX
                :type market:
                :param contract_name: try realtime.move.contract_name function for contract names. EXP : BTC-MOVE-2022Q4
                :type contract_name:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of historical open interest
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "historical_oi/" + market.lower() + "/" + contract_name.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "historical_oi/" + market.lower() + "/" + contract_name.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def historical_price(self, contract_name: str, market="ftx", start="", end="", limit="", page=""):
                """

                :param market: FTX
                :type market:
                :param contract_name: try realtime.move.contract_name function for contract names. EXP : BTC-MOVE-2022Q4
                :type contract_name:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of historical price
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "historical_price/" + market.lower() + "/" + contract_name.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "historical_price/" + market.lower() + "/" + contract_name.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def historical_volume(self, contract_name: str, market="ftx", start="", end="", limit="", page=""):
                """

                :param market: FTX
                :type market:
                :param contract_name: try realtime.move.contract_name function for contract names. EXP : BTC-MOVE-2022Q4
                :type contract_name:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of historical volume
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "historical_volume/" + market.lower() + "/" + contract_name.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "historical_volume/" + market.lower() + "/" + contract_name.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def open_future(self, contract_type: str):
                """
                :param contract_type: daily, weekly, quarterly
                :type contract_type:
                :return: json data of open future
                :rtype:
                """
                api_url = self.url + "open_future/" + contract_type
                response = requests.get(api_url, headers=api.header).json()
                return response

        class defi:
            url = "https://api.laevitas.ch/historical/defi/"
            pass

            @classmethod
            def dovs_auctions(self, protocol:str, start="", end="", currency="", limit="", page=""):
                """

                :param protocol: ribbon, friktion, thetanuts
                :type protocol:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param currency: BTC , ETH, BCH
                :type currency:
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of dovs auctions
                :rtype:
                """
                makequery = query(start=start, end=end,currency=currency, limit=limit, page=page)
                if makequery != "":
                    api_url = self.url + "dovs/auctions/" + protocol.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "dovs/auctions/" + protocol.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

        class derivs:
            url = "https://api.laevitas.ch/historical/derivs/"
            pass

            @classmethod
            def perpetuals(self, market:str,symbol:str, start="", end="", limit="", page=""):
                """
                :param market: Full list of supported exchanges on instruments endpoint. exp: BITMEX | BINANCE | FTX | BYBIT | DYDX | BITFINEX | DERIBIT | HUOBI | KRAKEN | OKEX
                :type market:
                :param symbol: exp : BTC-30DEC22, ETHUSDTH22, ETHUSD, BTCUSD
                :type symbol:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of dovs auctions
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
                    api_url = self.url + "perpetuals/" + market.lower()+ "/"+ symbol + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "perpetuals/" + market.lower()+ "/"+ symbol
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def futures(self, market: str, symbol: str, start="", end="", limit="", page=""):
                """
                :param market: Full list of supported exchanges on instruments endpoint. exp: BITMEX | BINANCE | FTX | BYBIT | DYDX | BITFINEX | DERIBIT | HUOBI | KRAKEN | OKEX
                :type market:
                :param symbol: exp : BTC-30DEC22, ETHUSDTH22, ETHUSD, BTCUSD
                :type symbol:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of futures
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                api_url = self.url + "futures/" + market.lower() + "/" + symbol + makequery
                response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def summary(self, currency: str, start="", end="", limit="", page=""):
                """
                :param currency: BTC | ETH | ALTS (Full list of supported assets on instruments endpoint)
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of summary
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
                    api_url = self.url + "summary/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "summary/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

