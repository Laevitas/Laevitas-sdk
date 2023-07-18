from Laevitas import SDK

sdk = SDK.api()
sdk.configure('your-api-key')
#test = sdk.realtime.options.instruments(market="deribit",currency="btc")
test2 = sdk.analytics.options.atm_iv_ts(market="BINANCE",currency="BTC")
print(test2)






