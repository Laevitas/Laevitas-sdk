from Laevitas import SDK

sdk = SDK.api()
sdk.configure('your-api-key')
#test = sdk.realtime.options.instruments(market="deribit",currency="btc")
test1 = sdk.realtime.options.oi_strike(market="deribit",currency="btc",maturity="30JUN23")
print(test1)




