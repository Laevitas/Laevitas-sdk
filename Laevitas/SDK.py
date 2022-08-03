import requests
from Laevitas.dataclasses import *
from dataclasses import dataclass, field,make_dataclass
from enum import Enum
from typing import List







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
            url = "https://gateway.devitas.ch/analytics/options/"
            pass

            @classmethod
            def get_atm(self, market: str, currency: str):
                """

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :return: returns object with attributes alldata, Today, Yesterday, Two_days_ago, One_week_ago, Two_weeks_ago,
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
                     resp = responsedata["data"]
                     Response = data_atm(responsedata,responsedata['date'])
                     for i in range(len(resp["Today"])):
                        Response.Today.append(MaturityIV(resp["Today"][i]['maturity'], resp["Today"][i]['iv']))
                     for i in range(len(resp["Yesterday"])):
                        Response.Yesterday.append(MaturityIV(resp["Yesterday"][i]['maturity'], resp["Yesterday"][i]['iv']))
                     for i in range(len(resp["2 Days Ago"])):
                        Response.Two_days_ago.append(MaturityIV(resp["2 Days Ago"][i]['maturity'], resp["2 Days Ago"][i]['iv']))
                     for i in range(len(resp["1 Week Ago"])):
                        Response.One_week_ago.append(MaturityIV(resp["1 Week Ago"][i]['maturity'], resp["1 Week Ago"][i]['iv']))
                     for i in range(len(resp["2 Weeks Ago"])):
                        Response.Two_weeks_ago.append(MaturityIV(resp["2 Weeks Ago"][i]['maturity'], resp["2 Weeks Ago"][i]['iv']))
                     for i in range(len(resp["3 Weeks Ago"])):
                        Response.Three_weeks_ago.append(MaturityIV(resp["3 Weeks Ago"][i]['maturity'], resp["3 Weeks Ago"][i]['iv']))
                     return Response


            @classmethod
            def gex_date(self, market: str, currency: str, maturity: str):
                """

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: EXP:30SEP22
                :type maturity:
                :return: Gamma Exposure by Expiration
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :return: json data of maturities
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :return: oi_expiry
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :return: all oi strike
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :return: json data of oi type
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :return: top traded options
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :return: v_expiry
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :return: v_expiry
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :return: json data of all volume buy/sell
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :return: json data of iv strike
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: EXP:30SEP22
                :type maturity:
                :return: json data of oi strike
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
                    api_url = self.url + "gex_date/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata
            @classmethod
            def oi_net_change_all(self, market: str, currency: str, hours: str):
                """

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param hours: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720
                :type hours:
                :return: json data of all oi net change
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param hours: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720
                :type hours:
                :return: json data of top instrument oi change
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: EXP:30SEP22
                :type maturity:
                :return: json data of volume buy sell
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: EXP:30SEP22
                :type maturity:
                :return: json data of v strike
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: EXP:30SEP22
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: EXP:30SEP22
                :type maturity:
                :param type: C , P
                :type type:
                :return: json data of all iv
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :return: json data of iv table
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: EXP:30SEP22
                :type maturity:
                :param hour: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720,
                :type hour:
                :return: json data of oi net change
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
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
            url = "https://gateway.devitas.ch/analytics/futures/"
            pass

            @classmethod
            def instruments(self):
                """
                :return: json data of instruments
                :rtype:
                """
                api_url = self.url + "instruments"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata
            @classmethod
            def perpetual_funding(self,currency: str):
                """

                :param currency: BTC,ETH,BCH
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

                :param currency: BTC,ETH,BCH
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

                :param currency: BTC,ETH,BCH
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

                :param currency: BTC,ETH,BCH
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

                :param currency: BTC,ETH,BCH
                :type currency:
                :return: json data of volume oi breakdown
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
            def markets_oi_gainers_and_losers(self, currency: str, option: str , hour: str):
                """

                :param currency: BTC,ETH,BCH
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
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
            url = "https://gateway.devitas.ch/analytics/move/"
            pass

            @classmethod
            def oi_group(self):
                """
                :return: json data of oi group
                :rtype:
                """
                api_url = self.url + "oi_group/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def oi_expiry(self):
                """
                :return: json data of oi expiry
                :rtype:
                """
                api_url = self.url + "oi_expiry/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_expiry(self):
                """
                :return: json data of volume expiry
                :rtype:
                """
                api_url = self.url + "volume_expiry/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_group(self):
                """
                :return: json data of volume group
                :rtype:
                """
                api_url = self.url + "volume_group/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_expiry_buy_sell(self):
                """
                :return: json data of volume expiry buy sell
                :rtype:
                """
                api_url = self.url + "volume_expiry_buy_sell/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_contract_buy_sell(self):
                """
                :return: json data of volume contract buy sell
                :rtype:
                """
                api_url = self.url + "volume_contract_buy_sell/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_top_contract(self):
                """
                :return: json data of volume top contract
                :rtype:
                """
                api_url = self.url + "volume_top_contract/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def oi_top_contract(self):
                """
                :return: json data of oi top contract
                :rtype:
                """
                api_url = self.url + "oi_top_contract/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def big_trades(self):
                """
                :return: json data of big trades
                :rtype:
                """
                api_url = self.url + "big_trades/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def contract_name(self):
                """
                :return: json data of contract names
                :rtype:
                """
                api_url = self.url + "contract_name/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def expirations(self):
                """
                :return: json data of expirations
                :rtype:
                """
                api_url = self.url + "expirations/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def ftx_vs_deribit(self):
                """
                :return: json data of ftx vs deribit
                :rtype:
                """
                api_url = self.url + "ftx_vs_deribit/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def live(self):
                """
                :return: json data of live
                :rtype:
                """
                api_url = self.url + "live/"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata


        class derivs:
            url = "https://gateway.devitas.ch/analytics/derivs/"
            pass

            @classmethod
            def oi_gainers(self, market: str, oitype: str, period: str):
                """

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param oitype: future, perpetual
                :type oitype:
                :param period: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720, ytd
                :type period:
                :return: oi_gainers
                :rtype:
                """
                market = market.upper()
                oitype = oitype.upper()
                if oitype not in ["FUTURE", "PERPETUAL"]:
                    raise TypeError("Type not available")
                elif market not in MARKET_CONSTS_DERIVS.__members__:
                    raise TypeError("Market not available")
                elif period not in [1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720, "ytd"]:
                    raise TypeError("period not available")
                else:
                    api_url = self.url + "oi_gainers/" + market + "/" + oitype + "/" + period
                    response = requests.get(api_url, headers=api.header).json()
                    Response = Ioi_gainers(response,response['date'])
                    for i in range(len(response['data'])):
                        Response.data.append(oi_gainers_data(response['data'][i]['symbol'],
                                                             response['data'][i]['open_interest_change'],
                                                             response['data'][i]['open_interest_change_notional']
                                                         ))
                    return Response

    class historical:
        def __init__(self):
            self.option = self.options()

        class options:
            url = "https://gateway.devitas.ch/historical/options/"
            pass

            @classmethod
            def option(self,market: str,instrument: str,start="",end="",limit="",page=""):
                """

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param instrument: exp: BTC-10JUN21-60000-P
                :type instrument:
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param instrument: exp: BTC-10JUN21-60000-P
                :type instrument:
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
                    Response = Ipaginationiv(response,
                        Ipaginationmeta(response['meta']['total'],response['meta']['page'],response['meta']['items']),

                    )
                    for i in range(len(response['items'])):
                        Response.items.append(ivdata(response['items'][i]['date'], response['items'][i]['mark_iv'],
                                                     response['items'][i]['bid_iv'],response['items'][i]['ask_iv']))
                    return Response
                else:
                    api_url = self.url+ "iv/" + market + "/" + instrument
                    response = requests.get(api_url,headers=api.header).json()
                    Response = Ipaginationiv(response,
                        Ipaginationmeta(response['meta']['total'], response['meta']['page'], response['meta']['items']),

                    )
                    for i in range(len(response['items'])):
                        Response.items.append(ivdata(response['items'][i]['date'], response['items'][i]['mark_iv'],
                                                     response['items'][i]['bid_iv'], response['items'][i]['ask_iv']))
                    return Response
            @classmethod
            def price(self,market: str,instrument: str,start="",end="",limit="",page=""):
                """

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param instrument: exp: BTC-10JUN21-60000-P
                :type instrument:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of price
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param instrument: exp: BTC-10JUN21-60000-P
                :type instrument:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of oi volume
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param instrument: exp: BTC-10JUN21-60000-P
                :type instrument:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of underlying price
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: EXP:30SEP22
                :type maturity:
                :param date: EXP:2022-05-25T02
                :type date :
                :return: json data of oi strike
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: EXP:30SEP22
                :type maturity:
                :param date: EXP:2022-05-25T02
                :type date :
                :return: json data of volume strike
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of volume pc ratio
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of gex index
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of max pain
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of atm iv
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of oi pc ratio
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of total oi
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
            def realized_vol(self, market: str, currency: str,start="", end="", limit="10", page="1"):
                """

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of realized vol
                :rtype:
                """
                makequery = query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "realized_vol/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "realized_vol/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response
            @classmethod
            def vix(self, market: str, currency: str,start="", end="", limit="10", page="1"):
                """

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of vix
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :return: json format data of dvol
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
                :return: json data of atm iv model
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 25d , 10d
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 25d , 10d
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 25d , 10d
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 25d , 10d
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 1d , 10d
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 25d , 10d
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param type: 1d default
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
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
                :return: iv bid ask, all data in json format or specific period in dataclass format
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: all
                :type maturity:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of total oi
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: all
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

                :param currency: BTC,ETH,BCH
                :type currency:
                :param maturity: all
                :type maturity:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of oi volume by exchange
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
            url = "https://gateway.devitas.ch/historical/futures/"
            pass

            @classmethod
            def oi_weighted_funding (self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of oi weighted funding
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

                :param currency: BTC,ETH,BCH
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

                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of oi weighted basis
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

                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of total oi
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

                :param currency: BTC,ETH,BCH
                :type currency:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of total oi by margin
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
            def total_volume (self, currency: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH
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

                :param currency: BTC,ETH,BCH
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

                :param currency: BTC,ETH,BCH
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

                :param currency: BTC,ETH,BCH
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

                :param currency: BTC,ETH,BCH
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

                :param currency: BTC,ETH,BCH
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

                :param currency: BTC,ETH,BCH
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
            def futures_annualized_basis(self, currency: str,option:str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH
                :type currency:
                :param option: C,P
                :type option:
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
                    api_url = self.url + "futures_annualized_basis/" + currency.lower() +"/"+ option + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "futures_annualized_basis/" + currency.lower()+ "/" + option
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def perpetual_funding_exchange(self, currency: str, option: str, start="", end="", limit="", page=""):
                """

                :param currency: BTC,ETH,BCH
                :type currency:
                :param option: C,P
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

                :param currency: BTC,ETH,BCH
                :type currency:
                :param option: C,P
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

                :param currency: BTC,ETH,BCH
                :type currency:
                :param option: C,P
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
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
            url = "https://gateway.devitas.ch/historical/move/"
            pass

            @classmethod
            def total_oi(self,market="ftx" ,currency="btc",start="",end="",limit="",page=""):
                """
                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
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
                :return: json data of iv type
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

                :param market: BIT, DERIBIT, BITCOM, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH
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
                :param contract_name: BTC-MOVE-2022Q4
                :type contract_name:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of historical iv
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
                :param contract_name: BTC-MOVE-2022Q4
                :type contract_name:
                :param start: EXP:2022-06-07
                :type end:
                :param end: EXP:2022-06-14
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :return: json data of historical oi
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
                :param contract_name: BTC-MOVE-2022Q4
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
                :param contract_name: BTC-MOVE-2022Q4
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
