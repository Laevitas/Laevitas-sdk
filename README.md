# API-SDK
test version which includes 13 endpoints:

## Requirements.

Python 3.7+

## Installation & Usage
### pip install



```sh
pip install SDK-Laevitas-test
```
Then import the package:
```python
from Laevitas import SDK 
```



## Getting Started

Please follow the procedure and then run the following:

```python
from Laevitas import SDK

# create an instance of the API class
sdk = SDK.api()

# Configure your api key
sdk.configure('your-api-key')

response = sdk.historical.move.total_oi(currency="btc", start="2022-06-07", end="2022-06-14", limit="10", page="2")
for i in response.items:
    print(i.v)
                                     


```

## Documentation for available API Endpoints

|Class | Sub-class | Method                                                                                  | Description                                        |
|------------ |-----------|-----------------------------------------------------------------------------------------|----------------------------------------------------|
|*realtime* | options   | get_atm(market, currency)                                                               | At the money Implied Volatility Term Structure     |
|*realtime* | options   | gex_date_all(market, currency)                                                          | Gamma Exposure All Expirations                     |
|*realtime* | options   | maturities(market, currency)                                                            | Active Expirations                                 |
|*realtime* | options   | oi_expiry(market, currency)                                                             | Open Interest By Expiration                        |
|*realtime* | options   | oi_strike_all(market, currency)                                                         | Open Interest By Strike All Expirations            |
|*realtime* | options   | oi_type(market, currency)                                                               | Open Interest By Type                              |
|*realtime* | options   | top_traded_option(market, currency)                                                     | Top Traded Instrument                              |
|*realtime* | options   | v_expiry(market, currency,)                                                             | Volume By Expiry                                   |
|*realtime* | options   | v_strike_all(market, currency,)                                                         | Volume By Strike All Expirations                   |
|*realtime* | options   | volume_buy_sell_all(market, currency,)                                                  | Buy/Sell Volume Last 24h All Expirations           |
|*realtime* | options   | iv_strike(market, currency,strike)                                                      | IV Term Structure By Strike                        |
|*realtime* | options   | oi_strike(market, currency,maturity)                                                    | Open Interest By Strike                            |
|*realtime* | options   | oi_net_change_all(market, currency,hours)                                               | Open Interest Change All Expirations               |
|*realtime* | options   | top_instrument_oi_change(market, currency,hours)                                        | Top Instrument OI Change                           |
|*realtime* | options   | volume_buy_sell(market, currency,maturity)                                              | Buy/Sell Volume Last 24h                           |
|*realtime* | options   | v_strike(market, currency,maturity)                                                     | Volume By Strike                                   |
|*realtime* | options   | summary_trades(market, currency,hours)                                                  | Summary trades                                     |
|*realtime* | options   | v_strike(market, currency,maturity)                                                     | Volume By Strike                                   |
|*realtime* | options   | oi_net_change_all(market, currency,hours)                                               | Open Interest Change All Expirations               |
|*realtime* | options   | gex_date(market, currency, maturity)                                                    | Gamma Exposure by Expiration                       |
|*realtime* | options   | greeks(market, currency, maturity, optiontype)                                          | Greeks                                             |
|*realtime* | options   | iv_all(market, currency, maturity, type)                                                | Implied Volatility Skew                            |
|*realtime* | options   | iv_table(market, currency)                                                              | Implied volatility table                           |
|*realtime* | options   | oi_net_change(market, currency, maturity, hour)                                         | Open Interest Change By Expiration                 |
|*realtime* | options   | snapshot(market, currency)                                                              | Snapshot                                           |
|*realtime* | futures   | instruments()                                                                           | Instruments                                        |
|*realtime* | futures   | perpetual_funding(currency)                                                             | Perpetual Funding                                  |
|*realtime* | futures   | futures_yield(currency)                                                                 | Futures Yield                                      |
|*realtime* | futures   | futures_basis(currency)                                                                 | Futures Basis                                      |
|*realtime* | futures   | volume_breakdown(currency)                                                              | Volume Breakdown                                   |
|*realtime* | futures   | oi_breakdown(currency)                                                                  | Open Interest Breakdown                            |
|*realtime* | futures   | markets_oi_gainers_and_losers(currency, option, hour)                                   | Futures OI Change                                  |
|*realtime* | futures   | snapshot(market)                                                                        | snapshot                                           |
|*realtime* | derivs    | oi_gainers(market, oitype, period)                                                      | oi gainers                                         |
|*historical* | options   | option(market, instrument, start(opt), end(opt), limit(opt), page(opt)                  | options                                            |
|*historical* | options   | iv(market, instrument, start(opt), end(opt), limit(opt), page(opt)                      | Instrument Historical Implied Volatility           |
|*historical* | options   | price(market, instrument, start(opt), end(opt), limit(opt), page(opt)                   | Instrument Historical Price                        |
|*historical* | options   | oi_volume(market, instrument, start(opt), end(opt), limit(opt), page(opt)               | Instrument Historical Open Interest & Volume       |
|*historical* | options   | underlying_price(market, instrument, start(opt), end(opt), limit(opt), page(opt)        | Instrument Historical Underlying Price             |
|*historical* | options   | oi_strike(market,currency, maturity ,date)                                              | Historical Open Interest By Strike                 |
|*historical* | options   | volume_strike(market,currency, maturity ,date)                                          | Historical Volume By Strike                        |
|*historical* | options   | volume_pc_ratio(market, currency, start(opt), end(opt), limit(opt), page(opt)           | Volume Put/Call Ratio                              |
|*historical* | options   | gex_index(market, currency, start(opt), end(opt), limit(opt), page(opt)                 | Gamma Exposure Index                               |
|*historical* | options   | max_pain(market, currency, start(opt), end(opt), limit(opt), page(opt)                  | Max Pain Monthly Expiration                        |
|*historical* | options   | atm_iv(market, currency, start(opt), end(opt), limit(opt), page(opt)                    | At the money Implied Volatility (Rolling Maturity) |
|*historical* | options   | volume_total(market, currency, start(opt), end(opt), limit(opt), page(opt)              | Volume total                                       |
|*historical* | options   | oi_pc_ratio(market, currency, start(opt), end(opt), limit(opt), page(opt)               | Open Interest Put/Call Ratio                       |
|*historical* | options   | oi_total(market, currency, start(opt), end(opt), limit(opt), page(opt)                  | Instrument Historical Implied Volatility           |
|*historical* | options   | realized_vol(market, currency, start(opt), end(opt), limit(opt), page(opt)              | Realized Volatility                                |
|*historical* | options   | vix(market, currency, start(opt), end(opt), limit(opt), page(opt)                       | Vol Index                                          |
|*historical* | options   | dvol(market, currency, start(opt), end(opt), limit(opt), page(opt)                      | Deribit Volatility Index (DVOL)                    |
|*historical* | options   | atm_iv_model(market, currency, type, start(opt), end(opt), limit(opt), page(opt)        | At the money Implied Volatility model              |
|*historical* | options   | butterfly(market, currency, type, start(opt), end(opt), limit(opt), page(opt)           | Butterfly                                          |
|*historical* | options   | butterfly_model(market, currency, type, start(opt), end(opt), limit(opt), page(opt)     | Butterfly model                                    |
|*historical* | options   | realized_vol(market, currency, start(opt), end(opt), limit(opt), page(opt)              | realized vol                                       |
|*historical* | options   | skew(market, currency, type, start(opt), end(opt), limit(opt), page(opt)                | Skew                                               |
|*historical* | options   | skew_model(market, currency, type, start(opt), end(opt), limit(opt), page(opt)          | Skew model                                         |
|*historical* | options   | risk_reversal(market, currency, type, start(opt), end(opt), limit(opt), page(opt)       | Risk Reversal                                      |
|*historical* | options   | risk_reversal_model(market, currency, type, start(opt), end(opt), limit(opt), page(opt) | Risk Reversal model                                |
|*historical* | options   | gamma_bands(market, currency, type, start(opt), end(opt), limit(opt), page(opt)         | Gamma Bands                                        |
|*historical* | options   | total_oi(market, currency, maturiy, start(opt), end(opt), limit(opt), page(opt)         | Total open interest                                |
|*historical* | options   | iv_bid_ask(market, currency, type, start(opt), end(opt), limit(opt), page(opt)          | iv bid/ask                                         |
|*historical* | options   | total_volume(market, currency, maturity, start(opt), end(opt), limit(opt), page(opt)    | total volume                                       |
|*historical* | options   | volumeOiByExchange(currency, maturity, start(opt), end(opt), limit(opt), page(opt)      | Volume open interest exchange                      |
|*historical* | move      | total_oi(currency, start(opt), end(opt), limit(opt), page(opt)                          | total oi                                           |








