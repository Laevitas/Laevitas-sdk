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

        class move:
            url = "https://gateway.devitas.ch/historical/move/"
            pass

            @classmethod
            def total_oi(self,currency: str,start="",end="",limit="",page=""):
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
                :return: total oi data
                :rtype:
                """
                currency=currency.upper()
                makequery = query(start=start,end=end,limit=limit,page=page)
                if currency not in CURRENCY.__members__:
                    raise TypeError("currency not available")
                elif makequery != "":
                    api_url = self.url+ "total_oi/ftx/" + currency.lower() + makequery
                    response = requests.get(api_url,headers=api.header).json()
                    Response = Ipagination(response,
                        Ipaginationmeta(response['meta']['total'], response['meta']['page'], response['meta']['items'])

                    )
                    for i in range(len(response['items'])):
                        Response.items.append(IDateV(response['items'][i]['v'], response['items'][i]['date']))
                    return Response
                else:
                    api_url = self.url+ "total_oi/ftx/" + currency.lower()
                    response = requests.get(api_url,headers=api.header).json()
                    Response = Ipagination(response,
                        Ipaginationmeta(response['meta']['total'],response['meta']['page'],response['meta']['items'])

                    )
                    for i in range(len(response['items'])):
                        Response.items.append(IDateV(response['items'][i]['v'], response['items'][i]['date']))
                    return Response

