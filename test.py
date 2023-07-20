from Laevitas import SDK

sdk = SDK.api()
sdk.configure('your-api-key')
#test = sdk.realtime.options.instruments(market="deribit",currency="btc")
test2 = sdk.analytics.options.volume_breakdown()
test3 = sdk.historical.options.option(market="DERIBIT",instrument="BTC-28JUN24-70000-C",start="2023-07-13",end="2023-07-20",granularity="5m")
test4 = sdk.historical.options.trades(currency="ETH",market="OKEX",date="2023-07-13")





