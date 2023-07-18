import requests
from Laevitas.dataclasses import *
# from dataclasses import dataclass, field, make_dataclass
from Laevitas.consts import prepare_query, MARKET_CONSTS


class api():
    header = {"apiKey": 'none'}

    def __init__(self, key="none"):
        self.header["apiKey"] = key
        self.r = self.analytics()

    @classmethod
    def configure(self, header):
        self.header["apiKey"] = header

    class analytics:
        def __init__(self):
            self.option = self.options()

        class options:
            url = "https://api.laevitas.ch/analytics/options/"
            pass

            @classmethod
            def instruments(self, market="BINANCE", currency="BTC", maturity="", strike="", optiontype="C"):

                """
                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB | ADA | ARB | OP
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :param strike: e.g., 25000
                :type strike:
                :param optiontype: C,P
                :type optiontype:
                :return: json data of dovs
                :rtype:
                """
                makequery = prepare_query(market=market, currency=currency, maturity=maturity, strike=strike,
                                          optiontype=optiontype)
                api_url = self.url + "Instruments" + makequery
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def atm_iv_ts(self, market: str, currency: str):
                """

                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: ADA,BTC,ETH,TONCOIN,1MLADYS,SOL,BNB,XRP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :return: This endpoint retrieves ATM (At-The-Money) implied volatility time lapse for a specific market and currency. The response includes implied volatility data for various time periods, such as today, yesterday, 2 days ago, 1 week ago, 2 weeks ago, 3 weeks ago, and 1 month ago. For each time period, the response includes an array of objects with the maturity of the option and the corresponding implied volatility.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "atm_iv_ts/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def gex_date(self, market: str, currency: str, maturity: str):
                """

                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | ADA | SOL | XRP | BNB | ARB | OP
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :return: This endpoint provides information about the Options Gamma Exposure (GEX) by date in a specific market, currency, and maturity. The response includes the strike price, option type (call or put), and the GEX value for each strike.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                maturity = maturity.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "gex_date/" + market + "/" + currency + "/" + maturity
                    responsedata = requests.get(api_url, headers=api.header).json()

                return responsedata

            @classmethod
            def gex_date_all(self, market: str, currency: str):
                """

                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :return: This endpoint retrieves GEX (Gamma Exposure) data for all options on a specific market and currency. The response includes an array of objects, where each object represents an option and provides information such as the strike price, option type (call or put), and the corresponding Gamma Exposure value. The Gamma Exposure value indicates the sensitivity of an options book's value to changes in the underlying asset's price.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "gex_date_all/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()

                return responsedata

            @classmethod
            def maturities(self, market: str, currency: str):
                """

                :param market: AGGREGATE | BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :return: This endpoint provides a list of available maturities for options in a specific market and currency.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "maturities/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def oi_expiry(self, market: str, currency: str):
                """

                :param market: AGGREGATE | BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :return: This endpoint provides the open interest data for options by expiry in a specific market and currency. The response includes the open interest for call and put options, as well as their corresponding notional and premium values.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "oi_expiry/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def oi_strike_all(self, market: str, currency: str):
                """

                :param market: AGGREGATE | BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :return: This endpoint provides the open interest data for options by strike in a specific market and currency. The response includes the open interest for call and put options at each strike, as well as their corresponding notional and premium values.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
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

                :param market: AGGREGATE | BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :return: This endpoint provides the open interest data for options by type in a specific market and currency. The response includes the open interest, notional value, and premium value for call and put options separately.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "oi_type/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def top_traded_option(self, market: str, currency: str):
                """

                :param market: AGGREGATE | BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :return: This endpoint provides information about the top traded options in a specific market and currency. The response includes the trading volume, instrument symbol, trading volume in USD, mark price, and premium value for each option.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "top_traded_option/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def v_expiry(self, market: str, currency: str):
                """

                :param market: AGGREGATE | BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :return: This endpoint provides information about the options volume by expiry in a specific market and currency. The response includes the expiry date, volume of call options, volume of put options, notional value of call options, notional value of put options, premium value of call options, and premium value of put options for each expiry.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
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

                :param market: AGGREGATE | BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :return: This endpoint provides information about the options volume by strike in a specific market and currency. The response includes the strike price, volume of call options, volume of put options, notional value of call options, and notional value of put options for each strike.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
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

                :param market: BIT  | DERIBIT  | BYBIT | OKEX
                :type market:
                :param currency: BTC | ETH | ADA | SOL
                :type currency:
                :return: This endpoint provides information about the options volume by buy/sell in a specific market and currency. The response includes the strike price, volume of call options bought, volume of call options sold, volume of put options bought, volume of put options sold, premium paid for call options bought, premium received from call options sold, premium paid for put options bought, premium received from put options sold, notional value of call options bought, notional value of call options sold, notional value of put options bought, and notional value of put options sold for each strike.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "volume_buy_sell_all/" + market.lower() + "/" + currency.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def iv_strike(self, market: str, currency: str, strike: str):
                """

                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :param strike: e.g., 25000 Check analytics/options/Instruments for more information about available strike
                :type strike:
                :return: This endpoint provides information about the Options Implied Volatility (IV) by strike in a specific market, currency, and strike price. The response includes the date and the corresponding IV value for each date.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "iv_strike/" + market + "/" + currency + "/" + str(strike)
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def oi_strike(self, market: str, currency: str, maturity: str):
                """

                :param market: AGGREGATE | BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :return: This endpoint provides information about the Options Open Interest (OI) by strike in a specific market, currency, and maturity. The response includes the date and various metrics such as open interest, notional value, premium value, and intrinsic value for call and put options at each strike.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                maturity = maturity.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "oi_strike/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def oi_net_change_all(self, market: str, currency: str, hours: str):
                """

                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | ADA | BNB | SOL | XRP | TONCOIN , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :param hours: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720
                :type hours:
                :return: This endpoint provides information about the net change in Options Open Interest (OI) for all strikes in a specific market, currency, and within a specified time period (in hours). The response includes the date and various net change metrics for call and put options at each strike.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "oi_net_change_all/" + market + "/" + currency + "/" + hours
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def top_instrument_oi_change(self, market: str, currency: str, hours: str):
                """

                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | ADA | BNB | SOL | XRP | TONCOIN , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :param hours: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720
                :type hours:
                :return: This endpoint retrieves information about the top instruments with the highest options open interest change within a specified market, currency, and time period (in hours). The response includes the date and various metrics related to the open interest change, such as notional value and premium value.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "top_instrument_oi_change/" + market.lower() + "/" + currency.lower() + "/" + str(
                        hours)
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def volume_buy_sell(self, market: str, currency: str, maturity: str):
                """

                :param market: BIT | DERIBIT | BYBIT | OKEX
                :type market:
                :param currency: BTC | ETH | SOL | ADA , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :return: This endpoint retrieves the options volume and buy/sell information for different strike prices within a specified market, currency, and maturity. The response includes the date and various metrics related to the volume and buy/sell activity, such as the number of options bought/sold, premium values, and notional values.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                maturity = maturity.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "volume_buy_sell/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def v_strike(self, market: str, currency: str, maturity: str):
                """

                :param market: AGGREGATE | BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | BCH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :return: This endpoint retrieves the options volume and various metrics (such as notional value and premium value) for different strike prices within a specified market, currency, and maturity. The response includes the date and the volume and metrics for both call and put options.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                maturity = maturity.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "v_strike/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def summary_trades(self, market: str, currency: str, hours: str):
                """

                :param market: BIT | DERIBIT
                :type market:
                :param currency: BTC | ETH | ADA , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :param hours: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720
                :type hours:
                :return: This endpoint retrieves the options trade summary for a specific market, currency, and time frame. The response includes the date of the trade summary and the summary details for different trading strategies, such as the BULL_CALL_SPREAD strategy. Each trading strategy includes various metrics and an array of trades representing individual trade details.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "summary_trades/" + market + "/" + currency + "/" + str(hours)
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def greeks(self, market: str, currency: str, maturity: str, optiontype: str):
                """

                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :param optiontype: C,P
                :type optiontype:
                :return: This endpoint retrieves the options implied volatility data for a specific market, currency, maturity, and type. The response includes the date and the implied volatility data for different strike prices within the specified market, currency, and maturity. The data contains information such as strike price, underlying price, delta, gamma, theta, and vega for each option.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                maturity = maturity.upper()
                optiontype = optiontype.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif optiontype not in ["P", "C"]:
                    raise TypeError("type is either C or P")
                else:
                    maturity = maturity.upper()
                    api_url = self.url + "greeks/" + market + "/" + currency + "/" + maturity + "/" + optiontype
                    responsedata = requests.get(api_url, headers=api.header).json()
                    # Response = Igreeks(responsedata, responsedata['date'])
                    # for i in range(len(responsedata['data'])):
                    #     Response.data.append(greeks_data(responsedata['data'][i]['strike'],
                    #                                      responsedata['data'][i]['underlying_price'],
                    #                                      responsedata['data'][i]['delta'],
                    #                                      responsedata['data'][i]['gamma'],
                    #                                      responsedata['data'][i]['theta'],
                    #                                      responsedata['data'][i]['vega']
                    #                                      ))
                    return responsedata

            @classmethod
            def iv_all(self, market: str, currency: str, maturity: str, type: str):
                """

                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :param type: C , P
                :type type:
                :return: This endpoint provides information on key risk parameters such as delta, gamma, theta, and vega, which are essential for analyzing and managing options trading positions.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "iv_all/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper() + "/" + type.upper()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def iv_table(self, market: str, currency: str):
                """

                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :return: This endpoint allows users to retrieve the implied volatility table for options based on the specified market and currency. Implied volatility is a crucial factor in options pricing, and having access to this data helps traders and investors analyze and make informed decisions about their options trading strategies.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "iv_table/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def oi_net_change(self, market: str, currency: str, maturity: str, hour: str):
                """

                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | ADA | SOL | XRP | BNB | TONCOIN , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :param hour: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720,
                :type hour:
                :return: This endpoint allows users to retrieve the net change in open interest for options based on the specified market, currency, maturity, and hours. Open interest reflects the total number of outstanding options contracts in the market, and tracking its net change provides insights into the market sentiment and potential shifts in options positions. Traders and analysts can utilize this information to assess market trends, identify trading opportunities, and make informed decisions regarding options trading strategies.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "oi_net_change/" + market + "/" + currency + "/" + maturity + "/" + str(hour)
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def snapshot(self, market: str, currency: str):
                """

                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | ADA | SOL | XRP | BNB | OP | ARB , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :return: This endpoint allows users to retrieve a snapshot of options data for the specified market and currency. The snapshot includes comprehensive information about individual options contracts, such as strike price, expiration date, open interest, volume, pricing data, and other relevant metrics. Traders and analysts can utilize this data to gain insights into the options market, monitor market trends, evaluate trading opportunities, and make informed decisions regarding options trading strategies.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "snapshot/" + market.lower() + "/" + currency.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def oi_breakdown(self):
                """
                :return: This endpoint is essential for obtaining insights into the distribution of open interest and open value for options across different exchanges. By providing the breakdown of notional and open value data, the API response enables users to analyze the significance of options trading activity on various exchanges. Traders, investors, and analysts can leverage this information to assess market sentiment, identify liquidity sources, and make informed decisions about options trading strategies. Additionally, this endpoint facilitates the monitoring and comparison of options market participation among different exchanges, aiding in the evaluation of market dynamics and exchange performance.
                :rtype:
                """
                api_url = self.url + "oi_breakdown"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_breakdown(self):
                """
                :return: This endpoint is crucial for obtaining insights into the distribution of trading volume and open value for options across different exchanges. By providing the breakdown of notional and open value data, the API response enables users to analyze the significance of options trading activity on various exchanges. Traders, investors, and analysts can leverage this information to assess market liquidity, identify trading opportunities, and monitor the overall trading activity for options. Additionally, this endpoint facilitates the comparison of trading volume and open value among different exchanges, aiding in the evaluation of market dynamics and exchange performance.
                :rtype:
                """
                api_url = self.url + "volume_breakdown"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def oi_breakdown_by_currency(self):
                """
                :return: This endpoint is useful for obtaining insights into the distribution of open interest and open value for options by currency. By providing the breakdown of notional and open value data, the API response enables users to analyze the significance of options trading activity in different currencies. Traders, investors, and analysts can leverage this information to assess the popularity and liquidity of options contracts in various currencies. It allows for the identification of dominant currencies in options trading and provides an understanding of the market dynamics specific to each currency. Additionally, this endpoint facilitates the comparison of open interest and open value among different currencies, aiding in the evaluation of market trends and currency-specific trading opportunities.
                :rtype:
                """
                api_url = self.url + "oi_breakdown_by_currency"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            def volume_breakdown_by_currency(self):
                """
                :return: This endpoint is useful for obtaining insights into the distribution of trading volume and open value for options by currency. By providing the breakdown of notional and open value data, the API response enables users to analyze the significance of options trading activity in different currencies. Traders, investors, and analysts can leverage this information to assess the popularity and liquidity of options contracts in various currencies. It allows for the identification of dominant currencies in options trading and provides an understanding of the market dynamics specific to each currency. Additionally, this endpoint facilitates the comparison of trading volume and open value among different currencies, aiding in the evaluation of market trends and currency-specific trading opportunities.
                :rtype:
                """
                api_url = self.url + "volume_breakdown_by_currency"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            def expired_expiries(self, market: str, currency: str, maturity=None):
                """

                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH | SOL | XRP | BNB | ADA | ARB | OP , Check analytics/options/Instruments for more information about available currency
                :type currency:
                :param maturity: (optional) Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :return: This endpoint allows users to retrieve the implied volatility table for options based on the specified market and currency. Implied volatility is a crucial factor in options pricing, and having access to this data helps traders and investors analyze and make informed decisions about their options trading strategies.
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif maturity:
                    makequery = prepare_query(maturity=maturity)
                    api_url = self.url + "expired_expiries/" + market + "/" + currency + makequery
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata
                else:
                    api_url = self.url + "expired_expiries/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            def custom_change(self, name: str, market: str, currency: str, end="", start=""):
                """
                :param name: historical_buy_sell_volume , atmivts_historical , heatmap_change , oi_net_change , iv_table_change , time_skew, oi_gainers_and_losers
                :type name:
                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | ZETA_EXCHANGE
                :type market:
                :param currency: BTC | ETH | SOL
                :type currency:
                :param start: eg: 2023-07-03 (optional)
                :type start:
                :param end: eg: 2023-07-10 (optional)
                :type end:
                :return: This endpoint allows users to retrieve the implied volatility table for options based on the specified market and currency. Implied volatility is a crucial factor in options pricing, and having access to this data helps traders and investors analyze and make informed decisions about their options trading strategies.
                :rtype:
                """
                market = market.lower()
                currency = currency.lower()
                name = name.lower()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif start or end:
                    makequery = prepare_query(start=start, end=end)
                    api_url = self.url + "custom_change/" + name + "/" + market + "/" + currency + makequery
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata
                else:
                    api_url = self.url + "custom_change/" + name + "/" + market + "/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def skew(self, currency: str, maturity: str, type: str, timelapse: False):
                """
                :param currency: BTC | ETH
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :param type: strike or delta , lowercase
                :type type:
                :param timelapse: True or False, Time-lapse data provides a historical perspective on the skew values and implied volatility (IV) for different strikes or deltas over a specific time period. By retrieving the time-lapse data, traders, investors, and analysts can analyze how the skew and IV have changed over time, identify trends or patterns in the market sentiment, and assess the impact of market events on the options market
                :type timelapse:
                :return: Skew data provides insights into the implied volatility of options at different strikes or deltas, allowing users to analyze the market's perception of potential price movements. By retrieving the skew data, traders, investors, and analysts can assess the relative pricing of options at different strike prices or delta levels, identify potential opportunities for arbitrage or hedging strategies, and gain a deeper understanding of market sentiment and risk perception.
                :rtype:
                """
                type = type.lower()
                currency = currency.upper()
                maturity = maturity.upper()
                if timelapse is True:
                    api_url = self.url + "model_charts/skew/" + currency + "/" + maturity + "/" + type + '/time_lapse'
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata
                else:
                    api_url = self.url + "model_charts/skew/" + currency + "/" + maturity + "/" + type
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def vol_run(self, currency: str, maturity: str):
                """
                :param currency: BTC | ETH
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :return: Volatility run data provides insights into the implied volatility and option parameters at different delta levels, allowing users to analyze the market's perception of potential price movements and risk profiles across various option strikes. By retrieving the volatility run data, traders, investors, and analysts can assess the relative pricing and skewness of options at different delta levels, identify potential opportunities for trading strategies, and gain a deeper understanding of market sentiment and risk perception   and risk perception.
                :rtype:
                """
                currency = currency.upper()
                maturity = maturity.upper()
                api_url = self.url + "model_charts/vol_run/" + currency + "/" + maturity
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def forward_curve(self, currency: str):
                """
                :param currency: BTC | ETH
                :type currency:
                :return: The forward curve is an essential tool in options pricing and risk management. It provides insights into the relationship between the time-to-maturity (TTM) and the corresponding forward prices for options. By retrieving the forward curve data, traders, investors, and analysts can assess the term structure of options prices, identify potential market inefficiencies or mispricings, and make informed decisions regarding options trading and portfolio management
                :rtype:
                """
                currency = currency.upper()
                api_url = self.url + "model_charts/forward_curve/" + currency
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def term_structure_atm(self, currency: str, timelapse: False):
                """
                :param currency: BTC | ETH
                :type currency:
                :param timelapse: True or False
                :type timelapse:
                :return: The term structure provides valuable insights into the relationship between the time-to-maturity (TTM) and the corresponding implied volatility (IV) for ATM options. Implied volatility is a critical component in options pricing, representing the market's expectation of future price volatility of the underlying asset. By analyzing the term structure, traders, investors, and analysts can gain insights into the market's perception of future volatility at different tenors and expiries
                :rtype:
                """
                currency = currency.upper()
                if timelapse is True:
                    api_url = self.url + "model_charts/term_structure_atm/" + currency + '/time_lapse'
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata
                else:
                    api_url = self.url + "model_charts/term_structure_atm/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def term_structure(self, currency: str, type: str):
                """
                :param currency: BTC | ETH
                :type currency:
                :param type: strike or delta , lowercase
                :type type:
                :return: The term structure provides insights into the relationship between a specific parameter (delta or strike) and the corresponding implied volatility (IV) for options with different expiries. By analyzing the term structure, traders, investors, and analysts can identify patterns or anomalies in implied volatility across different option expiries
                :rtype:
                """
                currency = currency.upper()
                type = type.lower()
                api_url = self.url + "model_charts/term_structure/" + currency + "/" + type
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def skew_currency(self, currency: str, maturity: str):
                """
                :param currency: BTC | ETH
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :return: Skew data provides insights into the market's perception of potential upside or downside risks in the underlying asset
                :rtype:
                """
                currency = currency.upper()
                maturity = maturity.upper()
                api_url = self.url + "skew_currency/" + currency + "/" + maturity
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def skew_market(self, market: str, maturity: str):
                """
                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 or "all" ,Check analytics/options/maturities for more information about available maturity
                :type maturity:
                :return:  Skew data provides insights into the market's perception of potential upside or downside risks in the underlying asset
                :rtype:
                """
                market = market.upper()
                maturity = maturity.upper()
                api_url = self.url + "skew_market/" + market + "/" + maturity
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def iv_currency(self, currency: str):
                """
                :param currency: BTC | ETH  | SOL | ADA | TONCOIN | BNB | XRP | ARB | OP
                :type currency:
                :return: Implied volatility (IV) is a key parameter in option pricing models. It represents the market's expectation of the future volatility of the underlying asset. IV data provides insights into the perceived level of risk and uncertainty in the market
                :rtype:
                """
                currency = currency.upper()
                api_url = self.url + "iv_currency/" + currency
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def iv_market(self, market: str):
                """
                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :return: Implied volatility (IV) is a key parameter in option pricing models. It represents the market's expectation of the future volatility of the underlying asset. IV data provides insights into the perceived level of risk and uncertainty in the market
                :rtype:
                """
                market = market.upper()
                api_url = self.url + "iv_market/" + market
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def eth_btc_atm_iv_term_structure(self):
                """
                :return: The term structure of at-the-money (ATM) implied volatility (IV) provides valuable information about the market's expectations of future volatility for Ethereum-Bitcoin (ETH-BTC) options. By analyzing the IV term structure, traders and investors can gain insights into how the market perceives the potential price movements of ETH-BTC options over different time periods
                :rtype:
                """
                api_url = self.url + "eth-btc_atm_iv_term_structure"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def skew_currency_market(self, currency: str, market: str):
                """
                :param market: BIT  | DERIBIT  | BYBIT  | OKEX  | POWERTRADE | DELTA_EXCHANGE | LYRA_ARBITRUM | AEVO | BINANCE | LYRA
                :type market:
                :param currency: BTC | ETH
                :type currency:
                :return: Skew data provides insights into the market's perception of potential upside or downside risks in the underlying asset
                :rtype:
                """
                currency = currency.upper()
                market = market.upper()
                api_url = self.url + "skew/" + market + "/" + currency
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

        class futures:
            url = "https://api.laevitas.ch/analytics/futures/"
            pass

            @classmethod
            def instruments(self):
                """
                :return: This endpoint provides information about futures instruments, including the market, type, currency, instrument name or identifier, and expiry date.
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
            def perpetual_funding(self, currency: str, type=""):
                """

                :param currency: BTC,ETH ... Check analytics/futures/alt_currency For more information about available currencies
                :type currency:
                :param type: optional , c or d (centralized , decentralized)
                :type type:
                :return: This endpoint provides information about the funding rates and yields of perpetual contracts for a specific currency
                :rtype:
                """
                currency = currency.upper()
                if len(type) == 1:
                    api_url = self.url + "perpetual_funding/" + currency + "/" + type.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "perpetual_funding/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def futures_yield(self, currency: str):
                """

                :param currency: ADA,BCH,BNB ... Check analytics/futures/alt_currency For more information about available currencies
                :type currency:
                :return: This endpoint provides information about the yield values of futures contracts for a specific currency.
                :rtype:
                """
                currency = currency.upper()
                api_url = self.url + "futures_yield/" + currency
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def futures_basis(self, currency: str):
                """
                :param currency: ADA,BCH,BNB ... Check analytics/futures/alt_currency For more information about available currencies
                :type currency:
                :return: This endpoint provides information about the basis values of futures contracts for a specific currency.
                :rtype:
                """
                currency = currency.upper()
                api_url = self.url + "futures_basis/" + currency
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def volume_breakdown(self, currency: str, type=""):
                """

                :param currency: BTC,ETH ... Check analytics/futures/alt_currency For more information about available currencies
                :type currency:
                :param type: optional , c or d (centralized , decentralized)
                :type type:
                :return: This endpoint retrieves volume breakdown data for a specific currency and type. The response includes the volume values in USD for different markets, categorized by all types, futures, and perpetual contracts.
                :rtype:
                """
                currency = currency.upper()
                if len(type) == 1:
                    api_url = self.url + "volume_breakdown/" + currency + '/' + type.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "volume_breakdown/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def oi_breakdown(self, currency: str, type=""):
                """

                :param currency: BTC,ETH ... Check analytics/futures/alt_currency For more information about available currencies
                :type currency:
                :param type: optional , c or d (centralized , decentralized)
                :type type:
                :return: This endpoint retrieves open interest breakdown data for a specific currency and type. The response includes the open interest values in USD for different markets, categorized by all types, futures, and perpetual contracts.
                :rtype:
                """
                currency = currency.upper()
                if len(type) == 1:
                    api_url = self.url + "oi_breakdown/" + currency + '/' + type.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "oi_breakdown/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()

                return responsedata

            @classmethod
            def futures_curve(self, currency: str, market=""):
                """

                :param currency: ADA,BCH,BNB ... Check analytics/futures/alt_currency For more information about available currencies
                :type currency:
                :param market: (optional) BINANCE, BITMEX , BITGET , DERIBIT, HUOBI, KRAKEN, BYBIT , OKEX
                :type market:
                :return: This endpoint provides information about the futures curve for a specific currency and market.
                :rtype:
                """
                currency = currency.upper()
                if len(market) >= 1:
                    market = market.upper()
                    api_url = self.url + "futures_curve/" + currency + "/" + market
                    responsedata = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "futures_curve/" + currency
                    responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def markets_oi_gainers_and_losers(self, currency: str, option: str, hour: str, type=""):
                """

                :param currency: BTC,ETH,ADA,BCH,BNB ... Check analytics/futures/alt_currency For more information about available currencies
                :type currency:
                :param option: perpetual, future , all
                :type option:
                :param hour: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720, ytd
                :type hour:
                :param type: optional , c or d (centralized , decentralized)
                :type type:
                :return: This endpoint provides information about the gainers and losers in open interest for futures markets of a specific currency, based on the specified option and parameter
                :rtype:
                """
                currency = currency.upper()
                if len(type) == 1:
                    api_url = self.url + "markets_oi_gainers_and_losers/" + currency + "/" + option.lower() + "/" + str(
                        hour) + "/" + type.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "markets_oi_gainers_and_losers/" + currency + "/" + option.lower() + "/" + str(
                        hour)
                    responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def snapshot(self, market: str):
                """

                :param market: BINANCE, BITMEX, DERIBIT, HUOBI, KRAKEN, BYBIT , OKX
                :type market:
                :return: This endpoint retrieves snapshot data for a specific futures market. The response includes information such as bid price, ask price, volume, open interest, and other relevant details about the futures contract.
                :rtype:
                """
                market = market.upper()
                if market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                else:
                    api_url = self.url + "snapshot/" + market
                    responsedata = requests.get(api_url, headers=api.header).json()
                    return responsedata

            @classmethod
            def aggregated_future_summary(self, currency: str):
                """
                :param currency: BTC,ETH,LTC ... Check analytics/futures/alt_currency For more information about available currencies
                :type currency:
                :return: This endpoint retrieves aggregated future summary data for a specific currency. The response includes information such as the future symbol, currency, expiry date, price, open interest, open interest notional, volume, volume notional, yield, basis, open interest volume, and markets associated with the future.
                :rtype:
                """
                currency = currency.upper()
                api_url = self.url + "aggregated_future_summary/" + currency
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def aggregated_option_summary(self, currency: str):
                """
                :param currency: BTC,ETH,LTC ... Check analytics/futures/alt_currency For more information about available currencies
                :type currency:
                :return: This endpoint retrieves aggregated option summary data for a specific currency. The response includes information such as the option symbol, currency, expiry date, price, open interest, open interest notional, volume, volume notional, yield, basis, open interest volume, and markets associated with the option.
                :rtype:
                """
                currency = currency.upper()
                api_url = self.url + "aggregated_option_summary/" + currency
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
                :return: json data of DOVs weekly auctions
                :rtype:
                """
                api_url = self.url + "dovs"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def ribbon(self):
                """
                :return: json data of ribbon weekly auctions
                :rtype:
                """
                api_url = self.url + "ribbon"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def friktion(self):
                """
                :return: json data of friktion weekly auctions
                :rtype:
                """
                api_url = self.url + "friktion"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def squeeth(self):
                """
                :return: json data of squeeth live data
                :rtype:
                """
                api_url = self.url + "squeeth"
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

        class derivs:
            url = "https://api.laevitas.ch/analytics/derivs/"
            pass

            @classmethod
            def futures(self, market: str, currency: str, maturity: str):
                """

                :param market: Full list of supported exchanges on instruments endpoint (futures.instrument function),exp: BITMEX | BINANCE | BYBIT | DYDX | BITFINEX | DERIBIT | HUOBI | KRAKEN | OKEX | GMX | PERP-PROTOCOL
                :type market:
                :param currency: BTC | ETH... Check analytics/futures/alt_currency For more information about available currencies
                :type currency:
                :param maturity: Uppercase (DMMMYY), e.g., 30JUN23, Check analytics/futures/instruments for more information about available maturity
                :type maturity:
                :return: json data of futures live data
                :rtype:
                """
                market = market.upper()
                maturity = maturity.upper()
                api_url = self.url + "futures/" + market + "/" + currency.lower() + "/" + maturity
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def perpetuals(self, market: str, currency: str):
                """

                :param market: Full list of supported exchanges on instruments endpoint (futures.instrument function),exp: BITMEX | BINANCE | BYBIT | DYDX | BITFINEX | DERIBIT | HUOBI | KRAKEN | OKEX | GMX | PERP-PROTOCOL
                :type market:
                :param currency: BTC | ETH... Check analytics/futures/alt_currency For more information about available currencies
                :type currency:
                :return: json live data of perpetual swaps
                :rtype:
                """
                market = market.upper()
                currency = currency.upper()
                api_url = self.url + "perpetuals/" + market + "/" + currency.lower()
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def summary(self, currency=""):
                """
                :param currency: BTC | ETH... Check analytics/futures/alt_currency For more information about available currencies
                :type currency:
                :return: json data of aggregated perps summary
                :rtype:
                """
                if len(currency) >= 1:
                    api_url = self.url + "summary/" + currency.lower()
                    responsedata = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "summary"
                    responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def oi_gainers(self, market: str, oitype: str, period: str):
                """
                :param market: Full list of supported exchanges on instruments endpoint (futures.instrument function),exp: BITMEX | BINANCE | BYBIT | DYDX | BITFINEX | DERIBIT | HUOBI | KRAKEN | OKEX | GMX | PERP-PROTOCOL
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
                if oitype not in ["future", "perpetual"]:
                    raise TypeError("Type not available")
                elif str(period) not in ["1", "2", "4", "8", "12", "18", "24", "48", "168", "336", "504", "720", "ytd"]:
                    raise TypeError("period not available")
                else:
                    api_url = self.url + "oi_gainers/" + market + "/" + oitype.lower() + "/" + str(period)
                    responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def price_gainers(self, market: str, oitype: str, period: str):
                """

                :param market: Full list of supported exchanges on instruments endpoint (futures.instrument function),exp: BITMEX | BINANCE | BYBIT | DYDX | BITFINEX | DERIBIT | HUOBI | KRAKEN | OKEX | GMX | PERP-PROTOCOL
                :type market:
                :param oitype: future, perpetual
                :type oitype:
                :param period: 1, 2, 4, 8, 12, 18, 24, 48, 168, 336, 504, 720, ytd
                :type period:
                :return: json data of price gainers
                :rtype:
                """
                market = market.upper()
                if oitype not in ["future", "perpetual"]:
                    raise TypeError("Type not available")
                elif str(period) not in ["1", "2", "4", "8", "12", "18", "24", "48", "168", "336", "504", "720", "ytd"]:
                    raise TypeError("period not available")
                else:
                    api_url = self.url + "price_gainers/" + market + "/" + oitype.lower() + "/" + str(period)
                    responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

            @classmethod
            def perpetuals_snapshot(self, market: str):
                """
                :param market: deribit, binance , okx, bybit
                :type market
                :return: json live data of perpetual swaps
                :rtype:
                """
                market = market.lower()
                api_url = self.url + "perpetuals_snapshot/" + market
                responsedata = requests.get(api_url, headers=api.header).json()
                return responsedata

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
            def top_gainers_losers(self, change: str, type: str):
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
            def option(self, market: str, instrument: str, start: str, end: str, limit="", page="", granularity=""):
                """
                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, AEVO, LYRA , LYRA_ARBITRUM, BYBIT
                :type market:
                :param instrument: Currency-Maturity-Strike-C/P e.g., BTC-30JUN23-80000-C Check analytics/options/Instruments for more information about available instrument
                :type instrument:
                :param start: EXP:2023-07-11
                :type end:
                :param end: EXP:2023-07-18
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :param granularity: 5m,15m,30m,1h,2h,4h,6h,12h,1d
                :type end :
                :return: options historical data for a specific contract
                :rtype:
                """
                market = market.upper()
                instrument = instrument.upper()
                x = instrument.split("-")
                makequery = prepare_query(start=start, end=end, limit=limit, page=page, granularity=granularity)
                if len(x) != 4:
                    raise TypeError("wrong instrument")
                elif x[3] not in ["P", "C"]:
                    raise TypeError("type in instument is either C or P")
                elif makequery != "":
                    api_url = self.url + market + "/" + instrument + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + market + "/" + instrument
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def iv(self, market: str, instrument: str, start: str, end: str, limit="", page="", granularity=""):
                """
                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, AEVO, LYRA , LYRA_ARBITRUM, BYBIT
                :type market:
                :param instrument: Currency-Maturity-Strike-C/P e.g., BTC-30JUN23-80000-C Check analytics/options/Instruments for more information about available instrument
                :type instrument:
                :param start: EXP:2023-07-11
                :type end:
                :param end: EXP:2023-07-18
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :param granularity: 5m,15m,30m,1h,2h,4h,6h,12h,1d
                :type end :
                :return: iv  historical data for a specific option contract
                :rtype:
                """
                market = market.upper()
                instrument = instrument.upper()
                x = instrument.split("-")
                makequery = prepare_query(start=start, end=end, limit=limit, page=page, granularity=granularity)
                if len(x) != 4:
                    raise TypeError("wrong instrument")
                elif x[3] not in ["P", "C"]:
                    raise TypeError("type in instument is either C or P")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "iv/" + market + "/" + instrument + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "iv/" + market + "/" + instrument
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def price(self, market: str, instrument: str, start: str, end: str, limit="", page="", granularity=""):
                """
                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, AEVO, LYRA , LYRA_ARBITRUM, BYBIT
                :type market:
                :param instrument: Currency-Maturity-Strike-C/P e.g., BTC-30JUN23-80000-C Check analytics/options/Instruments for more information about available instrument
                :type instrument:
                :param start: EXP:2023-07-11
                :type end:
                :param end: EXP:2023-07-18
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :param granularity: 5m,15m,30m,1h,2h,4h,6h,12h,1d
                :type end :
                :return:   historical price data for a specific option contract
                :rtype:
                """
                market = market.upper()
                instrument = instrument.upper()
                x = instrument.split("-")
                makequery = prepare_query(start=start, end=end, limit=limit, page=page, granularity=granularity)
                if len(x) != 4:
                    raise TypeError("wrong instrument")
                elif x[3] not in ["P", "C"]:
                    raise TypeError("type in instument is either C or P")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "price/" + market + "/" + instrument + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "price/" + market + "/" + instrument
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def oi_volume(self, market: str, instrument: str, start: str, end: str, limit="", page="", granularity=""):
                """
                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, AEVO, LYRA , LYRA_ARBITRUM, BYBIT
                :type market:
                :param instrument: Currency-Maturity-Strike-C/P e.g., BTC-30JUN23-80000-C Check analytics/options/Instruments for more information about available instrument
                :type instrument:
                :param start: EXP:2023-07-11
                :type end:
                :param end: EXP:2023-07-18
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :param granularity: 5m,15m,30m,1h,2h,4h,6h,12h,1d
                :type end :
                :return: open interest and volume historical data for a specific option contract
                :rtype:
                """
                market = market.upper()
                instrument = instrument.upper()
                x = instrument.split("-")
                makequery = prepare_query(start=start, end=end, limit=limit, page=page, granularity=granularity)
                if len(x) != 4:
                    raise TypeError("wrong instrument")
                elif x[3] not in ["P", "C"]:
                    raise TypeError("type in instument is either C or P")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "oi_volume/" + market + "/" + instrument + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "oi_volume/" + market + "/" + instrument
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def underlying_price(self, market: str, instrument: str, start: str, end: str, limit="", page="",
                                 granularity=""):
                """
                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, AEVO, LYRA , LYRA_ARBITRUM, BYBIT
                :type market:
                :param instrument: Currency-Maturity-Strike-C/P e.g., BTC-30JUN23-80000-C Check analytics/options/Instruments for more information about available instrument
                :type instrument:
                :param start: EXP:2023-07-11
                :type end:
                :param end: EXP:2023-07-18
                :type end :
                :param limit: 10
                :type limit:
                :param page: 1
                :type page:
                :param granularity: 5m,15m,30m,1h,2h,4h,6h,12h,1d
                :type end :
                :return: index and underlying historical data for a specific option contract
                :rtype:
                """
                market = market.upper()
                instrument = instrument.upper()
                x = instrument.split("-")
                makequery = prepare_query(start=start, end=end, limit=limit, page=page, granularity=granularity)
                if len(x) != 4:
                    raise TypeError("wrong instrument")
                elif x[3] not in ["P", "C"]:
                    raise TypeError("type in instument is either C or P")
                elif market not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "underlying_price/" + market + "/" + instrument + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "underlying_price/" + market + "/" + instrument
                    response = requests.get(api_url, headers=api.header).json()
                return response

            # @classmethod
            # def oi_strike(self, market: str, currency: str, maturity: str, date: str):
            #     """
            #
            #     :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, AEVO, LYRA , LYRA_ARBITRUM, BYBIT
            #     :type market:
            #     :param currency: BTC,ETH,BCH,SOL,XRP,BNB , Check analytics/options/Instruments for more information about available currencies and instruments
            #     :type currency:
            #     :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 Check analytics/options/Instruments for more information about available maturity
            #     :type maturity:
            #     :param date: YYYY-MM-DDTHH e.g., 2022-07-24T01
            #     :type date :
            #     :return: historical options open interest data
            #     :rtype:
            #     """
            #     market = market.upper()
            #     currency = currency.upper()
            #     if currency not in CURRENCY.__members__:
            #         raise TypeError("Currency not available")
            #     elif market not in MARKET_CONSTS.__members__:
            #         raise TypeError("Market not available")
            #     else:
            #         api_url = self.url + "oi_strike/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper() + "?date=" + date
            #         responsedata = requests.get(api_url, headers=api.header).json()
            #     return responsedata
            #
            # @classmethod
            # def volume_strike(self, market: str, currency: str, maturity: str, date: str):
            #     """
            #
            #     :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
            #     :type market:
            #     :param currency: BTC,ETH,BCH,SOL,XRP,BNB
            #     :type currency:
            #     :param maturity: Uppercase (DMMMYY), e.g., 30JUN23 Active expirations endpoint provide available maturities
            #     :type maturity:
            #     :param date: YYYY-MM-DDTHH e.g., 2022-07-24T01
            #     :type date :
            #     :return: json data of historical volume by strike
            #     :rtype:
            #     """
            #     market = market.upper()
            #     currency = currency.upper()
            #     if currency not in CURRENCY.__members__:
            #         raise TypeError("Currency not available")
            #     elif market not in MARKET_CONSTS.__members__:
            #         raise TypeError("Market not available")
            #     else:
            #         api_url = self.url + "volume_strike/" + market.lower() + "/" + currency.lower() + "/" + maturity.upper() + "?date=" + date
            #         responsedata = requests.get(api_url, headers=api.header).json()
            #     return responsedata

            @classmethod
            def snapshot(self, market: str, currency: str, start="", end="", limit="10", page="1", timezone=""):
                """
                :param market: BIT, DERIBIT, OKEX, POWERTRADE, BINANCE, DELTA_EXCHANGE, ZETA_EXCHANGE, FTX
                :type market:
                :param currency: BTC,ETH,BCH,SOL,XRP,BNB
                :type currency:
                :param start: EXP:2023-07-11
                :type end:
                :param end: EXP:2023-07-18
                :type end :
                :param limit: default: 10
                :type limit:
                :param page: default :1
                :type page:
                :param timezone: default :1
                :type timezone:
                :return: json format data of historical snapshot of options
                :rtype:
                """
                makequery = prepare_query(start=start, end=end, limit=limit, page=page, timezone=timezone)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "snapshot/" + market.lower() + "/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "snapshot/" + market.lower() + "/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def volume_pc_ratio(self, market: str, currency: str, start="", end="", limit="10", page="1"):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def gex_index(self, market: str, currency: str, start="", end="", limit="10", page="1"):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def max_pain(self, market: str, currency: str, start="", end="", limit="10", page="1"):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def atm_iv(self, market: str, currency: str, start="", end="", limit="10", page="1"):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def volume_total(self, market: str, currency: str, start="", end="", limit="10", page="1"):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def oi_pc_ratio(self, market: str, currency: str, start="", end="", limit="10", page="1"):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def oi_total(self, market: str, currency: str, start="", end="", limit="10", page="1"):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def vix(self, market: str, currency: str, start="", end="", limit="10", page="1"):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def dvol(self, market: str, currency: str, start="", end="", limit="10", page="1"):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def atm_iv_model(self, market: str, currency: str, type: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def butterfly(self, market: str, currency: str, type: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def butterfly_model(self, market: str, currency: str, type: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def skew(self, market: str, currency: str, type: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def skew_model(self, market: str, currency: str, type: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def risk_reversal(self, market: str, currency: str, type: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def risk_reversal_model(self, market: str, currency: str, type: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def iv_bid_ask(self, market: str, currency: str, type: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
            def volumeOiByExchange(self, currency: str, maturity: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
            def oi_weighted_funding(self, currency: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
                    api_url = self.url + "oi_weighted_funding/" + currency.lower() + makequery
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
                    api_url = self.url + "indices_price/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "indices_price/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def futures_annualized_basis(self, currency: str, period: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
                    api_url = self.url + "futures_annualized_basis/" + currency.lower() + "/" + period + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "futures_annualized_basis/" + currency.lower() + "/" + period
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
                    api_url = self.url + "total_volume_by_exchange/" + currency.lower() + "/" + option + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "total_volume_by_exchange/" + currency.lower() + "/" + option
                    response = requests.get(api_url, headers=api.header).json()
                return response

            @classmethod
            def perpetual_yield(self, market: str, currency: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if market.upper() not in MARKET_CONSTS.__members__:
                    raise TypeError("Market not available")
                elif makequery != "":
                    api_url = self.url + "perpetual_funding/" + currency.lower() + "/" + market.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "perpetual_funding/" + currency.lower() + "/" + market.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response

        # class move:
        #     url = "https://api.laevitas.ch/historical/move/"
        #     pass
        #
        #     @classmethod
        #     def total_oi(self, market="ftx", currency="btc", start="", end="", limit="", page=""):
        #         """
        #         :param market: FTX
        #         :type market:
        #         :param currency: BTC
        #         :type currency:
        #         :param start: EXP:2022-06-07
        #         :type end:
        #         :param end: EXP:2022-06-14
        #         :type end :
        #         :param limit: 10
        #         :type limit:
        #         :param page: 1
        #         :type page:
        #         :return: total oi data
        #         :rtype:
        #         """
        #         makequery = query(start=start, end=end, limit=limit, page=page)
        #         if market.upper() not in MARKET_CONSTS.__members__:
        #             raise TypeError("Market not available")
        #         elif currency.upper() not in CURRENCY.__members__:
        #             raise TypeError("Currency not available")
        #         elif makequery != "":
        #             api_url = self.url + "total_oi/" + market.lower() + "/" + currency.lower() + makequery
        #             response = requests.get(api_url, headers=api.header).json()
        #             Response = Ipagination(response,
        #                                    Ipaginationmeta(response['meta']['total'], response['meta']['page'],
        #                                                    response['meta']['items'])
        #
        #                                    )
        #             for i in range(len(response['items'])):
        #                 Response.items.append(IDateV(response['items'][i]['v'], response['items'][i]['date']))
        #             return Response
        #         else:
        #             api_url = self.url + "total_oi/" + market.lower() + "/" + currency.lower()
        #             response = requests.get(api_url, headers=api.header).json()
        #             Response = Ipagination(response,
        #                                    Ipaginationmeta(response['meta']['total'], response['meta']['page'],
        #                                                    response['meta']['items'])
        #
        #                                    )
        #             for i in range(len(response['items'])):
        #                 Response.items.append(IDateV(response['items'][i]['v'], response['items'][i]['date']))
        #             return Response
        #
        #     @classmethod
        #     def volume_buy_sell(self, market="ftx", currency="btc", start="", end="", limit="", page=""):
        #         """
        #
        #         :param market: FTX
        #         :type market:
        #         :param currency: BTC
        #         :type currency:
        #         :param start: EXP:2022-06-07
        #         :type end:
        #         :param end: EXP:2022-06-14
        #         :type end :
        #         :param limit: 10
        #         :type limit:
        #         :param page: 1
        #         :type page:
        #         :return: json data of volume buy sell
        #         :rtype:
        #         """
        #         makequery = query(start=start, end=end, limit=limit, page=page)
        #         if market.upper() not in MARKET_CONSTS.__members__:
        #             raise TypeError("Market not available")
        #         if currency.upper() not in CURRENCY.__members__:
        #             raise TypeError("Currency not available")
        #         elif makequery != "":
        #             api_url = self.url + "volume_buy_sell/" + market.lower() + "/" + currency.lower() + makequery
        #             response = requests.get(api_url, headers=api.header).json()
        #         else:
        #             api_url = self.url + "volume_buy_sell/" + market.lower() + "/" + currency.lower()
        #             response = requests.get(api_url, headers=api.header).json()
        #         return response
        #
        #     @classmethod
        #     def iv_type(self, market: str, currency: str, type: str, start="", end="", limit="", page=""):
        #         """
        #
        #         :param market: FTX
        #         :type market:
        #         :param currency: BTC
        #         :type currency:
        #         :param type: daily, weekly, quarterly
        #         :type type:
        #         :param start: EXP:2022-06-07
        #         :type end:
        #         :param end: EXP:2022-06-14
        #         :type end :
        #         :param limit: 10
        #         :type limit:
        #         :param page: 1
        #         :type page:
        #         :return: json data of implied volatility type
        #         :rtype:
        #         """
        #         makequery = query(start=start, end=end, limit=limit, page=page)
        #         if market.upper() not in MARKET_CONSTS.__members__:
        #             raise TypeError("Market not available")
        #         if currency.upper() not in CURRENCY.__members__:
        #             raise TypeError("Currency not available")
        #         elif makequery != "":
        #             api_url = self.url + "iv_type/" + market.lower() + "/" + currency.lower() + "/" + type + makequery
        #             response = requests.get(api_url, headers=api.header).json()
        #         else:
        #             api_url = self.url + "iv_type/" + market.lower() + "/" + currency.lower() + "/" + type
        #             response = requests.get(api_url, headers=api.header).json()
        #         return response
        #
        #     @classmethod
        #     def iv_historical_open_future(self, market: str, currency: str, is_open: str, start="", end="", limit="",
        #                                   page=""):
        #         """
        #
        #         :param market: FTX
        #         :type market:
        #         :param currency: BTC
        #         :type currency:
        #         :param is_open : true or false
        #         :type is_open :
        #         :param start: EXP:2022-06-07
        #         :type end:
        #         :param end: EXP:2022-06-14
        #         :type end :
        #         :param limit: 10
        #         :type limit:
        #         :param page: 1
        #         :type page:
        #         :return: json data of iv historical open future
        #         :rtype:
        #         """
        #         makequery = query(start=start, end=end, limit=limit, page=page)
        #         if market.upper() not in MARKET_CONSTS.__members__:
        #             raise TypeError("Market not available")
        #         if currency.upper() not in CURRENCY.__members__:
        #             raise TypeError("Currency not available")
        #         elif makequery != "":
        #             api_url = self.url + "iv_historical_open_future/" + market.lower() + "/" + currency.lower() + "/" + is_open.lower() + makequery
        #             response = requests.get(api_url, headers=api.header).json()
        #         else:
        #             api_url = self.url + "iv_historical_open_future/" + market.lower() + "/" + currency.lower() + "/" + is_open.lower()
        #             response = requests.get(api_url, headers=api.header).json()
        #         return response
        #
        #     @classmethod
        #     def total_volume(self, market="ftx", currency="btc", start="", end="", limit="", page=""):
        #         """
        #
        #         :param market: FTX
        #         :type market:
        #         :param currency: BTC
        #         :type currency:
        #         :param start: EXP:2022-06-07
        #         :type end:
        #         :param end: EXP:2022-06-14
        #         :type end :
        #         :param limit: 10
        #         :type limit:
        #         :param page: 1
        #         :type page:
        #         :return: json data of total volume
        #         :rtype:
        #         """
        #         makequery = query(start=start, end=end, limit=limit, page=page)
        #         if market.upper() not in MARKET_CONSTS.__members__:
        #             raise TypeError("Market not available")
        #         if currency.upper() not in CURRENCY.__members__:
        #             raise TypeError("Currency not available")
        #         elif makequery != "":
        #             api_url = self.url + "total_volume/" + market.lower() + "/" + currency.lower() + makequery
        #             response = requests.get(api_url, headers=api.header).json()
        #         else:
        #             api_url = self.url + "total_volume/" + market.lower() + "/" + currency.lower()
        #             response = requests.get(api_url, headers=api.header).json()
        #         return response
        #
        #     @classmethod
        #     def historical_iv(self, contract_name: str, market="ftx", start="", end="", limit="", page=""):
        #         """
        #
        #         :param market: FTX
        #         :type market:
        #         :param contract_name: try realtime.move.contract_name function for contract names. EXP : BTC-MOVE-2022Q4
        #         :type contract_name:
        #         :param start: EXP:2022-06-07
        #         :type end:
        #         :param end: EXP:2022-06-14
        #         :type end :
        #         :param limit: 10
        #         :type limit:
        #         :param page: 1
        #         :type page:
        #         :return: json data of historical implied volatility
        #         :rtype:
        #         """
        #         makequery = query(start=start, end=end, limit=limit, page=page)
        #         if market.upper() not in MARKET_CONSTS.__members__:
        #             raise TypeError("Market not available")
        #         elif makequery != "":
        #             api_url = self.url + "historical_iv/" + market.lower() + "/" + contract_name.lower() + makequery
        #             response = requests.get(api_url, headers=api.header).json()
        #         else:
        #             api_url = self.url + "historical_iv/" + market.lower() + "/" + contract_name.lower()
        #             response = requests.get(api_url, headers=api.header).json()
        #         return response
        #
        #     @classmethod
        #     def historical_oi(self, contract_name: str, market="ftx", start="", end="", limit="", page=""):
        #         """
        #
        #         :param market: FTX
        #         :type market:
        #         :param contract_name: try realtime.move.contract_name function for contract names. EXP : BTC-MOVE-2022Q4
        #         :type contract_name:
        #         :param start: EXP:2022-06-07
        #         :type end:
        #         :param end: EXP:2022-06-14
        #         :type end :
        #         :param limit: 10
        #         :type limit:
        #         :param page: 1
        #         :type page:
        #         :return: json data of historical open interest
        #         :rtype:
        #         """
        #         makequery = query(start=start, end=end, limit=limit, page=page)
        #         if market.upper() not in MARKET_CONSTS.__members__:
        #             raise TypeError("Market not available")
        #         elif makequery != "":
        #             api_url = self.url + "historical_oi/" + market.lower() + "/" + contract_name.lower() + makequery
        #             response = requests.get(api_url, headers=api.header).json()
        #         else:
        #             api_url = self.url + "historical_oi/" + market.lower() + "/" + contract_name.lower()
        #             response = requests.get(api_url, headers=api.header).json()
        #         return response
        #
        #     @classmethod
        #     def historical_price(self, contract_name: str, market="ftx", start="", end="", limit="", page=""):
        #         """
        #
        #         :param market: FTX
        #         :type market:
        #         :param contract_name: try realtime.move.contract_name function for contract names. EXP : BTC-MOVE-2022Q4
        #         :type contract_name:
        #         :param start: EXP:2022-06-07
        #         :type end:
        #         :param end: EXP:2022-06-14
        #         :type end :
        #         :param limit: 10
        #         :type limit:
        #         :param page: 1
        #         :type page:
        #         :return: json data of historical price
        #         :rtype:
        #         """
        #         makequery = query(start=start, end=end, limit=limit, page=page)
        #         if market.upper() not in MARKET_CONSTS.__members__:
        #             raise TypeError("Market not available")
        #         elif makequery != "":
        #             api_url = self.url + "historical_price/" + market.lower() + "/" + contract_name.lower() + makequery
        #             response = requests.get(api_url, headers=api.header).json()
        #         else:
        #             api_url = self.url + "historical_price/" + market.lower() + "/" + contract_name.lower()
        #             response = requests.get(api_url, headers=api.header).json()
        #         return response
        #
        #     @classmethod
        #     def historical_volume(self, contract_name: str, market="ftx", start="", end="", limit="", page=""):
        #         """
        #
        #         :param market: FTX
        #         :type market:
        #         :param contract_name: try realtime.move.contract_name function for contract names. EXP : BTC-MOVE-2022Q4
        #         :type contract_name:
        #         :param start: EXP:2022-06-07
        #         :type end:
        #         :param end: EXP:2022-06-14
        #         :type end :
        #         :param limit: 10
        #         :type limit:
        #         :param page: 1
        #         :type page:
        #         :return: json data of historical volume
        #         :rtype:
        #         """
        #         makequery = query(start=start, end=end, limit=limit, page=page)
        #         if market.upper() not in MARKET_CONSTS.__members__:
        #             raise TypeError("Market not available")
        #         elif makequery != "":
        #             api_url = self.url + "historical_volume/" + market.lower() + "/" + contract_name.lower() + makequery
        #             response = requests.get(api_url, headers=api.header).json()
        #         else:
        #             api_url = self.url + "historical_volume/" + market.lower() + "/" + contract_name.lower()
        #             response = requests.get(api_url, headers=api.header).json()
        #         return response
        #
        #     @classmethod
        #     def open_future(self, contract_type: str):
        #         """
        #         :param contract_type: daily, weekly, quarterly
        #         :type contract_type:
        #         :return: json data of open future
        #         :rtype:
        #         """
        #         api_url = self.url + "open_future/" + contract_type
        #         response = requests.get(api_url, headers=api.header).json()
        #         return response

        class defi:
            url = "https://api.laevitas.ch/historical/defi/"
            pass

            @classmethod
            def dovs_auctions(self, protocol: str, start="", end="", currency="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, currency=currency, limit=limit, page=page)
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
            def perpetuals(self, market: str, symbol: str, start="", end="", limit="", page=""):
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
                    api_url = self.url + "perpetuals/" + market.lower() + "/" + symbol + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "perpetuals/" + market.lower() + "/" + symbol
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
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
                makequery = prepare_query(start=start, end=end, limit=limit, page=page)
                if makequery != "":
                    api_url = self.url + "summary/" + currency.lower() + makequery
                    response = requests.get(api_url, headers=api.header).json()
                else:
                    api_url = self.url + "summary/" + currency.lower()
                    response = requests.get(api_url, headers=api.header).json()
                return response
